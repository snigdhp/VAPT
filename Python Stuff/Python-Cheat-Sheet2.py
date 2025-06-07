#PYTHON**CHEAT**SHEET

#Hello world
print("Hello world!")

##---------------------------------------------------------------------------##
#Hello World with message
msg = "Hello World"
print(msg)

##---------------------------------------------------------------------------##
#f-strings (using variables in strings)
first_name = {Snigdh}
second_name = {Panwar}
full_name = f"{first_name} {last_name}"
print(full_name)

##---------------------------------------------------------------------------##
#Data Types

    # Text Type:	str   -- x = "Hello World"
    # Numeric Types:	int, float, complex -- 20, 20.5, 1j
    # Sequence Types:	
        # list, ["apple", "banana", "cherry"]
        # tuple, ("apple", "banana", "cherry")
        # range -- x = range(6)  
        # Mapping Type:	dict --  {"name" : "John", "age" : 36}
    # Set Types:	set, frozenset --- {"apple", "banana", "cherry"}, frozenset({"apple", "banana", "cherry"})
    # Boolean Type:	bool -- True
    # Binary Types:	bytes, bytearray, memoryview --  b"Hello",  bytearray(5), memoryview(bytes(5))
    # None Type:	NoneType -- None

##---------------------------------------------------------------------------##
#Python Casting
    # * int() - constructs an integer number from an integer literal,
    # * float() - constructs a float number from an integer literal, 
    # * str() - constructs a string from a wide variety of data types, 

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3


x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2


x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
##---------------------------------------------------------------------------##
#Python String

    # String is a collection of alphabets, words or other characters.
    # It is one of the primitive data structures and are the building blocks for data manipulation.
    # Python has a built-in string class named str . 
    # Python strings are "immutable" which means they cannot be changed after they are created.

print("hello")      # print String

a = "hello"         # Assign String to a Variable
print(a)

a = "Hello, World!"
print(a[1])         # Strings are Arrays

for x in "banana":
   print(x)          #Looping Through a String

a = "Hello, World!"
print(len(a))    #get the length of a string, use the len() function.

a = "Hello im new to python"
print("new" in a) # in keyword is used to check whether sentence or character is present in String

txt = "The best things in life are free!"
print("expensive" not in txt)  #  certain phrase or character is NOT present in a string, we can use the keyword not in.

##String Slicing

b = "Hello, World!"
print(b[2:5]) # String slicing

b = "Hello, World!"
print(b[:5])  # Slice From the Start

b = "Hello, World!"
print(b[2:])  #Slice To the End

b = "Hello, World!"
print(b[-5:-2])# Negative slicing

txt = "We are the so-called \"Vikings\" from the north."
print(txt)  #escape character

#String Method
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning
##---------------------------------------------------------------------------## 
#python random Module
import random

random_integer = random.randint(1,10)
print(random_integer)


##---------------------------------------------------------------------------##

#What are lists?
#A list stores a series of items in a particular order. Lists
#allow you to store sets of information in one place,
#whether you have just a few items or millions of items

lst=[10, 20, 30, 40, 50]

#items count
print(len(lst))  # 5

#indexing index from 0 //(here from 0 to 4)

#Individual access to items via lst
lst[0] #10
lst[-1] # 50

lst[1] # 20
lst[-2] #40

lst[:-1]   #[10,20,30,40] 
lst[::-1]  #[50,40,30,20,10] 
lst[1:3]   #[20,30]
lst[1:-1]  #[20,30,40]
lst[-3:-1] #[30,40] 
lst[3:]    #[40,50]
lst[::-2]  #[50,30,10]
lst[::2]   #[10,30,50]
lst[:]     #[10,20,30,40,50]

#On mutable sequences (list), remove with del lst[3:5] and modify with assignment lst[1:4]=[15,25]

#Making a list
users = ['val', 'bob', 'mia', 'ron', 'ned']

#Getting the first element
first_user = users[0]

#Getting the second element
second__user = users[1]

