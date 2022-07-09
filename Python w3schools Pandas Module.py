# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 21:39:33 2022

@author: jiang
"""

# Python w3schools Pandas Module

# https://www.w3schools.com/python/pandas/default.asp

"""
Pandas Tutorial

Pandas is a Python library.
Pandas is used to analyze data.

Learning by Reading
We have created 14 tutorial pages for you to learn more about Pandas.
Starting with a basic introduction and ends up with cleaning and plotting data:

Basic

1. Introduction
 
2. Getting Started
 
3. Pandas Series
 
4. DataFrames
 
5. Read CSV
 
6. Read JSON
 
7. Analyze Data


Cleaning Data

1. Clean Data
 
2. Clean Empty Cells
 
3. Clean Wrong Format
 
4. Clean Wrong Data
 
5. Remove Duplicates


Advanced

1. Correlations
 
2. Plotting
"""

# Learning by Quiz Test
# Test your Pandas skills with a quiz test.
# Learning by Exercises
# Pandas Exercises

# Exercise:
# Insert the correct Pandas method to create a Series.

pd.series(mylist)

# Learning by Examples
# In our "Try it Yourself" editor, you can use the Pandas module, and modify the code to see the result.

# Example
# Load a CSV file into a Pandas DataFrame:

import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string())

#%%

# https://www.w3schools.com/python/pandas/pandas_intro.asp

"""
Pandas Introduction

What is Pandas?

Pandas is a Python library used for working with data sets.
It has functions for analyzing, cleaning, exploring, and manipulating data.
The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.

Why Use Pandas?

Pandas allows us to analyze big data and make conclusions based on statistical theories.
Pandas can clean messy data sets, and make them readable and relevant.
Relevant data is very important in data science.
Data Science: is a branch of computer science where we study how to store, use and analyze data for deriving information from it.

What Can Pandas Do?
Pandas gives you answers about the data. Like:
Is there a correlation between two or more columns?
What is average value?
Max value?
Min value?
Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values. This is called cleaning the data.

Where is the Pandas Codebase?

The source code for Pandas is located at this github repository https://github.com/pandas-dev/pandas

github: enables many people to work on the same codebase.
"""

#%%

# https://www.w3schools.com/python/pandas/pandas_getting_started.asp

"""
Pandas Getting Started
Installation of Pandas
If you have Python and PIP already installed on a system, then installation of Pandas is very easy.
Install it using this command:
"""
C:\Users\Your Name>pip install pandas

# If this command fails, then use a python distribution that already has Pandas installed like, Anaconda, Spyder etc.

# Import Pandas

# Once Pandas is installed, import it in your applications by adding the import keyword:

import pandas

# Now Pandas is imported and ready to use.

# Example

import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)

"""
output
    cars  passings
0    BMW         3
1  Volvo         7
2   Ford         2
"""

"""
Pandas as pd
Pandas is usually imported under the pd alias.
alias: In Python alias are an alternate name for referring to the same thing.
Create an alias with the as keyword while importing:
"""

import pandas as pd

# Now the Pandas package can be referred to as pd instead of pandas.

# Example
import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

"""
output
    cars  passings
0    BMW         3
1  Volvo         7
2   Ford         2
"""

import pandas as pd

TestDataset = {
    'Subject': ['Math', 'English', 'Science'],
    'Grade': [100, 80, 95]
}

myscore = pd.DataFrame(TestDataset)

print(myscore)

"""
output
   Subject  Grade
0     Math    100
1  English     80
2  Science     95
"""

import pandas as pd

Class = {
    "Programs": ["SQL", "Python", "R"],
    "Grade": ["A+", "A+", "A"]
    }

MyPrograms = pd.DataFrame(Class)

print(MyPrograms)

"""
output
  Programs Grade
0      SQL    A+
1   Python    A+
2        R     A
"""

# Checking Pandas Version
# The version string is stored under __version__ attribute.

# Example

import pandas as pd

print(pd.__version__)

# output - 1.0.5

#%%

# https://www.w3schools.com/python/pandas/pandas_series.asp

"""
Pandas Series
What is a Series?
A Pandas Series is like a column in a table.
It is a one-dimensional array holding data of any type.
"""

# Example
# Create a simple Pandas Series from a list:

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

"""
output
0    1
1    7
2    2
dtype: int64
"""

"""
Labels
If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
This label can be used to access a specified value.
"""

# Example
# Return the first value of the Series:

print(myvar[0])

# output - 1

print(myvar[-1])

# output - KeyError: -1
# cannot use negative index counting from the end

print(myvar[2])

# output - 2

# Create Labels
# With the index argument, you can name your own labels.

# Example
# Create you own labels:

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

"""
output
x    1
y    7
z    2
dtype: int64
"""

# When you have created labels, you can access an item by referring to the label.
# Example

# Return the value of "y":

print(myvar["y"])

# output - 7

import pandas as pd

b = (1, 3, 6)

TestVar = pd.Series(b, index = ['a', 'b', 'c'])

print(TestVar)

"""
output
a    1
b    3
c    6
dtype: int64
"""
# round brackets () can be used, single quotes '' can be used
# as a standard, use double quotes ""

# Key/Value Objects as Series
# You can also use a key/value object, like a dictionary, when creating a Series.

# Example
# Create a simple Pandas Series from a dictionary:

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

"""
output
day1    420
day2    380
day3    390
dtype: int64
"""
# "day1", "day2" and "day3" are labels or keys
# 420, 380 and 390 are values

"""
Note: The keys of the dictionary become the labels.
To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.
"""

# Example
# Create a Series using only data from "day1" and "day2":

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)

"""
output
day1    420
day2    380
dtype: int64
"""

import pandas as pd

subject_grade = {"Math": 100, "English": 80, "Science": 90}

grades = pd.Series(subject_grade, index = ("Math", "Science"))

print(grades)

"""
output
Math       100
Science     90
dtype: int64
"""
# round brackets () can be used

"""
DataFrames
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
Series is like a column, a DataFrame is the whole table.
"""

# Example
# Create a DataFrame from two Series:

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)

"""
output
   calories  duration
0       420        50
1       380        40
2       390        45
"""

import pandas as pd

programs = {
    "language": ("SQL", "Python", "R"),
    "grades": (100, 100, 95)
    }

program_score = pd.DataFrame(programs)

print(program_score)

"""
output
  language  grades
0      SQL     100
1   Python     100
2        R      95
"""

"""
Test Yourself With Exercises
Exercise:
Insert the correct Pandas method to create a Series.
"""
pd.Series(mylist)

#%%

# https://www.w3schools.com/python/pandas/pandas_dataframes.asp

"""
Pandas DataFrames
What is a DataFrame?
A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
"""
# Example
# Create a simple Pandas DataFrame:

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)

"""
Result
    calories  duration
  0       420        50
  1       380        40
  2       390        45
