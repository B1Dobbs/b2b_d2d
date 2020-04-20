#from book_data import BookData, Format
import sys
from checkmate_library.checkmate import get_book_site, Audiobooks, GoogleBooks, Kobo, LivrariaCultura, Scribd, TestBookstore
from checkmate_library.book_data import BookData, Format, ParseStatus


def testSiteQuery(book_site):
    book_data = BookData()
    book_data.format = Format.AUDIO_BOOK
    book_data.authors = ["suzanne collins"]
    print(book_site.find_book_matches(book_data))
    
'''Simple test for printing out the matches from a book site'''
if __name__ == "__main__":

    testToRun = sys.argv[1]

    """ Site Query Test for Scribd """
    if testToRun == Scribd.SLUG or testToRun == None:
        print("Starting test for Scribd.")
        testSiteQuery(get_book_site("SD"))

    if testToRun == Audiobooks.SLUG or testToRun == None:
        print("Starting test for Audiobooks.")
        testSiteQuery(get_book_site("AB"))

    if testToRun == GoogleBooks.SLUG or testToRun == None:
        print("Starting test for GoogleBooks.")
        testSiteQuery(get_book_site("GB"))

    if testToRun == Kobo.SLUG or testToRun == None:
        print("Starting test for Kobo.")
        testSiteQuery(get_book_site("KB"))

    if testToRun == LivrariaCultura.SLUG or testToRun == None:
        print("Starting test for LivrariaCulture.")
        testSiteQuery(get_book_site("LC"))

    if testToRun == TestBookstore.SLUG or testToRun == None:
        print("Starting test for Test Bookstore.")
        testSiteQuery(get_book_site("TB"))