from book_data import BookData
from book_site.common.utils import query_html, get_soup_from_url
import requests, bs4
from book_site import base_parser

class LivrariaCultura(base_parser.BookSite):

    SLUG = "LC"
    
    """Given a direct link to a book page at a site, parse it and return the SiteBookData of the info""" 
    def get_site_specific_data(self, root, book_data):
        title = query_html(root, ".//meta[@property='og:title']/@content")
        book_data.title = str(title)

        subtitle = query_html(root, ".//th[contains(text(), 'Subtitulo')]/following-sibling::td")
        if subtitle is not None:
            book_data.subtitle = subtitle.text

        imageUrl = query_html(root, ".//meta[@itemprop='image']/@content")
        book_data.image_url = str(imageUrl)
        book_data.isbn_13 = self.isbn10_to_isbn13(query_html(root, ".//th[contains(text(), 'ISBN')]/following-sibling::td").text)
        book_data.description = str(query_html(root, ".//meta[@property='og:title']/following-sibling::meta[@property='og:description']/@content"))

        #Series and Volume Number are not available on site

        authorsTag = query_html(root, ".//td[@class='value-field Colaborador']/descendant-or-self::*/text()")

        #Parsing Author Name
        collaborators = authorsTag.split("|")
        matchingAuthor = [s for s in collaborators if "Autor" in s]
        authorsArray = []

        for a in matchingAuthor:
            authorsNamesString = a.split(":")
            if "," in authorsNamesString[1]:
                authorsNamesArray = authorsNamesString[1].split(",")
                authorsArray.append(authorsNamesArray[1].strip() + " " + authorsNamesArray[0].strip())
        
        book_data.authors = authorsArray

        bookURL = str(query_html(root, ".//meta[@itemprop='url']/@content"))
        bookID = bookURL.split('.br')
        book_data.book_id = bookID[1]
        book_data.content = query_html(root, "/html")

        #Price is gathered as extra data
        book_data.extra = {"price" : str(query_html(root, ".//meta[@property='product:price:amount']/@content"))}

        return book_data

    def get_links_for_search(self, search_str, format):
        '''No differentiation between formats'''
        return self.get_links_for_page('https://www3.livrariacultura.com.br/ebooks/?ft=' + search_str)


    def get_links_for_page(self, url):
        links = []
        soup = get_soup_from_url(url)

        for div in soup.find_all('div', class_="prateleiraProduto__informacao__preco"):
            for a in div.find_all('a'):
                links.append(a.get('href'))

        # #This code is supposed to paginate, but for some reason libraria's pagination links don't work at all.
        # # First get the number of books
        # storage_span = soup.find('span', class_="resultado-busca-numero")
        # num_books_span = storage_span.find('span', class_="value")
        # num_books = int(num_books_span.contents[0])

        # books_per_pages_option = soup.find('option', attrs={"selected" : "selected"})
        # books_per_pages = int(books_per_pages_option.contents[0])
        
        # num_pages = num_books/books_per_pages

        
        # if num_pages > 1:
        #     for i in range(2, int(num_pages)):
        #         link = 'https://www3.livrariacultura.com.br/ebooks/?ft=' + search_str + '#' + str(i)
        #         print(link)
        #         res = requests.get(link)
        #         res.raise_for_status()
        #         soup = bs4.BeautifulSoup(res.text, "html.parser")

        #         for div in soup.find_all('div', class_="prateleiraProduto__informacao__preco"):
        #             for a in div.find_all('a'):                 
        #                 links.append(a.get('href'))


        return links


    """Given a book_id, return the direct url for the book.""" 
    def convert_book_id_to_url(self, book_id):
        # type: (str) -> str 
        return "https://www3.livrariacultura.com.br" + book_id