"""

import pandas as pd

mydata = {
    "programs": ['SQL', 'Python', 'R'], # can use either round brackets () or square brackets []
    "score": [100, 100, 100]
    }

dt = pd.DataFrame(mydata)

print(dt)

"""
output
  programs  score
0      SQL    100
1   Python    100
2        R    100
"""

"""
Locate Row
As you can see from the result above, the DataFrame is like a table with rows and columns.
Pandas use the loc attribute to return one or more specified row(s)
"""

# Example
# Return row 0:
# refer to the row index:

print(df.loc[0])

"""
output
calories    420
duration     50
Name: 0, dtype: int64
"""
# this is only one row of data, it is not a table or a DataFrame

print(dt.loc(1))

# output - <pandas.core.indexing._LocIndexer object at 0x000001DC6CE35A40>
# when refer to an index, must be in square brackets

print(dt.loc[1])

"""
output
programs    Python
score          100
Name: 1, dtype: object
"""

# Note: This example returns a Pandas Series.
# this is only one row of data, it is not a table or a DataFrame

# Example
# Return row 0 and 1:
# use a list of indexes:

print(df.loc[[0, 1]])

"""
output
   calories  duration
0       420        50
1       380        40
"""

# Note: When using [], the result is a Pandas DataFrame.

# Named Indexes
# With the index argument, you can name your own indexes.

# Example
# Add a list of names to give each row a name:

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 

"""
output
day1       420        50
day2       380        40
day3       390        45
"""
# index is changed from 0, 1, 2 to "day1", "day2", "day3"

# Locate Named Indexes
# Use the named index in the loc attribute to return the specified row(s).

# Example
# Return "day2":
# refer to the named index:
print(df.loc["day2"])

"""
output
calories    380
duration     40
Name: day2, dtype: int64
"""

# Load Files Into a DataFrame
# If your data sets are stored in a file, Pandas can load them into a DataFrame.

# Example
# Load a comma separated file (CSV file) into a DataFrame:

import pandas as pd

df = pd.read_csv('data.csv')

print(df)

# You will learn more about importing files in the next chapters.

"""
Test Yourself With Exercises
Exercise:
Insert the correct Pandas method to create a DataFrame.
"""

pd.DataFrame(data)

#%%

# https://www.w3schools.com/python/pandas/pandas_csv.asp

"""
Pandas Read CSV
Read CSV Files
A simple way to store big data sets is to use CSV files (comma separated files).
CSV files contains plain text and is a well know format that can be read by everyone including Pandas.
In our examples we will be using a CSV file called 'data.csv'.
Download data.csv. or Open data.csv
"""

# Example
# Load the CSV into a DataFrame:

import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string())

"""
output
     Duration  Pulse  Maxpulse  Calories
0          60    110       130     409.1
1          60    117       145     479.0
2          60    103       135     340.0
3          45    109       175     282.4
4          45    117       148     406.0
5          60    102       127     300.0
6          60    110       136     374.0
7          45    104       134     253.3
8          30    109       133     195.1
9          60     98       124     269.0
10         60    103       147     329.3
11         60    100       120     250.7
12         60    106       128     345.3
13         60    104       132     379.3
14         60     98       123     275.0
15         60     98       120     215.2
16         60    100       120     300.0
17         45     90       112       NaN
18         60    103       123     323.0
19         45     97       125     243.0
20         60    108       131     364.2
21         45    100       119     282.0
22         60    130       101     300.0
23         45    105       132     246.0
24         60    102       126     334.5
25         60    100       120     250.0
26         60     92       118     241.0
27         60    103       132       NaN
28         60    100       132     280.0
29         60    102       129     380.3
30         60     92       115     243.0
31         45     90       112     180.1
32         60    101       124     299.0
33         60     93       113     223.0
34         60    107       136     361.0
35         60    114       140     415.0
36         60    102       127     300.0
37         60    100       120     300.0
38         60    100       120     300.0
39         45    104       129     266.0
40         45     90       112     180.1
41         60     98       126     286.0
42         60    100       122     329.4
43         60    111       138     400.0
44         60    111       131     397.0
45         60     99       119     273.0
46         60    109       153     387.6
47         45    111       136     300.0
48         45    108       129     298.0
49         60    111       139     397.6
50         60    107       136     380.2
51         80    123       146     643.1
52         60    106       130     263.0
53         60    118       151     486.0
54         30    136       175     238.0
55         60    121       146     450.7
56         60    118       121     413.0
57         45    115       144     305.0
58         20    153       172     226.4
59         45    123       152     321.0
60        210    108       160    1376.0
61        160    110       137    1034.4
62        160    109       135     853.0
63         45    118       141     341.0
64         20    110       130     131.4
65        180     90       130     800.4
66        150    105       135     873.4
67        150    107       130     816.0
68         20    106       136     110.4
69        300    108       143    1500.2
70        150     97       129    1115.0
71         60    109       153     387.6
72         90    100       127     700.0
73        150     97       127     953.2
74         45    114       146     304.0
75         90     98       125     563.2
76         45    105       134     251.0
77         45    110       141     300.0
78        120    100       130     500.4
79        270    100       131    1729.0
80         30    159       182     319.2
81         45    149       169     344.0
82         30    103       139     151.1
83        120    100       130     500.0
84         45    100       120     225.3
85         30    151       170     300.0
86         45    102       136     234.0
87        120    100       157    1000.1
88         45    129       103     242.0
89         20     83       107      50.3
90        180    101       127     600.1
91         45    107       137       NaN
92         30     90       107     105.3
93         15     80       100      50.5
94         20    150       171     127.4
95         20    151       168     229.4
96         30     95       128     128.2
97         25    152       168     244.2
98         30    109       131     188.2
99         90     93       124     604.1
100        20     95       112      77.7
101        90     90       110     500.0
102        90     90       100     500.0
103        90     90       100     500.4
104        30     92       108      92.7
105        30     93       128     124.0
106       180     90       120     800.3
107        30     90       120      86.2
108        90     90       120     500.3
109       210    137       184    1860.4
110        60    102       124     325.2
111        45    107       124     275.0
112        15    124       139     124.2
113        45    100       120     225.3
114        60    108       131     367.6
115        60    108       151     351.7
116        60    116       141     443.0
117        60     97       122     277.4
118        60    105       125       NaN
119        60    103       124     332.7
120        30    112       137     193.9
121        45    100       120     100.7
122        60    119       169     336.7
123        60    107       127     344.9
124        60    111       151     368.5
125        60     98       122     271.0
126        60     97       124     275.3
127        60    109       127     382.0
128        90     99       125     466.4
129        60    114       151     384.0
130        60    104       134     342.5
131        60    107       138     357.5
132        60    103       133     335.0
133        60    106       132     327.5
134        60    103       136     339.0
135        20    136       156     189.0
136        45    117       143     317.7
137        45    115       137     318.0
138        45    113       138     308.0
139        20    141       162     222.4
140        60    108       135     390.0
141        60     97       127       NaN
142        45    100       120     250.4
143        45    122       149     335.4
144        60    136       170     470.2
145        45    106       126     270.8
146        60    107       136     400.0
147        60    112       146     361.9
148        30    103       127     185.0
149        60    110       150     409.4
150        60    106       134     343.0
151        60    109       129     353.2
152        60    109       138     374.0
153        30    150       167     275.8
154        60    105       128     328.0
155        60    111       151     368.5
156        60     97       131     270.4
157        60    100       120     270.4
158        60    114       150     382.8
159        30     80       120     240.9
160        30     85       120     250.4
161        45     90       130     260.4
162        45     95       130     270.0
163        45    100       140     280.9
164        60    105       140     290.8
165        60    110       145     300.0
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4
"""

# Tip: use to_string() to print the entire DataFrame.

# If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:

# Example
# Print the DataFrame without the to_string() method:

import pandas as pd

df = pd.read_csv('data.csv')

print(df)

"""
output
     Duration  Pulse  Maxpulse  Calories
