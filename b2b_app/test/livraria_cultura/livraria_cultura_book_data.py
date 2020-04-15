import unittest
import sys
sys.path.append(".")
from book_site.livraria_cultura import LivrariaCultura
from checkmate import get_book_site
from base_book_parse_test import BaseBookParseTest
from livraria_cultura.test_cases import LivrariaCulturaTestCases
  

class TestLivrariaCulturaBookDataLocal(BaseBookParseTest): 
    #@unittest.skip("Website down")
    def test_silvera(self):  
        local_url = "test/livraria_cultura/test_pages/what_if_its_us_silvera.html"
        self.common_test(local_url, LivrariaCulturaTestCases.silvera_local, LivrariaCultura())

    #@unittest.skip("Website down")
    def test_snowden(self):
        local_url = "test/livraria_cultura/test_pages/eterna_snowden.html"
        self.common_test(local_url, LivrariaCulturaTestCases.snowden_local, LivrariaCultura())

    #@unittest.skip("Website down")
    def test_aurelio(self):
        local_url = "test/livraria_cultura/test_pages/meditacoes_aurelio.html"
        self.common_test(local_url, LivrariaCulturaTestCases.aurelio_local, LivrariaCultura())

class TestLivrariaCulturaBookDataLive(BaseBookParseTest):
    #@unittest.skip("Website down")
    def test_silvera(self):  
        live_url = "https://www3.livrariacultura.com.br/what-if-its-us-2012739487/p"
        self.common_test(live_url, LivrariaCulturaTestCases.silvera_live, LivrariaCultura())
        
    #@unittest.skip("Website down")
    def test_snowden(self):
        live_url = "https://www3.livrariacultura.com.br/eterna-vigilancia-2112150829/p"
        self.common_test(live_url, LivrariaCulturaTestCases.snowden_live, LivrariaCultura())

    #@unittest.skip("Website down")
    def test_aurelio(self):
        live_url = "https://www3.livrariacultura.com.br/meditacoes-2112189903/p"
        self.common_test(live_url, LivrariaCulturaTestCases.aurelio_live, LivrariaCultura())