#Getting the last element
last_user = users[-1]

#Changing an element

users = ['val', 'bob', 'mia', 'ron', 'ned']
users[0] = 'valerie'
users[1] = 'robert'
users[-2] = 'ronald'
print(users)

#Adding an element to the end of the list
users.append("any")

#Starting with an empty list
users = []
users.append('amy')
users.append('val')
users.append('bob')
users.append('mia')

#Inserting elements at a particular position
users.insert(0, 'joe')
users.insert(3, 'bea')

#Deleting an element by its position
del users[-1]

#Removing an item by its value
users.remove('mia')

##Popping elemant
#Pop the last item from a list
most_recent_user = users.pop()
print(most_recent_user)

#Pop the first item in a list
first_user = users.pop(0)
print(first_user)

#List length
#The len() function returns the number of items in a list.

#Find the length of a list
num_users = len(users)
print(f"We have {num_users} users.")


#Sorting a list
#The sort() method changes the order of a list permanently.
#The sorted() function returns a copy of the list, leaving the
#original list unchanged.

#Sorting a list permanently
users.sort()

#Sorting a list permanently in reverse alphabetical order
users.sort(reverse=True)

#Sorting a list temporarily
print(sorted(users))
print(sorted(users, reverse=True))

#Reversing the order of a list
users.reverse()

#Printing all items in a list
users = ['val', 'bob', 'mia', 'ron', 'ned']
for user in users:
    print(user)

#Looping through a list
bikes = ['trek', 'redline', 'giant']
for bike in bikes:
    print(bike)

#Making numerical lists
squares = []
for x in range(1, 11):
    squares.append(x**2)

#List comprehensions
squares = [x**2 for x in range(1, 11)]


#Slicing a list
finishers = ['sam', 'bob', 'ada', 'bea']
first_two = finishers[:2]

#Copying a list // 3 ways of copy a list
bikes = ['trek', 'redline', 'giant']
copy_of_bikes = bikes[:]
print(copy_of_bikes)

bikes = ['trek', 'redline', 'giant']
copy_of_bikes = bikes.copy()
print(copy_of_bikes)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

##Combine two nested listed
fruits = ["apple","banan","kiwi","grapes","oranges","peaches"]
vegetable  = ["onion","tomato","cabage"]
combine_dozen = [fruits,vegetable]
print(combine_dozen)

#Methods - list
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

#apend()
bikes = ['trek', 'redline', 'giant']
bikes.append('Apple')
print(bikes)

#copy()
bikes = ['trek','redline','giant','apple']
copy_of_bikes = bikes.copy()
print(copy_of_bikes)

#clear()
bikes = ['trek','redline','giant','apple']
bikes.clear()
print(bikes)

#count()
bikes = ['trek','redline','giant','apple']
cb = bikes.count('trek')
print(cb)

#extend()
bikes = ['trek','redline','gaint','major']
fruits = ['pulp', 'water', 'organge']
bikes.extend(fruits)
print(bikes)

#pop()
bikes = ['trek','redline','gaint','major']
bikes.pop(1)
print(x)

#index()
bikes = ['trek','redline','gaint','major']
x = bikes.index('major')
print(x)

#insert()
bikes = ['trek','redline','gaint','major']
bikes.insert(1,'sxf')
print(bikes)

#remove()
bikes =  ['trek','redline','gaint','major']
bikes.remove('major')
print(bikes)

#reverse()
bikes =  ['trek','redline','gaint','major']
bikes.reverse()
print(bikes)


#sort()
bikes = ['trek','redline','gaint','major']
bikes.sort()
print(bikes)

##---------------------------------------------------------------------------##
#TUPLES
#Tuples are similar to lists, but the items in a tuple can't be
#modified.

#Making a tuple
dimensions = (1920, 1080)
resolutions = ('720p', '1080p', '4K')


#Looping through a tuple
for dimension in dimensions:
 print(dimension)

#Overwriting a tuple
dimensions = (800, 600)
print(dimensions)

