# Iterators

Iterable is any object capable of returning its elements one at a time. Can be iterated over
with loops. They don't do any work until we explicitly ask for the next item. It allows us not
to store all items in memory - not allocating large amounts of memory to a large collection.

Example of common iterable objects:

- List

````
for item in [1, 2, 3]:
    print(item)
````

- Tuples
- Sets
- Dictionaries
- Files

````
with open("filename.txt") as f:
    for line in f:
        print(line)
````

- Strings

````
for character in "hello":
    print(character)
````

In a for loop for example:

- When the `for` loop is executed, python calls the `__iter__` function which returns an
  iterator which is an object with `__next__` method. `__next__` method is repeatedly called
  until it sees a `StopIteration` exception - there is no more items to iterate over.

````
for num in nums:
    print(num)
````

# Generators

A generator is a function that returns an iterator that produces a sequence of values when
iterated over. It uses the keyword `yield` when it returns a value. `Yield` statement turns a
normal function into a generator object.

## Importance

- Easy to implement
- Memory efficient
    - Produces one result at a time.
- For representing infinite stream
- Efficient for pipelining
    - A pipeline is basically a series of operations.