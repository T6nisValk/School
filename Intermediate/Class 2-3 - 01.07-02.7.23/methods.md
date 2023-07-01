# Methods

## Instance methods
- This is the most common type of method
- First parameter of the method is called "`self`". "`Self`" is a reference to the instance of the class.
- Instance method can access and modify instance state - data stored in an instance variable
## Class methods
- Class method is one that is called for the whole class, not an instance of it
- It can access data that belongs to the class itself
- It is marked with "`@classmethod`" decorator
- The first parameter is "`cls`"
- It is useful when you need a method that is not specific to an instance but involves the class somehow
- To call a class method, use "`class.methodname`". You don't create an object of the class.
## Static methods