0          60    110       130     409.1
1          60    117       145     479.0
2          60    103       135     340.0
3          45    109       175     282.4
4          45    117       148     406.0
..        ...    ...       ...       ...
164        60    105       140     290.8
165        60    110       145     300.0
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4

[169 rows x 4 columns]
"""
# max_rows

# The number of rows returned is defined in Pandas option settings.
# You can check your system's maximum rows with the pd.options.display.max_rows statement.

# Example
# Check the number of maximum returned rows:

import pandas as pd

print(pd.options.display.max_rows)

# output - 60

# In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.
# You can change the maximum rows number with the same statement.

# Example
# Increase the maximum number of rows to display the entire DataFrame:

import pandas as pd

pd.options.display.max_rows = 9999

df = pd.read_csv('data.csv')

print(df)

# prints all the data

import pandas as pd

pd.options.display.max_rows = 168

df = pd.read_csv('data.csv')

print(df)

"""
output
     Duration  Pulse  Maxpulse  Calories
0          60    110       130     409.1
1          60    117       145     479.0
2          60    103       135     340.0
3          45    109       175     282.4
4          45    117       148     406.0
..        ...    ...       ...       ...
164        60    105       140     290.8
165        60    110       145     300.0
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4

[169 rows x 4 columns]

"""

# change max rows to 169, original output is from rows 0 to 168
# if change the max row number above 168, it will display all the data

import pandas as pd

pd.options.display.max_rows = 169

df = pd.read_csv('data.csv')

print(df)

# prints out all the data

#%%

# https://www.w3schools.com/python/pandas/pandas_json.asp

"""
Pandas Read JSON
Read JSON
Big data sets are often stored, or extracted as JSON.
JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.
In our examples we will be using a JSON file called 'data.json'.
Open data.json.
"""

# Example
# Load the JSON file into a DataFrame:

import pandas as pd

df = pd.read_json('data.json')

print(df.to_string())

# prints the whole file

pd.options.display.max_rows = 100

import pandas as pd

dt = pd.read_json('data.json')

print(dt)

# prints the first 5 rows and last 5 rows
# Because .to_string() function is not used and max row is automatically set at 60

# Tip: use to_string() to print the entire DataFrame.

"""
Dictionary as JSON
JSON = Python Dictionary
JSON objects have the same format as Python dictionaries.
If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly:
"""

# Example
# Load a Python Dictionary into a DataFrame:

import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df)

"""
output
   Duration  Pulse  Maxpulse  Calories
0        60    110       130       409
1        60    117       145       479
2        60    103       135       340
3        45    109       175       282
4        45    117       148       406
5        60    102       127       300
"""

import pandas as pd

TestData = {
    "Programs": {
        "A": "SQL",
        "B": "Python",
        "C": "R",
        },
    "Scores": {
        "A": 100,
        "B": 100,
        "C": 98
        },
    "Grade": {
        "A": "A+",
        "B": "A+",
        "C": "A"
        }
    }

dt = pd.DataFrame(TestData)

print(dt)

"""
output
  Programs  Scores Grade
A      SQL     100    A+
B   Python     100    A+
C        R      98     A
"""

#%%

# https://www.w3schools.com/python/pandas/pandas_analyzing.asp

"""
Pandas - Analyzing DataFrames

Viewing the Data
One of the most used method for getting a quick overview of the DataFrame, is the head() method.
The head() method returns the headers and a specified number of rows, starting from the top.
"""

# Example
# Get a quick overview by printing the first 10 rows of the DataFrame:

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))

"""
output
   Duration  Pulse  Maxpulse  Calories
0        60    110       130     409.1
1        60    117       145     479.0
2        60    103       135     340.0
3        45    109       175     282.4
4        45    117       148     406.0
5        60    102       127     300.0
6        60    110       136     374.0
7        45    104       134     253.3
8        30    109       133     195.1
9        60     98       124     269.0
"""
# first 10 rows

import pandas as pd

dt = pd.read_csv("data.csv")

print(dt.head(8))

"""
output
   Duration  Pulse  Maxpulse  Calories
0        60    110       130     409.1
1        60    117       145     479.0
2        60    103       135     340.0
3        45    109       175     282.4
4        45    117       148     406.0
5        60    102       127     300.0
6        60    110       136     374.0
7        45    104       134     253.3
"""
# first 8 rows

# In our examples we will be using a CSV file called 'data.csv'.
# Download data.csv, or open data.csv in your browser.

# Note: if the number of rows is not specified, the head() method will return the top 5 rows.

# Example
# Print the first 5 rows of the DataFrame:

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head())

"""
output
   Duration  Pulse  Maxpulse  Calories
0        60    110       130     409.1
1        60    117       145     479.0
2        60    103       135     340.0
3        45    109       175     282.4
4        45    117       148     406.0
"""
# when using head() without specifying the number of rows, it automatically returns the first 5 rows


# There is also a tail() method for viewing the last rows of the DataFrame.
# The tail() method returns the headers and a specified number of rows, starting from the bottom.

# Example
# Print the last 5 rows of the DataFrame:

print(df.tail())

"""
output
     Duration  Pulse  Maxpulse  Calories
164        60    105       140     290.8
165        60    110       145     300.0
166        60    115       145     310.2
167        75    120       150     320.4
168        75    125       150     330.4
"""

# Info About the Data
# The DataFrames object has a method called info(), that gives you more information about the data set.

# Example
# Print information about the data:

print(df.info())

"""
output
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 169 entries, 0 to 168
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   Duration  169 non-null    int64  
 1   Pulse     169 non-null    int64  
 2   Maxpulse  169 non-null    int64  
 3   Calories  164 non-null    float64
