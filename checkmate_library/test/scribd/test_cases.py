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

    links_book = ['https://www.scribd.com/book/353155930/Guide-to-The-Hunger-Games-The-World-of-The-Hunger-Games',
        'https://www.scribd.com/book/249308474/CliffsNotes-on-Collins-The-Hunger-Games',
        'https://www.scribd.com/book/283077581/The-Hunger-Games-The-Ultimate-Quiz-Book',
	    'https://www.scribd.com/book/224312747/The-Hunger-Pains-A-Parody',
		'https://www.scribd.com/book/161598128/The-Hunger-Games-AZ',
		'https://www.scribd.com/book/226412614/Quicklet-on-Suzanne-Collins-The-Hunger-Games',
		'https://www.scribd.com/book/182514522/The-Hunger-Games-Companion-The-Unauthorized-Guide-to-the-Series',
		'https://www.scribd.com/book/315606358/The-Hunger-Games-Literature-Kit-Gr-7-8',
		'https://www.scribd.com/book/226412073/Catching-Fire-Cookbook-Experience-The-Hunger-Games-Trilogy-with-Unofficial-Recipes-Inspired-by-Catching-Fire',
		'https://www.scribd.com/book/353174517/Beyond-District-12-The-Stars-of-The-Hunger-Games',
		'https://www.scribd.com/book/304217940/The-Hunger-Games-Behind-the-Story-A-Book-Companion',
		'https://www.scribd.com/book/336815394/The-Unofficial-Hunger-Games-Cookbook-From-Lamb-Stew-to-Groosling-More-than-150-Recipes-Inspired-by-The-Hunger-Games-Trilogy',
		'https://www.scribd.com/book/202769279/Study-Guide-The-Hunger-Games-Series-A-BookCaps-Study-Guide',
		'https://www.scribd.com/book/210942244/Study-Guide-The-Hunger-Games-Book-One-A-BookCaps-Study-Guide',
		'https://www.scribd.com/book/283078263/101-Amazing-Facts-about-The-Hunger-Games',
		'https://www.scribd.com/book/330631528/The-Hunger-Games-by-Suzanne-Collins-Book-Analysis-Detailed-Summary-Analysis-and-Reading-Guide',
		'https://www.scribd.com/book/210941330/Study-Guide-Mockingjay-The-Hunger-Games-Book-Three-A-BookCaps-Study-Guide',
		'https://www.scribd.com/book/194309531/The-World-s-Toughest-Hunger-Games-Quiz-Book',
		'https://www.scribd.com/book/351160351/Hunger-A-Memoir-of-My-Body',
		'https://www.scribd.com/book/393390807/Caraval',
		'https://www.scribd.com/book/224417324/The-Hunger',
		'https://www.scribd.com/book/225139445/The-Hunger',
		'https://www.scribd.com/book/224364303/Island-of-Silence',
		'https://www.scribd.com/book/122543478/Minecraft-For-Dummies',
		'https://www.scribd.com/book/306329139/Island-of-Dragons',
		'https://www.scribd.com/book/235681845/Island-of-Legends',
		'https://www.scribd.com/book/224266312/Island-of-Fire',
		'https://www.scribd.com/book/294395840/Fan-Phenomena-The-Hunger-Games',
		'https://www.scribd.com/book/193760374/Katniss-the-Cattail-An-Unauthorized-Guide-to-Names-and-Symbols-in-Suzanne-Collins-The-Hunger-Games',
		'https://www.scribd.com/book/333571163/Jennifer-Lawrence-The-Hunger-Games-Girl-on-Fire',
		'https://www.scribd.com/book/194786370/Ready-Reference-Treatise-The-Hunger-Games',
		'https://www.scribd.com/book/338709873/Hunting-Girls-Sexual-Violence-from-The-Hunger-Games-to-Campus-Rape',
		'https://www.scribd.com/book/431785374/The-Hunger-Games-SparkNotes-Literature-Guide',
		'https://www.scribd.com/book/202769276/Study-Guide-Catching-Fire-The-Hunger-Games-Book-Two-A-BookCaps-Study-Guide',
		'https://www.scribd.com/book/333569057/Jennifer-Lawrence-The-Hunger-Games-Girl-on-Fire',
		'https://www.scribd.com/book/253556033/Jennifer-Liam-and-Josh-An-Unauthorized-Biography-of-the-Stars-of-The-Hunger-Games',
		'https://www.scribd.com/book/248529800/The-Hunger-Games-101-Amazing-Facts-You-Didn-t-Know',
		'https://www.scribd.com/book/436273948/Defining-Dystopia-A-Genre-Between-The-Circle-and-The-Hunger-Games-A-Functional-Approach-to-Fiction',
		'https://www.scribd.com/book/269988968/The-Hunger-Games-101-Amazingly-True-Facts-You-Didn-t-Know',
		'https://www.scribd.com/book/452424972/FAME-Suzanne-Collins-The-creator-of-the-Hunger-Games',
		'https://www.scribd.com/book/340270751/Smart-Pop-Preview-2014-Standalone-Essays-on-Divergent-Zombies-the-Hunger-Games-Veronica-Mars-and-Fanfiction',
		'https://www.scribd.com/book/194846064/The-H-Unger-Games-Gone-Wild-A-Parody'
    ]

    links_audiobook = ['https://www.scribd.com/audiobook/389029058/The-Hunger-Games-Special-Edition',
		'https://www.scribd.com/audiobook/256094101/Hunger-Games',
		'https://www.scribd.com/audiobook/401485638/Catching-Fire-Special-Edition',
		'https://www.scribd.com/audiobook/401483969/Mockingjay-Special-Edition',
		'https://www.scribd.com/audiobook/281622947/The-Hunger-But-Mainly-Death-Games-A-Parody',
		'https://www.scribd.com/audiobook/237560397/Finding-God-in-The-Hunger-Games',
		'https://www.scribd.com/audiobook/337742398/101-Amazing-Facts-about-The-Hunger-Games',
		'https://www.scribd.com/audiobook/281642850/Red-Rising',
		'https://www.scribd.com/audiobook/371991881/Dragon-Bones',
		'https://www.scribd.com/audiobook/338628110/Dragon-Captives',
		'https://www.scribd.com/audiobook/286384349/Island-of-Shipwrecks-The-Unwanteds',
		'https://www.scribd.com/audiobook/405976444/Arena-1-Book-1-of-the-Survival-Trilogy',
		'https://www.scribd.com/audiobook/335431620/Jennifer-Lawrence-The-Hunger-Games-Girl-on-Fire',
		'https://www.scribd.com/audiobook/422142916/The-Dark-Fantastic-Race-and-the-Imagination-from-Harry-Potter-to-the-Hunger-Games',
		'https://www.scribd.com/audiobook/364167036/Suzanne-Collins-Author-of-the-Hunger-Games-Trilogy',
		'https://www.scribd.com/audiobook/246255614/The-Hunger-Gays',
		'https://www.scribd.com/audiobook/281628798/Golden-Son-Book-II-of-the-Red-Rising-Trilogy',
		'https://www.scribd.com/audiobook/266584922/Murder-Complex-2-The-The-Death-Code',
		'https://www.scribd.com/audiobook/402465426/Find-Me',
		'https://www.scribd.com/audiobook/409379926/Unite-Me',
		'https://www.scribd.com/audiobook/281647816/Highland-Hunger',
		'https://www.scribd.com/audiobook/329597661/The-Diabolic',
		'https://www.scribd.com/audiobook/390634463/The-Deepest-Blue-Tales-of-Renthia',
		'https://www.scribd.com/audiobook/237954340/Ignite-Me',
		'https://www.scribd.com/audiobook/286384236/The-Island-of-Graves',
		'https://www.scribd.com/audiobook/237977555/In-the-End',
		'https://www.scribd.com/audiobook/322718579/The-Call',
		'https://www.scribd.com/audiobook/408367636/Dragon-Curse',
		'https://www.scribd.com/audiobook/237893835/Rebel-Heart-Dust-Lands-Book-2',
		'https://www.scribd.com/audiobook/295944312/The-Capture',
		'https://www.scribd.com/audiobook/429880089/Red-Rising-Trilogy',
		'https://www.scribd.com/audiobook/358047620/Frankenstein-Dreams-A-Connoisseur-s-Collection-of-Victorian-Science-Fiction',
		'https://www.scribd.com/audiobook/405843683/Story-Structure-The-Key-to-Successful-Fiction',
		'https://www.scribd.com/audiobook/429862446/Murder-Complex',
		'https://www.scribd.com/audiobook/429861116/Spy-Girl',
		'https://www.scribd.com/audiobook/429984816/The-Hunt',
		'https://www.scribd.com/audiobook/398048264/The-Prince',
		'https://www.scribd.com/audiobook/308090103/Island-of-Dragons-The-Unwanteds',
		'https://www.scribd.com/audiobook/241862441/Artemis-The-Indomitable-Spirit-in-Everywoman',
		'https://www.scribd.com/audiobook/453736156/Shadowspell-Academy-The-Culling-Trials-Book-1',
		'https://www.scribd.com/audiobook/398047439/The-Dauntless',
		'https://www.scribd.com/audiobook/237587686/Glow']

    

    