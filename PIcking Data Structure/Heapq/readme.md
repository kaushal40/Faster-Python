**How to run the beanchmarking teat cases**

- `ipython`

- `run ptasks.py`

- `cases = gen_cases(1000)` 1000 is passed to avoid measuring the time it takes to generate the test cases

- `timeit benchmark_pq(cases)`  now we are timing it with our cases.

- `prun benchmark_pq(cases)` to check whcih line takes the most time (line profiling)