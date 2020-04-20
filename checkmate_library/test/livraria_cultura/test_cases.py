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


    links_book = ['https://www3.livrariacultura.com.br/snowdens-box-2013190773/p',
		'https://www3.livrariacultura.com.br/snowden-sin-un-lugar-donde-esconderse-2013252329/p',
		'https://www3.livrariacultura.com.br/snowden-2010954187/p',
		'https://www3.livrariacultura.com.br/snowden-86300321/p',
		'https://www3.livrariacultura.com.br/snowden-white-and-the-seven-short-mexicans-111598926/p',
		'https://www3.livrariacultura.com.br/snowden-2011302858/p',
		'https://www3.livrariacultura.com.br/pendejo-snowden-111166232/p',
		'https://www3.livrariacultura.com.br/edward-snowden-111074337/p',
		'https://www3.livrariacultura.com.br/beyond-snowden-2010391283/p',
		'https://www3.livrariacultura.com.br/arquivos-snowden-os-42200057/p',
		'https://www3.livrariacultura.com.br/beyond-snowden-111311798/p',
		'https://www3.livrariacultura.com.br/ciencias-politicas-edward-snowden-duthel-heinz-60357942/p',
		'https://www3.livrariacultura.com.br/the-snowden-files-103207007/p',
		'https://www3.livrariacultura.com.br/on-snowden-mountain-2011924653/p',
		'https://www3.livrariacultura.com.br/the-story-of-snowden-111158697/p',
		'https://www3.livrariacultura.com.br/the-snowden-avalanche-112104710/p',
		'https://www3.livrariacultura.com.br/journalism-after-snowden-112074031/p',
		'https://www3.livrariacultura.com.br/beyond-edward-snowden-2013102908/p',
		'https://www3.livrariacultura.com.br/the-post-snowden-era-111095647/p',
		'https://www3.livrariacultura.com.br/surveillance-after-snowden-95969820/p',
		'https://www3.livrariacultura.com.br/the-snowden-files-111973025/p',
		'https://www3.livrariacultura.com.br/ciencias-politicas-el-caso-snowden-lefebure-antoine-111230270/p',
		'https://www3.livrariacultura.com.br/summary-permanent-record-by-edward-snowden-2013042157/p',
		'https://www3.livrariacultura.com.br/if-i-was-analyzing-edward-snowden-108296114/p']

    