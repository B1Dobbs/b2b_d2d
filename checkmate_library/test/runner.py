import unittest
import sys
from scribd.tests import TestScribdBookDataLocal, TestScribdBookDataLive, TestScribdLinks
from google_books.tests import TestGoogleBooksDataLocal, TestGoogleBooksDataLive, TestGoogleBooksLinks
from kobo.tests import TestKoboBookDataLocal, TestKoboBookDataLive, TestKoboLinks
from test_bookstore.tests import TestTestBookstoreBookDataLocal, TestTestBookstoreBookDataLive, TestTestBookstoreLinks
from livraria_cultura.tests import TestLivrariaCulturaBookDataLocal, TestLivrariaCulturaBookDataLive, TestLivrariaCulturaLinks
from audiobooks.tests import TestAudiobooksBookDataLocal, TestAudiobooksBookDataLive, TestAudiobooksLinks
from book_site.google_books import GoogleBooks
from book_site.kobo import Kobo
from book_site.livraria_cultura import LivrariaCultura
from book_site.scribd import Scribd
from book_site.test_bookstore import TestBookstore
from book_site.audiobooks import Audiobooks
import argparse

def load_book_local(loader, slugs):
    tests = []

    if Scribd.SLUG == slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestScribdBookDataLocal)
    if GoogleBooks.SLUG == slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestGoogleBooksDataLocal)
    if Kobo.SLUG == slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestKoboBookDataLocal)
    if TestBookstore.SLUG == slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestTestBookstoreBookDataLocal)
    if LivrariaCultura.SLUG == slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestLivrariaCulturaBookDataLocal)
    if Audiobooks.SLUG == slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestAudiobooksBookDataLocal)
    return tests


'''Live tests are here to make it easy to identify is a book site has redone a page. 
Data on live sites changes all the time but these tests are here to make testing the live
site easier with the right data in the test case.'''
def load_book_live(loader, slugs):
    tests = []

    if Scribd.SLUG == slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestScribdBookDataLive)
    if GoogleBooks.SLUG == slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestGoogleBooksDataLive)
    if Kobo.SLUG == slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestKoboBookDataLive)
    if TestBookstore.SLUG == slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestTestBookstoreBookDataLive)
    if LivrariaCultura.SLUG == slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestLivrariaCulturaBookDataLive)
    if Audiobooks.SLUG == slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestAudiobooksBookDataLive)
    return tests

'''Only conducted locally - Cannot test live dynamically loaded links'''
def load_link_search(loader, slugs):
    tests = []
    if Scribd.SLUG == slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestScribdLinks)
    if Audiobooks.SLUG == slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestAudiobooksLinks)
    if Kobo.SLUG == slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestKoboLinks)
    if LivrariaCultura.SLUG == slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestLivrariaCulturaLinks)
    if GoogleBooks.SLUG == slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestGoogleBooksLinks)
    if TestBookstore.SLUG == slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestTestBookstoreLinks)
    return tests


#https://stackoverflow.com/questions/5360833/how-to-run-multiple-classes-in-single-test-suite-in-python-unit-testing/16823869
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Tests to run")
    parser.add_argument("-l", "--Live", action='store_true', help = "Will run live tests rather than local.")
    parser.add_argument('site_slug', nargs="?")

    argument = parser.parse_args()
    print(argument)

    loader = unittest.TestLoader()
    suite  = unittest.TestSuite()

    if argument.Live:
        print(argument.site_slug)
        tests = load_book_live(loader, argument.site_slug)
    else:
        tests = load_link_search(loader, argument.site_slug)
        tests += load_book_local(loader, argument.site_slug)

    suite.addTests(tests)
    
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)