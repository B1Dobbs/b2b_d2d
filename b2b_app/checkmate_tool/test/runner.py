import unittest
import sys
from scribd.tests import TestScribdBookDataLocal, TestScribdBookDataLive, TestScribdLinks
from google_books.google_book_data import TestGoogleBookDataLocal, TestGoogleBookDataLive
from kobo.tests import TestKoboBookDataLocal, TestKoboBookDataLive, TestKoboLinks
from test_bookstore.test_bookstore_book_data import TestTestBookstoreBookDataLocal, TestTestBookstoreBookDataLive
from livraria_cultura.livraria_cultura_book_data import TestLivrariaCulturaBookDataLocal, TestLivrariaCulturaBookDataLive
from audiobooks.tests import TestAudiobooksBookDataLocal, TestAudiobooksBookDataLive, TestAudiobooksLinks
from book_site.google_books import GoogleBooks
from book_site.kobo import Kobo
from book_site.livraria_cultura import LivrariaCultura
from book_site.scribd import Scribd
from book_site.test_bookstore import TestBookstore
from book_site.audiobooks import Audiobooks

def load_local_tests(loader, slugs):
    tests = []

    if Scribd.SLUG in slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestScribdBookDataLocal)
    if GoogleBooks.SLUG in slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestGoogleBookDataLocal)
    if Kobo.SLUG in slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestKoboBookDataLocal)
    if TestBookstore.SLUG in slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestTestBookstoreBookDataLocal)
        tests += loader.loadTestsFromTestCase(TestTestBookstoreBookDataLive)
    if LivrariaCultura.SLUG in slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestLivrariaCulturaBookDataLocal)
    if Audiobooks.SLUG in slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestAudiobooksBookDataLocal)
    return tests

def load_live_tests(loader, slugs):
    tests = []

    if Scribd.SLUG in slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestScribdBookDataLive)
    if GoogleBooks.SLUG in slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestGoogleBookDataLive)
    if Kobo.SLUG in slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestKoboBookDataLive)
    if TestBookstore.SLUG in slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestTestBookstoreBookDataLive)
    if LivrariaCultura.SLUG in slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestLivrariaCulturaBookDataLive)
    if Audiobooks.SLUG in slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestAudiobooksBookDataLive)
    return tests

'''Only conducted locally - Cannot test live dynamically loaded links'''
def load_link_search(loader, slugs):
    tests = []
    if Scribd.SLUG in slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestScribdLinks)
    if Audiobooks.SLUG in slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestAudiobooksLinks)
    if Kobo.SLUG in slugs or slugs == None:
        tests += loader.loadTestsFromTestCase(TestKoboLinks)
    return tests


#https://stackoverflow.com/questions/5360833/how-to-run-multiple-classes-in-single-test-suite-in-python-unit-testing/16823869
if __name__ == '__main__':
    # Run only the tests in the specified classes

    #test_classes_to_run = [TestScribdBookDataLocal]

    loader = unittest.TestLoader()
    suite  = unittest.TestSuite()

    tests = load_link_search(loader, {Kobo.SLUG})
    #tests += load_link_search(loader, {Scribd.SLUG})

    suite.addTests(tests)
    
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)

    # suites_list = []
    # for test_class in test_classes_to_run:
    #     suite = loader.loadTestsFromTestCase(test_class)
    #     suites_list.append(suite)

    # big_suite = unittest.TestSuite(suites_list)

    # runner = unittest.TextTestRunner()
    # results = runner.run(big_suite)