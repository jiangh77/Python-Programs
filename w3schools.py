# -*- coding: utf-8 -*-
"""
Created on Sun May 15 00:38:19 2022

@author: jiang
"""

# https://www.w3schools.com/python/
# run selection or current line - F9

# https://www.w3schools.com/python/python_getstarted.asp

print ("Hello, World!")

#%%

# https://www.w3schools.com/python/python_syntax.asp

if 5 > 2:
    print ("Five is greater than two!")

if 5 > 2:
 print ("Five is greater than two!")

if 5 > 2:
    print ("Five is greater than two!")

x = 5
y = "Hello, World!"

# This is a comment

print (y)

print ("Hello, World!")

#%%

# https://www.w3schools.com/python/python_comments.asp

# single line comment

print ("Hello, World!") # comment

"""
multi line comment

"""

# multi line
# comment

#%%

# https://www.w3schools.com/python/python_variables.asp

x = 5
y = "John"
print (x)
print (y)

x = 4 # x is type of int
x = "Sally" # x is reassigned as type str
print (x)

x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0

print (x)
print (y)
print (z)

x = 5
y = "John"
print (type(x))
print (type(y))

x = "John"
print (x)
print (type(x))
# is the same as
x = 'John'
print (x)
print (type(x))

a = 4
A = "Sally"
# A will not overwrite a
print (a)
print (A)

#%%

# https://www.w3schools.com/python/python_variables_names.asp

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print (myvar)
print (my_var)
print (_my_var)
print (myVar)
print (MYVAR)
print (myvar2)

"""

Illegal variable names:

2myvar = "John"
my-var = "John"
my var = "John"

"""

# Camel Case
# Each word, except the first, starts with a capital letter:

myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:

MyVariableName = "John"

# Snake Case
# Each word is separated by an underscore character:
    
my_variable_name = "John"

#%%

# https://www.w3schools.com/python/python_variables_multiple.asp

# Many Values to Multiple Variables

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables

x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#%%

# https://www.w3schools.com/python/python_variables_output.asp

# Output Variables
# The Python print statement is often used to output variables.

x = "Python is awesome"
print(x)

# In the print() function, you output multiple variables, separated by a comma:

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

# For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
# below causes an error
x = 5
y = "John"
print(x + y)

# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = 5
y = "John"
print(x, y)

#%%

# https://www.w3schools.com/python/python_variables_global.asp

"""

Global Variables
Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

"""

x = "awesome" # Global variable

# Define a function

def myfunc():
  print("Python is " + x)

myfunc() # this line executes the function

"""

If you create a variable with the same name inside a function
this variable will be local, and can only be used inside the function
The global variable with the same name will remain as it was, global and with the original value.

"""

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

"""
Normally, when you create a variable inside a function, that variable is local
and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.

"""
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

"""

Also, use the global keyword if you want to change a global variable inside a function.

"""
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#%%

# https://www.w3schools.com/python/python_datatypes.asp

#%%

# https://www.w3schools.com/python/python_numbers.asp

# Variables of numeric types are created when you assign a value to them:

# Example

x = 1    # int
y = 2.8  # float
z = 1j   # complex

# To verify the type of any object in Python, use the type() function:

# Example

print(type(x))
print(type(y))
print(type(z))


# Int
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

# Example

# Integers:
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Float

# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

# Example

# Floats:
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10.

# Example

# Floats:
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# Complex

# Complex numbers are written with a "j" as the imaginary part:

# Example

# Complex:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:

# Example

# Convert from one type to another:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Random Number

# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

# Example

# Import the random module, and display a random number between 1 and 9:

import random

print(random.randrange(1, 10))

#%%

# https://www.w3schools.com/python/python_casting.asp

"""

Python Casting

Specify a Variable Type

There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:
•	int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
•	float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
•	str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

"""
# Example

# Integers:
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

print (x)
print (y)
print (z)

# Example

# Floats:
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

print (x)
print (y)
print (z)
print (w)

# Example

# Strings:
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

print (x)
print (y)
print (z)

#%%

# https://www.w3schools.com/python/python_strings.asp

# Python Strings

"""
Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.
'hello' is the same as "hello".
You can display a string literal with the print() function:

"""

# Example
print("Hello")
print('Hello')

# Assign String to a Variable
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

# Example
a = "Hello"
print(a)

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:

# Example
# You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Or three single quotes:

# Example

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

"""
Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.

"""

# Example
# Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])

# Looping Through a String

# Since strings are arrays, we can loop through the characters in a string, with a for loop.

# Example
# Loop through the letters in the word "banana":

for x in "banana":
  print(x)


# String Length

# To get the length of a string, use the len() function.

# Example

# The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.

# Example
# Check if "free" is present in the following text: if it exists it is True (boolean)

txt = "The best things in life are free!"
print("free" in txt)

# Use it in an if statement:

# Example
# Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Check if NOT

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

# Example
# Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)

# Use it in an if statement:

# Example
# print only if "expensive" is NOT present:

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#%%

# https://www.w3schools.com/python/python_strings_slicing.asp

# Slicing
# Get the characters from position 2 to position 5 (not included):
# Note: The first character has index 0.

b = "Hello, World!"
print(b[2:5])

# Slice From the Start
# Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])

# Slice To the End
# Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])

"""
Negative Indexing
Use negative indexes to start the slice from the end of the string:
Example
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):

"""

# Negative indexing, index starts at 0 (the last character)

b = "Hello, World!"
print(b[-5:-2])

#%%

# https://www.w3schools.com/python/python_strings_modify.asp

# Upper Case

a = "Hello, World!"
print(a.upper())

# Lower Case

a = "Hello, World!"
print(a.lower())

# The strip() method removes any whitespace from the beginning or the end:

a = "  Hello,   World!  "
print(a.strip())

# The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))

# The split() method returns a list where the text between the specified separator becomes the list items.

a = "Hello, World!"
print(a.split(","))

#%%

# Merge variable a with variable b into variable c:

a = "Hello"
b = "World"
c = a + b
print(c)

# To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#%%

# https://www.w3schools.com/python/python_strings_format.asp

"""
String Format
As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

Example
age = 36
txt = "My name is John, I am " + age
print(txt)

"""

# Use the format() method to insert numbers into strings:

age = 44
txt = "My name is Howard, and I am {}"
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars"
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}"
print(myorder.format(quantity, itemno, price))

#%%

# https://www.w3schools.com/python/python_strings_escape.asp

"""

Python - Escape Characters

Escape Character
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.
An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

Example
You will get an error if you use double quotes inside a string that is surrounded by double quotes:

txt = "We are the so-called "Vikings" from the north."

"""

# To fix this problem, use the escape character \":

# Example
# The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the North."
print(txt)

#%%

# https://www.w3schools.com/python/python_strings_methods.asp

# Converts the first character to upper case, and only the first character, rest of the string is lower case

a = "test Capital"
print(a.capitalize())

# Searches the string for a specified value and returns the position of where it was found, only returns the first

a = "test Capital"
print(a.find("t"))

# Searches the string for a specified value and returns the position of where it was found, only returns the first

a = "test Capital"
print(a.index("t"))

a = "test Capital"
print(a.index("C"))

#%%

# https://www.w3schools.com/python/python_strings_exercises.asp

x = "Hello World"
print(len(x))

#%%

# https://www.w3schools.com/python/python_booleans.asp

# evaluate 2 values

print(10 > 9)
print(10 == 9)
print(10 < 9)

# Print a message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Evaluate a string and a number:

print(bool("Hello"))
print(bool(15))

# Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

"""

Most Values are True
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.

"""
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

"""

Some Values are False
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

"""

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

"""
One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
"""

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Print the answer of a function:

def myFunction() :
  return True

print(myFunction())

# Print "YES!" if the function returns True, otherwise print "NO!":
# definition of myFunction is to return a True value, so it will always be True

def myFunction():
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

"""
Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

Example
Check if an object is an integer or not:

"""

# check if x is an integer
# check if x is a string
# check if x is a float

x = 200
print(isinstance(x, int))

print(isinstance(x, str))

print(isinstance(x, float))

#%%

# https://www.w3schools.com/python/python_operators.asp

print(10 + 5)

"""

Python divides the operators in the following groups:
Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators

"""
print(10*5)

#%%

# https://www.w3schools.com/python/python_lists.asp

thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

list1 = ['abc', 34, True, 40, 'male']
print(list1)

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = list(('apple', 'banana', 'cherry'))
print(thislist)

#%%

# https://www.w3schools.com/python/python_lists_access.asp

# Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Print the last item of the list:
thislist = ['apple', 'banana', 'cherry']
print(thislist[-1])

