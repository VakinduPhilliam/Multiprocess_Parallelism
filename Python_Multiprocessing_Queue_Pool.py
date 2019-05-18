# Python Multiprocessing Queue
# A Queue is used to communicate the result of the factorial. The Queue object is stored in a global variable. 
# The child process will use the value of the variable when the child was created; because it’s a Queue, parent 
# and child can use the object to communicate. (If the parent were to change the value of the global variable, the
# child’s value would be unaffected, and vice versa.)
# Two other classes, Pool and Manager, provide higher-level interfaces. Pool will create a fixed number of worker
# processes, and requests can then be distributed to the workers by calling apply() or apply_async() to add a single
# request, and map() or map_async() to add a number of requests. The following code uses a Pool to spread requests 
# across 5 worker processes and retrieve a list of results:
 
from multiprocessing import Pool

def factorial(N, dictionary):
    "Compute a factorial."
    ...
p = Pool(5)

result = p.map(factorial, range(1, 1000, 10))

for v in result:
    print v
