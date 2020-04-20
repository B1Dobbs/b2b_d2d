from book_data import BookData, Format, ParseStatus
from book_site.audiobooks import Audiobooks

class AudiobooksTestCases():

    lackey_local = {
            "format" : Format.AUDIO_BOOK, 
            "title" : "Nail’s Crossing", 
            "subtitle" : "A Novel",
            "image" : None,
            "image_url" : "https://covers.audiobooks.com/images/covers/full/9781455123124.jpg",
            "isbn_13" : "9781455123124",
            "description" : "This debut mystery from a fresh voice in Southwestern fiction stakes",
            "series" : None,
            "vol_number" : None,
            "authors" : ['Kris Lackey', 'Mark Bramhall'],
            "ready_for_sale" : True,
            "site_slug" : Audiobooks.SLUG,
            "parse_status" : ParseStatus.FULLY_PARSED,
            "book_id" : "nails-crossing-a-novel/303764",
            "url" : "test/audiobooks/test_pages/nails_crossing_lackey.html",
            "content" : None,
            "extra" : {'Price': '0.0'}
        } 

    #These are the items that should have different results from the local test
    lackey_live =  {
            **lackey_local,
            "url" : "https://www.audiobooks.com/audiobook/nails-crossing-a-novel/303764",
    } 

    patterson_local = {
        "format" : Format.AUDIO_BOOK,
        "title" : "Blindside", 
        "subtitle" : None,
        "image" : None,
        "image_url" : "https://covers.audiobooks.com/images/covers/full/9781549118913.jpg",
        "isbn_13" : "9781549118913",
        "description" : "The mayor of New York has a daughter who's missing and in danger.",
        "series" : None,
        "vol_number" : None,
        "authors" : ['James O. Born', 'James Patterson', 'Danny Mastrogiorgio'],
        "ready_for_sale" : True,
        "site_slug" : Audiobooks.SLUG,
        "parse_status" : ParseStatus.FULLY_PARSED,
        "book_id" : "blindside/405228",
        "url" : "test/audiobooks/test_pages/blindside_patterson.html",
        "content" : None,
        "extra" : {'Price': '26.98'}
    } 

    #These are the items that should have different results from the local test
    patterson_live =  {
            **patterson_local, 
            "url" : "https://www.audiobooks.com/audiobook/blindside/405228",
    } 

    lewis_local = {
        "format" : Format.AUDIO_BOOK, 
        "title" : "The Chronicles of Narnia Adult Box Set", 
        "subtitle" : None,
        "image" : None,
        "image_url" : "https://covers.audiobooks.com/images/covers/full/9780061999888.jpg",
        "isbn_13" : "9780061999888",
        "description" : "For over sixty years, readers of all ages have been enchanted by the magical realms",
        "series" : None,
        "vol_number" : None,
        "authors" : ['C.S. Lewis', 'Kenneth Branagh', 'Derek Jacobi', 'Lynn Redgrave', 'Michael York', 'Alex Jennings', 'Patrick Stewart', 'Jeremy Northam'],
        "ready_for_sale" : True,
        "site_slug" : Audiobooks.SLUG,
        "parse_status" : ParseStatus.FULLY_PARSED,
        "book_id" : "chronicles-of-narnia-adult-box-set/347498",
        "url" : "test/audiobooks/test_pages/narnia_lewis.html",
        "content" : None,
        "extra" : {'Price': '46.99'}
    } 

    #These are the items that should have different results from the local test
    lewis_live =  {
            **lewis_local,
            "url" : "https://www.audiobooks.com/audiobook/chronicles-of-narnia-adult-box-set/347498",
    } 

    links_audiobook = ['https://www.audiobooks.com/audiobook/finding-god-in-the-land-of-narnia/218641',
		'https://www.audiobooks.com/audiobook/family-guide-to-narnia-biblical-truths-in-c-s-lewiss-the-chronicles-of-narnia/413188',
		'https://www.audiobooks.com/audiobook/everything-guide-to-c-s-lewis-and-narnia/341034',
		'https://www.audiobooks.com/audiobook/what-i-learned-in-narnia/388132',
		'https://www.audiobooks.com/audiobook/planet-narnia-the-seven-heavens-in-the-imagination-of-c-s-lewis/375557',
		'https://www.audiobooks.com/audiobook/world-according-to-narnia-christian-meaning-in-c-s-lewiss-beloved-chronicles/139468',
		'https://www.audiobooks.com/audiobook/narnian-the-life-and-imagination-of-c-s-lewis/33977',
		'https://www.audiobooks.com/audiobook/chronicles-of-narnia-adult-box-set/347498',
		'https://www.audiobooks.com/audiobook/magicians-nephew/102415',
		'https://www.audiobooks.com/audiobook/hidden-rock-rescue/279740',
		'https://www.audiobooks.com/audiobook/mission-to-moon-farm/269378',
		'https://www.audiobooks.com/audiobook/bearhaven-book-1-secrets-of-bearhaven/251520',
		'https://www.audiobooks.com/audiobook/picture-of-dorian-gray-penguin-classics/382867',
		'https://www.audiobooks.com/audiobook/master-of-one-find-and-focus-on-the-work-you-were-created-to-do/381183',
		'https://www.audiobooks.com/audiobook/childrens-home/251297',
		'https://www.audiobooks.com/audiobook/soul-of-the-lionthe-witch-and-the-wardrobe/340711',
		'https://www.audiobooks.com/audiobook/furthermore/269505',
		'https://www.audiobooks.com/audiobook/nethergrim/211165',
		'https://www.audiobooks.com/audiobook/c-s-lewis-a-life-eccentric-genius-reluctant-prophet/194083',
		'https://www.audiobooks.com/audiobook/jane-eyre/395639']
