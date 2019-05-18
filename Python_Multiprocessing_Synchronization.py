# Python multiprocessing - Process-based parallelism
# The following scripts are written to demonstrate multiprocessing (Process-based parallelism) 
# using Python.
# Multiprocessing is a Python package that supports spawning processes using an API similar to 
# the threading module. The multiprocessing package offers both local and remote concurrency, 
# effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads. 
# Due to this, the multiprocessing module allows the programmer to fully leverage multiple 
# processors on a given machine. It runs on both Unix and Windows.
# The multiprocessing module also introduces APIs which do not have analogs in the threading module. 
# A prime example of this is the Pool object which offers a convenient means of parallelizing the 
# execution of a function across multiple input values, distributing the input data across processes 
# (data parallelism). 
# Synchronization between processes.
# multiprocessing contains equivalents of all the synchronization primitives from threading. 
# For instance one can use a lock to ensure that only one process prints to standard output 
# at a time:
 

from multiprocessing import Process, Lock

def f(l, i):

    l.acquire()

    try:
        print('hello world', i)

    finally:
        l.release()

if __name__ == '__main__':

    lock = Lock()

    for num in range(10):

        Process(target=f, args=(lock, num)).start()

