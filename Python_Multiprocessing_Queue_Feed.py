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
# An example showing how to use queues to feed tasks to a collection of worker processes and collect 
# the results:
 
import time
import random

from multiprocessing import Process, Queue, current_process, freeze_support

#
# Function run by worker processes
#

def worker(input, output):

    for func, args in iter(input.get, 'STOP'):
        result = calculate(func, args)
        output.put(result)

#
# Function used to calculate result
#

def calculate(func, args):
    result = func(*args)
    return '%s says that %s%s = %s' % \
        (current_process().name, func.__name__, args, result)

#
# Functions referenced by tasks
#

def mul(a, b):
    time.sleep(0.5*random.random())
    return a * b

def plus(a, b):
    time.sleep(0.5*random.random())
    return a + b

#
#
#

def test():
    NUMBER_OF_PROCESSES = 4
    TASKS1 = [(mul, (i, 7)) for i in range(20)]
    TASKS2 = [(plus, (i, 8)) for i in range(10)]

    # Create queues

    task_queue = Queue()
    done_queue = Queue()

    # Submit tasks

    for task in TASKS1:
        task_queue.put(task)

    # Start worker processes

    for i in range(NUMBER_OF_PROCESSES):
        Process(target=worker, args=(task_queue, done_queue)).start()

    # Get and print results

    print('Unordered results:')
    for i in range(len(TASKS1)):
        print('\t', done_queue.get())

    # Add more tasks using `put()`

    for task in TASKS2:
        task_queue.put(task)

    # Get and print some more results

    for i in range(len(TASKS2)):
        print('\t', done_queue.get())

    # Tell child processes to stop

    for i in range(NUMBER_OF_PROCESSES):
        task_queue.put('STOP')

if __name__ == '__main__':
    freeze_support()
    test()