# Return the third, fourth, and fifth item:
thislist = ['apple', 'banana', 'cherry', "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# This example returns the items from "cherry" to the end:
thislist = ['apple', 'banana', 'cherry', "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

#%%

# https://www.w3schools.com/python/python_lists_change.asp

# To change the value of a specific item, refer to the index number:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)

thislist[1:3] = ["blackcurrent", "watermelon"]
print(thislist)

# Change the values "banana", "cherry" and "orange" with the values "blackcurrant", "watermelon" and "Test":
thislist[1:4] = ["blackcurrent", "watermelon", "Test"]
print(thislist)

# Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist[1:3] = ["watermelon"]
print(thislist)

# The insert() method inserts an item at the specified index:
thislist = ['apple', 'banana', 'cherry']
print(thislist)

thislist.insert(2, 'watermelon')
print(thislist)

# As a result of the example above, the list will now contain 4 items.

#%%

# https://www.w3schools.com/python/python_lists_add.asp

# Append items
# Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert items
# Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Extend list
# Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Add any iterable
# Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#%%

# https://www.w3schools.com/python/python_lists_remove.asp

# Remove "banana": 

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Only removes the first "banana"

thislist = ["apple", "banana", "cherry", "banana"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index
# The pop() method removes the specified index.

# Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# If you do not specify the index, the pop() method removes the last item.

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword also removes the specified index:
# Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely.
# Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)

#%%

# https://www.w3schools.com/python/python_lists_loop.asp

# You can loop through the list items by using a for loop:
# Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
# Print all items by referring to their index number:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# The iterable created in the example above is [0, 1, 2].

print(len(thislist))

# Using a While Loop

# You can loop through the list items by using a while loop.
# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by refering to their indexes.
# Remember to increase the index by 1 after each iteration.

# Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:
# A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


#%%

# https://www.w3schools.com/python/python_lists_comprehension.asp

# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Example:
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# With list comprehension you can do all that with only one line of code:
# Example

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# The Syntax
# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.

# Condition
# The condition is like a filter that only accepts the items that valuate to True.

# Example
# Only accept items that are not "apple":

newlist = [x for x in fruits if x != "apple"]
print(newlist)

# Example
# With no if statement:

print(fruits)
newlist = [x for x in fruits]
print(newlist)

# Iterable
# The iterable can be any iterable object, like a list, tuple, set etc.

#Example
# You can use the range() function to create an iterable:

newlist = [x for x in range(10)]

print(newlist)

# Same example, but with a condition:

# Example
# Accept only numbers lower than 5:

newlist = [x for x in range(10) if x < 5]
print(newlist)

# Expression
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

# Example
# Set the values in the new list to upper case:

newlist = [x.upper() for x in fruits]
print(newlist)

# You can set the outcome to whatever you like:

# Example
# Set all values in the new list to 'hello':

newlist = ['hello' for x in fruits]
print(newlist)

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

# Example
# Return "orange" instead of "banana":

newlist = [x if x != "banana" else "orange" for x in fruits]
print(fruits)
print(newlist)

# Input x if x is not ‘banana’, if it is ‘banana’ then put ‘orange’ in the list

#%%

# https://www.w3schools.com/python/python_lists_sort.asp

# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

# Example
# Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = ['orange', 'mango', 'kiwi', 'pineapple', 'banana']
thislist.sort()
print(thislist)

thislist.sort(reverse = True)
print(thislist)

# Example
# Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending
# To sort descending, use the keyword argument reverse = True:

# Example
# Sort the list descending:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Example
# Sort the list descending:

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first):

# Example
# Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort(key = myfunc)
print(thislist)

# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

# Example
# Case sensitive sorting can give an unexpected result:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Luckily we can use built-in functions as key functions when sorting a list.
# So if you want a case-insensitive sort function, use str.lower as a key function:

# Example
# Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Reverse Order
# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.

# Example
# Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#%%

# https://www.w3schools.com/python/python_lists_copy.asp

# Python - Copy Lists

# Copy a List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
# There are ways to make a copy, one way is to use the built-in List method copy().

# Example
# Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
print(thislist)

mylist = thislist.copy()
print(mylist)

# Another way to make a copy is to use the built-in method list().

# Example
# Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
print(thislist)

mylist = list(thislist)
print(mylist)

#%%

# https://www.w3schools.com/python/python_lists_join.asp

# Python - Join Lists

# Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.

# Example
# Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:

# Example
# Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

print(list2)

# Or you can use the extend() method, which purpose is to add elements from one list to another list:

# Example
# Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

print(list2)

#%%

# https://www.w3schools.com/python/python_lists_methods.asp

# Python - List Methods

# List Methods
# Python has a set of built-in methods that you can use on lists.


#%%

# https://www.w3schools.com/python/python_lists_exercises.asp

# Python List Exercises

# Test Yourself With Exercises
# Now you have learned a lot about lists, and how to use them in Python.
# Are you ready for a test?

# Try to insert the missing part to make the code work as expected:

# Exercise:
# Print the second item in the fruits list.

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#%%

# https://www.w3schools.com/python/python_tuples.asp

# Python Tuples

mytuple = ("apple", "banana", "cherry")

"""
Tuple

Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
"""

# Example
# Create a Tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)

"""
Tuple Items
Tuple items are ordered, unchangeable, and allow duplicate values.
Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Allow Duplicates
Since tuples are indexed, they can have items with the same value:

"""
    
# Example
# Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

"""
# Tuple Length
# To determine how many items a tuple has, use the len() function:
"""

# Example
# Print the number of items in the tuple:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

"""
# Create Tuple With One Item

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
"""

# Example
# One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))

# Below is NOT a tuple, it is a string

thistuple = ("apple")
print(type(thistuple))

"""
# Tuple Items - Data Types
# Tuple items can be of any data type:
"""

# Example
# String, int and boolean data types:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

# A tuple can contain different data types:

# Example
# A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

"""
# type()
# From Python's perspective, tuples are defined as objects with the data type 'tuple':
# <class 'tuple'>
"""

# Example
# What is the data type of a tuple?

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

"""
The tuple() Constructor
It is also possible to use the tuple() constructor to make a tuple.
"""

# Example
# Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove and/or add items whenever you like.
**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
"""
#%%

# https://www.w3schools.com/python/python_tuples_access.asp

"""
Python - Access Tuple Items

Access Tuple Items
You can access tuple items by referring to the index number, inside square brackets:
"""

# Example
# Print the second item in the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Note: The first item has index 0.

"""
Negative Indexing
Negative indexing means start from the end.
-1 refers to the last item, -2 refers to the second last item etc.
"""

# Example
# Print the last item of the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

"""
Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new tuple with the specified items.
"""

# Example
# Return the third, fourth, and fifth item:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

nexttuple = (thistuple[2:6])
print(nexttuple)

# Note: The search will start at index 2 (included) and end at index 5 (not included).

"""
Remember that the first item has index 0.
By leaving out the start value, the range will start at the first item:
"""

# Example
# This example returns the items from the beginning to, but NOT included, "kiwi":

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

# By leaving out the end value, the range will go on to the end of the list:

# Example
# This example returns the items from "cherry" and to the end:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

"""
Range of Negative Indexes
Specify negative indexes if you want to start the search from the end of the tuple:
"""

# Example
# This example returns the items from index -4 (included) to index -1 (excluded)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

"""
Check if Item Exists
To determine if a specified item is present in a tuple use the in keyword:
"""

# Example
# Check if "apple" is present in the tuple:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#%%

# https://www.w3schools.com/python/python_tuples_update.asp

"""
Python - Update Tuples

Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

But there are some workarounds.

Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
"""

# Example
# Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
print(type(x))

y = list(x)

print(type(y))
print(y)

y[1] = "kiwi"

print(type(y))
print(y)

x = tuple(y)

print(type(x))
print(x)

print(type(x))
print(type(y))

"""
Add Items
Since tuples are immutable, they do not have a build-in append() method, but there are other ways to add items to a tuple.

1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
"""

# Example
# Convert the tuple into a list, add "orange", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)

y = list(thistuple)

print(y)
print(type(y))

y.append("orange")
print(y)
print(type(y))

thistuple = tuple(y)

print(thistuple)
print(type(thistuple))


"""
2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
"""

# Example
# Create a new tuple with the value "orange", and add that tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

thistuple = thistuple + y
print(thistuple)

# Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.

"""
Remove Items
Note: You cannot remove items in a tuple.

Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
"""

# Example
# Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)

y = list(thistuple)
print(y)

y.remove("apple")
print(y)

thistuple = tuple(y)
print(thistuple)

# Or you can delete the tuple completely:

# Example
# The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
print(thistuple)

del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#%%

# https://www.w3schools.com/python/python_tuples_unpack.asp

"""
Python - Unpack Tuples

Unpacking a Tuple
When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
"""

# Example
# Packing a tuple:

fruits = ("apple", "banana", "cherry")

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

# Example
# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

print(fruits)

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

"""
Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

Using Asterisk*
If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
"""

# Example
# Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
print(fruits)

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

# Example
# Add a list of values the "tropic" variable:

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

print(fruits)

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


#%%

# https://www.w3schools.com/python/python_tuples_loop.asp
# https://www.w3schools.com/python/ref_func_range.asp

"""
Python - Loop Tuples

Loop Through a Tuple
You can loop through the tuple items by using a for loop.
"""

# Example
# Iterate through the items and print the values:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

"""
Learn more about for loops in our Python For Loops Chapter.

Loop Through the Index Numbers
You can also loop through the tuple items by referring to their index number.
Use the range() and len() functions to create a suitable iterable.
"""

# Example
# Print all items by referring to their index number:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

for i in range(len(thistuple)):
  print(thistuple[i])

print(thistuple.range()


"""
https://www.w3schools.com/python/ref_func_range.asp
Range function
"""

# Example
# Create a sequence of numbers from 0 to 5, and print each item in the sequence:
x = range(6)
for n in x:
  print(n)

"""
Using a While Loop

You can loop through the list items by using a while loop.
Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by refering to their indexes.
Remember to increase the index by 1 after each iteration.
"""

# Example
# Print all items, using a while loop to go through all the index numbers:

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# Learn more about while loops in our Python While Loops Chapter.

#%%

# https://www.w3schools.com/python/python_tuples_join.asp

# Python - Join Tuples

# Join Two Tuples
# To join two or more tuples you can use the + operator:

# Example
# Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator:

# Example
# Multiply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#%%

# https://www.w3schools.com/python/python_tuples_methods.asp

"""
Python - Tuple Methods

Tuple Methods
Python has two built-in methods that you can use on tuples.

Method
Description
count()
Returns the number of times a specified value occurs in a tuple
index()
Searches the tuple for a specified value and returns the position of where it was found

https://www.w3schools.com/python/ref_tuple_count.asp

Python Tuple count() Method

Example
Return the number of times the value 5 appears in the tuple:

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)

Definition and Usage
The count() method returns the number of times a specified value appears in the tuple.

Syntax

tuple.count(value)
Parameter Values
Parameter
Description
value
Required. The item to search for

"""

mytuple = ("100X", "200X", "300X", "400X", "100X", "500X", "100X")
print(mytuple.count("100X"))

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)

"""
https://www.w3schools.com/python/ref_tuple_index.asp

Python Tuple index() Method

Example
Search for the first occurrence of the value 8, and return its position:

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)

