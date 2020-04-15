from book_site.google_books import GoogleBooks
from book_site.kobo import Kobo
from book_site.livraria_cultura import LivrariaCultura
from book_site.scribd import Scribd
from book_site.test_bookstore import TestBookstore
from book_site.audiobooks import Audiobooks
"""
TB - TestBookstore
KB - Kobo
GB - Google Books
SD - Scribd
LC - LibrariaCultura
 """


def get_book_site(slug):
    """Will return one of the BookSite modules"""
    if slug == GoogleBooks.SLUG:
        return GoogleBooks()
    elif slug == Kobo.SLUG:
        return Kobo()
    elif slug == LivrariaCultura.SLUG:
        return LivrariaCultura()
    elif slug == Scribd.SLUG:
        return Scribd()
    elif slug == TestBookstore.SLUG:
        return TestBookstore()
    elif slug == Audiobooks.SLUG:
        return Audiobooks()
    else:
        print("Site Slug not found.")
    
