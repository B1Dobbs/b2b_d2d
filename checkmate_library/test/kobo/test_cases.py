from book_data import BookData, Format, ParseStatus
from book_site.kobo import Kobo

class KoboTestCases():

    austin_local = {
            "format" : Format.DIGITAL, 
            "title" : "Pride And Prejudice", 
            "subtitle" : None,
            "image" : None,
            "image_url" : "https://kbimages1-a.akamaihd.net/f665d1cd-f3f5-4f9a-b2e0-c0cfbeb7d3ff/353/569/90/False/pride-and-prejudice-27.jpg",
            "isbn_13" : "9781610420891",
            "description" : "Jane Austen's classic love story is presented here",
            "series" : None,
            "vol_number" : None,
            "authors" : ['Jane Austen'],
            "ready_for_sale" : True,
            "site_slug" : Kobo.SLUG,
            "parse_status" : ParseStatus.FULLY_PARSED,
            "book_id" : "pride-and-prejudice-27",
            "url" : "test/kobo/test_pages/pride_and_prejudice_austin.html",
            "content" : None,
            "extra" : {'Price': '$0.99', 'Release Date': 'July 21, 2010'}
        } 

    #These are the items that should have different results from the local test
    austin_live =  {
            **austin_local,
            "url" : "https://www.kobo.com/us/en/ebook/pride-and-prejudice-27",
    } 

    chbosky_local = {
        "format" : Format.AUDIO_BOOK, #Have to use live url to determine its an Audiobook
        "title" : "The Perks of Being a Wallflower", 
        "subtitle" : None,
        "image" : None,
        "image_url" : "https://kbimages1-a.akamaihd.net/c660676f-62d9-420c-adf2-172a7da5ba7f/353/569/90/False/the-perks-of-being-a-wallflower-6.jpg",
        "isbn_13" : "9781508251552",
        "description" : "Now with a brand-new afterword to mark the 20th anniversary",
        "series" : None,
        "vol_number" : None,
        "authors" : ['Stephen Chbosky', 'Noah Galvin'],
        "ready_for_sale" : True,
        "site_slug" : Kobo.SLUG,
        "parse_status" : ParseStatus.FULLY_PARSED,
        "book_id" : "the-perks-of-being-a-wallflower-6",
        "url" : "test/kobo/test_pages/the_perks_of_being_a_wallflower_chbosky.html",
        "content" : None,
        "extra" : {'Price': '$17.99', 'Release Date': 'September 19, 2017'}
    } 

    #These are the items that should have different results from the local test
    chbosky_live =  {
            **chbosky_local, 
            "url" : "https://www.kobo.com/us/en/audiobook/the-perks-of-being-a-wallflower-6",
    } 

    roth_local = {
        "format" : Format.DIGITAL, 
        "title" : "Divergent", 
        "subtitle" : None,
        "image" : None,
        "image_url" : "https://kbimages1-a.akamaihd.net/e173f164-fbdd-4110-8f63-161d29b887a6/353/569/90/False/divergent-1.jpg",
        "isbn_13" : "9780062077011",
        "description" : "This first book in Veronica Roth's #1 New York Times",
        "series" : "Divergent Series",
        "vol_number" : "1",
        "authors" : ['Veronica Roth'],
        "ready_for_sale" : True,
        "site_slug" : Kobo.SLUG,
        "parse_status" : ParseStatus.FULLY_PARSED,
        "book_id" : "divergent-1",
        "url" : "test/kobo/test_pages/divergent_1_roth.html",
        "content" : None,
        "extra" : {'Price': '$7.99', 'Release Date': 'May 3, 2011'}
    } 

    #These are the items that should have different results from the local test
    roth_live =  {
            **roth_local,
            "url" : "https://www.kobo.com/us/en/ebook/divergent-1",
    } 

    links_audiobook = ['https://www.kobo.com/us/en/audiobook/the-hunger-games-special-edition',
		'https://www.kobo.com/us/en/audiobook/anarchy-23',
		'https://www.kobo.com/us/en/audiobook/suzanne-collins-2',
		'https://www.kobo.com/us/en/audiobook/the-dark-fantastic-8',
		'https://www.kobo.com/us/en/audiobook/finding-god-in-the-hunger-games-1',
		'https://www.kobo.com/us/en/audiobook/101-amazing-facts-about-the-hunger-games-1',
		'https://www.kobo.com/us/en/audiobook/jennifer-lawrence-6',
		'https://www.kobo.com/us/en/audiobook/the-hunger-but-mainly-death-games-1',
		'https://www.kobo.com/us/en/audiobook/a-hunger-like-no-other-5',
		'https://www.kobo.com/us/en/audiobook/the-hunger-35',
		'https://www.kobo.com/us/en/audiobook/wild-hunger-8',
		'https://www.kobo.com/us/en/audiobook/the-body-book-8']

    links_book = ['https://www.kobo.com/us/en/ebook/the-hunger-games-official-illustrated-movie-companion',
		'https://www.kobo.com/us/en/ebook/the-hunger-games-catching-fire-the-official-illustrated-movie-companion',
		'https://www.kobo.com/us/en/ebook/mockingjay-the-final-book-of-the-hunger-games',
		'https://www.kobo.com/us/en/ebook/catching-fire-hunger-games-book-two',
		'https://www.kobo.com/us/en/ebook/the-hunger-games-hunger-games-book-one',
		'https://www.kobo.com/us/en/ebook/the-hunger-games-trilogy',
		'https://www.kobo.com/us/en/ebook/the-ballad-of-songbirds-and-snakes-a-hunger-games-novel',
		'https://www.kobo.com/us/en/ebook/the-hunger-games-tribute-guide',
		'https://www.kobo.com/us/en/ebook/the-world-of-the-hunger-games',
		'https://www.kobo.com/us/en/ebook/the-unofficial-recipes-of-the-hunger-games-187-recipes-inspired-by-the-hunger-games-catching-fire-and-mockingjay-1',
		'https://www.kobo.com/us/en/ebook/the-hunger-games-instructional-guides-for-literature',
		'https://www.kobo.com/us/en/ebook/the-hunger-games-catching-fire-piano-songbook'
    ]
