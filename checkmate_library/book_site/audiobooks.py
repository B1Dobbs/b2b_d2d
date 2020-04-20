from book_data import BookData, Format
from book_site.common.utils import query_html, get_soup_from_url
from book_site import base_parser
import requests, bs4
import re 

class Audiobooks(base_parser.BookSite):

    SLUG = "AB"

    """Given a direct link to a book page at a site, parse it and return the BookData of the info""" 
    def get_site_specific_data(self, root, book_data):
        book_data.format = Format.AUDIO_BOOK

        title = query_html(root, ".//h1[@class='audiobookTitle']").text
        #subtitle = query_html(root, ".//span[@class='subtitle product-field']")
        if ":" in title:
            title_array = title.split(":")
            book_data.title = title_array[0]
            book_data.subtitle = str.strip(title_array[1])
        else:
            book_data.title = title
        
        book_data.image_url = "https:" + query_html(root, ".//div[@class='book-details-sidenav']//img/@src")

        book_data.isbn_13 = re.findall('[0-9]+', book_data.image_url)[0]

        book_data.description = " "
        description = query_html(root, ".//div[@class='book-description']/descendant-or-self::*/text()")
        if description != None:
            for string in description:   
                book_data.description += string


        authors = query_html(root, ".//h4[@class='book-written-by' or @class='book-narrated-by']//a/text()")
        if authors != None:
            if isinstance(authors,list):
                book_data.authors += authors
            else:
                book_data.authors.append(authors)

        book_id = query_html(root, ".//meta[@property='og:url']/@content")
        book_data.book_id = book_id.replace("https://www.audiobooks.com/audiobook/", "")

        try:
            text = query_html(root, ".//div[@class='buy-button']//p").text
            price = text.replace("Price $", "")
        except:
            price = "0.0"
        book_data.extra = {"Price" : price}
        book_data.content = query_html(root, "/html")

        return book_data

    def get_links_for_search(self, search_str, format):
        '''Only audio books at this site'''
        return self.get_links_for_page('https://www.audiobooks.com/search/book/' + search_str)

    """ Searching Audiobooks for relevant links """
    def get_links_for_page(self, url):
        links = []
        soup = get_soup_from_url(url)
        
        for div in soup.find_all('div', class_="book__details--flex-child"):
            a_tag = div.find('a')
            links.append(a_tag.get('href'))

        return links

    """Given a book_id, return the direct url for the book.""" 
    def convert_book_id_to_url(self, book_id):
        # type: (str) -> str 
        return "https://www.audiobooks.com/audiobook/" + book_id