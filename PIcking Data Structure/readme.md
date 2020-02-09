**BigO of most common data structures in python** 


|Data Structure  |Operation  |Big O |
|---------|---------|---------|
|list     |append      |o(1)         |
|list     |sort   | o(n log n)        |
|list     |search     |    o(n)     | 
|dict     |get   |   o(1)      |


**Use Bisect**

- Only works on a sorted list

- This module provides support for maintaining a list in sorted order without having to sort the list after each insertion. For long lists of items with expensive comparison operations, this can be an improvement over the more common approach. The module is called bisect because it uses a basic bisection algorithm to do its work. The source code may be most useful as a working example of the algorithm (the boundary conditions are already right!).

- *Example Use* You want to insert the item in sorted list. If you just add it normly, it sorts the items after insertion so sorting + adding the item which is expensive
 
- https://docs.python.org/3.0/library/bisect.html



**Use deque**

- Use whenever you wanted to perform First in First out,  for example messages. 
- If you use list for queue, it will relocate the list in the memory again whenever the new element is added
_ so use deque which is double ended queue, downside of this is it might take some time to access the elements


**Use HeapQ**

- The priority queue order tasks 
- So when you pop the item, it will pop the item with highest priority
- Priority of 1 is higher than priority of 2
- The complexity of pushing and poping is o(log n)

