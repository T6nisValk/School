# Exercise 1

The likes function should take a string list of names as input people who "like" a given post /
photo, and output a properly formatted text.

- ``likes([])``  => "``nobody likes it"``
- ``likes(["Peter"])``  => ``Peter likes it!``
- ``likes(["Peter", "Anna"])``  => ``Peter and Anna like it``
- ``likes(["Peter", "Anna", "Mark"])``  => ``Peter, Anna and Mark like it``
- ``likes(["Peter", "Anna", "Mark", "Ola"])``  => ``Peter, Anna and 2 other people like it``

# Exercise 2

Write a function that finds all the anagrams of a given word from the list provided. Words found
should be return as a list.

- ``func('abba', ['aabb', 'abcd', 'bbaa', 'dada'])`` => ``['aabb', 'bbaa']``

- ``func('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])`` => ``['carer', 'racer']``

- ``func('laser', ['lazing', 'lazy',  'lacer'])`` => ``[]``

# Exercise 3

Write a function that takes a list of 11 integers and returns a string in a phone number format.

- ``func([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]) `` => returns ``(+12) 345-678-901``

# Exercise 4

Write the function WeIrD CaSe, which accepts a string and returns it with all even index letters
as uppercase, and odd index letters lowercase.

- ``func('String')`` => return ``StRiNg``
- ``func('Algorithms and data structures')`` => return ``AlGoRiThMs AnD DaTa StRuCtUrEs``

# Exercise 5

Write a function that decodes morse to letters. Remove start and end whitespaces.

- ``func('.... . -.-- .--- ..- -.. .')`` => ``HEY JUDE``
- ``func(' . ')`` => ``E``
- ``func('... --- ...')`` => ``S O S``