Definition and Usage
The index() method finds the first occurrence of the specified value.
The index() method raises an exception if the value is not found.

Syntax

tuple.index(value)

Parameter Values
Parameter
Description
value
Required. The item to search for
"""
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)

#%%

# https://www.w3schools.com/python/python_tuples_exercises.asp

"""
Python - Tuple Exercises

Test Yourself With Exercises
Now you have learned a lot about tuples, and how to use them in Python.
Are you ready for a test?
Try to insert the missing part to make the code work as expected:

Exercise:
Print the first item in the fruits tuple.
"""

fruits = ("apple", "banana", "cherry")
print(fruits[0])

#%%

# https://www.w3schools.com/python/python_sets.asp

# Python Sets

myset = {"apple", "banana", "cherry"}

"""
Set
Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.
* Note: Set items are unchangeable, but you can remove items and add new items.

Sets are written with curly brackets.
"""

# Example
# Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)

"""
Note: Sets are unordered, so you cannot be sure in which order the items will appear.

Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.
Once a set is created, you cannot change its items, but you can remove items and add new items.

Duplicates Not Allowed
Sets cannot have two items with the same value.
"""

# Example
# Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

"""
Get the Length of a Set
To determine how many items a set has, use the len() function.
"""

# Example
# Get the number of items in a set:

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

"""
Set Items - Data Types
Set items can be of any data type:
"""

# Example
# String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(type(set1))
print(type(set2))
print(type(set3))

# A set can contain different data types:

# Example
# A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}

print(type(set1))

"""
type()
From Python's perspective, sets are defined as objects with the data type 'set':
<class 'set'>
"""

# Example
# What is the data type of a set?

myset = {"apple", "banana", "cherry"}
print(type(myset))

"""
The set() Constructor
It is also possible to use the set() constructor to make a set.
"""
# Example
# Using the set() constructor to make a set:

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove items and add new items.
**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
"""

#%%

# https://www.w3schools.com/python/python_sets_access.asp

"""
Python - Access Set Items

Access Items
You cannot access items in a set by referring to an index or a key.
But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
"""

# Example
# Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Example
# Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

# Change Items
# Once a set is created, you cannot change its items, but you can add new items.

#%%

# https://www.w3schools.com/python/python_sets_add.asp

"""
Python - Add Set Items

Add Items
Once a set is created, you cannot change its items, but you can add new items.
To add one item to a set use the add() method.
"""

# Example
# Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

thisset.add("avacado")

print(thisset)

# Remember set is unordered, so new item can appear in any place in the set

"""
Add Sets
To add items from another set into the current set, use the update() method.
"""

# Example
# Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

vegetables = {"tomatoes", "peppers"}
thisset.update(vegetables)

print(thisset)

# Remember set is unordered, so new item can appear in any place in the set

"""
Add Any Iterable
The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
"""

# Example
# Add elements of a list to at set:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

nextlist = ["tomatoes", "peppers"]
thisset.update(nextlist)

print(thisset)

# Remember set is unordered, so new item can appear in any place in the set

#%%

# https://www.w3schools.com/python/python_sets_remove.asp

"""
Python - Remove Set Items

Remove Item
To remove an item in a set, use the remove(), or the discard() method.
"""

# Example
# Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

thisset.remove("apple")

print(thisset)

thisset.remove("tomatoes") # this causes an error

print(thisset)

# Note: If the item to remove does not exist, remove() will raise an error.
# Note: If the item to remove does not exist, discard() will NOT raise an error.

# Example
# Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

thisset.discard("tomatoes")

print(thisset)

"""
You can also use the pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.

The return value of the pop() method is the removed item.
"""

# Example
# Remove the last item by using the pop() method:

thisset = {"apple", "banana", "cherry"}

print(thisset)

x = thisset.pop()

print(x)

print(thisset)

# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# Example
# The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}

print(thisset)

thisset.clear()

print(thisset)

# Example
# The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

#%%

# https://www.w3schools.com/python/python_sets_loop.asp

"""
Python - Loop Sets

Loop Items
You can loop through the set items by using a for loop:
"""

# Example
# Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

myset = {"walk", "jump", "exercise"}

for y in myset:
    print(y)

#%%

# https://www.w3schools.com/python/python_sets_join.asp

"""
Python - Join Sets
Join Two Sets

There are several ways to join two or more sets in Python.
You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
"""

# Example
# The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set4 = {4, 5, 6}
print(set4)

set5 = set3.union(set4)
print(set5)

# Example
# The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

set4 = {3, 4, 5}
print(set4)

set1.update(set4)

print(set1)

"""
Note: Both union() and update() will exclude any duplicate items.

Keep ONLY the Duplicates
The intersection_update() method will keep only the items that are present in both sets.
"""

# Example
# Keep the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

a = {1, 2, 3}
b = {2, 3, 4}

a.intersection_update(b)

print(a)

# The intersection() method will return a new set, that only contains the items that are present in both sets.

# Example
# Return a set that contains the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

a = {1, 2, 3}
b = {2, 3, 4}

c = a.intersection(b)

print(c)

"""
Keep All, But NOT the Duplicates
The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
"""

# Example
# Keep the items that are not present in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

a = {1, 2, 3}
b = {2, 3, 4}

a.symmetric_difference_update(b)

print(a)

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

# Example
# Return a set that contains all items from both sets, except items that are present in both:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

a = {1, 2, 3}
b = {2, 3, 4}

c = a.symmetric_difference(b)

print(c)

#%%

# https://www.w3schools.com/python/python_sets_methods.asp

"""

Python - Set Methods

Set Methods
Python has a set of built-in methods that you can use on sets.

"""

#%%

# https://www.w3schools.com/python/python_sets_exercises.asp

"""
Python - Set Exercises

Test Yourself With Exercises
Now you have learned a lot about sets, and how to use them in Python.
Are you ready for a test?

Try to insert the missing part to make the code work as expected:
"""

# Exercise:
# Check if "apple" is present in the fruits set.

fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
  
#%%

# https://www.w3schools.com/python/python_dictionaries.asp

# Python Dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)

pokerdict = {
    "High Card": "A",
    "Mid Card": 8,
    "Card List": [2, 3, 4],
    "Result": True
}

print(pokerdict)

"""""
Dictionary

Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values:
"""

# Example
# Create and print a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

"""
Dictionary Items

Dictionary items are ordered, changeable, and does not allow duplicates.
Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
"""

# Example
# Print the "brand" value of the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

pokerdict = {
    "High Card": "A",
    "Mid Card": 8,
    "Card List": [2, 3, 4],
    "Result": True
}

print(pokerdict["High Card"])


"""
Ordered or Unordered?

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

Changeable

Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

Duplicates Not Allowed
Dictionaries cannot have two items with the same key:
"""

# Example
# Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


# Dictionary Length
# To determine how many items a dictionary has, use the len() function:

# Example
# Print the number of items in the dictionary:

print(len(thisdict))

# Dictionary Items - Data Types
# The values in dictionary items can be of any data type:

# Example
# String, int, boolean, and list data types:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

"""
type()

From Python's perspective, dictionaries are defined as objects with the data type 'dict':
<class 'dict'>
"""

# Example
# Print the data type of a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

# Try putting list, set and tuple in a dictionary

