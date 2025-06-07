#PYTHON**CHEAT**SHEET
#BASIC

#Print
print("Hello Print")

##//---------------------------------------------------------------------------------------//
#Input
print =input("Hello Input")

##//---------------------------------------------------------------------------------------//
##Python Numbers with their type
print(type(1))
print(type(-1))
print(type(0))
print(type(0.2))
print(type(2.34))

##//---------------------------------------------------------------------------------------//
#Arithmetic
print(10+3) #13
print(10-3) #7
print(10*3) #30
print(10 ** 3) # 1000
print(10/3) #3.33333
print(10//3) #3
print(10%3) # 1

##//---------------------------------------------------------------------------------------//
#Basic Function
print(pow(2,3)) # like - 2 * 2 * 2 
print(abs(-34)) # 34
print(round(4.6)) # 5
print(round(4.567,2)) # 4.57
print(bin(1024)) #0b10000000000
print(hex(36)) #0x24

##//---------------------------------------------------------------------------------------//
#Convert String into numbers
age = input("How old are you?")
age = int(age)

pi = input("What is the value of pi?")
pi = float(pi)

#fString in python
age = 12
print(f"You are {age} year old")

first_name = 'albert'
last_name = 'einstein'
full_name = f"{first_name} {last_name}"
print(full_name)

##//--------------------------------------------------------------------------------------------------------------------//
#Data Types 
fText #Type:	str
Numeric #Types:	#int, float, complex
Sequence #Types:	#list, tuple, range
Mapping #Type:	#dict
Set #Types:	#set, frozenset
Boolean #Type:	#bool
Binary #Types:	#bytes, bytearray, memoryview
None #Type:	NoneTypex = "Hello World"	#str	

x = 20	 #int	
x = 20.5  #loat	
x = 1j  	#complex	
x = ["apple", "banana", "cherry"] 	#list	
x = ("apple", "banana", "cherry") 	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36} 	#dict	
x = {"apple", "banana", "cherry"}   #set	
x = frozenset({"apple", "banana", "cherry"})  #frozenset	
x = True  #bool	
x = b"Hello" 	#bytes	
x = bytearray(5) 	#bytearray	
x = memoryview(bytes(5)) 	#memoryview	
x = None #NoneType


##//--------------------------------------------------------------------------------------------------------------------//
#Strings in python are stored as sequences of letters in memory
#String in python -- Indexing and Slicing
type('Hellloooooo') # str

'I\'m thirsty'
"I'm thirsty"
"\n" # new line
"\t" # adds a tab

'Hey you!'[4] # y
name = 'Andrei Neagoie'
name[4]     # e
name[:]     # Andrei Neagoie
name[1:]    # ndrei Neagoie
name[:1]    # A
name[-1]    # e
name[::1]   # Andrei Neagoie
name[::-1]  # eiogaeN ierdnA
name[0:10:2]# Ade e
# : is called slicing and has the format [ start : end : step ]

'Hi there ' + 'Timmy' # 'Hi there Timmy' --> This is called string concatenation
'*'*10 # **********

x = s.split() # creates string array of words
print(x[-3] + " " + x[-1] + " " + x[2] + "s")
 # '11 old popes'
## 5. Most Important String Methods
y = " This is lazy\t\n "
print(y.strip()) # Remove Whitespace: 'This is lazy'
print("DrDre".lower()) # Lowercase: 'drdre'
print("attention".upper()) # Uppercase: 'ATTENTION'
print("smartphone".startswith("smart")) # True
print("smartphone".endswith("phone")) # True
print("another".find("other")) # Match index: 2
print("cheat".replace("ch", "m")) # 'meat'
print(','.join(["F", "B", "I"])) # 'F,B,I'
print(len("Rumpelstiltskin")) # String length

# Basic Functions
len('turtle') # 6

