# This file has all the different functions we will be implementing for our project.
from data import Movie


# This function searches if a movie is on the platform
# str argument is the string title representation of the movie
# The function returns true if the movie is present and false if it is not present
# incorporates exception handling and the statement "Movie Unavailable"

def search_movie(title: str, filename: str = "movies.txt") -> bool:
    try:
        with open(filename, "r") as file:
            for line in file:
                if title.strip().lower() == line.strip().lower():
                    print("On platform: True")
                    return True
        print("Movie Unavailable")
        return False
    except FileNotFoundError:
        print("File not found")
        return False


# This function evaluates if certain movies fall above a certain threshold and creates a new list of those movies who do
# list argument is the list of various movie titles
# float argument is the threshold that is being compared
# This function returns a list of movies whose ratings fall above a certain threshold

def movies_above_rating(movies: list[Movie], threshold: float) -> list:
    result = []
    for movie in movies:
        if movie.rating >= threshold:
            result.append(movie)
    return result


# This function sorts movie titles alphabetically
# list argument is the list of various movie titles
# This function returns a list of movies in alphabetical order

def sort_alpha(movies: list[Movie]) -> list[Movie]:
    for i in range(0, len(movies) - 1):
        small_idx = i
        for j in range(i + 1, len(movies)):
            if movies[j].title < movies[small_idx].title:
                small_idx = j

        if small_idx != i:
            movies[i], movies[small_idx] = movies[small_idx], movies[i]
    return movies




# This function evaluates the average ticket sales for a particular region.
# list argument is the list of various movie titles
# string argument is the name of the continent being compared
# This function returns the average sales a movie received in a continent
# def average_sales_by_continent(movies: list[Movie], continent: str) -> float:

#This function sorts the list of movies by run time
#input: list of movies and a time limit
#output: returns a list of movies with a run time less than a certain time
#def run_time_less_than( movies: list[Movie], time: float) -> list[Movie]:

#This function sorts through the movies and return those with subtitles available
#input: a list of movies and a keyword "has subtitles"
#output: a list of movies
#def accessible(movies: list[Movie]) -> list[Movie]:

#This function sorts through movies of an appropriate maturity rating (for things like parental controls)
#input: a list of movies and a list of maturity levels
#output: a listr of movies
#def children's_movies(movies: list[Movies], maturity_level: list[maturity]) -> list[Movies]

#This function sorts through movies of an appropriate maturity level
#input: a list of movies and a list of maturity levels
#output: a listr of movies
#def young_adult_movies(movies: list[Movies], maturity_level:list[maturity]) -> list[Movies]

#This function sorts the movies by genre and alphabetically
#input: a list of movies and a genre
#output a sorted list of movies of a single genre
#def sorted_by_genre(movies: list[Movies], type: genre) -> list:Movies