dimensions = (1200, 900)
print(dimensions)

#E.g-2

my_tuple = ('apple','grapes','mango', 'grapes')
apple, grapes, mango, grapes = my_tuple# Tuple unpacking

len(my_tuple)                          # 4
my_tuple[2]                            # mango
my_tuple[-1]                           # 'grapes'

# Immutability
my_tuple[1] = 'donuts'  # TypeError
my_tuple.append('candy')# AttributeError

# Methods - Tuple
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

my_tuple.index('grapes') # 1
my_tuple.count('grapes') # 2


##---------------------------------------------------------------------------##
#DICTIONARY
#Dictionaries store connections between pieces of information. 
#Each item in a dictionary is a key-value pair

##A simple dictionary
alien = {'color': 'green', 'points': 5}

##Accessing a value
print(f"The alien's color is {alien['color']}.")

##Adding a new key-value pair
alien = {'color': 'green', 'points': 5}
alien['x_position'] = 0

#Adding a key-value pair
alien = {'color': 'green', 'points': 5}
alien['x'] = 0
alien['y'] = 25
alien['speed'] = 1.5

#Getting the value associated with a key
alien_= {'color': 'green', 'points': 5}
print(alien['color'])
print(alien['points'])

#Starting with an empty dictionary
alien = {}
alien['color'] = 'green'
alien['points'] = 5

#Modifying values in a dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# Change the alien's color and point value.
alien_0['color'] = 'yellow'
alien_0['points'] = 10
print(alien_0)

#Deleting a key-value pair
alien= {'color': 'green', 'points': 5}
print(alien)
del alien['points']
print(alien)


##Looping through all key-value pairs
fav_numbers = {'eric': 7, 'ever': 4, 'erin': 47}

for name, number in fav_numbers.items():
    print(f"{name} loves {number}.")

##Looping through all keys
fav_numbers = {'eric': 7, 'ever': 4, 'erin': 47}
for name in fav_numbers.keys():
    print(f"{name} loves a number.")

##Looping through all the values
fav_numbers = {'eric': 7, 'ever': 4, 'erin': 47}
for number in fav_numbers.values():
    print(f"{number} is a favorite.")

#Python dictionaries have several methods such as These methods allow you to access, modify,
#and manipulate data in your dictionaries in various ways.

# get(),  - The get() method allows you to retrieve the value of a specific key from the dictionary
# keys(),values(), - The keys() and values() methods return a list of all the keys and values in the dictionary, respectively.  
# items(), - The items() method is used to return a list of all key-value pairs in the dictionary. 
# update(), The update() method allows you to add new key-value pairs to a dictionary or modify existing ones. 
# pop(). - The pop() method is used to remove a key-value pair from a dictionary.

#Methods - Dictionary
fav_numbers = {'eric': 7, 'ever': 4, 'erin': 47}
#get()
print(fav_numbers.get('eric'))
print(fav_numbers.get('david', 'notfound'))


#Keys()  & values ()
print(fav_numbers.keys())
print(fav_numbers.values())

#items()
print(fav_numbers.items())

#update()
print(fav_numbers.update({'eric': 10}))
print(fav_numbers)

##---------------------------------------------------------------------------##
#User input
#Your programs can prompt the user for input. All input is
#stored as a string.


#Prompting for a value
name = input("What's your name? ")
print(f"Hello, {name}!")


#Prompting for numerical input
age = input("How old are you? ")
age = int(age)

pi = input("What's the value of pi? ")
pi = float(pi)

##---------------------------------------------------------------------------##
##Logical Operators
1 < 2 and 4 > 1 # True
1 > 3 or 4 > 1  # True
1 is not 4      # True
not True        # False
1 not in [2,3,4]# True

#And
s = 58
if s < 60 and s > 50:
    print("Your grade is C")

#or
age = 12
if age < 16 or age > 200:
    print("Can't drive")

#not
if not 3 > 1:
    print("something")
    #Will not be printed.

