**__slots__**

- https://www.python-course.eu/python3_slots.php

- https://tech.oyster.com/save-ram-with-python-slots/

- https://stackoverflow.com/questions/472000/usage-of-slots

- to many small object can create a problem

- Object stores attributes in dictionary called __dict__

- These dictionary are 1/3 empty 

- __slots__  removes the __dict__ but the downside is you can't add the attribute to the object