dtypes: float64(1), int64(3)
memory usage: 5.4 KB
None
"""

Result
 <class 'pandas.core.frame.DataFrame'>
  RangeIndex: 169 entries, 0 to 168
  Data columns (total 4 columns):
   #   Column    Non-Null Count  Dtype  
  ---  ------    --------------  -----  
   0   Duration  169 non-null    int64  
   1   Pulse     169 non-null    int64  
   2   Maxpulse  169 non-null    int64  
   3   Calories  164 non-null    float64
  dtypes: float64(1), int64(3)
  memory usage: 5.4 KB
  None

Result Explained
The result tells us there are 169 rows and 4 columns:
 RangeIndex: 169 entries, 0 to 168
  Data columns (total 4 columns):


And the name of each column, with the data type:
  #   Column    Non-Null Count  Dtype  
  ---  ------    --------------  -----  
   0   Duration  169 non-null    int64  
   1   Pulse     169 non-null    int64  
   2   Maxpulse  169 non-null    int64  
   3   Calories  164 non-null    float64

"""
Null Values
The info() method also tells us how many Non-Null values there are present in each column, and in our data set it seems like there are 164 of 169 Non-Null values in the "Calories" column.

Which means that there are 5 rows with no value at all, in the "Calories" column, for whatever reason.

Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values. This is a step towards what is called cleaning data, and you will learn more about that in the next chapters.
"""

#%%

# https://www.w3schools.com/python/pandas/pandas_cleaning.asp

"""
Pandas - Cleaning Data

Data Cleaning
Data cleaning means fixing bad data in your data set.

Bad data could be:
Empty cells
Data in wrong format
Wrong data
Duplicates

In this tutorial you will learn how to deal with all of them.

Our Data Set
In the next chapters we will use this data set:
     Duration          Date  Pulse  Maxpulse  Calories
  0         60  '2020/12/01'    110       130     409.1
  1         60  '2020/12/02'    117       145     479.0
  2         60  '2020/12/03'    103       135     340.0
  3         45  '2020/12/04'    109       175     282.4
  4         45  '2020/12/05'    117       148     406.0
  5         60  '2020/12/06'    102       127     300.0
  6         60  '2020/12/07'    110       136     374.0
  7        450  '2020/12/08'    104       134     253.3
  8         30  '2020/12/09'    109       133     195.1
  9         60  '2020/12/10'     98       124     269.0
  10        60  '2020/12/11'    103       147     329.3
  11        60  '2020/12/12'    100       120     250.7
  12        60  '2020/12/12'    100       120     250.7
  13        60  '2020/12/13'    106       128     345.3
  14        60  '2020/12/14'    104       132     379.3
  15        60  '2020/12/15'     98       123     275.0
  16        60  '2020/12/16'     98       120     215.2
  17        60  '2020/12/17'    100       120     300.0
  18        45  '2020/12/18'     90       112       NaN
  19        60  '2020/12/19'    103       123     323.0
  20        45  '2020/12/20'     97       125     243.0
  21        60  '2020/12/21'    108       131     364.2
  22        45           NaN    100       119     282.0
  23        60  '2020/12/23'    130       101     300.0
  24        45  '2020/12/24'    105       132     246.0
  25        60  '2020/12/25'    102       126     334.5
  26        60    2020/12/26    100       120     250.0
  27        60  '2020/12/27'     92       118     241.0
  28        60  '2020/12/28'    103       132       NaN
  29        60  '2020/12/29'    100       132     280.0
  30        60  '2020/12/30'    102       129     380.3
  31        60  '2020/12/31'     92       115     243.0


The data set contains some empty cells ("Date" in row 22, and "Calories" in row 18 and 28).
The data set contains wrong format ("Date" in row 26).
The data set contains wrong data ("Duration" in row 7).
The data set contains duplicates (row 11 and 12).
"""

#%%

# https://www.w3schools.com/python/pandas/pandas_cleaning_empty_cells.asp

"""
Pandas - Cleaning Empty Cells

Empty Cells
Empty cells can potentially give you a wrong result when you analyze data.

Remove Rows
One way to deal with empty cells is to remove rows that contain empty cells.
This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
"""

# Example
# Return a new Data Frame with no empty cells:

import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())

"""
output
row 19, 29, 93 and 120 are gone
"""

import pandas as pd

dt = pd.read_csv("dirtydata.csv")

new_dt = dt.dropna()

print(new_dt.to_string())

"""
output
2 rows with empty cells are gone
"""

"""
In our cleaning examples we will be using a CSV file called 'dirtydata.csv'.
Download dirtydata.csv. or Open dirtydata.csv

Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
If you want to change the original DataFrame, use the inplace = True argument:
In this case changing the original DataFrame does not make any changes to file
"""
# Example
# Remove all rows with NULL values:

import pandas as pd

df = pd.read_csv('data.csv')

df.dropna(inplace = True)

print(df.to_string())

"""
output
row 19, 29, 93 and 120 are gone
"""

import pandas as pd

dt = pd.read_csv("dirtydata.csv")

dt.dropna(inplace = True)

print(dt.to_string())

"""
output
2 rows with empty cells are gone
"""

# Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containg NULL values from the original DataFrame.

"""
Replace Empty Values
Another way of dealing with empty cells is to insert a new value instead.
This way you do not have to delete entire rows just because of some empty cells.
The fillna() method allows us to replace empty cells with a value:
"""

# Example
# Replace NULL values with the number 130:

import pandas as pd

df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)

print(df.to_string())

"""
output
row 19, 29, 93 and 120 have value 130 put into them
"""
import pandas as pd

dt = pd.read_csv("dirtydata.csv")

dt.fillna("Fill", inplace = True)

print(dt.to_string())

"""
output
2 rows that were empty has "Fill" put into it
"""

print(dt.info())

"""
output
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 32 entries, 0 to 31
Data columns (total 5 columns):
 #   Column    Non-Null Count  Dtype 
---  ------    --------------  ----- 
 0   Duration  32 non-null     int64 
 1   Date      32 non-null     object
 2   Pulse     32 non-null     int64 
 3   Maxpulse  32 non-null     int64 
 4   Calories  32 non-null     object
dtypes: int64(3), object(2)
memory usage: 1.4+ KB
"""

print(df.info())

print(dt.info())


import pandas as pd

dt1 = pd.read_csv("dirtydata.csv")

print(dt1.to_string())

print(dt1.info())

dt1.fillna("Fill", inplace = True)

print(dt1.to_string())

"""
output
2 rows that were empty has "Fill" put into it
"""

print(dt1.info())

"""
output
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 32 entries, 0 to 31
Data columns (total 5 columns):
 #   Column    Non-Null Count  Dtype 
---  ------    --------------  ----- 
 0   Duration  32 non-null     int64 
 1   Date      32 non-null     object
 2   Pulse     32 non-null     int64 
 3   Maxpulse  32 non-null     int64 
 4   Calories  32 non-null     object
