import unittest
import sys
sys.path.append(".")
from book_site.google_books import GoogleBooks
from checkmate import get_book_site
from base_book_parse_test import BaseBookParseTest
from google_books.test_cases import GoogleBooksTestCases
  

class TestGoogleBookDataLocal(BaseBookParseTest): 
  
    def test_adams(self):  
        local_url = "test/google_books/test_pages/murder_and_intrigue_on_the_mexican_border_by_adams.html"
        self.common_test(local_url, GoogleBooksTestCases.adams_local, GoogleBooks())

    #@unittest.skip("Audiobook downloaded html is always different from live page")
    def test_dickens(self):  
        local_url = "test/google_books/test_pages/a_tale_of_two_cities_dickens.html"
        self.common_test(local_url, GoogleBooksTestCases.dickens_local, GoogleBooks())
    
    def test_sandford(self):  
        local_url = "test/google_books/test_pages/neon_prey_sandford.html"
        self.common_test(local_url, GoogleBooksTestCases.sandford_local, GoogleBooks())


class TestGoogleBookDataLive(BaseBookParseTest):

    def test_adams(self):  
        local_url = "https://play.google.com/store/books/details?id=-lRoDwAAQBAJ&source=gbs_api"
        self.common_test(local_url, GoogleBooksTestCases.adams_live, GoogleBooks())
    
    def test_dickens(self):  
        local_url = "https://play.google.com/store/audiobooks/details/Charles_Dickens_A_Tale_of_Two_Cities?id=AQAAAECMCD9IoM&hl=en_US"
        self.common_test(local_url, GoogleBooksTestCases.dickens_live, GoogleBooks())

    def test_sandford(self):  
        local_url = "https://play.google.com/store/books/details/John_Sandford_Neon_Prey?id=m75mDwAAQBAJ&hl=en_US"
        self.common_test(local_url, GoogleBooksTestCases.sandford_live, GoogleBooks())

