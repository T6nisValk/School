# Multithreading

It is a way to concurrently run multiple threads. Run different part of code simulteneously.
Multithreading in python doesn't actually result in true parallel execution due to Global
Interpreter Lock(GIL)

GIL is a lock that allows only one thread to execute at a time in a single process. Python uses
GIL to simplify memory allocation and avoid conflicts among threads.

# Multiprocessing

Multiprocessing is a way to concurrently run tasks in python. The module allows us to spawn
multiple processes and manage and synchronize their execution. Each python process gets its own
python interpreter and memory space so that they can work independently without affecting others.
Thus no GIL problem.

Multiprocessing is highly CPU intensive, as each process can be assigned to a different cpu core.
It is heavy weight as it requires duplicating resource between processes. Data isn't shared
directly between processes, thus inter-process communication is difficult.

NOTE: Multiprocessing is not a universal solution to make things faster. If you have a task that
requires I/O or heavy communication, multithreading or asynchronous I/O might be efficient.

# Profiling

Profiling is a process that helps you understand the runtime performance of your program.
Profiler modules like `cprofile` are designed to provide execution profile not for benchmarking.

## Timeit

Module `timeit` is used to measure the execution time of a code snippet. It does not take into
account background processes. It runs the code multiple times and gets the average time, making the
result statistically significant.

````
import timeit
timeit.timeit(stmt, setup, number

OR

from timeit import timeit
timeit(stmt, stup, number)
````

Where:

- stmt is the block of code you want to measure the execution time.
- setup is things required before executing the statement.
- number is the number of times your code runs. 