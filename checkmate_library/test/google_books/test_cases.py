from book_data import BookData, Format, ParseStatus
from book_site.google_books import GoogleBooks

class GoogleBooksTestCases():

    adams_local = {
            "format" : Format.DIGITAL, 
            "title" : "Murder and Intrigue on the Mexican Border", 
            "subtitle" : None,
            "image" : None,
            "image_url" : "https://books.google.com/books/content/images/frontcover/-lRoDwAAQBAJ?fife",
            "isbn_13" : "9781623495855",
            "description" : "In early 1914, Clemente Vergara discovered",
            "series" : "Elma Dill Russell Spencer Series in the West and Southwest",
            "vol_number" : "Book 43",
            "authors" : ['John A. Adams'],
            "ready_for_sale" : True,
            "site_slug" : GoogleBooks.SLUG,
            "parse_status" : ParseStatus.FULLY_PARSED,
            "book_id" : "-lRoDwAAQBAJ&hl",
            "url" : "test/google_books/test_pages/murder_and_intrigue_on_the_mexican_border_by_adams.html",
            "content" : None,
            "extra" : {'Price': '$9.99'}
        } 

    #These are the items that should have different results from the local test
    adams_live =  {
            **adams_local,
            "url" : "https://play.google.com/store/books/details?id=-lRoDwAAQBAJ&source=gbs_api",
    } 

    dickens_local = {
        "format" : Format.DIGITAL, #Have to use live url to determine its an Audiobook
        "title" : "A Tale of Two Cities", 
        "subtitle" : None,
        "image" : None,
        "image_url" : "https://lh3.googleusercontent.com/qSHBZcK21sEgTKIqo6d8TEh0Kp-pcQMeQKQrBv5bqlQD6sIjV9ej0iXO5EQbaB7qGxVWi2wx7VAx",
        "isbn_13" : "9782378981556",
        "description" : "A Tale of Two Cities is a novel by Charles Dickens",
        "series" : None,
        "vol_number" : None,
        "authors" : ['Charles Dickens'],
        "ready_for_sale" : True,
        "site_slug" : GoogleBooks.SLUG,
        "parse_status" : ParseStatus.FULLY_PARSED,
        "book_id" : "AQAAAECMCD9IoM&hl",
        "url" : "test/google_books/test_pages/a_tale_of_two_cities_dickens.html",
        "content" : None,
        "extra" : {'Price': '$3.99'}
    } 

    #These are the items that should have different results from the local test
    dickens_live =  {
            **dickens_local,
            "format" : Format.AUDIO_BOOK, 
            "url" : "https://play.google.com/store/audiobooks/details/Charles_Dickens_A_Tale_of_Two_Cities?id=AQAAAECMCD9IoM&hl=en_US",
    } 

    sandford_local = {
        "format" : Format.DIGITAL, 
        "title" : "Neon Prey", 
        "subtitle" : None,
        "image" : None,
        "image_url" : "https://books.google.com/books/content/images/frontcover/m75mDwAAQBAJ?fife",
        "isbn_13" : "9780525536598",
        "description" : "Lucas Davenport tracks a prolific serial killer",
        "series" : "A Prey Novel",
        "vol_number" : "Book 29",
        "authors" : ['John Sandford'],
        "ready_for_sale" : True,
        "site_slug" : GoogleBooks.SLUG,
        "parse_status" : ParseStatus.FULLY_PARSED,
        "book_id" : "m75mDwAAQBAJ&hl",
        "url" : "test/google_books/test_pages/neon_prey_sandford.html",
        "content" : None,
        "extra" : {'Price': '$9.99'}
    } 

    #These are the items that should have different results from the local test
    sandford_live =  {
            **sandford_local,
            "url" : "https://play.google.com/store/books/details/John_Sandford_Neon_Prey?id=m75mDwAAQBAJ&hl=en_US",
    } 

    links_book = ['https://play.google.com/store/books/details?id=vMYVAAAAYAAJ&source=gbs_api',
		'http://books.google.com/books?id=JHVwuAAACAAJ&dq=charles+dickens&hl=&source=gbs_api',
		'https://play.google.com/store/books/details?id=0pprAwAAQBAJ&source=gbs_api',
		'https://play.google.com/store/books/details?id=uilZDwAAQBAJ&source=gbs_api',
		'https://play.google.com/store/books/details?id=bT5WAAAAcAAJ&source=gbs_api',
		'http://books.google.com/books?id=D0zFr3xc4bMC&dq=charles+dickens&hl=&source=gbs_api',
		'http://books.google.com/books?id=RJ_yAAAAMAAJ&dq=charles+dickens&hl=&source=gbs_api',
		'https://play.google.com/store/books/details?id=a71KDwAAQBAJ&source=gbs_api',
		'http://books.google.com/books?id=e6dlAAAAMAAJ&dq=charles+dickens&hl=&source=gbs_api',
		'http://books.google.com/books?id=j5c9GqZ_7BMC&dq=charles+dickens&hl=&source=gbs_api',
		'http://books.google.com/books?id=5ERSPN-ytEoC&dq=charles+dickens&hl=&source=gbs_api',
		'https://play.google.com/store/books/details?id=jYp91-w4HmIC&source=gbs_api',
		'http://books.google.com/books?id=AzYnFAaFb48C&dq=charles+dickens&hl=&source=gbs_api',
		'http://books.google.com/books?id=cTEfjV_1tscC&dq=charles+dickens&hl=&source=gbs_api',
		'http://books.google.com/books?id=m0QoSPuRTaEC&dq=charles+dickens&hl=&source=gbs_api',
		'http://books.google.com/books?id=7tcpAeDEx1AC&dq=charles+dickens&hl=&source=gbs_api',
		'http://books.google.com/books?id=OagmAQAAMAAJ&dq=charles+dickens&hl=&source=gbs_api',
		'http://books.google.com/books?id=jzUfAQAAIAAJ&dq=charles+dickens&hl=&source=gbs_api',
		'http://books.google.com/books?id=JaEjtYQG_lwC&dq=charles+dickens&hl=&source=gbs_api',
		'http://books.google.com/books?id=GUZvDwAAQBAJ&dq=charles+dickens&hl=&source=gbs_api',
		'http://books.google.com/books?id=GjIlriah_2EC&dq=charles+dickens&hl=&source=gbs_api']