# Basic Methods
'  I am alone '.strip()               # 'I am alone' --> Strips all whitespace characters from both ends.
'On an island'.strip('d')             # 'On an islan' --> # Strips all passed characters from both ends.
'but life is good!'.split()           # ['but', 'life', 'is', 'good!']
'Help me'.replace('me', 'you')        # 'Help you' --> Replaces first with second param
'Need to make fire'.startswith('Need')# True
'and cook rice'.endswith('rice')      # True
'bye bye'.index('e')                  # 2
'still there?'.upper()                # STILL THERE?
'HELLO?!'.lower()                     # hello?!
'ok, I am done.'.capitalize()         # 'Ok, I am done.'
'oh hi there'.find('i')               # 4 --> returns the starting index position of the first occurrence
'oh hi there'.count('e')              # 2


# String Formatting
name1 = 'Andrei'
name2 = 'Sunny'
print(f'Hello there {name1} and {name2}')       # Hello there Andrei and Sunny - Newer way to do things as of python 3.6
print('Hello there {} and {}'.format(name1, name2))# Hello there Andrei and Sunny
print('Hello there %s and %s' %(name1, name2))  # Hello there Andrei and Sunny --> you can also use %d, %f, %r for integers, floats, string representations of objects respectively



#Palindrome check
word = 'reviver'
p = bool(word.find(word[::-1]) + 1)
print(p) # True


##//--------------------------------------------------------------------------------------------------------------------//
##Boolean
bool(True)
bool(False)

# all of the below evaluate to False. Everything else will evaluate to True in Python.
print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(''))
print(bool(range(0)))
print(bool(set()))

# See Logical Operators and Comparison Operators section for more on booleans.


##//--------------------------------------------------------------------------------------------------------------------//
##LIST - Unlike strings, lists are mutable sequences in python
##Check type of list
i = ['a', 'b','c']
print(type(i))

my_list = [1, 2, '3', True]# We assume this list won't mutate for each example below
len(my_list)               # 4
my_list.index('3')         # 2
my_list.count(2)           # 1 --> count how many times 2 appears

my_list[3]                 # True
my_list[1:]                # [2, '3', True]
my_list[:1]                # [1]
my_list[-1]                # True
my_list[::1]               # [1, 2, '3', True]
my_list[::-1]              # [True, '3', 2, 1]
my_list[0:3:2]             # [1, '3']

# : is called slicing and has the format [ start : end : step ]
# Add to List
my_list * 2                # [1, 2, '3', True, 1, 2, '3', True]
my_list + [100]            # [1, 2, '3', True, 100] --> doesn't mutate original list, creates new one
my_list.append(100)        # None --> Mutates original list to [1, 2, '3', True, 100]          # Or: <list> += [<el>]
my_list.extend([100, 200]) # None --> Mutates original list to [1, 2, '3', True, 100, 200]
my_list.insert(2, '!!!')   # None -->  [1, 2, '!!!', '3', True] - Inserts item at index and moves the rest to the right.

' '.join(['Hello','There'])# 'Hello There' --> Joins elements using string as separator.


# Copy a List
basket = ['apples', 'pears', 'oranges']
new_basket = basket.copy()
new_basket2 = basket[:]


# Remove from List
[1,2,3].pop()    # 3 --> mutates original list, default index in the pop method is -1 (the last item)
[1,2,3].pop(1)   # 2 --> mutates original list
[1,2,3].remove(2)# None --> [1,3] Removes first occurrence of item or raises ValueError.
[1,2,3].clear()  # None --> mutates original list and removes all items: []
del [1,2,3][0] # 


# Ordering
[1,2,5,3].sort()         # None --> Mutates list to [1, 2, 3, 5]
[1,2,5,3].sort(reverse=True) # None --> Mutates list to [5, 3, 2, 1]
[1,2,5,3].reverse()      # None --> Mutates list to [3, 5, 2, 1]
sorted([1,2,5,3])        # [1, 2, 3, 5] --> new list created
list(reversed([1,2,5,3]))# [3, 5, 2, 1] --> reversed() returns an iterator

