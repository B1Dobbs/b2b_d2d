from book_data import BookData
import sys
from checkmate import get_book_site, Scribd, LivrariaCultura, GoogleBooks, TestBookstore, Kobo

    
def testSiteQuery(book_site):
    book_data = BookData()
    book_data.authors = ["vergara"]
    book_site.find_book_matches(book_data)
    

if __name__ == "__main__":

    testToRun = sys.argv[1]

    """ Site Query Test for Scribd """
    if testToRun == Scribd.SLUG or testToRun == None:
        print("Starting test for Scribd.")
        testSiteQuery(get_book_site("SD"))

    """ Site Query Test for Kobo """
    if testToRun == Kobo.SLUG or testToRun == None:
        print("Starting test for Kobo.")
        testSiteQuery(get_book_site("KB"))

    """ Site Query Test for Google """
    if testToRun == GoogleBooks.SLUG or testToRun == None:
        print("Starting test for Google Books.")
        testSiteQuery(get_book_site("GB"))

    """ Site Query Test for Livraria Cultura """
    if testToRun == LivrariaCultura.SLUG or testToRun == None:
        print("Starting test for Livraria Cultura.")
        testSiteQuery(get_book_site("KB"))

    """ Site Query Test for Test Bookstore """
    if testToRun == TestBookstore.SLUG or testToRun == None:
        print("Starting test for Test Bookstore.")
        testSiteQuery(get_book_site("TB"))