# Putting a list within a dictionary

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "List": ["List 1", "List 2", "List 3"]
}
print(thisdict)

# Putting a tuple within a dictionary

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "Tuple": ("Tuple 1", "Tuple 2", "Tuple 3")
}
print(thisdict)



# Putting a set within a dictionary

"""
Set is mutable so it can not be a key in a dictionary
"""

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "Set": ("Set 1", "Set 2", "Set 3") # this is wrong
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "List": ["List 1", "List 2", "List 3"],
  "Tuple": ("Tuple 1", "Tuple 2", "Tuple 3"),
  "Set": (["Set 1", "Set 2", "Set 3"])  # this is wrong
}
print(thisdict)

print(type(thisdict))

#%%

# https://www.w3schools.com/python/python_dictionaries_access.asp

"""
Python - Access Dictionary Items
Accessing Items
You can access the items of a dictionary by referring to its key name, inside square brackets:
"""
    
# Example
# Get the value of the "model" key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

print(x) # output - Mustang

# There is also a method called get() that will give you the same result:

# Example
# Get the value of the "model" key:

x = thisdict.get("model")

print(x) # output - Mustang

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.

# Example
# Get a list of the keys:

x = thisdict.keys()

print(x)

# output - dict_keys(['brand', 'model', 'year'])

# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
# Example
# Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) # before the change

# output - dict_keys(['brand', 'model', 'year'])

car["color"] = "white"

print(x) # after the change

# output - dict_keys(['brand', 'model', 'year', 'color'])
# key 'color' is added, corresonding value is added at the same time

# Get Values
# The values() method will return a list of all the values in the dictionary.

# Example
# Get a list of the values:

x = thisdict.values()
print(x)

# output - dict_values(['Ford', 'Mustang', 1964])

y = car.values()
print(y)

# output - dict_values(['Ford', 'Mustang', 1964, 'white'])

# The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
# Example
# Make a change in the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

# output - dict_values(['Ford', 'Mustang', 1964])

car["year"] = 2020

print(x) #after the change

# output - dict_values(['Ford', 'Mustang', 2020])

#Example
#Add a new item to the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

# output - dict_values(['Ford', 'Mustang', 1964])

car["color"] = "red"

print(x) #after the change

# output - dict_values(['Ford', 'Mustang', 1964, 'red'])

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.

# Example
# Get a list of the key:value pairs

x = thisdict.items()

print(x)

# output - dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.

# Example
# Make a change in the original dictionary, and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) # before the change

# output - dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car["year"] = 2020

print(x) # after the change

# output - dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])

# Example
# Add a new item to the original dictionary, and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) # before the change

# output - dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car["color"] = "red"

print(x) # after the change

# output - dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:

# Example
# Check if "model" is present in the dictionary:

thisdict = {
 "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# output - Yes, 'model' is one of the keys in the thisdict dictionary

#%%

# https://www.w3schools.com/python/python_dictionaries_change.asp

"""
Python - Change Dictionary Items

Change Values
You can change the value of a specific item by referring to its key name:
"""

# Example
# Change the "year" to 2018:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)

# output - {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

thisdict["year"] = 2018

print(thisdict)

# output - {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

"""
Update Dictionary
The update() method will update the dictionary with the items from the given argument.
The argument must be a dictionary, or an iterable object with key:value pairs.
"""

# Example
# Update the "year" of the car by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)

# output - {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

thisdict.update({"year": 2020})

print(thisdict)

# output - {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#%%

# https://www.w3schools.com/python/python_dictionaries_add.asp

"""
Python - Add Dictionary Items

Adding Items
Adding an item to the dictionary is done by using a new index key and assigning a value to it:
"""

# Example

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)

# output - {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

thisdict["color"] = "red"

print(thisdict)

# output - {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

"""
Update Dictionary

The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
The argument must be a dictionary, or an iterable object with key:value pairs.
"""

# Example
# Add a color item to the dictionary by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)

# output - {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

thisdict.update({"color": "red"})

print(thisdict)

# output - {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

#%%

# https://www.w3schools.com/python/python_dictionaries_remove.asp

"""
Python - Remove Dictionary Items

Removing Items
There are several methods to remove items from a dictionary:
"""

# Example
# The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
# output - {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

thisdict.pop("model")

print(thisdict)
# output - {'brand': 'Ford', 'year': 1964}

# Example
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
# output - {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

thisdict.popitem()

print(thisdict)
# output - {'brand': 'Ford', 'model': 'Mustang'}

# Example
# The del keyword removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
# output - {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

del thisdict["model"]

print(thisdict)
# output - {'brand': 'Ford', 'year': 1964}

# Example
# The del keyword can also delete the dictionary completely:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
# output - {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

del thisdict
print(thisdict) # this will cause an error because "thisdict" no longer exists.

# NameError: name 'thisdict' is not defined

# Example
# The clear() method empties the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
# output - {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

thisdict.clear()

print(thisdict)
# output - {}

#%%
# https://www.w3schools.com/python/python_dictionaries_loop.asp

"""
Python - Loop Dictionaries

Loop Through a Dictionary
You can loop through a dictionary by using a for loop.
When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
"""

# Example
# Print all key names in the dictionary, one by one:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(x)

"""
output
brand
model
year
"""

# Example
# Print all values in the dictionary, one by one:

for x in thisdict:
  print(thisdict[x])

"""
output
Ford
Mustang
1964
"""

# Example
# You can also use the values() method to return values of a dictionary:

for x in thisdict.values():
  print(x)

"""
output
Ford
Mustang
1964
"""

# Example
# You can use the keys() method to return the keys of a dictionary:

for x in thisdict.keys():
  print(x)

"""
output
brand
model
year
"""

# Example
# Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y)

"""
output
brand Ford
model Mustang
year 1964
"""

#%%

# https://www.w3schools.com/python/python_dictionaries_copy.asp

"""
Python - Copy Dictionaries

Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
There are ways to make a copy, one way is to use the built-in Dictionary method copy().
"""
# Example
# Make a copy of a dictionary with the copy() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
# output - {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Another way to make a copy is to use the built-in function dict().

# Example
# Make a copy of a dictionary with the dict() function:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
# output - {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#%%

# https://www.w3schools.com/python/python_dictionaries_nested.asp

"""
Python - Nested Dictionaries
Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.
"""

# Example
# Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
# output - {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

# Or, if you want to add three dictionaries into a new dictionary:
# Example
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

print(child1)
# output - {'name': 'Emil', 'year': 2004}

print(child2)
# output - {'name': 'Tobias', 'year': 2007}

print(child3)
# output - {'name': 'Linus', 'year': 2011}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)
# output - {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

#%%

"""
Python Dictionary Methods
Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.
"""
#%%

# https://www.w3schools.com/python/python_dictionaries_exercises.asp

"""
Python Dictionary Exercises

Test Yourself With Exercises
Now you have learned a lot about dictionaries, and how to use them in Python.
Are you ready for a test?
Try to insert the missing part to make the code work as expected:

Test Yourself With Exercises
"""
# Exercise:
# Use the get method to print the value of the "model" key of the car dictionary.

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)

x = car.get("model")
print(x)
# output - Mustang

print(car.get('model'))
# output - Mustang

print(car.get("model"))
# output - Mustang

#%%

# https://www.w3schools.com/python/python_conditions.asp

"""
Python If ... Else
Python Conditions and If statements
Python supports the usual logical conditions from mathematics:
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.
An "if statement" is written by using the if keyword.
"""

# Example
# If statement:

a = 33
b = 200
if b > a:
  print("b is greater than a")
# output - b is greater than a

# In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a. As a is 33, and b is 200, we know that 200 is greater than 33, and so we print to screen that "b is greater than a".


# Indentation
# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

# Example
# If statement, without indentation (will raise an error):

a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error

# output - IndentationError: expected an indented block

# Elif
# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

# Example
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
# output - a and b are equal

# In this example a is equal to b, so the first condition is not true, but the elif condition is true, so we print to screen that "a and b are equal".

# Else
# The else keyword catches anything which isn't caught by the preceding conditions.

# Example

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
# output - a is greater than b

# In this example a is greater than b, so the first condition is not true, also the elif condition is not true, so we go to the else condition and print to screen that "a is greater than b".
# You can also have an else without the elif:

# Example

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
# output - b is not greater than a

# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.

# Example
# One line if statement:
    
if a > b: print("a is greater than b")
# output - a is greater than b

# Short Hand If ... Else
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

# Example
# One line if else statement:

a = 2
b = 330
print("A") if a > b else print("B")
# output - B

# This technique is known as Ternary Operators, or Conditional Expressions.
# You can also have multiple else statements on the same line:

# Example
# One line if else statement, with 3 conditions:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# output =

# And
# The and keyword is a logical operator, and is used to combine conditional statements:

# Example
# Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
# output - Both conditions are True

# Or
# The or keyword is a logical operator, and is used to combine conditional statements:

# Example
# Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
# output - At least one of the conditions is True

# Nested If
# You can have if statements inside if statements, this is called nested if statements.

# Example

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

"""
output
Above ten,
and also above 20!
"""