# Useful operations
1 in [1,2,5,3]  # True
min([1,2,3,4,5])# 1
max([1,2,3,4,5])# 5
sum([1,2,3,4,5])# 15

# Get First and Last element of a list
mList = [63, 21, 30, 14, 35, 26, 77, 18, 49, 10]
first, *x, last = mList
print(first) #63
print(last) #10

# List Comprehensions
# new_list[<action> for <item> in <iterator> if <some condition>]
a = [i for i in 'hello']                  # ['h', 'e', 'l', 'l', '0']
b = [i*2 for i in [1,2,3]]                # [2, 4, 6]
c = [i for i in range(0,10) if i % 2 == 0]# [0, 2, 4, 6, 8]


##Advanced Functions
list_of_chars = list('Helloooo')                                   # ['H', 'e', 'l', 'l', 'o', 'o', 'o', 'o']
sum_of_elements = sum([1,2,3,4,5])                                 # 15
element_sum = [sum(pair) for pair in zip([1,2,3],[4,5,6])]         # [5, 7, 9]
sorted_by_second = sorted(['hi','you','man'], key=lambda el: el[1])# ['man', 'hi', 'you']
sorted_by_key = sorted([
                       {'name': 'Bina', 'age': 30},
                       {'name':'Andy', 'age': 18},
                       {'name': 'Zoey', 'age': 55}],
                       key=lambda el: (el['name']))# [{'name': 'Andy', 'age': 18}, {'name': 'Bina', 'age': 30}, {'name': 'Zoey', 'age': 55}]

##//--------------------------------------------------------------------------------------------------------------------//
##Dictionaries - Also known as mappings or hash tables.
my_dict = {'name': 'Andrei Neagoie', 'age': 30, 'magic_power': False}
my_dict['name']                      # Andrei Neagoie
len(my_dict)                         # 3
list(my_dict.keys())                 # ['name', 'age', 'magic_power']
list(my_dict.values())               # ['Andrei Neagoie', 30, False]
list(my_dict.items())                # [('name', 'Andrei Neagoie'), ('age', 30), ('magic_power', False)]
my_dict['favourite_snack'] = 'Grapes'# {'name': 'Andrei Neagoie', 'age': 30, 'magic_power': False, 'favourite_snack': 'Grapes'}
my_dict.get('age')                   # 30 --> Returns None if key does not exist.
my_dict.get('ages', 0 )              # 0 --> Returns default (2nd param) if key is not found

#Remove key
del my_dict['name']
my_dict.pop('name', None)




my_dict.update({'cool': True})                                         # {'name': 'Andrei Neagoie', 'age': 30, 'magic_power': False, 'favourite_snack': 'Grapes', 'cool': True}
{**my_dict, **{'cool': True} }                                         # {'name': 'Andrei Neagoie', 'age': 30, 'magic_power': False, 'favourite_snack': 'Grapes', 'cool': True}
new_dict = dict([['name','Andrei'],['age',32],['magic_power',False]])  # Creates a dict from collection of key-value pairs.
new_dict = dict(zip(['name','age','magic_power'],['Andrei',32, False]))# Creates a dict from two collections.
new_dict = my_dict.pop('favourite_snack')                              # Removes item from dictionary.


# Dictionary Comprehension
{key: value for key, value in new_dict.items() if key == 'age' or key == 'name'} # {'name': 'Andrei', 'age': 32} --> Filter dict by keys


##//--------------------------------------------------------------------------------------------------------------------//
##Tuples -  Like lists, but they are used for immutable things (that don't change)
my_tuple = ('apple','grapes','mango', 'grapes')
apple, grapes, mango, grapes = my_tuple# Tuple unpacking
len(my_tuple)                          # 4
my_tuple[2]                            # mango
my_tuple[-1]                           # 'grapes'

# Immutability
my_tuple[1] = 'donuts'  # TypeError
my_tuple.append('candy')# AttributeError