dtypes: int64(3), object(2)
memory usage: 1.4+ KB
None
"""

"""
Replace Only For Specified Columns
The example above replaces all empty cells in the whole Data Frame.
To only replace empty values for one column, specify the column name for the DataFrame:
"""

# Example
# Replace NULL values in the "Calories" columns with the number 130:

import pandas as pd

df = pd.read_csv('data.csv')

df["Calories"].fillna(130, inplace = True)

print(df.to_string())

"""
output
in Calories column where there were empty cells have 130 put in them
"""

import pandas as pd

dt = pd.read_csv("dirtydata.csv")

dt["Calories"].fillna("Fill", inplace = True)

print(dt.to_string())

"""
output
2 rows in "Calories" where there were empty now has "Fill" put in them
"""

"""
Replace Using Mean, Median, or Mode
A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:
"""

# Example
# Calculate the MEAN, and replace any empty values with it:

import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

print(df.to_string())

"""
output
16         60    100       120   300.000000
17         45     90       112   375.790244
18         60    103       123   323.000000

26         60     92       118   241.000000
27         60    103       132   375.790244
28         60    100       132   280.000000

90        180    101       127   600.100000
91         45    107       137   375.790244
92         30     90       107   105.300000

117        60     97       122   277.400000
118        60    105       125   375.790244
119        60    103       124   332.700000
"""
# the MEAN value of 375.790244 were put into rows that were empty

# Mean = the average value (the sum of all values divided by number of values).

# Example
# Calculate the MEDIAN, and replace any empty values with it:

import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True)

print(df.to_string())

"""
output
16         60    100       120     300.0
17         45     90       112     318.6
18         60    103       123     323.0

26         60     92       118     241.0
27         60    103       132     318.6
28         60    100       132     280.0

90        180    101       127     600.1
91         45    107       137     318.6
92         30     90       107     105.3

117        60     97       122     277.4
118        60    105       125     318.6
119        60    103       124     332.7
"""

# the Median value of 318.6 were put into rows that were empty

# Median = the value in the middle, after you have sorted all values ascending.

# Example
# Calculate the MODE, and replace any empty values with it:

import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)

print(df.to_string())

"""
output
16         60    100       120     300.0
17         45     90       112     300.0
18         60    103       123     323.0

26         60     92       118     241.0
27         60    103       132     300.0
28         60    100       132     280.0

90        180    101       127     600.1
91         45    107       137     300.0
92         30     90       107     105.3

117        60     97       122     277.4
118        60    105       125     300.0
119        60    103       124     332.7
"""
# the Mode value of 300.0 were put into rows that were empty

# Mode = the value that appears most frequently.

# Summary
# df = pd.read_csv('data.csv')
# print(df.to_string())
# print(df) - will print first 5 and last 5 rows unless max rows is changed
# pd.options.display.max_rows = 9999
# print(df)


# df.dropna(), df.dropna(inplace = True)
# df.fillna(value, inplace = True), df["Calories"].fillna(value, inplace = True)

# x = df["Calories"].mean()
# df["Calories"].fillna(x, inplace = True)

# x = df["Calories"].medium()
# df["Calories"].fillna(x, inplace = True)

# x = df["Calories"].mode()[0]
# df["Calories"].fillna(x, inplace = True)


import pandas as pd

dt = pd.read_csv('dirtydata.csv')

print(dt.to_string())

"""
output

    Duration          Date  Pulse  Maxpulse  Calories
0         60  '2020/12/01'    110       130     409.1
1         60  '2020/12/02'    117       145     479.0
2         60  '2020/12/03'    103       135     340.0
3         45  '2020/12/04'    109       175     282.4
4         45  '2020/12/05'    117       148     406.0
5         60  '2020/12/06'    102       127     300.0
6         60  '2020/12/07'    110       136     374.0
7        450  '2020/12/08'    104       134     253.3
8         30  '2020/12/09'    109       133     195.1
9         60  '2020/12/10'     98       124     269.0
10        60  '2020/12/11'    103       147     329.3
11        60  '2020/12/12'    100       120     250.7
12        60  '2020/12/12'    100       120     250.7
13        60  '2020/12/13'    106       128     345.3
14        60  '2020/12/14'    104       132     379.3
15        60  '2020/12/15'     98       123     275.0
16        60  '2020/12/16'     98       120     215.2
17        60  '2020/12/17'    100       120     300.0
18        45  '2020/12/18'     90       112       NaN
19        60  '2020/12/19'    103       123     323.0
20        45  '2020/12/20'     97       125     243.0
21        60  '2020/12/21'    108       131     364.2
22        45           NaN    100       119     282.0
23        60  '2020/12/23'    130       101     300.0
24        45  '2020/12/24'    105       132     246.0
25        60  '2020/12/25'    102       126     334.5
26        60      20201226    100       120     250.0
27        60  '2020/12/27'     92       118     241.0
28        60  '2020/12/28'    103       132       NaN
29        60  '2020/12/29'    100       132     280.0
30        60  '2020/12/30'    102       129     380.3
31        60  '2020/12/31'     92       115     243.0
"""

new_dt = dt.dropna()

print(new_dt.to_string())

"""
output
    Duration          Date  Pulse  Maxpulse  Calories
0         60  '2020/12/01'    110       130     409.1
1         60  '2020/12/02'    117       145     479.0
2         60  '2020/12/03'    103       135     340.0
3         45  '2020/12/04'    109       175     282.4
4         45  '2020/12/05'    117       148     406.0
5         60  '2020/12/06'    102       127     300.0
6         60  '2020/12/07'    110       136     374.0
7        450  '2020/12/08'    104       134     253.3
8         30  '2020/12/09'    109       133     195.1
9         60  '2020/12/10'     98       124     269.0
10        60  '2020/12/11'    103       147     329.3
11        60  '2020/12/12'    100       120     250.7
12        60  '2020/12/12'    100       120     250.7
13        60  '2020/12/13'    106       128     345.3
14        60  '2020/12/14'    104       132     379.3
15        60  '2020/12/15'     98       123     275.0
16        60  '2020/12/16'     98       120     215.2
17        60  '2020/12/17'    100       120     300.0
19        60  '2020/12/19'    103       123     323.0
20        45  '2020/12/20'     97       125     243.0
21        60  '2020/12/21'    108       131     364.2
23        60  '2020/12/23'    130       101     300.0
24        45  '2020/12/24'    105       132     246.0
25        60  '2020/12/25'    102       126     334.5
26        60      20201226    100       120     250.0
27        60  '2020/12/27'     92       118     241.0
29        60  '2020/12/29'    100       132     280.0
30        60  '2020/12/30'    102       129     380.3
31        60  '2020/12/31'     92       115     243.0
"""
# row 18, 22, 28 are gone

import pandas as pd

dt = pd.read_csv('dirtydata.csv')

dt.dropna(inplace = True)

print(dt.to_string())

# row 18, 22, 28 are gone
# original DataFrame is changed

import pandas as pd
dt = pd.read_csv('dirtydata.csv')
dt.fillna(130, inplace = True)
print(dt.to_string())

# row 18, 22, 28 are filled with 130
# row 22 Date column is filled with 130
# row 18, 28 Calories column are filled with 130

import pandas as pd
dt = pd.read_csv('dirtydata.csv')
dt["Calories"].fillna(130, inplace = True)
print(dt.to_string())

# row 18, 28 Calories column are filled with 130

import pandas as pd
dt = pd.read_csv("dirtydata.csv")
x = dt["Calories"].mean()
dt["Calories"].fillna(x, inplace = True)
print(dt.to_string())

# row 18, 28 Calories column are filled with mean value of 304.68

import pandas as pd
dt = pd.read_csv("dirtydata.csv")
x = dt["Calories"].median()
dt["Calories"].fillna(x, inplace = True)
print(dt.to_string())

# row 18, 28 Calories column are filled with medium value of 291.2

import pandas as pd
dt = pd.read_csv("dirtydata.csv")
x = dt["Calories"].mode()[0]
dt["Calories"].fillna(x, inplace = True)
print(dt.to_string())

# row 18, 28 Calories column are filled with mode value of 300

#%%

# https://www.w3schools.com/python/pandas/pandas_cleaning_wrong_format.asp

"""
Pandas - Cleaning Data of Wrong Format
Data of Wrong Format
Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.

