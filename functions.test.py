import unittest

import data
import functions
from functions import search_movie


class Testing(unittest.TestCase):
    pass

# function 1
    def test_search_movie1(self):
        self.assertFalse(search_movie("Inception", "movies.txt"))
            # fix this one

    def test_search_movie2(self):
        self.assertFalse(search_movie("Harry Potter and the Goblet of Fire", "movies.txt"))

# function 2
    def test_movies_above_rating1(self):
        self.movie1 = data.Movie(
            title="Shrek",
            genre="Comedy",
            duration=89,
            rating=7.9,
            actors=["Mike Myers, Eddie Murphy, Cameron Diaz"],
            director="Andrew Adamson",
            cast_racial_demographics={"White": 75, "Black": 25},
            language= "English",
            release_year= 2001,
            sales= {"North America" : 40, "Europe": 35, "Asia": 10, "South America": 8, "Africa": 5, "Oceania": 2},
            maturity= "PG",
            subtitles= {"English": True, "Spanish": True, "French": False, "German": False})

        self.movie2 = data.Movie(
            title="Superbad",
            genre="Comedy",
            duration=119,
            rating=7.6,
            actors=["Jonah Hill, Seth Rogen, Michael Cera"],
            director="Greg Mottola",
            cast_racial_demographics={"White": 90, "Black": 10},
            language="English",
            release_year=2007,
            sales={"North America": 65, "Europe": 20, "Asia": 5, "South America": 5, "Africa": 2, "Oceania": 3},
            maturity="R",
            subtitles={"English": True, "Spanish": True, "French": True, "German": True})

        self.movie3 = data.Movie(
            title="Barbie",
            genre="Comedy",
            duration=113,
            rating=6.8,
            actors=["Margot Robbie, Ryan Gosling, Will Ferrell"],
            director="Greta Gerwig",
            cast_racial_demographics={ "White": 60, "Black": 15,"Asian": 10, "Latino": 10, "Other": 5},
            language="English",
            release_year=2023,
            sales={"North America": 98, "Europe": 0, "Asia": 15, "South America": 7, "Africa": 3, "Oceania": 0},
            maturity="PG-13",
            subtitles={"English": True, "Spanish": True, "French": True, "German": True})

        self.movie4 = data.Movie(
            title="The Godfather",
            genre="Crime",
            duration=175,
            rating=9.2,
            actors=["Al Pacino, Marlon Brando, James Caan"],
            director="Francis Ford Coppola",
            cast_racial_demographics={"White": 98, "Black": 0, "Asian": 0, "Latino": 0, "Other": 2},
            language="English",
            release_year=1972,
            sales={"North America": 55, "Europe": 30, "Asia": 5, "South America": 5, "Africa": 2, "Oceania": 3},
            maturity="R",
            subtitles={"English": True, "Spanish": True, "French": True, "German": True})

        self.movies = [self.movie1 ,self.movie2, self.movie3, self.movie4]

        result = functions.movies_above_rating(self.movies, 8.0)
        expected = [self.movie4]
        self.assertEqual(result, expected)


    def test_movies_above_rating2(self):
        self.movie1 = data.Movie(
            title="Shrek",
            genre="Comedy",
            duration=89,
            rating=7.9,
            actors=["Mike Myers, Eddie Murphy, Cameron Diaz"],
            director="Andrew Adamson",
            cast_racial_demographics={"White": 75, "Black": 25},
            language= "English",
            release_year= 2001,
            sales= {"North America" : 40, "Europe": 35, "Asia": 10, "South America": 8, "Africa": 5, "Oceania": 2},
            maturity= "PG",
            subtitles= {"English": True, "Spanish": True, "French": False, "German": False})

        self.movie2 = data.Movie(
            title="Superbad",
            genre="Comedy",
            duration=119,
            rating=7.6,
            actors=["Jonah Hill, Seth Rogen, Michael Cera"],
            director="Greg Mottola",
            cast_racial_demographics={"White": 90, "Black": 10},
            language="English",
            release_year=2007,
            sales={"North America": 65, "Europe": 20, "Asia": 5, "South America": 5, "Africa": 2, "Oceania": 3},
            maturity="R",
            subtitles={"English": True, "Spanish": True, "French": True, "German": True})

        self.movie3 = data.Movie(
            title="Barbie",
            genre="Comedy",
            duration=113,
            rating=6.8,
            actors=["Margot Robbie, Ryan Gosling, Will Ferrell"],
            director="Greta Gerwig",
            cast_racial_demographics={ "White": 60, "Black": 15,"Asian": 10, "Latino": 10, "Other": 5},
            language="English",
            release_year=2023,
            sales={"North America": 98, "Europe": 0, "Asia": 15, "South America": 7, "Africa": 3, "Oceania": 0},
            maturity="PG-13",
            subtitles={"English": True, "Spanish": True, "French": True, "German": True})

        self.movie4 = data.Movie(
            title="The Godfather",
            genre="Crime",
            duration=175,
            rating=9.2,
            actors=["Al Pacino, Marlon Brando, James Caan"],
            director="Francis Ford Coppola",
            cast_racial_demographics={"White": 98, "Black": 0, "Asian": 0, "Latino": 0, "Other": 2},
            language="English",
            release_year=1972,
            sales={"North America": 55, "Europe": 30, "Asia": 5, "South America": 5, "Africa": 2, "Oceania": 3},
            maturity="R",
            subtitles={"English": True, "Spanish": True, "French": True, "German": True})

        self.movies = [self.movie1 ,self.movie2, self.movie3, self.movie4]

        result = functions.movies_above_rating(self.movies, 7.0)
        expected = [self.movie1, self.movie2, self.movie4]
        self.assertEqual(result, expected)




if __name__ == '__main__':
    unittest.main()