from book_data import BookData, Format, ParseStatus
from book_site.livraria_cultura import LivrariaCultura

class LivrariaCulturaTestCases():

    silvera_local = {
            "format" : Format.DIGITAL, 
            "title" : "WHAT IF IT'S US", 
            "subtitle" : None,
            "image" : None,
            "image_url" : "https://livrariacultura.vteximg.com.br/arquivos/ids/15991505-292-292/2012739487.jpg?v=637142235054270000",
            "isbn_13" : "9780062795243",
            "description" : "A New York Times, USA Today, and Indie bestseller!Critically acclaimed",
            "series" : None,
            "vol_number" : None,
            "authors" : ['BECKY ALBERTALLI', 'ADAM SILVERA'],
            "ready_for_sale" : True,
            "site_slug" : LivrariaCultura.SLUG,
            "parse_status" : ParseStatus.FULLY_PARSED,
            "book_id" : "/what-if-its-us-2012739487/p",
            "url" : "test/livraria_cultura/test_pages/what_if_its_us_silvera.html",
            "content" : None,
            "extra" : {'price': '32.59'}
        } 

    #These are the items that should have different results from the local test
    silvera_live =  {
            **silvera_local,
            "url" : "https://www3.livrariacultura.com.br/what-if-its-us-2012739487/p",
    } 

    snowden_local = {
        "format" : Format.DIGITAL, 
        "title" : "ETERNA VIGILÂNCIA", 
        "subtitle" : None,
        "image" : None,
        "image_url" : "https://livrariacultura.vteximg.com.br/arquivos/ids/16374331-292-292/2112150829.jpg?v=637193706490230000",
        "isbn_13" : "9788542217438",
        "description" : "Em 2013, Edward Snowden, ex-analista da CIA (Agência Central de Inteligência)",
        "series" : None,
        "vol_number" : None,
        "authors" : ['EDWARD SNOWDEN'],
        "ready_for_sale" : True,
        "site_slug" : LivrariaCultura.SLUG,
        "parse_status" : ParseStatus.FULLY_PARSED,
        "book_id" : "/eterna-vigilancia-2112150829/p",
        "url" : "test/livraria_cultura/test_pages/eterna_snowden.html",
        "content" : None,
        "extra" : {'price': '44.90'}
    }

    #These are the items that should have different results from the local test
    snowden_live =  {
            **snowden_local,
            "url" : "https://www3.livrariacultura.com.br/eterna-vigilancia-2112150829/p",
    } 

    aurelio_local = {
        "format" : Format.DIGITAL, 
        "title" : "MEDITAÇÕES", 
        "subtitle" : None,
        "image" : None,
        "image_url" : "https://livrariacultura.vteximg.com.br/arquivos/ids/16373915-292-292/2112189903.jpg?v=637193705287600000",
        "isbn_13" : "9788552100911",
        "description" : "Estas são anotações pessoais do imperador romano Marco Aurélio",
        "series" : None,
        "vol_number" : None,
        "authors" : ['MARCO AURELIO'],
        "ready_for_sale" : True,
        "site_slug" : LivrariaCultura.SLUG,
        "parse_status" : ParseStatus.FULLY_PARSED,
        "book_id" : "/meditacoes-2112189903/p",
        "url" : "test/livraria_cultura/test_pages/meditacoes_aurelio.html",
        "content" : None,
        "extra" : {'price': '25.13'}
    }

    #These are the items that should have different results from the local test
    aurelio_live =  {
            **aurelio_local,
            "url" : "https://www3.livrariacultura.com.br/meditacoes-2112189903/p",
    } 

    