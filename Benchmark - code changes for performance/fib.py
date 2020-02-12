"""Simple fibonacci"""

from functools import lru_cache

# remove caching and see the benchmarking result
# @lru_cache()
def fib(n):
    """Return n'th fibonacci number"""
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)