# Methods
my_tuple.index('grapes') # 1
my_tuple.count('grapes') # 2

# Zip
list(zip([1,2,3], [4,5,6])) # [(1, 4), (2, 5), (3, 6)]

# unzip
z = [(1, 2), (3, 4), (5, 6), (7, 8)] # Some output of zip() function
unzip = lambda z: list(zip(*z))
unzip(z)

##//--------------------------------------------------------------------------------------------------------------------//
##Sets - Unordered collection of unique elements
my_set = set()
my_set.add(1)  # {1}
my_set.add(100)# {1, 100}
my_set.add(100)# {1, 100} --> no duplicates!
new_list = [1,2,3,3,3,4,4,5,6,1]
set(new_list)           # {1, 2, 3, 4, 5, 6}

my_set.remove(100)      # {1} --> Raises KeyError if element not found
my_set.discard(100)     # {1} --> Doesn't raise an error if element not found
my_set.clear()          # {}
new_set = {1,2,3}.copy()# {1,2,3}

set1 = {1,2,3}
set2 = {3,4,5}
set3 = set1.union(set2)               # {1,2,3,4,5}
set4 = set1.intersection(set2)        # {3}
set5 = set1.difference(set2)          # {1, 2}
set6 = set1.symmetric_difference(set2)# {1, 2, 4, 5}
set1.issubset(set2)                   # False
set1.issuperset(set2)                 # False
set1.isdisjoint(set2)                 # False --> return True if two sets have a null intersection.

##//--------------------------------------------------------------------------------------------------------------------//
##Comparison Operators
    # ==                   # equal values
    # !=                   # not equal
    #  >                    # left operand is greater than right operand
    #  <                    # left operand is less than right operand
    # >=                   # left operand is greater than or equal to right operand
    # <=                   # left operand is less than or equal to right operand  
    # <element> is <element> # check if two operands refer to same object in memory


##//--------------------------------------------------------------------------------------------------------------------//

##Logical Operators
1 < 2 and 4 > 1 # True
1 > 3 or 4 > 1  # True
1 is not 4      # True
not True        # False
1 not in [2,3,4]# True
#if <condition that evaluates to boolean>:
  # perform action1
#elif <condition that evaluates to boolean>:
  # perform action2
#else:
  # perform action3


##//--------------------------------------------------------------------------------------------------------------------//
##Loops
#my_list3 = [1,2,3]
#my_tuple2 = (1,2,3)
#my_list2 = [(1,2), (3,4), (5,6)]
#y_dict = {'a': 1, 'b': 2. 'c': 3}

for num in my_list3:
    print(num) # 1, 2, 3

for num in my_tuple2:
    print(num) # 1, 2, 3

for num in my_list2:
    print(num) # (1,2), (3,4), (5,6)

for num in '123':
    print(num) # 1, 2, 3

for k,v in my_dict.items(): # Dictionary Unpacking
    print(k) # 'a', 'b', 'c'
    print(v) # 1, 2, 3

#while <condition that evaluates to boolean>:
  # action
#  if <condition that evaluates to boolean>:
#    break # break out of while loop
#  if <condition that evaluates to boolean>:
#    continue # continue to the next line in the block
  
##Range
range(10)          # range(0, 10) --> 0 to 9
range(1,10)        # range(1, 10)
list(range(0,10,2))# [0, 2, 4, 6, 8]

##Enumerate
for i, el in enumerate('helloo'):
  print(f'{i}, {el}')
# 0, h
# 1, e
# 2, l
# 3, l
# 4, o
# 5, o

##Lambda
# lambda: <return_value>
# lambda <argument1>, <argument2>: <return_value>

# Factorial
from functools import reduce
n = 3
factorial = reduce(lambda x, y: x*y, range(1, n+1))
print(factorial) #6


# Fibonacci
fib = lambda n : n if n <= 1 else fib(n-1) + fib(n-2)
result = fib(10)
print(result) #55

##//--------------------------------------------------------------------------------------------------------------------//
