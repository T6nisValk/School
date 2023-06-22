# Examples of lists

fruits = ["Apple", "Orange", "Pear"]  # List of values
print(f"Length of the list {fruits}: {len(fruits)}")

# Adds values to the end of the list
fruits.append("Lemon")
fruits.append("Plum")

# Adds a new list to the list
fruits.extend(["Dragonfruit", "Some other fruit"])
print(f"\nLength of the list after appending {fruits}: {len(fruits)}")

# Sorts by alphabet or numbers sorted()
# Sorts the values only for this print.
print(f"Current state of the list: {sorted(fruits)}")
# Stores the sorted value in a different variable, original remains unsorted
sorted_fruits = sorted(fruits)
# fruits.sort()  # Sorts the values in the variable
print(f"Current state of the list: {fruits}")
print(f"Current state of the list after sorting: {sorted_fruits}")

# .count(x)
print("\nCounts the given values in a list", fruits.count("Orange"))
# .index(x)
print("Index", fruits.index("Pear"))
# .insert(index, x)
# Inserts a new value to the given index, moving everything else up by one index
fruits.insert(2, "Another Pear")
print(fruits)
# .pop(index)
fruits.pop(2)  # Delete the value at an index
print(fruits.pop(2))  # Can use the popped value
print(fruits)
# .pop()
fruits.pop()  # Delete the last value from the list
print(fruits)
# .remove(x)
fruits.remove("Dragonfruit")  # Deletes the first given value from the list
print(fruits)
# .reverse()
fruits.reverse()  # Reverses the list
print(fruits)
# .clear()
fruits.clear()  # Deletes all values from the list
print(fruits)
