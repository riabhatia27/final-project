import unittest

import data
from functions import search_movie


class Testing(unittest.TestCase):
    pass

# fix these
    def test_search_movie1(self):
        self.assertTrue(search_movie("Inception", "movies.txt"))

    def test_search_movie2(self):
        self.assertFalse(search_movie("Harry Potter and the Goblet of Fire", "movies.txt"))