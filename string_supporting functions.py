Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name = 'saradha'

name.capitalize
<built-in method capitalize of str object at 0x000001F24684C870>
name.casefold()
'saradha'
name.center()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    name.center()
TypeError: center expected at least 1 argument, got 0
name.center(20)
'      saradha       '
name.ljust(20)
'saradha             '
name.rjust(20)
'             saradha'
name.count('a')
3
name.count('u')
0
name.endswith('a')
True
name.endswith('r')
False
name.endswith('s')
False
name.find('a')
1
name.find('h')
5
name.find('t')
-1
name.index('t')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    name.index('t')
ValueError: substring not found
#index is used for only sub strings.
#find is used if u have a doubt in is there sub string is or not


name.isalnum()
True
#saradha
#'saradha'
#'Saradha'
#'sara1210'
#'1235433'



name.isalpha()
True
name.isdecimal()
False
name.islower()
True
name.isprintable()
True
name.isspace()
False
name.istitle()
False
name.title()
'Saradha'
>>> name.join'1234')
SyntaxError: unmatched ')'
>>> name.join('1234')
'1saradha2saradha3saradha4'
>>> name.partition('d')
('sara', 'd', 'ha')
>>> name.removeprefix('r')
'saradha'
>>> name.removeprefix('a')
'saradha'
>>> name.removeprefix('s')
'aradha'
>>> name.removesuffix('h')
'saradha'
>>> name.removesuffix('a')
'saradh'
>>> name.strip('a')
'saradh'
>>> name.replace('a','A')
'sArAdhA'
>>> name
'saradha'
>>> name.split('r')
['sa', 'adha']
>>> name.swapcase('SaraDHa')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    name.swapcase('SaraDHa')
TypeError: str.swapcase() takes no arguments (1 given)
>>> 'saRaDha'.swapcase()
'SArAdHA'
>>> name.swapcase()
'SARADHA'
>>> name.index('a')
1
>>> name.rindex('a')
6
>>> name.rfind('r')
2
