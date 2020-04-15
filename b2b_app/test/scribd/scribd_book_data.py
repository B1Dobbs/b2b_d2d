import unittest
import sys
sys.path.append(".")
from book_site.scribd import Scribd
from checkmate import get_book_site
from base_book_parse_test import BaseBookParseTest
from scribd.test_cases import ScribdTestCases
  

class TestScribdBookDataLocal(BaseBookParseTest): 
    #@unittest.skip("Website down")
    def test_collins(self):  
        local_url = "test/scribd/test_pages/the_hunger_games_by_suzanne_collins.html"
        self.common_test(local_url, ScribdTestCases.collins_local, Scribd())
    #@unittest.skip("Website down")
    def test_dalio(self):
        local_url = "test/scribd/test_pages/principles_by_ray_dalio.html"
        self.common_test(local_url, ScribdTestCases.dalio_local, Scribd())
    #@unittest.skip("Website down")
    def test_bryant(self):
        local_url = "test/scribd/test_pages/the_mamba_mentality_by_kobe_bryant.html"
        self.common_test(local_url, ScribdTestCases.bryant_local, Scribd())

class TestScribdBookDataLive(BaseBookParseTest):
    #@unittest.skip("Website down")
    def test_collins(self):  
        local_url = "https://www.scribd.com/audiobook/389029058/The-Hunger-Games-Special-Edition"
        self.common_test(local_url, ScribdTestCases.collins_live, Scribd())
    #@unittest.skip("Website down")
    def test_dalio(self):
        local_url = "https://www.scribd.com/book/357813054/Principles-Life-and-Work"
        self.common_test(local_url, ScribdTestCases.dalio_live, Scribd())
    #@unittest.skip("Website down")
    def test_bryant(self):
        local_url = "https://www.scribd.com/book/445929040/The-Mamba-Mentality-How-I-Play"
        self.common_test(local_url, ScribdTestCases.bryant_live, Scribd())


