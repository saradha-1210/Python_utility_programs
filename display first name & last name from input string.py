Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #create a function to display the first name & last name from inut string
... 
... 
... def get_fname():
...     name = input('enter your name:')
...     print(name.split(' ')[0])
... 
...     
>>> get_fname()
enter your name:sree saradha
sree
>>> 
>>> def get_lname():
...     name = input('enter your name:')
...     print(name.split(' ')[1])
... 
...     
>>> get_lname()
enter your name:deems dinesh
dinesh
