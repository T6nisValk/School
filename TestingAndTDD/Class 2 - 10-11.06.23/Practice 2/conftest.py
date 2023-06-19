import pytest
import food


@pytest.fixture()
def mock_item():
    result = food.Item("Potato", "Lithuania")
    return result
