class Movie:
    def __init__(self, title, imdb_rating, release_date):
        self.title = title
        self.imdb_rating = imdb_rating
        self.release_date = release_date

    def __repr__(self):
        result = repr(
            {"title": self.title,
             "imdb_rating": self.imdb_rating,
             "release_date": self.release_date}
        )
        return result


class MoviesIHaveSeen:
    def __init__(self):
        self.movies = []

    def __len__(self):
        return len(self.movies)

    def add_movie_to_my_list(self, title, my_rating):
        self.movies.append(
            {"title": title,
             "my_rating": my_rating}
        )
        return self.movies

    def delete_from_my_list(self):
        self.movies.pop()

    def delete_certain_movie_from_my_list(self, title):
        for index, item in enumerate(self.movies):
            if item["title"] == title:
                self.movies.pop(index)

    def write_to_a_file(self):
        with open("my_movies.txt", "w") as fp:
            for item in self.movies:
                fp.write(
                    f"{item['title']} "
                    f"{item['my_rating']}"
                )


class CreatedMovies:
    def __init__(self):
        self.created = []

    def add_movie(self, movie):
        self.created.append(movie)


def data_about_movies_in_the_lists(created_list, seen_list):
    return {"created": created_list, "seen": seen_list}


available_movies = []