x = 19

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

"""
output
Above ten,
but not above 20.
"""

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

# Example
a = 33
b = 200

if b > a:
  pass
# output - empty line

# Test Yourself With Exercises
# Exercise:
# Print "Hello World" if a is greater than b.

a = 50
b = 10
if a > b:
    print("Hello World")
# output - Hello World

#%%

# https://www.w3schools.com/python/python_while_loops.asp

"""
Python While Loops

Python Loops
Python has two primitive loop commands:
while loops
for loops

The while Loop
With the while loop we can execute a set of statements as long as a condition is true.
"""

# Example
# Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1
# output - 1 2 3 4 5

print(i)
# output - 6

"""
Note: remember to increment i, or else the loop will continue forever.

The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

The break Statement
With the break statement we can stop the loop even if the while condition is true:
"""

# Example
# Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# output - 1 2 3

print(i)
# output - 3

# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:

# Example
# Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
# output - 1 2 4 5 6

print(i)
# output - 6

# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:

# Example
# Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

"""
output
1 2 3 4 5
i is no longer less than 6
"""

print(i)

# output - 6

# Test Yourself With Exercises
# Exercise:
# Print i as long as i is less than 6.

i = 1
while i < 6:
    print(i)
    i += 1
# output - 1 2 3 4 5

print(i)
# output - 6

#%%

# https://www.w3schools.com/python/python_for_loops.asp

"""
Python For Loops

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""

# Example
# Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

"""
output
apple
banana
cherry
"""

# The for loop does not require an indexing variable to set beforehand.

# Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters:

# Example
# Loop through the letters in the word "banana":

for x in "banana":
  print(x)

"""
output
b
a
n
a
n
a
"""

# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:

# Example
# Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

"""
output
apple
banana
"""

# Example
# Exit the loop when x is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

"""
output
apple
"""


"""
The continue Statement
With the continue statement we can stop the current iteration of the loop, and continue with the next:
"""

# Example
# Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

"""
output
apple
cherry
"""

"""
The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
"""

# Example
# Using the range() function:

for x in range(6):
  print(x)

"""
output
0
1
2
3
4
5
"""

"""
Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
"""

# Example
# Using the start parameter:

for x in range(2, 6):
  print(x)

"""
output
2
3
4
5
"""

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

# Example
# Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)

"""
output
2
5
8
11
14
17
20
23
26
29
"""

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

# Example
# Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")

"""
output
0
1
2
3
4
5
Finally finished!
"""

# Note: The else block will NOT be executed if the loop is stopped by a break statement.

# Example
# Break the loop when x is 3, and see what happens with the else block:

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

# For loop is breaked when x = 3, the else part is not executed since For loop is not finished

"""
output
0
1
2
"""


"""
Nested Loops
A nested loop is a loop inside a loop.
The "inner loop" will be executed one time for each iteration of the "outer loop":
"""

# Example
# Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

"""
output
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry
"""

"""
The pass Statement
for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
"""

# Example
for x in [0, 1, 2]:
  pass

# prints nothing

"""
Test Yourself With Exercises
Exercise:
Loop through the items in the fruits list.
"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

"""
output
apple
banana
cherry
"""

#%%

# https://www.w3schools.com/python/python_functions.asp

"""
Python Functions

A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.

Creating a Function
In Python a function is defined using the def keyword:
"""
# Example

def my_function():
  print("Hello from a function")

"""
Calling a Function
To call a function, use the function name followed by parenthesis:
"""

# Example
def my_function():
  print("Hello from a function")

my_function()

# output - Hello from a function

"""
Arguments
Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
"""

# Example
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

"""
output
Emil Refsnes
Tobias Refsnes
Linus Refsnes
"""

"""
Arguments are often shortened to args in Python documentations.

Parameters or Arguments?

The terms parameter and argument can be used for the same thing: information that are passed into a function.
From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.

Number of Arguments
By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
"""

# Example
# This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

# output - Emil Refsnes

# If you try to call the function with 1 or 3 arguments, you will get an error:

# Example
This function expects 2 arguments, but gets only 1:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")

# output - SyntaxError: invalid syntax

"""
Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:
"""

# Example
# If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# output - The youngest child is Linus

"""
Arbitrary Arguments are often shortened to *args in Python documentations.

Keyword Arguments
You can also send arguments with the key = value syntax.
This way the order of the arguments does not matter.
"""

# Example
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
# output - The youngest child is Linus

"""
The phrase Keyword Arguments are often shortened to kwargs in Python documentations.

Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly:
"""

# Example
# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
# output - His last name is Refsnes

"""
Default Parameter Value
The following example shows how to use a default parameter value.
If we call the function without argument, it uses the default value:
"""

# Example
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

"""
output
I am from Sweden
I am from India
I am from Norway
I am from Brazil
"""

"""
Passing a List as an Argument
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
E.g. if you send a List as an argument, it will still be a List when it reaches the function:
"""

# Example
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

"""
output
apple
banana
cherry
"""

"""
Return Values
To let a function return a value, use the return statement:
"""

# Example
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

"""
output
15
25
45
"""

"""
The pass Statement
function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
"""

# Example
def myfunction():
  pass

# empty line

"""
Recursion

Python also accepts function recursion, which means a defined function can call itself.
Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).
To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
"""

# Example
# Recursion Example

def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k -1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)

"""
output
1
3
6
10
15
21
"""

def repeat(k):
    if (k > 0):
        result = k + repeat(k -1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
repeat(6)

"""
output
1
3
6
10
15
21
"""

"""
Test Yourself With Exercises
Exercise:
Create a function named my_function.
"""
def my_function():
  print("Hello from a function")

my_function()

# output - Hello from a function

#%%

# https://www.w3schools.com/python/python_lambda.asp

"""
Python Lambda
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

Syntax
lambda arguments : expression
The expression is executed and the result is returned:
"""

# Example
# Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(5))

# output - 15

# Lambda functions can take any number of arguments:
# Example
# Multiply argument a with argument b and return the result:

x = lambda a, b : a * b
print(x(5, 6))

# output - 30

# Example
# Summarize argument a, b, and c and return the result:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# output - 13

"""
Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.
Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
"""

def myfunc(n):
  return lambda a : a * n

# Use that function definition to make a function that always doubles the number you send in:
# Example

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# output - 22
# n = 11, a = 2

# Or, use the same function definition to make a function that always triples the number you send in:

# Example

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

# output - 22
# n = 11, a = 3

# Or, use the same function definition to make both functions, in the same program:

# Example
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

"""
output
22
33
"""

# Use lambda functions when an anonymous function is required for a short period of time.

# Test Yourself With Exercises
# Exercise:
# Create a lambda function that takes one parameter (a) and returns it.

x = lambda a : a
# output - there is no output

#%%

# https://www.w3schools.com/python/python_arrays.asp

"""
Python Arrays
Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

Arrays
Note: This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.
Arrays are used to store multiple values in one single variable:
"""

# Example
# Create an array containing car names:

cars = ["Ford", "Volvo", "BMW"]

print(cars)
# output - ['Ford', 'Volvo', 'BMW']

"""
What is an Array?
An array is a special variable, which can hold more than one value at a time.
If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:
"""

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

"""
However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?
The solution is an array!
An array can hold many values under a single name, and you can access the values by referring to an index number.

Access the Elements of an Array
You refer to an array element by referring to the index number.
"""

# Example
# Get the value of the first array item:

x = cars[0]
print(x)
# output - Ford

# Example
# Modify the value of the first array item:

cars[0] = "Toyota"
print(cars)
# output - ['Toyota', 'Volvo', 'BMW']

# The Length of an Array
# Use the len() method to return the length of an array (the number of elements in an array).

# Example
# Return the number of elements in the cars array:

x = len(cars)
print(x)
# output - 3

# Note: The length of an array is always one more than the highest array index.

# Looping Array Elements
# You can use the for in loop to loop through all the elements of an array.

# Example
# Print each item in the cars array:

for x in cars:
  print(x)

"""
output
Toyota
Volvo
BMW
"""

# Adding Array Elements
# You can use the append() method to add an element to an array.

# Example
# Add one more element to the cars array:

cars.append("Honda")
print(cars)
# output - ['Toyota', 'Volvo', 'BMW', 'Honda']

# Removing Array Elements
# You can use the pop() method to remove an element from the array.

# Example
# Delete the second element of the cars array:

cars.pop(1)
print(cars)
# output - ['Toyota', 'BMW', 'Honda']

# You can also use the remove() method to remove an element from the array.

# Example
# Delete the element that has the value "Volvo":

# cars.remove("Volvo")

cars.remove("BMW")
print(cars)
# output - ['Toyota', 'Honda']

# Note: The list's remove() method only removes the first occurrence of the specified value.

# Array Methods
# Python has a set of built-in methods that you can use on lists/arrays.

#%%

# https://www.w3schools.com/python/python_classes.asp

"""
Python Classes and Objects
Python Classes/Objects
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
"""
# Create a Class
# To create a class, use the keyword class:

# Example
# Create a class named MyClass, with a property named x:

class MyClass:
  x = 5

# Create Object
# Now we can use the class named MyClass to create objects:

# Example
# Create an object named p1, and print the value of x:

p1 = MyClass()
print(p1.x)
# output - 5

"""
The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
To understand the meaning of classes we have to understand the built-in __init__() function.
All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
"""

# Example
# Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

"""
output
John
36
"""

"""
Note: The __init__() function is called automatically every time the class is being used to create a new object.

Object Methods
Objects can also contain methods. Methods in objects are functions that belong to the object.
Let us create a method in the Person class:
"""

# Example
# Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36) # gives object p1 values
p1.myfunc()
# output - Hello my name is John

"""
Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
"""

# Example
# Use the words mysillyobject and abc instead of self:

class Person:
  def __init__(mysillyobject, name, age):
      mysillyobject.name = name
      mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36) # gives object p1 values
