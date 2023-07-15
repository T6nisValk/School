import cProfile
import timeit


# Uses the stats class
def decrease(start=10000, end=5000):
    while start >= end:
        start -= 1


print(cProfile.run("decrease()"))  # in quotes
print("-" * 120)


# For benchmarking use timeit

def string_join():
    return "-".join(str(n) for n in range(100))


if __name__ == "__main__":
    setup = "from __main__ import string_join"
    stmt = "string_join()"
    print(timeit.timeit(stmt=string_join, setup=setup, number=1000))

t = timeit.Timer(lambda: "-".join(str(n) for n in range(100)))
print(t.timeit(1000))
