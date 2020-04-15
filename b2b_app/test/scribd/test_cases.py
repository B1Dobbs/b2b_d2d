from book_data import BookData, Format, ParseStatus
from book_site.scribd import Scribd

class ScribdTestCases():

    collins_local = {
            "format" : Format.AUDIO_BOOK, 
            "title" : "The Hunger Games", 
            "subtitle" : "Special Edition",
            "image" : None,
            "image_url" : "https://imgv2-2-f.scribdassets.com/img/audiobook_square_badge/389029058/original/216x216/eeb9d14dfe/1585934067?v=1",
            "isbn_13" : "9781338334906",
            "description" : "Emmy Award-winning actress Tatiana Maslany",
            "series" : None,
            "vol_number" : None,
            "authors" : ['Suzanne Collins', 'Tatiana Maslany'],
            "ready_for_sale" : True,
            "site_slug" : Scribd.SLUG,
            "parse_status" : ParseStatus.FULLY_PARSED,
            "book_id" : "audiobook/389029058/The-Hunger-Games-Special-Edition",
            "url" : "test/scribd/test_pages/the_hunger_games_by_suzanne_collins.html",
            "content" : None,
            "extra" : None
        } 

    #These are the items that should have different results from the local test
    collins_live =  {
            **collins_local,
            "url" : "https://www.scribd.com/audiobook/389029058/The-Hunger-Games-Special-Edition",
    } 

    dalio_local = {
        "format" : Format.DIGITAL, 
        "title" : "Principles", 
        "subtitle" : "Life and Work",
        "image" : None,
        "image_url" : "https://imgv2-2-f.scribdassets.com/img/word_document/357813054/original/216x287/2b5f9477ff/1586017758?v=1",
        "isbn_13" : "9781501124051",
        "description" : "Ray Dalio, one of the world’s most",
        "series" : None,
        "vol_number" : None,
        "authors" : ['Ray Dalio'],
        "ready_for_sale" : True,
        "site_slug" : Scribd.SLUG,
        "parse_status" : ParseStatus.FULLY_PARSED,
        "book_id" : "book/357813054/Principles-Life-and-Work",
        "url" : "test/scribd/test_pages/principles_by_ray_dalio.html",
        "content" : None,
        "extra" : None
    }

    #These are the items that should have different results from the local test
    dalio_live =  {
            **dalio_local,
            "url" : "https://www.scribd.com/book/357813054/Principles-Life-and-Work",
    } 

    bryant_local = {
        "format" : Format.DIGITAL, 
        "title" : "The Mamba Mentality", 
        "subtitle" : "How I Play",
        "image" : None,
        "image_url" : "https://imgv2-2-f.scribdassets.com/img/word_document/445929040/original/216x287/3b641d389b/1586081667?v=1",
        "isbn_13" : "9780374719159",
        "description" : "The Mamba Mentality: How I Play is Kobe Bryant’s personal perspective",
        "series" : None,
        "vol_number" : None,
        "authors" : ['Kobe Bryant', 'Phil Jackson', 'Pau Gasol'],
        "ready_for_sale" : True,
        "site_slug" : Scribd.SLUG,
        "parse_status" : ParseStatus.FULLY_PARSED,
        "book_id" : "book/445929040/The-Mamba-Mentality-How-I-Play",
        "url" : "test/scribd/test_pages/the_mamba_mentality_by_kobe_bryant.html",
        "content" : None,
        "extra" : None
    }

    #These are the items that should have different results from the local test
    bryant_live =  {
            **bryant_local,
            "url" : "https://www.scribd.com/book/445929040/The-Mamba-Mentality-How-I-Play",
    } 

    