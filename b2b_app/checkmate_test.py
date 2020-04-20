''' 
This is a test file for the Checkmate library identical to test_book_data.py in the checkmate_library module.
To install checkmate run: pip install -i https://test.pypi.org/simple/ checkmate-library
To run a test from this script: python checkmate_test.py SD
---SD is just an example but you can use any site slug.
To import into other files for use: from checkmate_library.checkmate import *
'''
import sys
sys.path.append("..\checkmate_library")
from checkmate import get_book_site, Scribd, LivrariaCultura, GoogleBooks, TestBookstore, Kobo, Audiobooks
from book_data import BookData, Format, ParseStatus

def testBookstore():
    book_site = get_book_site("TB")
    book_data = book_site.get_book_data("http://127.0.0.1:8000/library/9781524243456/")
    book_data.print_data()

def testKobo():
    book_site = get_book_site("KB")
    book_data = book_site.get_book_data("https://www.kobo.com/us/en/ebook/snow-white-before-the-hea-2")
    book_data.print_data()

def testLivrariaCultura():
    book_site = get_book_site("LC")
    book_data = book_site.get_book_data("https://www3.livrariacultura.com.br/what-if-its-us-2012739487/p")
    book_data.print_data()

def testScribd():
    book_site = get_book_site("SD")
    book_data = book_site.get_book_data("https://www.scribd.com/book/357813054/Principles-Life-and-Work")
    book_data.print_data()

def testGoogle():
    book_site = get_book_site("GB")
    book_data = book_site.get_book_data("https://play.google.com/store/books/details?id=-lRoDwAAQBAJ&source=gbs_api")
    book_data.print_data()

def testAudiobooks():
    book_site = get_book_site("AB")
    book_data = book_site.get_book_data("https://www.audiobooks.com/audiobook/chronicles-of-narnia-adult-box-set/347498")
    book_data.print_data()

'''Simple test for printing out the book data from a book site'''
if __name__ == "__main__":

    testToRun = sys.argv[1]

    """ Site Query Test for Scribd """
    if testToRun == Scribd.SLUG or testToRun == None:
        print("Starting test for Scribd.")
        testScribd()

    """ Site Query Test for Kobo """
    if testToRun == Kobo.SLUG or testToRun == None:
        print("Starting test for Kobo.")
        testKobo()

    """ Site Query Test for Google """
    if testToRun == GoogleBooks.SLUG or testToRun == None:
        print("Starting test for Google Books.")
        testGoogle()

    """ Site Query Test for Livraria Cultura """
    if testToRun == LivrariaCultura.SLUG or testToRun == None:
        print("Starting test for Livraria Cultura.")
        testLivrariaCultura()

    """ Site Query Test for Test Bookstore """
    if testToRun == TestBookstore.SLUG or testToRun == None:
        print("Starting test for Test Bookstore.")
        testBookstore()

    """ Site Query Test for Audiobooks """
    if testToRun == Audiobooks.SLUG or testToRun == None:
        print("Starting test for Audiobooks.")
        testAudiobooks()
