# this function shows how to do line profiling

"""memory_profiler example"""
from memory_profiler import profile

@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


if __name__ == '__main__':
    my_func()

#python3 memory_profiler.py
# https://pypi.org/project/memory-profiler/

# use mprof to create and visulize the data 
# mprof run memory_profiler.py
# mprof plot <name_of_the_file>