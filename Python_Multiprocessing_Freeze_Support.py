# Python multiprocessing - Process-based parallelism.
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
# 'multiprocessing.freeze_support()'.
# Add support for when a program which uses multiprocessing has been frozen to produce a Windows 
# executable. (Has been tested with py2exe, PyInstaller and cx_Freeze.)
# One needs to call this function straight after the if __name__ == '__main__' line of the main module.
 
from multiprocessing import Process, freeze_support

def f():
    print('hello world!')

if __name__ == '__main__':

    freeze_support()
    Process(target=f).start()
