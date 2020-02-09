**BigO of most common data structures in python** 


|Data Structure  |Operation  |Big O |
|---------|---------|---------|
|list     |append      |o(1)         |
|list     |sort   | o(n log n)        |
|list     |search     |    o(n)     | 
|dict     |get   |   o(1)      |


**Use Bisect**

- This module provides support for maintaining a list in sorted order without having to sort the list after each insertion. For long lists of items with expensive comparison operations, this can be an improvement over the more common approach. The module is called bisect because it uses a basic bisection algorithm to do its work. The source code may be most useful as a working example of the algorithm (the boundary conditions are already right!).

- *Example Use* You want to insert the item in sorted list. If you just add it normly, it sorts the items after insertion so sorting + adding the item which is expensive
 
https://docs.python.org/3.0/library/bisect.html

