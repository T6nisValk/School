import food


def test_create_item(mock_item):
    assert mock_item.name == "Potato"
    assert mock_item.origin == "Lithuania"


def test_add_item_to_list(mock_item):
    shopping_list = food.FoodList()

    assert shopping_list.length == 0
    shopping_list.add_item(mock_item, "5kg")
    assert shopping_list.length == 1
    assert shopping_list.items[0]["name"] == "Potato"


def test_remove_ite_from_list(mock_item):
    shopping_list = food.FoodList()

    assert shopping_list.length == 0
    shopping_list.add_item(mock_item, "5kg")
    assert shopping_list.length == 1
    shopping_list.delete()
    assert shopping_list.length == 0


def test_shopping_list_access(mock_item):
    shopping_list = food.FoodList()
    shopping_list.add_item(mock_item, "5kg")
    shopping_list.add_item(mock_item, "5kg")
    assert shopping_list.items == \
           [{"name": "Potato", "amount": "5kg"},
            {"name": "Potato", "amount": "5kg"}]


def test_available_products_list_access(mock_item):
    assert food.available_products == []
    food.available_products.append(mock_item)
    food.available_products.append(mock_item)
    food.available_products.append(mock_item)
    assert food.available_products == \
           [{"name": "Potato", "origin": "Lithuania"},
            {"name": "Potato", "origin": "Lithuania"},
            {"name": "Potato", "origin": "Lithuania"}]
