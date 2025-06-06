# This file has all the different functions we will be implementing for our project.
import data


# This function searches if a movie is on the platform (Ria)
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
# def movies_above_rating(movies: list[Movie], threshold: float) -> list:

# This function sorts movie titles alphabetically
# list argument is the list of various movie titles
# This function returns a list of movies in alphabetical order
# def sort_alpha(movies: list[Movie]) -> list:

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
def accessible(movies: list[data.Movie], sub: str) -> list[data.Movie]:
    movies_list = []
    for movie in movies:
        subtitle = movie.subtitles.get(sub)
        if subtitle in movie:
            movies_list.append(movie)
    return movies_list


#This function sorts through movies of an appropriate maturity rating (for things like parental controls)
#input: a list of movies and a list of maturity levels
#output: a listr of movies
def children_movies(movies: list[data.Movie]) -> list[data.Movie]:
    sorted_list = []
    for movie in movies:
        if movie.maturity == "G" or movie.maturity == "PG":
            sorted_list.append(movie)
    return sorted_list


#This function sorts through movies of an appropriate maturity level
#input: a list of movies and a list of maturity levels
#output: a listr of movies
def young_adult_movies(movies: list[data.Movie]) -> list[data.Movie]:
    sorted_list = []
    for movie in movies:
        if movie.maturity =="G" or movie.maturity == "PG" or movie.maturity =="PG-13":
            sorted_list.append(movie)
    return sorted_list

#This function sorts the movies by genre and alphabetically
#input: a list of movies and a genre
#output a sorted list of movies of a single genre
def sorted_by_genre(movies: list[data.Movie], genre_type: str) -> list[data.Movie]:
   sorted_list = []
   for movie in movies:
       if movie.genre == genre_type: #sorts through only the movies of a certain genre
           sorted_list.append(movie) #creates a list of the movies of a certain genre
   for i in range(len(sorted_list)-1):
       smallest_idx = i
       for j in range(i + 1, len(sorted_list)):
           if sorted_list[j].title < sorted_list[smallest_idx].title:
               smallest_idx = j
       sorted_list[i], sorted_list[smallest_idx] = sorted_list[smallest_idx], sorted_list[i]
   return sorted_list

