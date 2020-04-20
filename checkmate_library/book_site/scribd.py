from book_data import BookData, Format
from lxml import etree
from book_site.common.utils import query_html, get_soup_from_url
import requests, bs4
import json
import re 
from book_site import base_parser
import regex

class Scribd(base_parser.BookSite):

    SLUG = "SD"

    """Given a direct link to a book page at a site, parse it and return the SiteBookData of the info""" 
    def get_site_specific_data(self, root, book_data):
        # type: (str) -> BookData  
        
        #Get the Title and Subtitle
        title = query_html(root, "//h1[@class='document_title']").text
        if ':' in title:
            title = title.split(': ')
            book_data.title = title[0]
            book_data.subtitle = title[1]
        else:    
            book_data.title = title

        #Get the format, default digital
        book_format = query_html(root, "//dd[@class='meta_description format']/descendant-or-self::*/text()")
        if book_format == "Audiobook":
            book_data.format = Format.AUDIO_BOOK

        #Get main image url
        book_data.image_url = query_html(root, ".//div[@class='document_cell']//img/@src")

        #Get description
        book_data.description = query_html(root, ".//meta[@property='og:description']/@content")

        #Get ISBN
        isbn = query_html(root, "//dd[@class='meta_description isbn']")
        if( isbn != None):
            book_data.isbn_13 = isbn.text

        #Get Author List
        authors = query_html(root, ".//a[@class='contributor']/descendant-or-self::*/text()")
        if authors != None:
            if isinstance(authors,list):
                book_data.authors += authors
            else:
                book_data.authors.append(authors)

        #Get Book ID From URL
        bookID = query_html(root, "//link[@rel = 'alternate'][1]/@href")
        book_data.book_id =query_html(root, ".//meta[@property='og:url']/@content").replace('https://www.scribd.com/', '')

        return book_data

    def get_links_for_search(self, search_str, format, page=1):
        if(format == Format.DIGITAL):
            return self.get_links_for_page(self.format_url('books', search_str), 'books')
        elif(format == Format.AUDIO_BOOK):
            return self.get_links_for_page(self.format_url('audiobooks', search_str), 'audiobooks')
        else:
            return []

    def format_url(self, format, search_str, page=1):
        return 'https://www.scribd.com/search?content_type=' + format + '&page='+ str(page) +'&query=' + search_str + '&language=1'

    def get_links_for_page(self, url, format='books'):
        links = []

        soup = get_soup_from_url(url)
        pattern = re.compile(r'function prefetchResource') # Create a python regex to find the function in which the json resides
        string = str(soup.find('script', text=pattern)) # Find the function by looking for the pattern

        pattern = regex.compile(r'\{(?:[^{}]|(?R))*\}') # Because python regex is not as powerful, we have to import a more powerful standardized regex
                                                       # This code selects actual json code
        new_string = pattern.findall(string)
        parsed_json = json.loads(new_string[1]) # parse the json

        if parsed_json['result_count'] != '0': # If there are any results
            results = parsed_json['results']  
            for book in results[format]['content']['documents']:
                links.append(book['book_preview_url'])

        return links

    """Given a book_id, return the direct url for the book.""" 
    def convert_book_id_to_url(self, book_id):
        # type: (str) -> str 
        return "https://www.scribd.com/" + book_id