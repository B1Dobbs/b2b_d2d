from book_data import BookData, Format
from book_site.common.utils import query_html
from book_site import base_parser
import requests, bs4

class Kobo(base_parser.BookSite):

    SLUG = "KB"

    """Given a direct link to a book page at a site, parse it and return the BookData of the info""" 
    def get_site_specific_data(self, root, book_data):
        format = query_html(root, ".//div[@class='bookitem-secondary-metadata']/h2").text
        if 'Audiobook' in format:
            book_data.format = Format.AUDIO_BOOK
        title = str.strip(query_html(root, ".//span[@class='title product-field']").text)
        subtitle = query_html(root, ".//span[@class='subtitle product-field']")
        if ":" in title:
            title_array = title.split(":")
            book_data.title = title_array[0]
            book_data.subtitle = title_array[1]
        elif subtitle != None:
            book_data.subtitle = str.strip(subtitle.text)
        else:
            book_data.title = title
        
        image_url = query_html(root, ".//div[@class='item-image']//img/@src")
        if isinstance(image_url,list):
            book_data.image_url = "https:" + query_html(root, ".//div[@class='item-image']//img/@src")[0]
        else:
            book_data.image_url = "https:" + query_html(root, ".//div[@class='item-image']//img/@src")

        book_data.isbn_13 = query_html(root, ".//li[contains(text(), 'ISBN')]/span").text

        book_data.description = " "
        description = query_html(root, ".//div[@class='synopsis-description']/descendant-or-self::*/text()")
        if description != None:
            for string in description:   
                book_data.description += string

        series_info = query_html(root, ".//span[@class='product-sequence-field']/a[1]")
        if series_info is not None:
            series_info = series_info.text.split("#")
            book_data.series = str.strip(series_info[0])
            if len(series_info) > 1:
                book_data.vol_number = series_info[1]


        authors = query_html(root, ".//a[@class='contributor-name']/text()")
        if authors != None:
            if isinstance(authors,list):
                book_data.authors += authors
            else:
                book_data.authors.append(authors)

        book_id = str(query_html(root, ".//link[@rel='canonical']/@href"))
        book_data.book_id = book_id.split("/")[-1]

        try:
            price = query_html(root, ".//div[@class='active-price']//span[@class='price']")[0].text
        except:
            price = 0.0
        book_data.extra = {"Price" : price, "Release Date" : query_html(root, ".//div[@class='bookitem-secondary-metadata']/ul[1]/li[2]/span[1]").text}
        book_data.content = query_html(root, "/html")

        return book_data

    """Given a SiteBookData, search for the book at the `book_site` site
    and provide a list of likely matches paired with how good
    of a match it is (1.0 is an exact match). 
    This should take into account all the info we have about a book, 
    including the cover.""" 
    def get_site_links(self, book_data):
        links = []

        query_string = ""

        if book_data.authors != None: # Add authors to query string if provided
            query_string += book_data.get_authors_as_string()
        
        if book_data.title != None: # Add title to query string if provided
            if query_string != "":
                query_string += " " + book_data.title
            else:
                query_string = book_data.title

        if book_data.isbn_13 != None: # Search by ISBN if provided
            links += self.get_links_for_search(book_data.isbn_13)
        
        if query_string != "": # Search with everything in the query string
            links += self.get_links_for_search(query_string)
            
        return links

    """ Searching Kobo for relevant links """
    def get_links_for_search(self, search_str):
        links = []
        link = 'https://www.kobo.com/us/en/search?query=' + search_str
        res = requests.get(link)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        
        for p in soup.find_all('p', class_="title product-field"):
            for link in p.find_all('a'):
                links.append(link.get('href'))

        aLink = soup.find('a', class_="page-link final") # Find the function by looking for the pattern
        if aLink != "None": #There's more than one page
            num_pages = aLink.contents[0]
            num_pages = int(num_pages) + 1
            print(num_pages)
            for i in range(2, num_pages):
                link = 'https://www.kobo.com/us/en/search?query=' + search_str + '&pageNumber=' + str(i)
                res = requests.get(link)
                res.raise_for_status()
                soup = bs4.BeautifulSoup(res.text, "html.parser")

                for p in soup.find_all('p', class_="title product-field"):
                    for link in p.find_all('a'):
                        links.append(link.get('href'))
    
        return links

    """Given a book_id, return the direct url for the book.""" 
    def convert_book_id_to_url(self, book_id):
        # type: (str) -> str 
        return "https://www.kobo.com/us/en/ebook/" + book_id