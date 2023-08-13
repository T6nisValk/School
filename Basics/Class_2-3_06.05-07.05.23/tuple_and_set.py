# Tuples, Can't be changed but can be overwritten.
tuple_1 = ("dog", "cat", 2000, 5.0, True)
print("My tuple is:", tuple_1)
# Read methods
print("\nCounts the given values in tuple:", tuple_1.count("dog"))
print("Gives you the index of a given value in tuple:", tuple_1.index(True))
print("Gives you the value of a given index in tuple:", tuple_1[3])

# Set - not sorted and doesn't allow duplicates.
# set_1 = set() # Empty set
set_2 = {"dog", "cat", "elephant"}
print("\nMy set:", set_2)

# Add a new item/same as appending to list
set_2.add("mouse")
print("\nAfter adding a value mouse to list:", set_2)

# Add several items at once
set_2.update(["bird", "horse"])
print("\nAdding multiple values bird, horse to list:", set_2)

# Add the same item again
set_2.add("mouse")
print(
    "\nAdds a value mouse that's inside the set already:", set_2
)  # It doesn't change anything

# Remove an item, Python will throw an error if it is not in the set
set_2.remove("cat")
print("\nAfter removing a value cat from set:", set_2)

# Remove an item, Python will NOT throw an error if it is not in the set
set_2.discard("cat")
