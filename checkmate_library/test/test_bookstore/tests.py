import unittest
import sys
sys.path.append(".")
from book_site.test_bookstore import TestBookstore
from checkmate import get_book_site
from base_tests import BaseBookParseTest
from test_bookstore.test_cases import TestBookstoreTestCases
  

class TestTestBookstoreBookDataLocal(BaseBookParseTest): 
  
    def test_morgan(self):  
        local_url = "test/test_bookstore/test_pages/moms_against_zombies_morgan.html"
        self.common_test(local_url, TestBookstoreTestCases.morgan_local, TestBookstore())

    def test_walker(self):
        local_url = "test/test_bookstore/test_pages/ruin_me_walker.html"
        self.common_test(local_url, TestBookstoreTestCases.walker_local, TestBookstore())

    def test_reid(self):
        local_url = "test/test_bookstore/test_pages/ancient_voices_reid.html"
        self.common_test(local_url, TestBookstoreTestCases.reid_local, TestBookstore())

class TestTestBookstoreBookDataLive(BaseBookParseTest):

    def test_morgan(self):  
        local_url = "http://127.0.0.1:8000/library/9781386842842/"
        self.common_test(local_url, TestBookstoreTestCases.morgan_live, TestBookstore())

    def test_walker(self):
        local_url = "http://127.0.0.1:8000/library/9781386944362/"
        self.common_test(local_url, TestBookstoreTestCases.walker_live, TestBookstore())

    def test_reid(self):
        local_url = "http://127.0.0.1:8000/library/9781533791917/"
        self.common_test(local_url, TestBookstoreTestCases.reid_live, TestBookstore())


class TestTestBookstoreLinks(unittest.TestCase): 
  
    def test_books(self):  
        parser = TestBookstore()
        links = parser.get_links_for_page("test/test_bookstore/test_pages/search_books.html")
        self.assertEqual(links, TestBookstoreTestCases.links_book)

 

