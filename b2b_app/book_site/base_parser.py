from book_site.common.utils import get_image_from_url, get_root_from_url, query_html
from book_data import BookData, Format, ParseStatus
import sys, traceback
import requests
from isbnlib import to_isbn13

class BookSite:

    def __init__(self):
        pass
    def get_site_specific_data(self):
        pass
    def get_site_links(self):
        pass
    def get_links_for_search(self, search_str):
        pass
    def convert_book_id_to_url(self, book_id):
        pass

    def get_book_data(self, url):
        # type: (str) -> SiteBookData 
        book_data = BookData()
        book_data.url = url
        book_data.ready_for_sale = True
        book_data.format = Format.DIGITAL
        book_data.site_slug = self.SLUG
        book_data.authors = []
        
        try:
            root = get_root_from_url(url)
            book_data.content = query_html(root, "/html")

            book_data = self.get_site_specific_data(root, book_data)
            
            if book_data.image_url != None:
                book_data.image = get_image_from_url(book_data.image_url)

            book_data.parse_status = ParseStatus.FULLY_PARSED
            
        except requests.exceptions.ConnectionError:
            print("ERROR: Could not connect to url ", url)
            book_data.parse_status = ParseStatus.UNSUCCESSFUL
        except:
            print("ERROR: Processing book at " + url)
            traceback.print_exc()

        return book_data

    def find_book_matches(self, book_data): 
        links = set(self.get_site_links(book_data))
        print(links)
        return get_matches_from_links(links, book_data)

    def get_matches_from_links(self, link_list, book_data):
        # For each link, get the book data and compare it with the passed in book_data
        book_matches = []
        for lnk in link_list:
            search_book_data = self.get_book_data(lnk)
            match_value = search_book_data.compare(book_data)
            search_book_data.print_data()
            print("MATCH: ", match_value)
            if match_value != 0.0 :
                book_matches.append((match_value, search_book_data))

        return book_matches


    def found_enough_matches(self, matches):
        has_good_match = False
        for match in matches:
            if match[0] > 0.7 :
                has_good_match = True
                break
        
        if has_good_match and len(matches >= 30):
            return True
        else:
            return False

    def isbn10_to_isbn13(self, isbn10):
        return to_isbn13(isbn10)