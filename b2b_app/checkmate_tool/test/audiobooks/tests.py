import unittest
import sys
sys.path.append(".")
from book_site.audiobooks import Audiobooks
from checkmate import get_book_site
from base_tests import BaseBookParseTest
from audiobooks.test_cases import AudiobooksTestCases
  

class TestAudiobooksBookDataLocal(BaseBookParseTest): 
    #@unittest.skip("Website down")
    def test_lackey(self):  
        local_url = "test/audiobooks/test_pages/nails_crossing_lackey.html"
        self.common_test(local_url, AudiobooksTestCases.lackey_local, Audiobooks())

    #@unittest.skip("Website down")
    def test_patterson(self):  
        local_url = "test/audiobooks/test_pages/blindside_patterson.html"
        self.common_test(local_url, AudiobooksTestCases.patterson_local, Audiobooks())
    #@unittest.skip("Website down")
    def test_lewis(self):  
        local_url = "test/audiobooks/test_pages/narnia_lewis.html"
        self.common_test(local_url, AudiobooksTestCases.lewis_local, Audiobooks())


class TestAudiobooksBookDataLive(BaseBookParseTest):
    #@unittest.skip("Website down")
    def test_lackey(self):  
        local_url = "https://www.audiobooks.com/audiobook/nails-crossing-a-novel/303764"
        self.common_test(local_url, AudiobooksTestCases.lackey_live, Audiobooks())
    #@unittest.skip("Website down")
    def test_patterson(self):  
        local_url = "https://www.audiobooks.com/audiobook/blindside/405228"
        self.common_test(local_url, AudiobooksTestCases.patterson_live, Audiobooks())
    #@unittest.skip("Website down")
    def test_lewis(self):  
        local_url = "https://www.audiobooks.com/audiobook/chronicles-of-narnia-adult-box-set/347498"
        self.common_test(local_url, AudiobooksTestCases.lewis_live, Audiobooks())

class TestAudiobooksLinks(unittest.TestCase): 

    def test_audiobooks(self):  
        parser = Audiobooks()
        links = parser.get_links_for_page("test/audiobooks/test_pages/search_audiobooks.html")
        self.assertEqual(links, AudiobooksTestCases.links_audiobook)

