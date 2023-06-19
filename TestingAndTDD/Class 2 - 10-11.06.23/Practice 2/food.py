"""
Create a program for Groceries list.
1. I should be able to create Item.
- Each item should have a name, origin
2. I should be able to add Items to the list.
- When registering item to the list I want to be able
    to provide the amount of this item that I need.
_________________________________________________
There should be an option to delete item
from the shopping list.
There should be options to show available products
and current shopping list.
"""


class Item:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

    def __repr__(self):
        result = repr({"name": self.name, "origin": self.origin})
        return result


class FoodList:
    def __init__(self):
        self.items = []
        self.length = len(self.items)

    def add_item(self, item, amount):
        self.items.append({"name": item.name, "amount": amount})
        self.length = len(self.items)

    def delete(self):
        self.items.pop()
        self.length = len(self.items)


available_products = []

shopping_list = FoodList()
while True:
    action = input("WHat you want to do?\n"
                   "A) Add new item\n"
                   "B) Show shopping list\n"
                   "C) Show available items\n"
                   "D) Delete items")
    if action.lower() == "a":
        item_name = input("Enter the item name: ")
        item_origin = input("Enter the origin of the item: ")
        item_amount = input("Enter the amount of the item: ")
        new_item = Item(item_name, item_origin)
        available_products.append(new_item)
        shopping_list.add_item(new_item, item_amount)
