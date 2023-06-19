import time_of_day


def test_what_time():
    time = 19
    assert time_of_day.what_time(time) == "Evening"
    time = 10
    assert time_of_day.what_time(time) == "Morning"
    time = 3
    assert time_of_day.what_time(time) == "Night"
    time = 15
    assert time_of_day.what_time(time) == "Day"
