from Levenshtein import distance, ratio
import re

class ParseStatus:
    UNSUCCESSFUL = "UNSUCCESSFUL"
    FULLY_PARSED = "FULLY_PARSED"

class Format:
    DIGITAL = "DIGITAL"
    AUDIO_BOOK = "AUDIO_BOOK"
    PAPER_BACK = "PAPER_BACK"

_default_data = {
            "format" : None, 
            "title" : None, 
            "subtitle" : None,
            "image" : None,
            "image_url" : None,
            "isbn_13" : None,
            "description" : None,
            "series" : None,
            "vol_number" : None,
            "authors" : [],
            "ready_for_sale" : None,
            "site_slug" : None,
            "parse_status" : None,
            "book_id" : None,
            "url" : None,
            "content" : None,
            "extra" : None
        }

class BookData:

    def __init__(self):
        self.data = _default_data.copy()

    def __getattr__(self, item):
        if item in _default_data:
            return self.data[item]
        else:
            raise AttributeError("'BookData' object has no attribute '%s'" % item)

    def __setattr__(self, item, value):
        if item in _default_data:
            self.data[item] = value
            return self.data[item]
        else: 
            return super().__setattr__(item, value)

    def print_data(self):
        for k, v in self.data.items():
            k_name = k.capitalize() + ":"
            print("{0:16} {1}".format(k_name, v))

    def get_authors_as_string(self):
        pattern =  '[^A-Za-z0-9 ,]+'
        return re.sub(pattern, "", str(self.authors))

    def compare(self, book2):
        """ Calculates the perecent match between two book_data objects using the Levenshtein Formula

        Args:
            self (book_data): The book data used for the 1st book in the comparison
            book2 (book_data): The book data used for the 2nd book in the comparison

        Returns:
            float: the percent match between the two book_data objects
        """
        percent = 0
        count = 0
        # print(self.data.items())
        # print(book2.data.items())
        for attr, value in self.data.items():
            isEmptyList = value == [] or book2.data[attr] == []

            # Testing if both values of a certain attribute are none for both book_data objects
            # print(value)
            # print(book2.data[attr])
            if value != None and book2.data[attr] != None and not isEmptyList :

                # Creating a regex pattern that will filter out all special characters from the values
                pattern =  '[^A-Za-z0-9 ,]+'
                book2Str = str.lower(re.sub(pattern, "", str(book2.data[attr])))
                book1Str = str.lower(re.sub(pattern, "", str(self.data[attr])))

                # Testing if book2's value is a substring of book1's value
                # or if the distance (number of edits) are less than or equal to 5
                isSubstring = book2Str in book1Str or book1Str in book2Str
                if(isSubstring or distance(book2Str, book1Str) <= 5):
                    percent += ratio(book2Str, book1Str)
                count += 1

        # Testing if there were 0 matches else return the percent match rounded to the 2nd decimal place
        if count == 0 :
            return 0.0
        else:
            return round((percent / count), 2)
