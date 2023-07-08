# Lambda expressions

- They are anonymous functions
- They have no name (dont define them with a name) and does not use the keyword `def` like
  normal functions
- Anonymous functions are defined using `lambda` keyword

```
# Regular function
def function_name():
    pass
```

## Syntax for defining lambda functions

````
lambda arguments: expression
````

- Lambda keyword
- Argument(s)
- Colon
- Expression

## Applications

- Map(`map()`)
    - It applies a given function to each
      item of an iterable(list, set, tuple, etc.)
- Filter(`filter()`)
    - Constructs a list from elements of an iterable(list
      tuple) for which the function contition return True.
    - Returns elements that the condition holds True.
- Reduce(`reduce()`)
    - Returns a single value from an iterable. Processes the elements of a collection from left
      to right(cumulatively), taking 2 arguments at a time. For instance taking `[1, 2, 3, 4, 5]`,
      In the first cucle it takes `1` and `2`, performs transformatiion/action you stated, in
      this example addition, then
      it returns the result of the transformation `3`. The second cycle it takes the result of
      the previous transformation `3` and `4`, returns `7`. The third cycle it takes `7` and `5`
      and returns `12`. It does it until the end of the iterable.
- Any other time you want a function object

## Limitations for using lambda

- Readability
    - Harder to understand the code.
- Lambdas can only evaluate a single expression.
    - Not suitable for larger/complex functions.
- Cannot use statements like `assert` or `pass` in lambda.
- Does not allow docstrings `""" this is a docstring """`.
- Limited traceback information during debugging.
    - Error refers to `<lambda>` instead of the function name.

