import task_1


def test_create_movie(mock_item):
    """Create movie object"""
    assert mock_item.title == "Mission Impossible"
    assert mock_item.imdb_rating == 7.1
    assert mock_item.release_date == 1996


def test_add_movie_to_my_list(mock_item):
    """Add movie object to list"""
    movie_list = task_1.MoviesIHaveSeen()
    assert len(movie_list.movies) == 0
    movie_list.add_movie_to_my_list(mock_item.title,
                                    8.5)
    assert len(movie_list.movies) == 1


def test_delete_last_movie_from_my_list(mock_item):
    """Delete last movie from list"""
    movie_list = task_1.MoviesIHaveSeen()
    assert len(movie_list.movies) == 0
    movie_list.add_movie_to_my_list(mock_item.title,
                                    8.5)
    assert len(movie_list.movies) == 1
    movie_list.delete_from_my_list()
    assert len(movie_list.movies) == 0


def test_delete_certain_movie_from_my_list(mock_item):
    """Delete certain movie from list"""
    movie_list = task_1.MoviesIHaveSeen()
    assert len(movie_list.movies) == 0
    movie_list.add_movie_to_my_list(mock_item.title,
                                    8.5)
    assert len(movie_list.movies) == 1
    movie_list.delete_certain_movie_from_my_list(mock_item.title)
    assert len(movie_list.movies) == 0


def test_show_movies_list(mock_item):
    my_movie_list = task_1.MoviesIHaveSeen()
    my_movie_list.add_movie_to_my_list(mock_item.title,
                                       8.5)
    assert my_movie_list.movies == [
        {"title": mock_item.title,
         "my_rating": 8.5}
    ]
    assert task_1.available_movies == []
    task_1.available_movies.append(mock_item)
    assert eval(repr(task_1.available_movies)) == [
        {"title": mock_item.title,
         "imdb_rating": 7.1,
         "release_date": 1996}
    ]


def test_prepare_data_for_display(mock_item):
    my_seen_list = task_1.MoviesIHaveSeen()
    my_created_list = task_1.CreatedMovies()
    my_seen_list.add_movie_to_my_list(mock_item, 5)
    my_created_list.add_movie(mock_item)
    result = task_1.data_about_movies_in_the_lists(my_created_list, my_seen_list)
    assert result == \
           {"created": my_created_list, "seen": my_seen_list}


def test_write_my_list(mock_item):
    file = open('my_movies.txt')
    movie_list = task_1.MoviesIHaveSeen()
    movie_list.add_movie_to_my_list(mock_item.title, 8.5)
    write_to_file = task_1.MoviesIHaveSeen
    write_to_file.write_to_a_file(movie_list)
    assert file.read() == "Mission Impossible 8.5"
