Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# python string handling management
# ----------------------------------

# String = sequence of characters/alphabets enclosed with a ''

name = 'alvina rk'

type(name)
<class 'str'>

# alvina rk
# 012345678

# string operations
# -----------------
# indexing / slicing / ranging

# indexing ---> get a char from a string using its index value
# -------------------------------------------------------------

name
'alvina rk'

name[0]
'a'
name[1]
'l'
name[2]
'v'
name[5]
'a'
name[6]
' '
name[7]
'r'
name[8]
'k'
name[10]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    name[10]
IndexError: string index out of range

# this process is called "POSITIVE INDEXING" and also called as traversing


# NEGATIVE INDEX
# ----------------


# a l v i n a  r k
#-9-8-7-6-5-4-3-2-1

name[-1]
'k'
name[-2]
'r'
name[-3]
' '
name[-4]
'a'
name[-8]
'l'

# this  is called back traversing / tracking

trainer = 'jason andrew rajeshkumar'

# slicing ---> getting a particular portion of a string using :
# -------------------------------------------------------------

name
'alvina rk'

name[0:3]
'alv'
name[0:4] # 0123
'alvi'
name[0:5]
'alvin'
name[2:5]
'vin'
name[7:8]
'r'
name[7:9]
'rk'
# this is called POSITIVE SLICING

name[-9]
'a'
name[-9:-5]
'alvi'
# -9 -8 -7 -6

name[-9:-4]
'alvin'

name
'alvina rk'

# ranging ---> almost similar SLICING (but ur requested to give either start/stop value with :)

name[5:]
'a rk'
name[6:]
' rk'
name[:6]
'alvina'


name = 'jason rajesh'

name[2:5] # 234
'son'
name[7:10]# 789
'aje'
name[6:9]# 678
'raj'

name[6]
'r'

name[6:]
'rajesh'
name[:6]
'jason '
name[:0]
''
name[0:]
'jason rajesh'
name = ' kavin'

name[0:]
' kavin'
name[:0]
''

name[0:1] # 0
' '
name[0:2] # 01
' k'
name[1:4]
'kav'
name[2:5] # 234
'avi'

name = 'rajesh kumar'

name[::-1]
'ramuk hsejar'

'remote'[::-1]
'etomer'

name='rajeshkumar'

name
'rajeshkumar'

name[6:]
'kumar'
name[:6]
'rajesh'

name[::2]
'rjskmr'
name[::4]
'rsm'
name[::-1]
'ramukhsejar'
name[::-2]
'rmksjr'
name[::-3]
'rusa'

# string handling operations
# ---------------------------

# string concatenation
# string repetition
# string formatting


name='alvi'
age=8
city='chennai'

# concatenation (connecting string using +)
# -----------------------------------------

'vino'+'thini'
'vinothini'
'20'+'30'
'2030'
20+30
50
print('my baby name is '+ name)
my baby name is alvi
print('my baby name is '+ name + ' from ' + city)
my baby name is alvi from chennai

print('alvina age is ' + age)
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    print('alvina age is ' + age)
TypeError: can only concatenate str (not "int") to str
print('alvina age is ' + str(age))
alvina age is 8
age
8
type(age)
<class 'int'>
8
8
'8'
'8'
print('alvina age is ' + 'age')
alvina age is age


print('alvina age is ' + '8')
alvina age is 8


# string repetition
# ------------------

name
'alvi'
'alvialvialvialvialvi'
'alvialvialvialvialvi'

name
'alvi'


name * 5
'alvialvialvialvialvi'
print('calculator program')
calculator program


=============================== RESTART: C:/Python312/c.py ===============================
calculator program
------------------

=============================== RESTART: C:/Python312/c.py ===============================
calculator program
----------------------------------------------------------------------------------------------------

=============================== RESTART: C:/Python312/c.py ===============================
calculator program
--------------------


# string formatting
# -----------------

name
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    name
NameError: name 'name' is not defined
name='rk'
age=40
city='chennai'



# manual formatting
# -----------------

print('my name is {0} from {1} aged {2}')
my name is {0} from {1} aged {2}
print('my name is {0} from {1} aged {2}'.format(name, age, city))
my name is rk from 40 aged chennai
print('my name is {0} from {2} aged {1}'.format(name, age, city))
my name is rk from chennai aged 40

# f strings
# ---------
>>> 
>>> print(f'my name is {name} from {city} aged {age}')
my name is rk from chennai aged 40
>>> 
>>> 
>>> # general formatting
>>> # -------------------
>>> 
>>> name
'rk'
>>> age
40
>>> city
'chennai'

>>> 
\
>>> 
>>> print('my name is',name)
my name is rk
>>> print('my name is',name,'home town is',city)
my name is rk home town is chennai
>>> print('my name is',name,'home town is',city,'my age is',age)
my name is rk home town is chennai my age is 40
>>> 