Convert Into a Correct Format
In our Data Frame, we have two cells with the wrong format. Check out row 22 and 26, the 'Date' column should be a string that represents a date:

     Duration          Date  Pulse  Maxpulse  Calories
  0         60  '2020/12/01'    110       130     409.1
  1         60  '2020/12/02'    117       145     479.0
  2         60  '2020/12/03'    103       135     340.0
  3         45  '2020/12/04'    109       175     282.4
  4         45  '2020/12/05'    117       148     406.0
  5         60  '2020/12/06'    102       127     300.0
  6         60  '2020/12/07'    110       136     374.0
  7        450  '2020/12/08'    104       134     253.3
  8         30  '2020/12/09'    109       133     195.1
  9         60  '2020/12/10'     98       124     269.0
  10        60  '2020/12/11'    103       147     329.3
  11        60  '2020/12/12'    100       120     250.7
  12        60  '2020/12/12'    100       120     250.7
  13        60  '2020/12/13'    106       128     345.3
  14        60  '2020/12/14'    104       132     379.3
  15        60  '2020/12/15'     98       123     275.0
  16        60  '2020/12/16'     98       120     215.2
  17        60  '2020/12/17'    100       120     300.0
  18        45  '2020/12/18'     90       112       NaN
  19        60  '2020/12/19'    103       123     323.0
  20        45  '2020/12/20'     97       125     243.0
  21        60  '2020/12/21'    108       131     364.2
  22        45           NaN    100       119     282.0
  23        60  '2020/12/23'    130       101     300.0
  24        45  '2020/12/24'    105       132     246.0
  25        60  '2020/12/25'    102       126     334.5
  26        60      20201226    100       120     250.0
  27        60  '2020/12/27'     92       118     241.0
  28        60  '2020/12/28'    103       132       NaN
  29        60  '2020/12/29'    100       132     280.0
  30        60  '2020/12/30'    102       129     380.3
  31        60  '2020/12/31'     92       115     243.0


Let's try to convert all cells in the 'Date' column into dates.
Pandas has a to_datetime() method for this:
"""

# Example
# Convert to date:

import pandas as pd

df = pd.read_csv('dirtydata.csv')

df["Date"] = pd.to_datetime(df["Date"])

print(df.to_string())


"""
output
    Duration       Date  Pulse  Maxpulse  Calories
0         60 2020-12-01    110       130     409.1
1         60 2020-12-02    117       145     479.0
2         60 2020-12-03    103       135     340.0
3         45 2020-12-04    109       175     282.4
4         45 2020-12-05    117       148     406.0
5         60 2020-12-06    102       127     300.0
6         60 2020-12-07    110       136     374.0
7        450 2020-12-08    104       134     253.3
8         30 2020-12-09    109       133     195.1
9         60 2020-12-10     98       124     269.0
10        60 2020-12-11    103       147     329.3
11        60 2020-12-12    100       120     250.7
12        60 2020-12-12    100       120     250.7
13        60 2020-12-13    106       128     345.3
14        60 2020-12-14    104       132     379.3
15        60 2020-12-15     98       123     275.0
16        60 2020-12-16     98       120     215.2
17        60 2020-12-17    100       120     300.0
18        45 2020-12-18     90       112       NaN
19        60 2020-12-19    103       123     323.0
20        45 2020-12-20     97       125     243.0
21        60 2020-12-21    108       131     364.2
22        45        NaT    100       119     282.0
23        60 2020-12-23    130       101     300.0
24        45 2020-12-24    105       132     246.0
25        60 2020-12-25    102       126     334.5
26        60 2020-12-26    100       120     250.0
27        60 2020-12-27     92       118     241.0
28        60 2020-12-28    103       132       NaN
29        60 2020-12-29    100       132     280.0
30        60 2020-12-30    102       129     380.3
31        60 2020-12-31     92       115     243.0
"""

# As you can see from the result, the date in row 26 was fixed, but the empty date in row 22 got a NaT (Not a Time) value, in other words an empty value. One way to deal with empty values is simply removing the entire row.

# Removing Rows
# The result from the converting in the example above gave us a NaT value, which can be handled as a NULL value, and we can remove the row by using the dropna() method.

# Example
# Remove rows with a NULL value in the "Date" column:

df.dropna(subset=['Date'], inplace = True)

print(df.to_string())

"""
output
    Duration       Date  Pulse  Maxpulse  Calories
0         60 2020-12-01    110       130     409.1
1         60 2020-12-02    117       145     479.0
2         60 2020-12-03    103       135     340.0
3         45 2020-12-04    109       175     282.4
4         45 2020-12-05    117       148     406.0
5         60 2020-12-06    102       127     300.0
6         60 2020-12-07    110       136     374.0
7        450 2020-12-08    104       134     253.3
8         30 2020-12-09    109       133     195.1
9         60 2020-12-10     98       124     269.0
10        60 2020-12-11    103       147     329.3
11        60 2020-12-12    100       120     250.7
12        60 2020-12-12    100       120     250.7
13        60 2020-12-13    106       128     345.3
14        60 2020-12-14    104       132     379.3
15        60 2020-12-15     98       123     275.0
16        60 2020-12-16     98       120     215.2
17        60 2020-12-17    100       120     300.0
18        45 2020-12-18     90       112       NaN
19        60 2020-12-19    103       123     323.0
20        45 2020-12-20     97       125     243.0
21        60 2020-12-21    108       131     364.2
23        60 2020-12-23    130       101     300.0
24        45 2020-12-24    105       132     246.0
25        60 2020-12-25    102       126     334.5
26        60 2020-12-26    100       120     250.0
27        60 2020-12-27     92       118     241.0
28        60 2020-12-28    103       132       NaN
29        60 2020-12-29    100       132     280.0
30        60 2020-12-30    102       129     380.3
31        60 2020-12-31     92       115     243.0
"""
# row 22 is removed.  df.dropna(subset=['Date'], inplace = True) drops the row where the Date is NULL

"""
Summary
df["Date"] = pd.to_datetime(df["Date"])
f.dropna(subset=['Date'], inplace = True)
"""

#%%

# https://www.w3schools.com/python/pandas/pandas_cleaning_wrong_data.asp

"""
Pandas - Fixing Wrong Data

