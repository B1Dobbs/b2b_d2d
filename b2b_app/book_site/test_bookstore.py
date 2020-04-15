from book_data import BookData, Format
from book_site.common.utils import query_html
import requests, bs4
import re 
from book_site import base_parser

class TestBookstore(base_parser.BookSite):

    SLUG = "TB"
        
    """Given a direct link to a book page at a site, parse it and return the SiteBookData of the info""" 
    def get_site_specific_data(self, root, book_data):
        format = query_html(root, ".//p[@class='details']").text
        if 'Audiobook' in format: 
            book_data.format = Format.AUDIO_BOOK
        title = str.strip(query_html(root, ".//p[@id='title']/strong").text)
        if ":" in title:
            title_array = title.split(":")
            book_data.title = title_array[0]
            book_data.subtitle = str.strip(title_array[1])
        else:
            book_data.title = title

        """Will work if you add an image to testbook store description page """
        #book_data.image_url = root.xpath(".//img/@src")[0]

        book_data.isbn_13 = str.strip(query_html(root, ".//span[@id='isbn']").text)
        book_data.description = query_html(root, "//script[@type='text/javascript']/text()").split("\"")[19]

        series = str.strip(query_html(root, ".//span[@id='series']").text)
        if series != 'None':
            book_data.series = series
            vol_number = str.strip(query_html(root, ".//span[@id='volume_number']").text)
            if vol_number != 'None':
                book_data.vol_number = vol_number
        
        book_data.authors = str.strip(query_html(root, ".//span[@id='author']/text()")).split(", ")
        
        book_data.book_id = book_data.isbn_13
        book_data.content = query_html(root, "/html")

        book_data.ready_for_sale = query_html(root, ".//i/@class")
        if book_data.ready_for_sale == "fa fa-times-circle x-mark":
            book_data.ready_for_sale = False
        else: 
            book_data.ready_for_sale = True

        book_data.extra = {"Price" : query_html(root, ".//span[@id='price']").text, "ReleaseDate" : query_html(root, ".//span[@id='release_date']").text}

        return book_data


    """Given a SiteBookData, search for the book at the `book_site` site
    and provide a list of likely matches paired with how good
    of a match it is (1.0 is an exact match). 
    This should take into account all the info we have about a book, 
    including the cover.""" 
    def get_site_links(self, book_data):

        links = []

        if book_data.authors != None: # If an author is sent in to search by, record link matches
            links += self.get_links_for_search(book_data.get_authors_as_string())

        if book_data.isbn_13 != None: # If an isbn is sent in to search by, record link matches
            links += self.get_links_for_search(book_data.isbn_13)

        if book_data.title != None: # If a title is sent in to search by, record link matches
            links += self.get_links_for_search(book_data.title)

        # For each link, get the book data and compare it with the passed in book_data
        return links

    """ Search test Book Store for relevant links """
    def get_links_for_search(self, search_str):
        links = []
        link = 'http://127.0.0.1:8000/testBookstore/library/?q=' + search_str
        res = requests.get(link)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, "html.parser")

        for link in soup.find_all('a', class_="book_title"):
            links.append("http://127.0.0.1:8000/testBookstore" + link.get('href'))

        pattern = re.compile(r'Last')
        find_page_num = str(soup.find('a', text=pattern))
        if find_page_num != "None":
            temp = re.findall(r'\d+', find_page_num)
            num_pages = temp[0]
        
            for i in range(2, int(num_pages)+1):
                link = 'http://127.0.0.1:8000/testBookstore/library/?page=' + str(i)
                res = requests.get(link)
                res.raise_for_status()
                soup = bs4.BeautifulSoup(res.text, "html.parser")

                for link in soup.find_all('a', class_="book_title"):
                    links.append("http://127.0.0.1:8000/testBookstore" + link.get('href')) 

        
        return links 




    """Given a book_id, return the direct url for the book.""" 
    def convert_book_id_to_url(self, book_id):
        # type: (str) -> str
        return "http://localhost:8000/library/" + book_id + "/"