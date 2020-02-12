**Numba**

- Provide JIT compilation for optimization 
- If function called once it dosen't help 
- But if we have many function call it helps
- Python dosen't have Numba you have to add the package 


**How to run**

`ipython`

`run jit.py`

`timeit poly(coeffs, 7)`

*now use Numba property to make it JIT efficient*

`run jit.py` # This will make the machine code during run time and use it for further execution 

`poly(coeffs, 7)`

`poly_j(coeffs, 7)` (this will generate JIT version of the code)

`timeit poly_j(coeffs, 7)`