Wrong Data
"Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".

Sometimes you can spot wrong data by looking at the data set, because you have an expectation of what it should be.

If you take a look at our data set, you can see that in row 7, the duration is 450, but for all the other rows the duration is between 30 and 60.

It doesn't have to be wrong, but taking in consideration that this is the data set of someone's workout sessions, we conclude with the fact that this person did not work out in 450 minutes.

     Duration          Date  Pulse  Maxpulse  Calories
  0         60  '2020/12/01'    110       130     409.1
  1         60  '2020/12/02'    117       145     479.0
  2         60  '2020/12/03'    103       135     340.0
  3         45  '2020/12/04'    109       175     282.4
  4         45  '2020/12/05'    117       148     406.0
  5         60  '2020/12/06'    102       127     300.0
  6         60  '2020/12/07'    110       136     374.0
  7        450  '2020/12/08'    104       134     253.3
  8         30  '2020/12/09'    109       133     195.1
  9         60  '2020/12/10'     98       124     269.0
  10        60  '2020/12/11'    103       147     329.3
  11        60  '2020/12/12'    100       120     250.7
  12        60  '2020/12/12'    100       120     250.7
  13        60  '2020/12/13'    106       128     345.3
  14        60  '2020/12/14'    104       132     379.3
  15        60  '2020/12/15'     98       123     275.0
  16        60  '2020/12/16'     98       120     215.2
  17        60  '2020/12/17'    100       120     300.0
  18        45  '2020/12/18'     90       112       NaN
  19        60  '2020/12/19'    103       123     323.0
  20        45  '2020/12/20'     97       125     243.0
  21        60  '2020/12/21'    108       131     364.2
  22        45           NaN    100       119     282.0
  23        60  '2020/12/23'    130       101     300.0
  24        45  '2020/12/24'    105       132     246.0
  25        60  '2020/12/25'    102       126     334.5
  26        60      20201226    100       120     250.0
  27        60  '2020/12/27'     92       118     241.0
  28        60  '2020/12/28'    103       132       NaN
  29        60  '2020/12/29'    100       132     280.0
  30        60  '2020/12/30'    102       129     380.3
  31        60  '2020/12/31'     92       115     243.0
"""

# How can we fix wrong values, like the one for "Duration" in row 7?

# Replacing Values
# One way to fix wrong values is to replace them with something else.
# In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7:

# Example
# Set "Duration" = 45 in row 7:

df.loc[7, 'Duration'] = 45

print(df.to_string())

"""
output
6         60 2020-12-07    110       136     374.0
7         45 2020-12-08    104       134     253.3
8         30 2020-12-09    109       133     195.1
"""
# Duration was 450 now Duraiton is set to 45

# For small data sets you might be able to replace the wrong data one by one, but not for big data sets.
# To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.

# Example
# Loop through all values in the "Duration" column.
# If the value is higher than 120, set it to 120:

df = pd.read_csv("Dirtydata.csv")

print(df.to_string())

"""
output
6         60  '2020/12/07'    110       136     374.0
7        450  '2020/12/08'    104       134     253.3
8         30  '2020/12/09'    109       133     195.1
"""

for y in df.index:
    if df.loc[y, "Duration"] > 120:
        df.loc[y, "Duration"] = 120

print(df.to_string())

"""
output
6         60  '2020/12/07'    110       136     374.0
7        120  '2020/12/08'    104       134     253.3
8         30  '2020/12/09'    109       133     195.1
"""

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

print(df.to_string())

"""
output
6         60  '2020/12/07'    110       136     374.0
7        120  '2020/12/08'    104       134     253.3
8         30  '2020/12/09'    109       133     195.1
"""
# nothing is changed, in row 7 "Duration" has already been changed to 120

# Removing Rows
# Another way of handling wrong data is to remove the rows that contains wrong data.
# This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.

# Example
# Delete rows where "Duration" is higher than 120:

df = pd.read_csv("Dirtydata.csv")

print(df.to_string())    

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

print(df.to_string())

"""
output
5         60  '2020/12/06'    102       127     300.0
6         60  '2020/12/07'    110       136     374.0
8         30  '2020/12/09'    109       133     195.1
9         60  '2020/12/10'     98       124     269.0
"""
# row 7 is removed because Duration is 450 > 120

for x in df.index:
  if df.loc[x, "Duration"] < 60:
    df.drop(x, inplace = True)

print(df.to_string())

"""
output
    Duration          Date  Pulse  Maxpulse  Calories
0         60  '2020/12/01'    110       130     409.1
1         60  '2020/12/02'    117       145     479.0
2         60  '2020/12/03'    103       135     340.0
5         60  '2020/12/06'    102       127     300.0
6         60  '2020/12/07'    110       136     374.0
9         60  '2020/12/10'     98       124     269.0
10        60  '2020/12/11'    103       147     329.3
11        60  '2020/12/12'    100       120     250.7
12        60  '2020/12/12'    100       120     250.7
13        60  '2020/12/13'    106       128     345.3
14        60  '2020/12/14'    104       132     379.3
15        60  '2020/12/15'     98       123     275.0
16        60  '2020/12/16'     98       120     215.2
17        60  '2020/12/17'    100       120     300.0
19        60  '2020/12/19'    103       123     323.0
21        60  '2020/12/21'    108       131     364.2
23        60  '2020/12/23'    130       101     300.0
25        60  '2020/12/25'    102       126     334.5
26        60      20201226    100       120     250.0
27        60  '2020/12/27'     92       118     241.0
28        60  '2020/12/28'    103       132       NaN
29        60  '2020/12/29'    100       132     280.0
30        60  '2020/12/30'    102       129     380.3
31        60  '2020/12/31'     92       115     243.0
"""
# all rows with Duration < 60 are removed

"""
Summary
df.loc[7, 'Duration'] = 45
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
"""

#%%

# https://www.w3schools.com/python/pandas/pandas_cleaning_duplicates.asp

"""
Pandas - Removing Duplicates
Discovering Duplicates
Duplicate rows are rows that have been registered more than one time.

     Duration          Date  Pulse  Maxpulse  Calories
  0         60  '2020/12/01'    110       130     409.1
  1         60  '2020/12/02'    117       145     479.0
  2         60  '2020/12/03'    103       135     340.0
  3         45  '2020/12/04'    109       175     282.4
  4         45  '2020/12/05'    117       148     406.0
  5         60  '2020/12/06'    102       127     300.0
  6         60  '2020/12/07'    110       136     374.0
  7        450  '2020/12/08'    104       134     253.3
  8         30  '2020/12/09'    109       133     195.1
  9         60  '2020/12/10'     98       124     269.0
  10        60  '2020/12/11'    103       147     329.3
  11        60  '2020/12/12'    100       120     250.7
  12        60  '2020/12/12'    100       120     250.7
  13        60  '2020/12/13'    106       128     345.3
  14        60  '2020/12/14'    104       132     379.3
  15        60  '2020/12/15'     98       123     275.0
  16        60  '2020/12/16'     98       120     215.2
  17        60  '2020/12/17'    100       120     300.0
  18        45  '2020/12/18'     90       112       NaN
  19        60  '2020/12/19'    103       123     323.0
  20        45  '2020/12/20'     97       125     243.0
  21        60  '2020/12/21'    108       131     364.2
  22        45           NaN    100       119     282.0
  23        60  '2020/12/23'    130       101     300.0
  24        45  '2020/12/24'    105       132     246.0
  25        60  '2020/12/25'    102       126     334.5
  26        60      20201226    100       120     250.0
  27        60  '2020/12/27'     92       118     241.0
  28        60  '2020/12/28'    103       132       NaN
  29        60  '2020/12/29'    100       132     280.0
  30        60  '2020/12/30'    102       129     380.3
  31        60  '2020/12/31'     92       115     243.0