p1.myfunc()
# output - Hello my name is John

class Person:
  def __init__(myobject, name, age):
      myobject.name = name
      myobject.age = age

  def myfunc(xyz):
    print("Hello my name is " + xyz.name)

p1 = Person("John", 36) # gives object p1 values
p1.myfunc()
# output - Hello my name is John

print(p1)
# output - <__main__.Person object at 0x0000026E0FF3A280>.  You need to refer to an attribute in a object

# Modify Object Properties
# You can modify properties on objects like this:

# Example
# Set the age of p1 to 40:

print(p1.age)
# output - 36

p1.age = 40
print(p1.age)
# output - 40

# Delete Object Properties
# You can delete properties on objects by using the del keyword:

# Example
# Delete the age property from the p1 object:

del p1.age
print(p1.age)
# output - AttributeError: 'Person' object has no attribute 'age'

print(p1.name)
# output - John
# name attribute in the object p1 has not been deleted

# Delete Objects
# You can delete objects by using the del keyword:

# Example
# Delete the p1 object:

del p1
print(p1.age)
# output - NameError: name 'p1' is not defined
# p1 has already been deleted

# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

# Example
class Person:
  pass
# no output

# Test Yourself With Exercises

# Exercise:
# Create a class named MyClass:

class MyClass:
  x = 5
# no output

test = MyClass()
print(test.x)
# output - 5

#%%

# https://www.w3schools.com/python/python_inheritance.asp

"""
Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.

Create a Parent Class
Any class can be a parent class, so the syntax is the same as creating any other class:
"""
# Example
# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
  def __init__(self, fname, lname):
      self.firstname = fname
      self.lastname = lname

  def printname(self):
      print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# output - John Doe

class Person:
  def __init__(ABC, fname, lname):
      ABC.firstname = fname
      ABC.lastname = lname

  def printit(ABC):
      print(ABC.firstname, ABC.lastname)

# Use the Person class to create an object, and then execute the printit method:

x = Person("Howard", "Jiang")
x.printit()

# output - Howard Jiang

class People:
  def __init__(ABC, name1, name2):
      ABC.firstname = name1
      ABC.lastname = name2

  def printit(ABC):
      print(ABC.firstname, ABC.lastname)

# Use the People class to create an object, and then execute the printit method:

y = People("Howard", "Jiang")
y.printit()

# output - Howard Jiang

"""
Create a Child Class
To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
"""

# Example
# Create a class named Student, which will inherit the properties and methods from the Person class:

class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()


x = 10
    
class Print(Person):
  print(x)

# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
# Now the Student class has the same properties and methods as the Person class.

# Example
# Use the Student class to create an object, and then execute the printname method:


"""
Add the __init__() Function
So far we have created a child class that inherits the properties and methods from its parent.
We want to add the __init__() function to the child class (instead of the pass keyword).
Note: The __init__() function is called automatically every time the class is being used to create a new object.
"""

# Example
# Add the __init__() function to the Student class:

class Student(Person):
    def __init__(self, fname, lname):
#add properties etc.

class Student(Person):
    def __init__(self, fname, lname):
        #add properties etc.
        self.firstname = fname
        self.lastname = lname

def printname(self): # method within 
      print(self.firstname, self.lastname)

x = Student("John", "Doe")
x.printname()

# output - John Doe

"""
When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
"""

# Example
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("John", "Doe")
x.printname()

y = Person("Howard", "Jiang")
y.printname()

"""
output
John Doe
Howard Jiang
"""

# methods from parent class and child class can be used at the same time

"""
Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.

Use the super() Function
Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
"""

# Example
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)


# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

"""
Add Properties
Example
Add a property called graduationyear to the Student class:
"""

class Student(Person):
  def __init__(self, fname, lname):
      super().__init__(fname, lname)
      self.graduationyear = 2019

# In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the __init__() function:

# Example
# Add a year parameter, and pass the correct year when creating objects:

class Student(Person):
  def __init__(self, fname, lname, year):
      super().__init__(fname, lname)
      self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)

# output Mike Olsen

"""
Add Methods
Example
Add a method called welcome to the Student class:
"""
class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
      super().__init__(fname, lname)
      self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()

# output - Welcome Mike Olsen to the class of 2019

# If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.

"""
Test Yourself With Exercises
Exercise:
What is the correct syntax to create a class named Student that will inherit properties and methods from a class named Person?
"""
class Student(Person):

#%%

# https://www.w3schools.com/python/python_iterators.asp

"""
Python Iterators
An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

Iterator vs Iterable
Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
All these objects have a iter() method which is used to get an iterator:
"""

# Example
# Return an iterator from a tuple, and print each value:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
mynum = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

"""
output
apple
banana
cherry
"""

yourtuple = ("Howard", "Xue Hao", "Jiang")
yournum = iter(yourtuple)

print(next(yournum))
print(next(yournum))
print(next(yournum))

"""
output
Howard
Xue Hao
Jiang
"""


# Even strings are iterable objects, and can return an iterator:
# Example
# Strings are also iterable objects, containing a sequence of characters:

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

"""
output
b
a
n
a
n
a
"""

# if there is one more print(next(myit)), there will be an error

# Looping Through an Iterator
# We can also use a for loop to iterate through an iterable object:

# Example
# Iterate the values of a tuple:

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

"""
output
apple
banana
cherry
"""

# Example
# Iterate the characters of a string:

mystr = "banana"

for x in mystr:
  print(x)

"""
output
b
a
n
a
n
a
"""

# The for loop actually creates an iterator object and executes the next() method for each loop.

"""
Create an Iterator
To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
The __next__() method also allows you to do operations, and must return the next item in the sequence.
"""

# Example
# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

"""
output
1
2
3
4
5
"""
# if there are 2 more 
# print(next(myiter))
# print(next(myiter))
# output - 1 2 3 4 5 6 7

class MyNumbers:
    def __iter__(self):
        self.a = -1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

"""
output
-1
0
1
2
3
"""

"""
StopIteration
The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
To prevent the iteration to go on forever, we can use the StopIteration statement.
In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:
"""

# Example
# Stop after 20 iterations:

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

# output - 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# raise StopIteration will stop the further action

#%%

# https://www.w3schools.com/python/python_scope.asp

"""
Python Scope
A variable is only available from inside the region it is created. This is called scope.

Local Scope
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
"""

# Example
# A variable created inside a function is available inside that function:

def myfunc():
  x = 300
  print(x)

myfunc()

# output - 300

# Function Inside Function
# As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:

# Example
# The local variable can be accessed from a function within the function:

def myfunc():
  x = 300 # local variable x
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

# output - 300

"""
Global Scope
A variable created in the main body of the Python code is a global variable and belongs to the global scope.
Global variables are available from within any scope, global and local.
"""

# Example
# A variable created outside of a function is global and can be used by anyone:

x = 300

def myfunc():
  print(x) # print global variable x

myfunc() # call myfunc function

print(x) # print global variable x

"""
output
300
300
"""

# Naming Variables
# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):

# Example
# The function will print the local x, and then the code will print the global x:

x = 300 # global variable x

def myfunc():
  x = 200 # inside local variable x
  print(x) # print inside local variable x

myfunc() # call function myfunc

print(x) # print global variable x

"""
output
200
300
"""

"""
Global Keyword
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
The global keyword makes the variable global.
"""

# Example
# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x # define x as a global variable
  x = 300 # assign value 300 to global variable x

myfunc() # calls funtion, inside the function create global variable x = 300

print(x) # print variable x, which is created inside the function

# output - 300

# Also, use the global keyword if you want to make a change to a global variable inside a function.

# Example
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = 300

def myfunc():
  global x # make change to global variable x
  x = 200 # assign value 200 to global variale x

myfunc()

print(x)

# output - 200

#%%

# https://www.w3schools.com/python/python_modules.asp

"""
Python Modules
What is a Module?
Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application.

Create a Module
To create a module just save the code you want in a file with the file extension .py:
"""

# Example
# Save this code in a file named mymodule.py

def greeting(name):
  print("Hello, " + name)

# Use a Module
# Now we can use the module we just created, by using the import statement:

# Example
# Import the module named mymodule, and call the greeting function:

import mymodule # the module file must be in the same directory as this file

mymodule.greeting("Jonathan")

