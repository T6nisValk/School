import pytest
import task_1


@pytest.fixture()
def mock_item():
    result = task_1.Movie("Mission Impossible", 7.1, 1996)
    return result
