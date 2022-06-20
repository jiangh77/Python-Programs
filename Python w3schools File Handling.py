# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 07:13:28 2022

@author: jiang
"""

# Python w3schools File Handling

# https://www.w3schools.com/python/python_file_handling.asp

"""
Python File Open
File handling is an important part of any web application.
Python has several functions for creating, reading, updating, and deleting files.

File Handling
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"""

# Syntax
# To open a file for reading it is enough to specify the name of the file:

f = open("demofile.txt")
f.close()

# open then close a file

# The code above is the same as:

f = open("demofile.txt", "rt")
f.close()

# Because "r" for read, and "t" for text are the default values, you do not need to specify them.
# Note: Make sure the file exists, or else you will get an error.

#%%

# https://www.w3schools.com/python/python_file_open.asp

"""
Python File Open

Open a File on the Server
Assume we have the following file, located in the same folder as Python:
demofile.txt
Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!
To open the file, use the built-in open() function.
The open() function returns a file object, which has a read() method for reading the content of the file:
"""

# Example

f = open("demofile.txt", "r")
print(f.read())

"""
output
Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!
"""

# If the file is located in a different location, you will have to specify the file path, like this:
# Example
# Open a file on a different location:

f = open("D:\\myfiles\welcome.txt", "r") # 
print(f.read())

f = open("C:\Programs\Python Code\w3schools.com\demofile.txt", "r")
print(f.read())

f = open("C:\\Programs\Python Code\w3schools.com\demofile.txt", "r")
print(f.read())

"""
output
Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!
"""

# Single and Double Back Slash both work for file path "C:\Programs\Python Code\w3schools.com\demofile.txt" and "C:\\Programs\Python Code\w3schools.com\demofile.txt"

# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:

# Example
# Return the 5 first characters of the file:

f = open("demofile.txt", "r")
print(f.read(5))

# output - Hello

# Read Lines
# You can return one line by using the readline() method:

# Example
# Read one line of the file:

f = open("demofile.txt", "r")
print(f.readline())

# output - Hello! Welcome to demofile.txt

# By calling readline() two times, you can read the two first lines:

# Example
# Read two lines of the file:

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

"""
output
Hello! Welcome to demofile.txt

This file is for testing purposes.
"""

# By looping through the lines of the file, you can read the whole file, line by line:

# Example
# Loop through the file line by line:

f = open("demofile.txt", "r")
for x in f:
  print(x)

"""
output
Hello! Welcome to demofile.txt

This file is for testing purposes.

Good Luck!
"""

# Close Files
# It is a good practice to always close the file when you are done with it.

# Example
# Close the file when you are finish with it:

f = open("demofile.txt", "r")
print(f.readline())
f.close()

# output - Hello! Welcome to demofile.txt
# The file is closed
# Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.

#%%

# https://www.w3schools.com/python/python_file_write.asp

"""
Python File Write
Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:
"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
"""

# Example
# Open the file "demofile2.txt" and append content to the file:

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

# when demofile2.txt does not exist, the python code creates one
# open and read the file after the appending:

f = open("demofile2.txt", "r")
print(f.read())

# output - Now the file has more content!

f = open("demofile2.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

f = open("demofile2.txt", "r")
print(f.read())    

# output - Woops! I have deleted the content!

f = open("demofile2.txt", "w")
f.write("Now the file has more content!")
f.close()

f = open("demofile2.txt", "r")
print(f.read())

# output - Now the file has more content!

# Example
# Open the file "demofile3.txt" and overwrite the content:

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after the appending:

f = open("demofile3.txt", "r")
print(f.read())

# output - Woops! I have deleted the content!

# Note: the "w" method will overwrite the entire file.

"""
Create a New File
To create a new file in Python, use the open() method, with one of the following parameters:
"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist
"""

# Example
# Create a file called "myfile.txt":

f = open("myfile.txt", "x")

# Result: a new empty file is created!

# Example
# Create a new file if it does not exist:

f = open("myfile.txt", "w")

f.close()

# Must close a file
# below is an experiment

f = open("myfile.txt", "w")
f.write("Writing the first line")

f = open("myfile.txt", "r")
print(f.read())

# output - Writing the first line

f = open("myfile.txt", "a")
f.write("Writing the second line")

f = open("myfile.txt", "r")
print(f.read())

"""
output
Writing the first lineWriting the second line
"""
# If you want a space in between you must write it

# Example 1

f = open("testfile.txt", "w")
f.write("Writing the first line\n")

f = open("testfile.txt", "r")
print(f.read())

# output - Writing the first line

f = open("testfile.txt", "a")
f.write("\nWriting the second line")

f = open("testfile.txt", "r")
print(f.read())

"""
output
Writing the first line