# output - Hello, Jonathan

# Note: When using a function from a module, use the syntax: module_name.function_name.

# Variables in Module
# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):

# Example
# Save this code in the file mymodule.py

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

# Example
# Import the module named mymodule, and access the person1 dictionary:

import mymodule

a = mymodule.person1["age"]
print(a)

# output - 36

"""
Naming a Module
You can name the module file whatever you like, but it must have the file extension .py

Re-naming a Module
You can create an alias when you import a module, by using the as keyword:
"""

# Example
# Create an alias for mymodule called mx:

import mymodule as mx

a = mx.person1["age"]
print(a)

# output - 36

# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.

# Example
# Import and use the platform module:

import platform

x = platform.system()
print(x)

# output - Windows
# If computer is Mac then the output will say Mac

# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

# Example
# List all the defined names belonging to the platform module:
import platform

x = dir(platform)
print(x)

# List all the defined names belonging to the mymodule module:
import mymodule

y = dir(mymodule)
print(y)

# output - all the defined names belonging to the platform module
# Note: The dir() function can be used on all modules, also the ones you create yourself.

# Import From Module
# You can choose to import only parts from a module, by using the from keyword.

# Example
# The module named mymodule has one function and one dictionary:

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

# Example
# Import only the person1 dictionary from the module:

from mymodule import person1

print (person1["age"])

# output - 36

# Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]

# Test Yourself With Exercises
# Exercise:
# What is the correct syntax to import a module named "mymodule"?

import mymodule

#%%

# https://www.w3schools.com/python/python_datetime.asp

"""
Python Datetime
Python Dates
A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
"""

# Example
# Import the datetime module and display the current date:

import datetime

x = datetime.datetime.now()
print(x)

# output - 2022-06-15 18:45:09.645022

"""
Date Output
When we execute the code from the example above the result will be:
2022-06-15 18:20:05.364450
The date contains year, month, day, hour, minute, second, and microsecond.
The datetime module has many methods to return information about the date object.
Here are a few examples, you will learn more about them later in this chapter:
"""

# Example
# Return the year and name of weekday:

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A")) # %A Weekday, full version

"""
output
2022
Wednesday
"""

"""
Creating Date Objects
To create a date, we can use the datetime() class (constructor) of the datetime module.
The datetime() class requires three parameters to create a date: year, month, day.
"""

# Example
# Create a date object:

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).

import datetime

x = datetime.datetime(2022, 6, 15, 18, 49, 30, 156)

print(x)

# output - 2022-06-15 18:49:30.000156

"""
The strftime() Method
The datetime object has a method for formatting date objects into readable strings.
The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
"""

# Example
# Display the name of the month:

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B")) # %B Month name, full version

# output - June

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%Y")) # %Y Year, full version

# A reference of all the legal format codes:

#%%

# https://www.w3schools.com/python/python_math.asp

"""
Python Math
Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.

Built-in Math Functions
The min() and max() functions can be used to find the lowest or highest value in an iterable:
"""

# Example

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

"""
output
5
25
"""

a = min(2, 4, 6, 8, 10)
b = max(2, 4, 6, 8, 10)

print(a)
print(b)

"""
output
2
10
"""

# The abs() function returns the absolute (positive) value of the specified number:
# Example

x = abs(-7.25)

print(x)

# output - 7.25

# The pow(x, y) function returns the value of x to the power of y (xy).
# Example
# Return the value of 4 to the power of 3 (same as 4 * 4 * 4):

x = pow(4, 3)

print(x)

# output - 64

"""
The Math Module
Python has also a built-in module called math, which extends the list of mathematical functions.
To use it, you must import the math module:
import math
When you have imported the math module, you can start using methods and constants of the module.
The math.sqrt() method for example, returns the square root of a number:
"""

# Example
import math

x = math.sqrt(64)

print(x)

# output - 8.0

# The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:

# Example

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

"""
output
2
1
"""

# The math.pi constant, returns the value of PI (3.14...):

# Example

import math

x = math.pi

print(x)

# output - 3.141592653589793

# Complete Math Module Reference
# In our Math Module Reference you will find a complete reference of all methods and constants that belongs to the Math module.

#%%

# https://www.w3schools.com/python/python_json.asp

"""
Python JSON
JSON is a syntax for storing and exchanging data.
JSON is text, written with JavaScript object notation.

JSON in Python
Python has a built-in package called json, which can be used to work with JSON data.
"""

# Example
# Import the json module:

import json

"""
Parse JSON - Convert from JSON to Python
If you have a JSON string, you can parse it by using the json.loads() method.
The result will be a Python dictionary.
"""

# Example
# Convert from JSON to Python:

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# output - 30

# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# Example
# Convert from Python to JSON:

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# output - {"name": "John", "age": 30, "city": "New York"}

"""
You can convert Python objects of the following types, into JSON strings:
dict
list
tuple
string
int
float
True
False
None
"""

# Example
# Convert Python objects into JSON strings, and print the values:

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

"""
output
{"name": "John", "age": 30}
["apple", "bananas"]
["apple", "bananas"]
"hello"
42
31.76
true
false
null
"""

"""
When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

Python - JSON
dict - Object
list - Array
tuple - Array
str - String
int - Number
float - Number
True - true
False - false
None - null
"""

# Example
# Convert a Python object containing all the legal data types:

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
	{"model": "BMW 230", "mpg": 27.5},
	{"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

"""
output
{"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}
"""

"""
Format the Result
The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
The json.dumps() method has parameters to make it easier to read the result:
"""

# Example
# Use the indent parameter to define the numbers of indents:

json.dumps(x, indent=4)

"""
output
'{\n    "name": "John",\n    "age": 30,\n    "married": true,\n    "divorced": false,\n    "children": [\n        "Ann",\n        "Billy"\n    ],\n    "pets": null,\n    "cars": [\n        {\n            "model": "BMW 230",\n            "mpg": 27.5\n        },\n        {\n            "model": "Ford Edge",\n            "mpg": 24.1\n        }\n    ]\n}'
"""

# You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:

# Example
# Use the separators parameter to change the default separator:

json.dumps(x, indent=4, separators=(". ", " = "))

"""
output
'{\n    "name" = "John". \n    "age" = 30. \n    "married" = true. \n    "divorced" = false. \n    "children" = [\n        "Ann". \n        "Billy"\n    ]. \n    "pets" = null. \n    "cars" = [\n        {\n            "model" = "BMW 230". \n            "mpg" = 27.5\n        }. \n        {\n            "model" = "Ford Edge". \n            "mpg" = 24.1\n        }\n    ]\n}'
"""
# Order the Result
# The json.dumps() method has parameters to order the keys in the result:

# Example
# Use the sort_keys parameter to specify if the result should be sorted or not:

json.dumps(x, indent=4, sort_keys=True)

"""
output
'{\n    "age": 30,\n    "cars": [\n        {\n            "model": "BMW 230",\n            "mpg": 27.5\n        },\n        {\n            "model": "Ford Edge",\n            "mpg": 24.1\n        }\n    ],\n    "children": [\n        "Ann",\n        "Billy"\n    ],\n    "divorced": false,\n    "married": true,\n    "name": "John",\n    "pets": null\n}'
"""

#%%

# https://www.w3schools.com/python/python_regex.asp

"""
Python RegEx
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.

RegEx Module
Python has a built-in package called re, which can be used to work with Regular Expressions.
Import the re module:
"""
import re

# RegEx in Python
# When you have imported the re module, you can start using regular expressions:

# Example
# Search the string to see if it starts with "The" and ends with "Spain":

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print(x)
# output - <re.Match object; span=(0, 17), match='The rain in Spain'>

"""
RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:

Metacharacters
Metacharacters are characters with a special meaning:

Special Sequences
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

Sets
A set is a set of characters inside a pair of square brackets [] with a special meaning:

# The findall() Function
# The findall() function returns a list containing all matches.
"""

# Example
# Print a list of all matches:

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# output - ['ai', 'ai']

# The list contains the matches in the order they are found.
# If no matches are found, an empty list is returned:

# Example
# Return an empty list if no match was found:

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

# output - []

"""
The search() Function
The search() function searches the string for a match, and returns a Match object if there is a match.
If there is more than one match, only the first occurrence of the match will be returned:
"""

# Example
# Search for the first white-space character in the string:

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
# output - The first white-space character is located in position: 3

print(x)
# output - <re.Match object; span=(3, 4), match=' '>

# If no matches are found, the value None is returned:

# Example
# Make a search that returns no match:

import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

# output - None

# The split() Function
# The split() function returns a list where the string has been split at each match:

# Example
# Split at each white-space character:

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# output - ['The', 'rain', 'in', 'Spain']

# You can control the number of occurrences by specifying the maxsplit parameter:

# Example
# Split the string only at the first occurrence:

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

# output - ['The', 'rain in Spain']

txt = "The rain in Spain"
x = re.split("\s", txt, 2)
print(x)

# output - ['The', 'rain', 'in Spain']

# The sub() Function
# The sub() function replaces the matches with the text of your choice:

# Example
# Replace every white-space character with the number 9:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# output - The9rain9in9Spain
# replaces all the white space with 9

# You can control the number of replacements by specifying the count parameter:
# Example
# Replace the first 2 occurrences:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

# output - The9rain9in Spain

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 1)
print(x)

