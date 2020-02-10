"""Cachine fibonnaci"""


def fib(n):
    """Return nth fiboacci number"""
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)


_fib_cache = {}


# cached fibonaci which is way faster and do not run the same nu,ber again 
def fibc(n):
    """Return nth fiboacci number (cached)"""
    if n < 2:
        return 1

    # get if the value is in the cache
    val = _fib_cache.get(n)

    # if it is None add it in the cache and calculate the fibbonaci 
    if val is None:
        _fib_cache[n] = val = fibc(n-1) + fibc(n-2)
    return val