Writing the second line
"""
# the first \n makes an extra carriage return at the end of the first line
# the second \n makes an extra carriage return before the second line starts

# Example 2

f = open("Example File.txt", "x")

# Below is experiment

f = open("Example File.txt", "w")
f.write("My Story\n")

# \n will create an extra carriage return

f = open("Example File.txt", "r")
print(f.read())

# output - My Story

g = open("Example File.txt", "a")
g.write("Starts like this.")

g = open("Example File.txt", "r")
print(g.read())

"""
output
My Story
Starts like this.
"""

g.close()

# You can not delete a file unless it is closed

# \n will create an extra carriage return
# https://stackoverflow.com/questions/4025760/python-file-write-creating-extra-carriage-return

# https://stackoverflow.com/questions/2918362/writing-string-to-a-file-on-a-new-line-every-time

"""
Writing string to a file on a new line every time
I want to append a newline to my string every time I call file.write(). What's the easiest way to do this in Python?

Answers
Use "\n":
file.write("My String\n")
"""

#%%

# https://www.w3schools.com/python/python_file_remove.asp

# Python Delete File
# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:

# Example
# Remove the file "demofile.txt":

import os
os.remove("demofile.txt")

# demofile.txt is deleted

# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:

# Example
# Check if file exists, then delete it:

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

# output - The file does not exist

# Delete Folder
# To delete an entire folder, use the os.rmdir() method:

# Example
# Remove the folder "myfolder":

import os
os.rmdir("myfolder")

# output - FileNotFoundError: [WinError 2] The system cannot find the file specified: 'myfolder'

# I created the folder "myfolder" and put a file in it

import os
os.rmdir("myfolder")

# output - OSError: [WinError 145] The directory is not empty: 'myfolder'

import os
file = 'testfile.txt'
location = "C:\Programs\Python Code\w3schools.com\myfolder"
path = os.path.join(location, file)
os.remove(path)

# this removes the file
"""
https://www.geeksforgeeks.org/python-os-remove-method/

Python | os.remove() method

OS module in Python provides functions for interacting with the operating system. OS comes under Python’s standard utility modules. This module provides a portable way of using operating system dependent functionality.

All functions in os module raise OSError in the case of invalid or inaccessible file names and paths, or other arguments that have the correct type, but are not accepted by the operating system.

os.remove() method in Python is used to remove or delete a file path. This method can not remove or delete a directory. If the specified path is a directory then OSError will be raised by the method. os.rmdir() can be used to remove directory.

Syntax: os.remove(path, *, dir_fd = None)

Parameter:
path: A path-like object representing a file path. A path-like object is either a string or bytes object representing a path.
dir_fd (optional) : A file descriptor referring to a directory. The default value of this parameter is None.
If the specified path is absolute then dir_fd is ignored.

Note: The ‘*’ in parameter list indicates that all following parameters (Here in our case ‘dir_fd’) are keyword-only parameters and they can be provided using their name, not as positional parameter.

Return Type: This method does not return any value.

Code #1: Use of os.remove() method to remove a file
# Python program to explain os.remove() method 
    
# importing os module 
import os
  
# File name
file = 'file.txt'
  
# File location
location = "/home/User/Documents"
  
# Path
path = os.path.join(location, file)
  
# Remove the file
# 'file.txt'
os.remove(path)
print("%s has been removed successfully" %file)

Output:
file.txt has been removed successfully

Code #2: If the specified path is a directory
# Python program to explain os.remove() method 
    
# importing os module 
import os
  
# Path
path = "/home/User/Documents/ihritik"
  
# Remove the specified
# file path
os.remove(path)
print("% s has been removed successfully" % file)
  
# if the specified path 
# is a directory then 
# 'IsADirectoryError' error
# will raised 
  
# Similarly if the specified
# file path does not exists or  
# is invalid then corresponding
# OSError will be raised

Output:
Traceback (most recent call last):
  File "osremove.py", line 11, in 
    os.remove(path)
IsADirectoryError: [Errno 21] Is a directory: '/home/User/Documents/ihritik'

Code #3: Handling error while using os.remove() method

# Python program to explain os.remove() method 
    
# importing os module 
import os
  
# path
path = '/home/User/Documents/ihritik'
  
# Remove the specified 
# file path
try:
    os.remove(path)
    print("% s removed successfully" % path)
except OSError as error:
    print(error)
    print("File path can not be removed")

Output:
[Errno 21] Is a directory: '/home/User/Documents/ihritik'
File path can not be removed
Reference: https://docs.python.org/3/library/os.html

"""

os.rmdir("myfolder")

# myfolder folder is removed

# Note: You can only remove empty folders.

# The end