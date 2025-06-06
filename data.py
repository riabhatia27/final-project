class Movie:
    # Initialize a new Movie object.
    # input: the movie's title as a string
    # input: the movie's genre as a string
    # input: the movie's duration as a float
    # input: the movie's rating as a float
    # input: the movie's leading actors as a list of strings
    # input: the movie's director as a string
    # input: the movie's racial demographics as a dictionary
    # input: the movie's language as a string
    # input: the movie's release year as an integer
    # input: the movie's sales by continent as a dictionary
    # input: the movie's appropriateness rating as a string
    # input: the movie's accessibility to deaf viewers. outputs true or false

    def __init__(self,
                 title: str,
                 genre: str,
                 duration: float,
                 rating: float,
                 actors: list[str],
                 director: str,
                 cast_racial_demographics: dict[str, int],
                 language: str,
                 release_year: int,
                 sales:dict[str, int],
                 maturity: dict[str, bool],
                 subtitles: dict[str, str]):

        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating
        self.actors = actors
        self.director = director
        self.cast_racial_demographics = cast_racial_demographics
        self.language = language
        self.release_year = release_year
        self.sales = sales
        self.maturity = maturity
        self.subtitles = subtitles

    # Provide a developer-friendly string representation of the object.
    # input: Movie for which a string representation is desired.
    # output: string representation
    def __repr__(self):
        return 'Movie({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(
                self.title,
                self.genre,
                self.duration,
                self.rating,
                self.actors,
                self.director,
                self.cast_racial_demographics,
                self.language,
                self.release_year,
                self.sales,
                self.maturity,
                self.subtitles)


    def __lt__(self, other):
        return self.title.lower() < other.title.lower()
