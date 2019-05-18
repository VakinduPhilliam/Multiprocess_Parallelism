# Python multiprocessing Package.
# The new Python multiprocessing lets Python programs create new processes that will perform 
# a computation and return a result to the parent. The parent and child processes can communicate 
# using queues and pipes, synchronize their operations using locks and semaphores, and can share simple 
# arrays of data.
# The multiprocessing module started out as an exact emulation of the threading module using processes 
# instead of threads. That goal was discarded along the path to Python 2.6, but the general approach of 
# the module is still similar. The fundamental class is the Process, which is passed a callable object 
# and a collection of arguments. 
# The start() method sets the callable running in a subprocess, after which you can call the is_alive()
# method to check whether the subprocess is still running and the join() method to wait for the process 
# to exit.
# Here’s a simple example where the subprocess will calculate a factorial. The function doing the calculation
# is written strangely so that it takes significantly longer when the input argument is a multiple of 4.
 
import time
from multiprocessing import Process, Queue


def factorial(queue, N):
    "Compute a factorial."

    # If N is a multiple of 4, this function will take much longer.

    if (N % 4) == 0:
        time.sleep(.05 * N/4)

    # Calculate the result

    fact = 1L
    for i in range(1, N+1):
        fact = fact * i

    # Put the result on the queue

    queue.put(fact)

if __name__ == '__main__':

    queue = Queue()

    N = 5

    p = Process(target=factorial, args=(queue, N))
    p.start()
    p.join()

    result = queue.get()

    print 'Factorial', N, '=', result