# output - The9rain in Spain

# Match Object
# A Match Object is an object containing information about the search and the result.
# Note: If there is no match, the value None will be returned, instead of the Match Object.

# Example
# Do a search that will return a Match Object:

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) # this will print an object

# output - <re.Match object; span=(5, 7), match='ai'>

"""
The Match object has properties and methods used to retrieve information about the search, and the result:
.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""

# Example
# Print the position (start- and end-position) of the first match occurrence.
# The regular expression looks for any words that starts with an upper case "S":

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

# output - (12, 17)
# 12 th position in a string of 17 characters

# Example
# Print the string passed into the function:

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

# output - The rain in Spain

# Example
# Print the part of the string where there was a match.
# The regular expression looks for any words that starts with an upper case "S":

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

# output - Spain

# Note: If there is no match, the value None will be returned, instead of the Match Object.

#%%

# https://www.w3schools.com/python/python_pip.asp

"""
Python PIP
What is PIP?
PIP is a package manager for Python packages, or modules if you like.
Note: If you have Python version 3.4 or later, PIP is included by default.

What is a Package?
A package contains all the files you need for a module.
Modules are Python code libraries you can include in your project.

Check if PIP is Installed
Navigate your command line to the location of Python's script directory, and type the following:
Example
Check PIP version:

C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip --version

Install PIP
If you do not have PIP installed, you can download and install it from this page: https://pypi.org/project/pip/

Download a Package
Downloading a package is very easy.
Open the command line interface and tell PIP to download the package you want.
Navigate your command line to the location of Python's script directory, and type the following:
Example
Download a package named "camelcase":

C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip install camelcase

Now you have downloaded and installed your first package!

Using a Package
Once the package is installed, it is ready to use.
Import the "camelcase" package into your project.
"""

# Example
# Import and use "camelcase":

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))

# Find Packages
# Find more packages at https://pypi.org/.

# Remove a Package
# Use the uninstall command to remove a package:

# Example
# Uninstall the package named "camelcase":

# C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip uninstall camelcase

"""
The PIP Package Manager will ask you to confirm that you want to remove the camelcase package:
Uninstalling camelcase-02.1:
  Would remove:
	c:\users\Your Name\appdata\local\programs\python\python36-32\lib\site-packages\camecase-0.2-py3.6.egg-info
	c:\users\Your Name\appdata\local\programs\python\python36-32\lib\site-packages\camecase\*
Proceed (y/n)?
Press y and the package will be removed.
"""
# List Packages
# Use the list command to list all the packages installed on your system:

# Example
# List installed packages:

"""
C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip list

Result:
Package     	Version
-----------------------
camelcase   	0.2
mysql-connector 2.1.6
pip         	18.1
pymongo     	3.6.1
setuptools  	39.0.1
"""

#%%

# https://www.w3schools.com/python/python_try_except.asp

"""
Python Try Except
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.

Exception Handling
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
These exceptions can be handled using the try statement:
"""

# Example
# The try block will generate an exception, because x is not defined:

try:
    print(x)
except:
    print("An exception occurred")

# output - <re.Match object; span=(12, 17), match='Spain'>
# x is defined earlier

try:
    print(z)
except:
    print("An exception occurred")

# output - An exception occurred
# z is not defined

# Since the try block raises an error, the except block will be executed.
# Without the try block, the program will crash and raise an error:

# Example
# This statement will raise an error, because x is not defined:

print(x)

# output - <re.Match object; span=(12, 17), match='Spain'>
# x is defined earlier

# Many Exceptions
# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

# Example
# Print one message if the try block raises a NameError and another for other errors:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# output - <re.Match object; span=(12, 17), match='Spain'>
# x is defined earlier

try:
  print(r)
except NameError:
  print("Variable r is not defined")
except:
  print("Something else went wrong")

# output - Variable r is not defined

# Else
# You can use the else keyword to define a block of code to be executed if no errors were raised:

# Example
# In this example, the try block does not generate any error:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

"""
output
Hello
Nothing went wrong
"""

# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.

# Example

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

"""
output
<re.Match object; span=(12, 17), match='Spain'>
The 'try except' is finished
"""

try:
  print(r)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

"""
output
Something went wrong
The 'try except' is finished
"""

# This can be useful to close objects and clean up resources:

# Example
# Try to open and write to a file that is not writable:

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

# output - Something went wrong when opening the file
# Because demofile.txt file does not exist

# I created a file called demofile.txt

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

# output - Something went wrong when writing to the file

# The program can continue, without leaving the file object open.

# Raise an exception
# As a Python developer you can choose to throw an exception if a condition occurs.
# To throw (or raise) an exception, use the raise keyword.

# Example
# Raise an error and stop the program if x is lower than 0:

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

# output - Exception: Sorry, no numbers below zero

# The raise keyword is used to raise an exception.
# You can define what kind of error to raise, and the text to print to the user.

# Example
# Raise a TypeError if x is not an integer:

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

# output - TypeError: Only integers are allowed

x = 6

if not type(x) is int:
  raise TypeError("Only integers are allowed")

# output - there is no output because there is no error

try:
    print(x)
except:
    print("An exception occured")

try:
    x = 10
    print(x)
except:
    if x > 10:
        print("x is greater than 10")

# output - 10
# only prints the try part, except condition is not met so didn't print that part

try:
    x = 10
    print("Try part ")
except:
    if x > 10:
        print("x is greater than 10")
else:
    if x < 10:
        print("x is less than 10")
finally:
    if x == 10:
            print("Finally Part ")
"""
output
Try part
Finally part
"""

try:
    x = 10
    print("Try part " + x)
except:
    if x > 10:
        print("x is greater than 10")
else:
    if x < 10:
        print("x is less than 10")
finally:
    if x == 10:
            print("Finally Part " + x)

# cannot concatenate str (not "int") to str

"""
output
Traceback (most recent call last):

  File "<ipython-input-10-fb96d3d06738>", line 12, in <module>
    print("Finally Part " + x)

TypeError: can only concatenate str (not "int") to str
"""
try:
    x = 10
    print("Try part " + x)
except:
    if x > 10:
        print("x is greater than 10")
else:
    if x < 10:
        print("x is less than 10")

# output - empty
# cannot concatenate str (not "int") to str

#%%

# https://www.w3schools.com/python/python_user_input.asp

"""
Python User Input

User Input
Python allows for user input.
That means we are able to ask the user for input.
The method is a bit different in Python 3.6 than Python 2.7.
Python 3.6 uses the input() method.
Python 2.7 uses the raw_input() method.
The following example asks for the username, and when you entered the username, it gets printed on the screen:
"""

# Python 3.6
username = input("Enter username:")
print("Username is: " + username)

"""
output
Enter username:jiangh77
Username is: jiangh77
"""
# Python 3.6 uses the input() method.

# Python 2.7
username = raw_input("Enter username:")
print("Username is: " + username)

# output - NameError: name 'raw_input' is not defined

# Python stops executing when it comes to the input() function, and continues when the user has given some input.

#%%

# https://www.w3schools.com/python/python_string_formatting.asp

"""
Python String Formatting
To make sure a string will display as expected, we can format the result with the format() method.

String format()
The format() method allows you to format selected parts of a string.
Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?
To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:
"""

# Example
# Add a placeholder where you want to display the price:

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

# output - The price is 49 dollars
# format int into string

# You can add parameters inside the curly brackets to specify how to convert the value:
# Example
# Format the price to be displayed as a number with two decimals:

txt = "The price is {:.2f} dollars"
print(txt.format(price))

# output - The price is 49.00 dollars

# Check out all formatting types in our String format() Reference.

# Multiple Values
# If you want to use more values, just add more values to the format() method:

print(txt.format(price, itemno, count))

# And add more placeholders:
# Example

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# output - I want 3 pieces of item number 567 for 49.00 dollars.

# Index Numbers
# You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
# Example

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# output - I want 3 pieces of item number 567 for 49.00 dollars.

# Also, if you want to refer to the same value more than once, use the index number:
# Example

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# output - His name is John. John is 36 years old.

age = 44
name = 'Howard Jiang'
txt = "My name is {1}.  {1} is {0} years old."
print(txt.format(name, age))

# output - My name is 44.  44 is Howard Jiang years old.
# value must be coded in order

age = 44
name = 'Howard Jiang'
txt = "My name is {1}.  {1} is {0} years old."
print(txt.format(age, name))

# output - My name is Howard Jiang.  Howard Jiang is 44 years old.
# value must be coded in order
# Named Indexes
# You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):

# Example

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

# output - I have a Ford, it is a Mustang.

myplace = "I want to buy a {place}, it must be easy for {travel}"
print(myplace.format(place = 'condo', travel = 'commute'))

# output - I want to buy a condo, it must be easy for commute

# The end