#comparison operators
    #> Greater than
    #< Lesser than
    #>= Greater than or equal to
    #<= Lesser than or equal to
    #== Is equal to
    #!= Is not equal to

##---------------------------------------------------------------------------##
#The range() function
#You can use the range() function to work with a set of
#numbers efficiently. The range() function starts at 0 by
#default, and stops one number below the number passed to
#it. You can use the list() function to efficiently generate a
#large list of numbers.

#Printing the numbers 0 to 1000
for number in range(1001):
 print(number)

#Printing the numbers 1 to 1000
for number in range(1, 1001):
 print(number)

#Making a list of numbers from 1 to a million
numbers = list(range(1, 1_000_001))
print(numbers)


#Finding the minimum value in a list
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
youngest = min(ages)

#Finding the maximum value
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
oldest = max(ages)

#Finding the sum of all values
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
total_years = sum(ages)

#Slicing a list
#Getting the first three items
finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']
first_three = finishers[:3]

#Getting the middle three items
middle_three = finishers[1:4]

#Getting the last three items
last_three = finishers[-3:]

##List Comprehension
#Using a loop to generate a list of square numbers
squares = []
for x in range(1, 11):
 square = x**2
 squares.append(square)

#Using a comprehension to generate a list of square
numbers
squares = [x**2 for x in range(1, 11)]

#Using a loop to convert a list of names to upper case
names = ['kai', 'abe', 'ada', 'gus', 'zoe']
upper_names = []
for name in names:
 upper_names.append(name.upper())

#Using a comprehension to convert a list of names to upper case
names = ['kai', 'abe', 'ada', 'gus', 'zoe']
upper_names = [name.upper() for name in names]

##---------------------------------------------------------------------------##
#If statements
#If statements are used to test for particular conditions and
#espond appropriately.

# Conditional tests
# equal              x == y
# not equal          x != y
# greater than       x > y
# or equal to        x >= y
# less than          x < y
# or equal to        x <= y



##---------------------------------------------------------------------------##
#IF Statements
#E.g -1
if age >= 18:
    print("You can vote!")

#E.g - 2
number = int(input("Please enter the number\n"))
if (number%2) == 0:
    print("This is an even number")
else:
    print("This is an odd number")

#E-g- 3 
n = 5
if n > 2:
    print("Larger than 2")

#elif
# he elif keyword is Python's way of saying 
# "if the previous conditions were not true, then try this condition".

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#Else statements
#Else - This is a way to specify some code that will be executed if a condition is false

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


#If-elif-else statements
if age < 4:
    ticket_price = 0
elif age < 18:
    ticket_price = 10
elif age < 65:
    ticket_price = 40
else:
    ticket_price = 15

#E-g-1
weather = str(input("Please enter the weather"))
weather = "sunny"
if weather == "rain":
    print("bring umbrella")
elif weather == "sunny":
    print("bring sunglasses")
elif weather == "snow":
    print("bring gloves")

#Short hand if
if a > b: print("a is greater than b")

#short hand if else
a = 2
b = 330
print("A") if a > b else print("B") 


#Nested If
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
##---------------------------------------------------------------------------##
#While loops
#A while loop repeats a block of code as long as a certain condition is true. While loops are especially useful when you
#can't know ahead of time how many times a loop should run


#A simple while loop
i = 1
while i < 6:
   print(i)
   i+=1

#break Statement 
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#continue Statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

##---------------------------------------------------------------------------##
#For loops
# A for loop is used for iterating over a sequence 
# (that is either a list, a tuple, a dictionary, a set, or a string).

fruits = ['apple','grapes','oranges']
for x in fruits:
   print(x)

#loops for a string 
for x in "banana":
  print(x) 

#breaks Statments
fruits = ['apple','grapes','oranges']
for x in fruits:
   print(x)
   if x == 'grapes':
      break
##---------------------------------------------------------------------------##  
#Define a Function  
def my_function():
  print("Hello from a function")


#Python Lambdas