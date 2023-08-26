class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class SingletonClass(metaclass=Singleton):
    pass


class NotSingletonClass:
    pass


x = SingletonClass()
y = SingletonClass()

print(x == y)

x1 = NotSingletonClass()
y1 = NotSingletonClass()

print(x1 == y1)
