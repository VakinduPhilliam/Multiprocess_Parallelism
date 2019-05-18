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
# ThreadPoolExecutor.
# ThreadPoolExecutor is an Executor subclass that uses a pool of threads to execute calls 
# asynchronously.
# Deadlocks can occur when the callable associated with a Future waits on the results of another 
# Future.
 
import time

def wait_on_b():
    time.sleep(5)

    print(b.result())  # b will never complete because it is waiting on a.
    return 5

def wait_on_a():
    time.sleep(5)

    print(a.result())  # a will never complete because it is waiting on b.
    return 6

executor = ThreadPoolExecutor(max_workers=2)
a = executor.submit(wait_on_b)
b = executor.submit(wait_on_a)
