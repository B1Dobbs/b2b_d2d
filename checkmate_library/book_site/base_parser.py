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
    def get_links_for_search(self, search_str):
        pass
    def convert_book_id_to_url(self, book_id):
        pass
    def get_links_for_page(self, url):
        pass

    _MAX_DISTANCE = 0.2
    _STOP_SEARCH = False

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
        search_str = self.get_search_str(book_data)

        matches = []
        links = self.get_links_for_search(search_str, book_data.format)
        print(links)
        if links != []:
            matches += self.get_matches_from_links(links, book_data)

        '''This commented out section is for pagnation. It was determined that getting
        results from more than one page was out of scope because the user should be making
        searches that would result in the book being found on the first page.'''
        # while links != [] and not self.found_enough_matches(matches):
        #     print("PAGE: ", page)
        #     page += 1
        #     matches += self.get_matches_from_links(links, book_data)
        #     links = self.get_links_for_page(page, search_str)
        #     # for match in matches:
            #     match[1].print_data()
            #     print("MATCH: ", match[0])
            # print('ENOUGH: ', self.found_enough_matches(matches))

        return matches


    def get_search_str(self, book_data):
        query_string = ""

        # If authors is included, add to the query
        if book_data.authors != None: 
            query_string += book_data.get_authors_as_string()
        
        # If a title is included, add to the query
        if book_data.title != None: 
            query_string += " " + book_data.title
        
        # If an isbn included, only search by isbn
        if book_data.isbn_13 != None:
            query_string = book_data.isbn
        
        return query_string

    def get_matches_from_links(self, link_list, book_data):
        # For each link, get the book data and compare it with the passed in book_data
        matches = []
        last_match = 1
        index = 1

        for lnk in link_list:
            search_book_data = self.get_book_data(lnk)
            match_value = search_book_data.compare(book_data)
            if match_value != 0.0:
                matches.append((match_value, search_book_data))
                last_match = index
            # elif (last_match / index) < self._MAX_DISTANCE:
            #     self._STOP_SEARCH = True
            #     break

            index += 1

        return matches

    '''Only used when needing to search more than one page for a match.'''
    def found_enough_matches(self, matches):
        has_good_match = False
    
        for match in matches:
            if match[0] >= 0.8 :
                has_good_match = True
                break

        # print("GOOD MATCH: ", has_good_match)
        # print("STOP: ", self._STOP_SEARCH)
        # print("LENGTH: ", len(matches) >= 20)
        
        if (has_good_match and len(matches) >= 20) or self._STOP_SEARCH:
            return True
        else:
            return False

        """ISBN 10 to ISBN 13 conversion """
    def isbn10_to_isbn13(self, isbn10):
        return to_isbn13(isbn10)