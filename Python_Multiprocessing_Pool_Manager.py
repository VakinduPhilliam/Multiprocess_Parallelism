# Python multiprocessing Manager
# The other high-level interface, the Manager class, creates a separate server process that can hold master 
# copies of Python data structures. Other processes can then access and modify these data structures using 
# proxy objects. The following example creates a shared dictionary by calling the dict() method; the worker 
# processes then insert values into the dictionary. (Locking is not done for you automatically, which doesn’t
# matter in this example. Manager’s methods also include Lock(), RLock(), and Semaphore() to create shared
# locks.)
 
import time
from multiprocessing import Pool, Manager

def factorial(N, dictionary):
    "Compute a factorial."

    # Calculate the result

    fact = 1L

    for i in range(1, N+1):
        fact = fact * i

    # Store result in dictionary

    dictionary[N] = fact

if __name__ == '__main__':

    p = Pool(5)
    mgr = Manager()
    d = mgr.dict()         # Create shared dictionary

    # Run tasks using the pool

    for N in range(1, 1000, 10):
        p.apply_async(factorial, (N, d))

    # Mark pool as closed -- no more tasks can be added.

    p.close()

    # Wait for tasks to exit

    p.join()

    # Output results

    for k, v in sorted(d.items()):
        print k, v
