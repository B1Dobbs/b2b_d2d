import unittest
import sys
sys.path.append(".")
from book_site.kobo import Kobo
from checkmate import get_book_site
from base_tests import BaseBookParseTest
from kobo.test_cases import KoboTestCases
  

class TestKoboBookDataLocal(BaseBookParseTest): 
  
    def test_austin(self):  
        local_url = "test/kobo/test_pages/pride_and_prejudice_austin.html"
        self.common_test(local_url, KoboTestCases.austin_local, Kobo())

    #@unittest.skip("Audiobook downloaded html is always different from live page")
    def test_chbosky(self):
        local_url = "test/kobo/test_pages/the_perks_of_being_a_wallflower_chbosky.html"
        self.common_test(local_url, KoboTestCases.chbosky_local, Kobo())
    
    def test_roth(self):  
        local_url = "test/kobo/test_pages/divergent_1_roth.html"
        self.common_test(local_url, KoboTestCases.roth_local, Kobo())


class TestKoboBookDataLive(BaseBookParseTest):

    def test_adams(self):  
        local_url = "https://www.kobo.com/us/en/ebook/pride-and-prejudice-27"
        self.common_test(local_url, KoboTestCases.austin_live, Kobo())
    
    def test_chbosky(self):  
        local_url = "https://www.kobo.com/us/en/audiobook/the-perks-of-being-a-wallflower-6"
        self.common_test(local_url, KoboTestCases.chbosky_live, Kobo())

    def test_roth(self):  
        local_url = "https://www.kobo.com/us/en/ebook/divergent-1"
        self.common_test(local_url, KoboTestCases.roth_live, Kobo())


class TestKoboLinks(unittest.TestCase): 
  
    def test_books(self):  
        parser = Kobo()
        links = parser.get_links_for_page("test/kobo/test_pages/search_books.html", "Book")
        self.assertEqual(links, KoboTestCases.links_book)

    def test_audiobooks(self):  
        parser = Kobo()
        links = parser.get_links_for_page("test/kobo/test_pages/search_audiobooks.html", "Audiobook")
        self.assertEqual(links, KoboTestCases.links_audiobook)

