import multiprocessing
import timeit
import threading


# Have to import:


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


def count_with_multiprocess():
    process_1 = multiprocessing.Process(target=decrease, args=(10000, 0))
    process_2 = multiprocessing.Process(target=decrease, args=(20000, 10000))

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()


if __name__ == "__main__":
    thread_func = "count_with_threading()"
    no_thread_func = "count_without_threading()"
    setup = "from __main__ import count_with_threading, count_without_threading, " \
            "count_with_multiprocess"
    multi = "count_with_multiprocess()"

    print("Without thread: ", timeit.timeit(stmt=no_thread_func, setup=setup, number=100))
    print("With thread: ", timeit.timeit(stmt=thread_func, setup=setup, number=100))
    print("With multi: ", timeit.timeit(stmt=multi, setup=setup, number=100))
