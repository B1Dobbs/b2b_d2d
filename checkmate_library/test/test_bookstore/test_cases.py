from book_data import BookData, Format, ParseStatus
from book_site.test_bookstore import TestBookstore

class TestBookstoreTestCases():

    morgan_local = {
            "format" : Format.DIGITAL, 
            "title" : "Moms Against Zombies", 
            "subtitle" : None,
            "image" : None,
            "image_url" : None,
            "isbn_13" : "9781386842842",
            "description" : "Emma Jackson is an army wife and new mom",
            "series" : "Against Zombies",
            "vol_number" : "1.0",
            "authors" : ['Alathia Paris Morgan'],
            "ready_for_sale" : True,
            "site_slug" : TestBookstore.SLUG,
            "parse_status" : ParseStatus.FULLY_PARSED,
            "book_id" : "9781386842842",
            "url" : "test/test_bookstore/test_pages/moms_against_zombies_morgan.html",
            "content" : None,
            "extra" : {'Price': ' $5.99', 'ReleaseDate': ' June 5, 2018'}
        } 

    #These are the items that should have different results from the local test
    morgan_live =  {
            **morgan_local,
            "url" : "http://127.0.0.1:8000/library/9781386842842/",
    } 

    walker_local = {
        "format" : Format.DIGITAL, #Have to use live url to determine its an Audiobook
        "title" : "Ruin Me", 
        "subtitle" : None,
        "image" : None,
        "image_url" : None,
        "isbn_13" : "9781386944362",
        "description" : "The perfect romance!",
        "series" : "Vegas Knights",
        "vol_number" : None,
        "authors" : ['Bella Love-Wins', 'Shiloh Walker'],
        "ready_for_sale" : True,
        "site_slug" : TestBookstore.SLUG,
        "parse_status" : ParseStatus.FULLY_PARSED,
        "book_id" : "9781386944362",
        "url" : "test/test_bookstore/test_pages/ruin_me_walker.html",
        "content" : None,
        "extra" : {'Price': ' $9.99', 'ReleaseDate': ' Sept. 26, 2017'}
    } 

    #These are the items that should have different results from the local test
    walker_live =  {
            **walker_local, 
            "url" : "http://127.0.0.1:8000/library/9781386944362/",
    } 

    reid_local = {
        "format" : Format.DIGITAL, 
        "title" : "Ancient Voices", 
        "subtitle" : "Into the Depths",
        "image" : None,
        "image_url" : None,
        "isbn_13" : "9781533791917",
        "description" : "The Kinship rides victorious into the small village",
        "series" : "Wind Rider Chronicles",
        "vol_number" : "2.0",
        "authors" : ['Allison D. Reid'],
        "ready_for_sale" : True,
        "site_slug" : TestBookstore.SLUG,
        "parse_status" : ParseStatus.FULLY_PARSED,
        "book_id" : "9781533791917",
        "url" : "test/test_bookstore/test_pages/ancient_voices_reid.html",
        "content" : None,
        "extra" : {'Price': ' $7.99', 'ReleaseDate': ' Nov. 12, 2015'}
    } 

    #These are the items that should have different results from the local test
    reid_live =  {
            **reid_local,
            "url" : "http://127.0.0.1:8000/library/9781533791917/",
    } 

    links_book = ['http://127.0.0.1:8000/testBookstore/library/9781524243456/',
		'http://127.0.0.1:8000/testBookstore/library/9781927767498/',
		'http://127.0.0.1:8000/testBookstore/library/9781386820031/',
		'http://127.0.0.1:8000/testBookstore/library/9781386420248/',
		'http://127.0.0.1:8000/testBookstore/library/9781386989752/',
		'http://127.0.0.1:8000/testBookstore/library/9781386865063/',
		'http://127.0.0.1:8000/testBookstore/library/9781386494683/',
		'http://127.0.0.1:8000/testBookstore/library/9781386910961/',
		'http://127.0.0.1:8000/testBookstore/library/9781515044413/',
		'http://127.0.0.1:8000/testBookstore/library/9781386172093/']
