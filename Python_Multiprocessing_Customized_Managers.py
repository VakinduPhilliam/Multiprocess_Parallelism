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
# Customized managers.
# To create one’s own manager, one creates a subclass of BaseManager and uses the register() 
# classmethod to register new types or callables with the manager class.
 
from multiprocessing.managers import BaseManager

class MathsClass:

    def add(self, x, y):
        return x + y

    def mul(self, x, y):
        return x * y

class MyManager(BaseManager):
    pass

MyManager.register('Maths', MathsClass)

if __name__ == '__main__':

    with MyManager() as manager:
        maths = manager.Maths()

        print(maths.add(4, 3))         # prints 7
        print(maths.mul(7, 8))         # prints 56