"""

# By taking a look at our test data set, we can assume that row 11 and 12 are duplicates.
# To discover duplicates, we can use the duplicated() method.
# The duplicated() method returns a Boolean values for each row:

# Example
# Returns True for every row that is a duplicate, othwerwise False:

import pandas as pd

df = pd.read_csv("Dirtydata.csv")

print(df.to_string())

"""
output
9         60  '2020/12/10'     98       124     269.0
10        60  '2020/12/11'    103       147     329.3
11        60  '2020/12/12'    100       120     250.7
12        60  '2020/12/12'    100       120     250.7
"""
print(df.duplicated())

"""
output
10    False
11    False
12     True
13    False
14    False
"""
# row 12 is a duplicate

# Removing Duplicates
# To remove duplicates, use the drop_duplicates() method.

# Example
# Remove all duplicates:

df.drop_duplicates(inplace = True)

print(df.duplicated())

"""
output
10    False
11    False
13    False
14    False
"""
# row 12 is removed

print(df.to_string())

"""
output
10        60  '2020/12/11'    103       147     329.3
11        60  '2020/12/12'    100       120     250.7
13        60  '2020/12/13'    106       128     345.3
14        60  '2020/12/14'    104       132     379.3
"""
# row 12 is removed

# Remember: The (inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.

# Test Yourself With Exercises
# Exercise:
# Insert the correct syntax for removing rows with empty cells.

df.dropna()

"""
Summary
print(df.duplicated())

df.drop_duplicates(inplace = True)
print(df.duplicated())
"""

#%%

# https://www.w3schools.com/python/pandas/pandas_correlations.asp

"""
Pandas - Data Correlations

Finding Relationships
A great aspect of the Pandas module is the corr() method.
The corr() method calculates the relationship between each column in your data set.
The examples in this page uses a CSV file called: 'data.csv'.
Download data.csv. or Open data.csv
"""

# Example
# Show the relationship between the columns:

import pandas as pd    

df = pd.read_csv('data.csv')

print(df.to_string())

df.corr()

"""
output
          Duration     Pulse  Maxpulse  Calories
Duration  1.000000 -0.155408  0.009403  0.922717
Pulse    -0.155408  1.000000  0.786535  0.025121
Maxpulse  0.009403  0.786535  1.000000  0.203813
Calories  0.922717  0.025121  0.203813  1.000000
"""

# Note: The corr() method ignores "not numeric" columns.

"""
Result Explained

The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.

The number varies from -1 to 1.

1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well.

0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.

-0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.

0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.

What is a good correlation? It depends on the use, but I think it is safe to say you have to have at least 0.6 (or -0.6) to call it a good correlation.

Perfect Correlation:
We can see that "Duration" and "Duration" got the number 1.000000, which makes sense, each column always has a perfect relationship with itself.

Good Correlation:
"Duration" and "Calories" got a 0.922721 correlation, which is a very good correlation, and we can predict that the longer you work out, the more calories you burn, and the other way around: if you burned a lot of calories, you probably had a long work out.

Bad Correlation:
"Duration" and "Maxpulse" got a 0.009403 correlation, which is a very bad correlation, meaning that we can not predict the max pulse by just looking at the duration of the work out, and vice versa.
"""

# Test Yourself With Exercises
# Exercise:
# Insert a correct syntax for finding relationships between columns in a DataFrame.

df.corr()

"""
Summary
df.corr()
"""

#%%

# https://www.w3schools.com/python/pandas/pandas_plotting.asp

"""
Pandas - Plotting

Plotting
Pandas uses the plot() method to create diagrams.
We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.
Read more about Matplotlib in our Matplotlib Tutorial.
"""

# Example
# Import pyplot from Matplotlib and visualize our DataFrame:

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

dt = pd.read_csv('Dirtydata.csv')

print(dt.to_string())

dt.plot()

plt.show()

# Date column is ignored since it does not contain numbers

# The examples in this page uses a CSV file called: 'data.csv'.
# Download data.csv or Open data.csv

"""
Scatter Plot

Specify that you want a scatter plot with the kind argument:

kind = 'scatter'

A scatter plot needs an x- and a y-axis.

In the example below we will use "Duration" for the x-axis and "Calories" for the y-axis.
Include the x and y arguments like this:

x = 'Duration', y = 'Calories'
"""
# Example

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

dt = pd.read_csv('Dirtydata.csv')

dt.plot(kind = "scatter", x = "Duration", y = "Calories")

plt.show()

# Remember: In the previous example, we learned that the correlation between "Duration" and "Calories" was 0.922721, and we conluded with the fact that higher duration means more calories burned.

# By looking at the scatterplot, I will agree.
# Let's create another scatterplot, where there is a bad relationship between the columns, like "Duration" and "Maxpulse", with the correlation 0.009403:

# Example
# A scatterplot where there are no relationship between the columns:

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

plt.show()

"""
Histogram

Use the kind argument to specify that you want a histogram:
kind = 'hist'

A histogram needs only one column.

A histogram shows us the frequency of each interval, e.g. how many workouts lasted between 50 and 60 minutes?

In the example below we will use the "Duration" column to create the histogram:
"""

# Example

df["Duration"].plot(kind = 'hist')

# Test Yourself With Exercises
# Exercise:
# Insert a correct syntax for visualize the data in DataFrame as a diagram (plotting).

df.plot()

"""
Summary

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()

df["Duration"].plot(kind = 'hist')
"""

#%%

# https://www.w3schools.com/python/pandas/pandas_quiz.asp

# https://www.w3schools.com/python/pandas/exercise.asp

# The end