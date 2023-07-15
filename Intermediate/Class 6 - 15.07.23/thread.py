import threading
import timeit


def iterate_a_concept(itr):
    for item in itr:
        print(item, end="")


thread_1 = threading.Thread(target=iterate_a_concept, args=("python intermediate",))  # Tuple(x, )
thread_2 = threading.Thread(target=iterate_a_concept, args=(range(9),))

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print("Done")
print("-" * 100)


def decrease(start, end):
    while start >= end:
        start -= 1


def count_without_threading():
    decrease(10000, 0)


def count_with_threading():
    t1 = threading.Thread(target=decrease, args=(10000, 0))
    t2 = threading.Thread(target=decrease, args=(20000, 10000))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    thread_func = "count_with_threading()"
    no_thread_func = "count_without_threading()"
    setup = "from __main__ import count_with_threading, count_without_threading"

    print("Without thread: ", timeit.timeit(stmt=no_thread_func, setup=setup, number=500))
    print("With thread: ", timeit.timeit(stmt=thread_func, setup=setup, number=500))
