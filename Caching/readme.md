**Caching**

- The act of saving computation result and reusing them instead of running the calculation again
- It uses memory
- LRU caches all the function argument to cache, if one or more arguments are list or dict it will fail. You might need to hash it.
- Example use of LRU cache - if you are accessing same function frequently, which returns idempotent data (like user details)


**How to run the code - FIBONNACI**

- `ipython`

- `timeit fib(20)`

- `timeit fibc(20)`


**How to run the code - LRU CACHE**

- `ipython`

- comment the lrucache on line 16

- `timeit user_from_keys('bugs')`

- uncomment the lrucache on line 16

- `timeit user_from_keys('bugs')`
