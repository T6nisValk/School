# Methods

## Instance methods

- This is the most common type of method
- First parameter of the method is called "`self`". "`Self`" is a reference to the instance of the
  class.
- Instance method can access and modify instance state - data stored in an instance variable

## Class methods

- Class method is one that is called for the whole class, not an instance of it
- It can access data that belongs to the class itself
- It is marked with "`@classmethod`" decorator
- The first parameter is "`cls`"
- It is useful when you need a method that is not specific to an instance but involves the class
  somehow
- To call a class method, use "`class.methodname`". You don't create an object of the class.

## Static methods

- It can not access instance or class data directly
- Has no idea about the instance or the class they are called on
- It is marked with "`@staticmethod`" decorator
- It does not have a specific first parameter - acts as a normal function within the class
- It is usually used as an utility method, that is related to the class

## Class ordering

1. Class definition
2. Class variables
3. Class constructor
4. Class methods
