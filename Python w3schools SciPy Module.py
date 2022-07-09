# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 21:40:19 2022

@author: jiang
"""

# Python w3schools SciPy Module

# https://www.w3schools.com/python/scipy/index.php

"""
SciPy Tutorial

SciPy is a scientific computation library that uses NumPy underneath.
SciPy stands for Scientific Python.
Learning by Reading
We have created 10 tutorial pages for you to learn the fundamentals of SciPy:

Basic SciPy

Introduction
 
Getting Started
 
Constants
 
Optimizers
 
Sparse Data
 
Graphs
 
Spatial Data
 
Matlab Arrays
 
Interpolation
 
Significance Tests

"""

# Learning by Quiz Test
# Test your SciPy skills with a quiz test.

# Learning by Exercises
# SciPy Exercises

# Exercise:
# Insert the correct syntax for printing the kilometer unit (in meters):

print(constants.kilo);

#%%

# https://www.w3schools.com/python/scipy/scipy_intro.php

"""
SciPy Introduction

What is SciPy?
SciPy is a scientific computation library that uses NumPy underneath.
SciPy stands for Scientific Python.
It provides more utility functions for optimization, stats and signal processing.
Like NumPy, SciPy is open source so we can use it freely.
SciPy was created by NumPy's creator Travis Olliphant.

Why Use SciPy?
If SciPy uses NumPy underneath, why can we not just use NumPy?
SciPy has optimized and added functions that are frequently used in NumPy and Data Science.

Which Language is SciPy Written in?
SciPy is predominantly written in Python, but a few segments are written in C.

Where is the SciPy Codebase?
The source code for SciPy is located at this github repository https://github.com/scipy/scipy
github: enables many people to work on the same codebase.
"""

#%%

# https://www.w3schools.com/python/scipy/scipy_getting_started.php

"""
SciPy Getting Started

Installation of SciPy
If you have Python and PIP already installed on a system, then installation of SciPy is very easy.
Install it using this command:

C:\Users\Your Name>pip install scipy

If this command fails, then use a Python distribution that already has SciPy installed like, Anaconda, Spyder etc.
"""

# Import SciPy
# Once SciPy is installed, import the SciPy module(s) you want to use in your applications by adding the from scipy import module statement:

from scipy import constants

# Now we have imported the constants module from SciPy, and the application is ready to use it:

# Example
# How many cubic meters are in one liter:

from scipy import constants

print(constants.liter)

# output - 0.001

# constants: SciPy offers a set of mathematical constants, one of them is liter which returns 1 liter as cubic meters.
# You will learn more about constants in the next chapter.

# Checking SciPy Version
# The version string is stored under the __version__ attribute.
# Example

import scipy

print(scipy.__version__)

# output - 1.5.0

# Note: two underscore characters are used in __version__.

#%%

# https://www.w3schools.com/python/scipy/scipy_constants.php

"""
SciPy Constants

Constants in SciPy
As SciPy is more focused on scientific implementations, it provides many built-in scientific constants.
These constants can be helpful when you are working with Data Science.
PI is an example of a scientific constant.
"""

# Example
# Print the constant value of PI:

from scipy import constants

print(constants.pi)

# output - 3.141592653589793

# Constant Units
# A list of all units under the constants module can be seen using the dir() function.

# Example
# List all constants:

from scipy import constants

print(dir(constants))

# output - list of all units

"""
Unit Categories
The units are placed under these categories:

Metric
Binary
Mass
Angle
Time
Length
Pressure
Volume
Speed
Temperature
Energy
Power
Force
"""

# Metric (SI) Prefixes:
# Return the specified unit in meter (e.g. centi returns 0.01)

# Example

from scipy import constants

print(constants.yotta)    #1e+24
print(constants.zetta)    #1e+21
print(constants.exa)      #1e+18
print(constants.peta)     #1000000000000000.0
print(constants.tera)     #1000000000000.0
print(constants.giga)     #1000000000.0
print(constants.mega)     #1000000.0
print(constants.kilo)     #1000.0
print(constants.hecto)    #100.0
print(constants.deka)     #10.0
print(constants.deci)     #0.1
print(constants.centi)    #0.01
print(constants.milli)    #0.001
print(constants.micro)    #1e-06
print(constants.nano)     #1e-09
print(constants.pico)     #1e-12
print(constants.femto)    #1e-15
print(constants.atto)     #1e-18
print(constants.zepto)    #1e-21

# Binary Prefixes:
# Return the specified unit in bytes (e.g. kibi returns 1024)

# Example

from scipy import constants

print(constants.kibi)    #1024
print(constants.mebi)    #1048576
print(constants.gibi)    #1073741824
print(constants.tebi)    #1099511627776
print(constants.pebi)    #1125899906842624
print(constants.exbi)    #1152921504606846976
print(constants.zebi)    #1180591620717411303424
print(constants.yobi)    #1208925819614629174706176

# Mass:
# Return the specified unit in kg (e.g. gram returns 0.001)

# Example

from scipy import constants

print(constants.gram) 	   #0.001
print(constants.metric_ton)  #1000.0
print(constants.grain)       #6.479891e-05
print(constants.lb)          #0.45359236999999997
print(constants.pound)	   #0.45359236999999997
print(constants.oz)          #0.028349523124999998
print(constants.ounce)       #0.028349523124999998
print(constants.stone)       #6.3502931799999995
print(constants.long_ton)    #1016.0469088
print(constants.short_ton)   #907.1847399999999
print(constants.troy_ounce)  #0.031103476799999998
print(constants.troy_pound)  #0.37324172159999996
print(constants.carat)  	 #0.0002
print(constants.atomic_mass) #1.66053904e-27
print(constants.m_u)         #1.66053904e-27
print(constants.u)           #1.66053904e-27

# Angle:
# Return the specified unit in radians (e.g. degree returns 0.017453292519943295)

# Example

from scipy import constants

print(constants.degree)     #0.017453292519943295
print(constants.arcmin)     #0.0002908882086657216
print(constants.arcminute)  #0.0002908882086657216
print(constants.arcsec)     #4.84813681109536e-06
print(constants.arcsecond)  #4.84813681109536e-06

# Time:
# Return the specified unit in seconds (e.g. hour returns 3600.0)

# Example

from scipy import constants

print(constants.minute)      #60.0
print(constants.hour)  	  #3600.0
print(constants.day)    	 #86400.0
print(constants.week)  	  #604800.0
print(constants.year)        #31536000.0
print(constants.Julian_year) #31557600.0

# Length:
# Return the specified unit in meters (e.g. nautical_mile returns 1852.0)

# Example

from scipy import constants

print(constants.inch)     	     #0.0254
print(constants.foot)   		   #0.30479999999999996
print(constants.yard)  	   	 #0.9143999999999999
print(constants.mile)  	        #1609.3439999999998
print(constants.mil)    	       #2.5399999999999997e-05
print(constants.pt)                #0.00035277777777777776
print(constants.point)       	  #0.00035277777777777776
print(constants.survey_foot) 	  #0.3048006096012192
print(constants.survey_mile)  	 #1609.3472186944373
print(constants.nautical_mile)     #1852.0
print(constants.fermi)      	   #1e-15
print(constants.angstrom)     	 #1e-10
print(constants.micron)     	   #1e-06
print(constants.au)        	    #149597870691.0
print(constants.astronomical_unit) #149597870691.0
print(constants.light_year)  	  #9460730472580800.0
print(constants.parsec)            #3.0856775813057292e+16

# Pressure:
# Return the specified unit in pascals (e.g. psi returns 6894.757293168361)

# Example

from scipy import constants

print(constants.atm)	     #101325.0
print(constants.atmosphere)  #101325.0
print(constants.bar)    	 #100000.0
print(constants.torr)  	  #133.32236842105263
print(constants.mmHg)        #133.32236842105263
print(constants.psi)         #6894.757293168361

# Area:
# Return the specified unit in square meters(e.g. hectare returns 10000.0)

# Example

from scipy import constants

print(constants.hectare) #10000.0
print(constants.acre)    #4046.8564223999992

# Volume:
# Return the specified unit in cubic meters (e.g. liter returns 0.001)

# Example

from scipy import constants

print(constants.liter) 	 	  #0.001
print(constants.litre) 		   #0.001
print(constants.gallon)      	 #0.0037854117839999997
print(constants.gallon_US)        #0.0037854117839999997
print(constants.gallon_imp)       #0.00454609
print(constants.fluid_ounce)      #2.9573529562499998e-05
print(constants.fluid_ounce_US)   #2.9573529562499998e-05
print(constants.fluid_ounce_imp)  #2.84130625e-05
print(constants.barrel)     	  #0.15898729492799998
print(constants.bbl)      	    #0.15898729492799998

# Speed:
# Return the specified unit in meters per second (e.g. speed_of_sound returns 340.5)

# Example

from scipy import constants

print(constants.kmh) 	 	  #0.2777777777777778
print(constants.mph) 		   #0.44703999999999994
print(constants.mach)      	 #340.5
print(constants.speed_of_sound) #340.5
print(constants.knot) 		  #0.5144444444444445

# Temperature:
# Return the specified unit in Kelvin (e.g. zero_Celsius returns 273.15)

# Example

from scipy import constants

print(constants.zero_Celsius)      #273.15
print(constants.degree_Fahrenheit) #0.5555555555555556

# Energy:
# Return the specified unit in joules (e.g. calorie returns 4.184)

# Example

from scipy import constants

print(constants.eV) 	 	  #1.6021766208e-19
print(constants.electron_volt) #1.6021766208e-19
print(constants.calorie)       #4.184
print(constants.calorie_th)    #4.184
print(constants.calorie_IT)    #4.1868
print(constants.erg)     	  #1e-07
print(constants.Btu)           #1055.05585262
print(constants.Btu_IT)   	 #1055.05585262
print(constants.Btu_th)  	  #1054.3502644888888
print(constants.ton_TNT)	   #4184000000.0

# Power:
# Return the specified unit in watts (e.g. horsepower returns 745.6998715822701)

# Example

from scipy import constants

print(constants.hp) 	    #745.6998715822701
print(constants.horsepower) #745.6998715822701

# Force:
# Return the specified unit in newton (e.g. kilogram_force returns 9.80665)

# Example

from scipy import constants

print(constants.dyn)    	     #1e-05
print(constants.dyne)   	     #1e-05
print(constants.lbf)    	     #4.4482216152605
print(constants.pound_force)	 #4.4482216152605
print(constants.kgf)     	    #9.80665
print(constants.kilogram_force)  #9.80665

# Test Yourself With Exercises
# Exercise:
# Insert the correct syntax for printing the kilometer unit (in meters):

print(constants.kilo)

# output - 1000.0

#%%

# https://www.w3schools.com/python/scipy/scipy_optimizers.php

"""
SciPy Optimizers

Optimizers in SciPy
Optimizers are a set of procedures defined in SciPy that either find the minimum value of a function, or the root of an equation.

Optimizing Functions
Essentially, all of the algorithms in Machine Learning are nothing more than a complex equation that needs to be minimized with the help of given data.

Roots of an Equation
NumPy is capable of finding roots for polynomials and linear equations, but it can not find roots for non linear equations, like this one:
x + cos(x)
For that you can use SciPy's optimze.root function.
This function takes two required arguments:
fun - a function representing an equation.
x0 - an initial guess for the root.
The function returns an object with information regarding the solution.
The actual solution is given under attribute x of the returned object:
"""

# Example
# Find root of the equation x + cos(x):

from scipy.optimize import root
from math import cos

def eqn(x):
  return x + cos(x)

myroot = root(eqn, 0)

print(myroot.x)

# output - [-0.73908513]

# Note: The returned object has much more information about the solution.

# Example
# Print all information about the solution (not just x which is the root)

print(myroot)

"""
output
fjac: array([[-1.]])
     fun: array([0.])
 message: 'The solution converged.'
    nfev: 9
     qtf: array([-2.66786593e-13])
       r: array([-1.67361202])
  status: 1
 success: True
       x: array([-0.73908513])
"""

"""
Minimizing a Function
A function, in this context, represents a curve, curves have high points and low points.
High points are called maxima.
Low points are called minima.
The highest point in the whole curve is called global maxima, whereas the rest of them are called local maxima.
The lowest point in whole curve is called global minima, whereas the rest of them are called local minima.

Finding Minima
We can use scipy.optimize.minimize() function to minimize the function.
The minimize() function takes the following arguments:
fun - a function representing an equation.
x0 - an initial guess for the root.
method - name of the method to use. Legal values:
    'CG'
    'BFGS'
    'Newton-CG'
    'L-BFGS-B'
    'TNC'
    'COBYLA'
    'SLSQP'
callback - function called after each iteration of optimization.
options - a dictionary defining extra params:
{
 	"disp": boolean - print detailed description
 	"gtol": number - the tolerance of the error
  }
"""

# Example
# Minimize the function x^2 + x + 2 with BFGS:

from scipy.optimize import minimize

def eqn(x):
  return x**2 + x + 2

mymin = minimize(eqn, 0, method='BFGS')

print(mymin)

"""
output
fun: 1.75
 hess_inv: array([[0.49999999]])
      jac: array([-0.])
  message: 'Optimization terminated successfully.'
     nfev: 8
      nit: 2
     njev: 4
   status: 0
  success: True
        x: array([-0.49999999])
"""

# Test Yourself With Exercises
# Exercise:
# Insert the missing parts to print the square root of the equation:

from scipy.optimize import root
from math import cos

def eqn(x):
  return x + cos(x)

myroot = root (eqn, 0)

print(myroot.x)

# output - [-0.73908513]

#%%

# https://www.w3schools.com/python/scipy/scipy_sparse_data.php

"""
SciPy Sparse Data

What is Sparse Data
Sparse data is data that has mostly unused elements (elements that don't carry any information ).
It can be an array like this one:
[1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0]
Sparse Data: is a data set where most of the item values are zero.
Dense Array: is the opposite of a sparse array: most of the values are not zero.
In scientific computing, when we are dealing with partial derivatives in linear algebra we will come across sparse data.

How to Work With Sparse Data

SciPy has a module, scipy.sparse that provides functions to deal with sparse data.
There are primarily two types of sparse matrices that we use:
CSC - Compressed Sparse Column. For efficient arithmetic, fast column slicing.
CSR - Compressed Sparse Row. For fast row slicing, faster matrix vector products
We will use the CSR matrix in this tutorial.
"""

# CSR Matrix
# We can create CSR matrix by passing an arrray into function scipy.sparse.csr_matrix().

# Example
# Create a CSR matrix from an array:

import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])

print(csr_matrix(arr))

"""
The example above returns:
(0, 5)	1
(0, 6)	1
(0, 8)	2

From the result we can see that there are 3 items with value.
The 1. item is in row 0 position 5 and has the value 1.
The 2. item is in row 0 position 6 and has the value 1.
The 3. item is in row 0 position 8 and has the value 2.
"""

# Sparse Matrix Methods
# Viewing stored data (not the zero items) with the data property:

# Example

import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

print(csr_matrix(arr).data)

# output - [1 1 2]

# Counting nonzeros with the count_nonzero() method:

# Example

import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

print(csr_matrix(arr).count_nonzero())

# output - 3

# Removing zero-entries from the matrix with the eliminate_zeros() method:

# Example

import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

mat = csr_matrix(arr)

print(mat)

"""
output
(1, 2) 1
(2, 0) 1
(2, 2) 2
"""

mat.eliminate_zeros()

print(mat)

"""
output
(1, 2) 1
(2, 0) 1
(2, 2) 2
"""

# Same output

# Eliminating duplicate entries with the sum_duplicates() method:

# Example
# Eliminating duplicates by adding them:

import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

mat = csr_matrix(arr)
mat.sum_duplicates()

print(mat)

"""
output
(1, 2) 1
(2, 0) 1
(2, 2) 2
"""

# Converting from csr to csc with the tocsc() method:

# Example

import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

newarr = csr_matrix(arr).tocsc()

print(newarr)

"""
output
(2, 0)	1
(1, 2)	1
(2, 2)	2
"""

# Note: Apart from the mentioned sparse specific operations, sparse matrices support all of the operations that normal matrices support e.g. reshaping, summing, arithemetic, broadcasting etc.

# Test Yourself With Exercises
# Exercise:
# Insert the missing method to print the number of values in the array that are NOT zeros:

import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

print(csr_matrix(arr).count_nonzero())

# output - 3

#%%

# https://www.w3schools.com/python/scipy/scipy_graphs.php

"""
SciPy Graphs

Working with Graphs
Graphs are an essential data structure.
SciPy provides us with the module scipy.sparse.csgraph for working with such data structures.

Adjacency Matrix
Adjacency matrix is a nxn matrix where n is the number of elements in a graph.
And the values represents the connection between the elements.
"""

# Example:

"""
For a graph like this, with elements A, B and C, the connections are:
A & B are connected with weight 1.
A & C are connected with weight 2.
C & B is not connected.
The Adjency Matrix would look like this:

    A B C
A:[0 1 2]  
B:[1 0 0]
C:[2 0 0]


Below follows some of the most used methods for working with adjacency matrices.

Connected Components
Find all of the connected components with the connected_components() method.
"""

# Example

import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(connected_components(newarr))

# output - (1, array([0, 0, 0]))

"""
Dijkstra

Use the dijkstra method to find the shortest path in a graph from one element to another.
It takes following arguments:
return_predecessors: boolean (True to return whole path of traversal otherwise False).
indices: index of the element to return all paths from that element only.
limit: max weight of path.
"""

# Example
# Find the shortest path from element 1 to 2:

import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(dijkstra(newarr, return_predecessors=True, indices=0))

# output - (array([0., 1., 2.]), array([-9999,     0,     0]))

# Floyd Warshall
# Use the floyd_warshall() method to find shortest path between all pairs of elements.

# Example
# Find the shortest path between all pairs of elements:

import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(floyd_warshall(newarr, return_predecessors=True))

"""
output
(array([[0., 1., 2.],
       [1., 0., 3.],
       [2., 3., 0.]]), array([[-9999,     0,     0],
       [    1, -9999,     0],
       [    2,     0, -9999]]))
"""
                            
# Bellman Ford
# The bellman_ford() method can also find the shortest path between all pairs of elements, but this method can handle negative weights as well.

# Example
# Find shortest path from element 1 to 2 with given graph with a negative weight:

import numpy as np
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix

arr = np.array([
  [0, -1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(bellman_ford(newarr, return_predecessors=True, indices=0))

# output - (array([ 0., -1.,  2.]), array([-9999,     0,     0]))

"""
Depth First Order

The depth_first_order() method returns a depth first traversal from a node.
This function takes following arguments:
the graph.
the starting element to traverse graph from.
"""

# Example
# Traverse the graph depth first for given adjacency matrix:

import numpy as np
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(depth_first_order(newarr, 1))

# output - (array([1, 0, 3, 2]), array([    1, -9999,     1,     0]))

"""
Breadth First Order

The breadth_first_order() method returns a breadth first traversal from a node.
This function takes following arguments:
the graph.
the starting element to traverse graph from.
"""

# Example
# Traverse the graph breadth first for given adjacency matrix:

import numpy as np
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(breadth_first_order(newarr, 1))

# output - (array([1, 0, 2, 3]), array([    1, -9999,     1,     1]))

# Test Yourself With Exercises
# Exercise:
# Insert the missing method to find all the connected components:

import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(connected_components(newarr))

# output - (1, array([0, 0, 0]))

#%%

# https://www.w3schools.com/python/scipy/scipy_spatial_data.php

"""
SciPy Spatial Data

Working with Spatial Data

Spatial data refers to data that is represented in a geometric space.
E.g. points on a coordinate system.

We deal with spatial data problems on many tasks.
E.g. finding if a point is inside a boundary or not.

SciPy provides us with the module scipy.spatial, which has functions for working with spatial data.

Triangulation
A Triangulation of a polygon is to divide the polygon into multiple triangles with which we can compute an area of the polygon.

A Triangulation with points means creating surface composed triangles in which all of the given points are on at least one vertex of any triangle in the surface.

One method to generate these triangulations through points is the Delaunay() Triangulation.
"""

# Example
# Create a triangulation from following points:

import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
])

simplices = Delaunay(points).simplices

plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')

plt.show()

# Result:

# Note: The simplices property creates a generalization of the triangle notation.

# Convex Hull
# A convex hull is the smallest polygon that covers all of the given points.
# Use the ConvexHull() method to create a Convex Hull.

# Example
# Create a convex hull for following points:

import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1],
  [1, 2],
  [5, 0],
  [3, 1],
  [1, 2],
  [0, 2]
])

hull = ConvexHull(points)
hull_points = hull.simplices

plt.scatter(points[:,0], points[:,1])
for simplex in hull_points:
  plt.plot(points[simplex,0], points[simplex,1], 'k-')

plt.show()

# Result:

"""
KDTrees

KDTrees are a datastructure optimized for nearest neighbor queries.
E.g. in a set of points using KDTrees we can efficiently ask which points are nearest to a certain given point.

The KDTree() method returns a KDTree object.
The query() method returns the distance to the nearest neighbor and the location of the neighbors.
"""

# Example
# Find the nearest neighbor to point (1,1):

from scipy.spatial import KDTree

points = [(1, -1), (2, 3), (-2, 3), (2, -3)]

kdtree = KDTree(points)

res = kdtree.query((1, 1))

print(res)

# Result:
(2.0, 0)

"""
Distance Matrix

There are many Distance Metrics used to find various types of distances between two points in data science, Euclidean distsance, cosine distsance etc.

The distance between two vectors may not only be the length of straight line between them, it can also be the angle between them from origin, or number of unit steps required etc.

Many of the Machine Learning algorithm's performance depends greatly on distance metrices. E.g. "K Nearest Neighbors", or "K Means" etc.

Let us look at some of the Distance Metrices:
"""

# Euclidean Distance
# Find the euclidean distance between given points.

# Example

from scipy.spatial.distance import euclidean

p1 = (1, 0)
p2 = (10, 2)

res = euclidean(p1, p2)

print(res)

# Result:
9.21954445729

# Cityblock Distance (Manhattan Distance)
# Is the distance computed using 4 degrees of movement.
# E.g. we can only move: up, down, right, or left, not diagonally.

# Example
# Find the cityblock distance between given points:

from scipy.spatial.distance import cityblock

p1 = (1, 0)
p2 = (10, 2)

res = cityblock(p1, p2)

print(res)

# Result:
11

# Cosine Distance
# Is the value of cosine angle between the two points A and B.

# Example
# Find the cosine distsance between given points:

from scipy.spatial.distance import cosine

p1 = (1, 0)
p2 = (10, 2)

res = cosine(p1, p2)

print(res)

# Result:
0.019419324309079777

# Hamming Distance
# Is the proportion of bits where two bits are difference.
# It's a way to measure distance for binary sequences.

# Example
# Find the hamming distance between given points:

from scipy.spatial.distance import hamming

p1 = (True, False, True)
p2 = (False, True, True)

res = hamming(p1, p2)

print(res)

# Result:
0.666666666667

# Test Yourself With Exercises
# Exercise:
# Consider this image:


# Which method is most likely to be used to find the smallest polygon that covers all of the given points?

# The ConvexHull () method

#%%

# https://www.w3schools.com/python/scipy/scipy_matlab_arrays.php

"""
SciPy Matlab Arrays

Working With Matlab Arrays
We know that NumPy provides us with methods to persist the data in readable formats for Python. But SciPy provides us with interoperability with Matlab as well.
SciPy provides us with the module scipy.io, which has functions for working with Matlab arrays.

Exporting Data in Matlab Format
The savemat() function allows us to export data in Matlab format.
The method takes the following parameters:
filename - the file name for saving data.
mdict - a dictionary containing the data.
do_compression - a boolean value that specifies whether to compress the result or not. Default False.
"""

# Example
# Export the following array as variable name "vec" to a mat file:

from scipy import io
import numpy as np

arr = np.arange(10)

io.savemat('arr.mat', {"vec": arr})

# Note: The example above saves a file name "arr.mat" on your computer.
# To open the file, check out the "Import Data from Matlab Format" example below:

# Import Data from Matlab Format
# The loadmat() function allows us to import data from a Matlab file.
# The function takes one required parameter:
# filename - the file name of the saved data.
# It will return a structured array whose keys are the variable names, and the corresponding values are the variable values.

# Example
# Import the array from following mat file.:

from scipy import io
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])

# Export:
io.savemat('arr.mat', {"vec": arr})

# Import:
mydata = io.loadmat('arr.mat')

print(mydata)

# Result:
{
   '__header__': b'MATLAB 5.0 MAT-file Platform: nt, Created on: Tue Sep 22 13:12:32 2020',
   '__version__': '1.0',
   '__globals__': [],
   'vec': array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
 }

# Use the variable name "vec" to display only the array from the matlab data:
# Example
...

print(mydata['vec'])

# Result:
[[0 1 2 3 4 5 6 7 8 9]]

# Note: We can see that the array originally was 1D, but on extraction it has increased one dimension.
# In order to resolve this we can pass an additional argument squeeze_me=True:

# Example
# Import:

mydata = io.loadmat('arr.mat', squeeze_me=True)

print(mydata['vec'])

# Result:
[0 1 2 3 4 5 6 7 8 9]

# Test Yourself With Exercises
# Exercise:
# Insert the missing method to export data in Matlab format:

from scipy import io
import numpy as np

arr = np.arange(10)

io.savemat('arr.mat', {"vec": arr})

#%%

# https://www.w3schools.com/python/scipy/scipy_interpolation.php

"""
SciPy Interpolation

What is Interpolation?
Interpolation is a method for generating points between given points.
For example: for points 1 and 2, we may interpolate and find points 1.33 and 1.66.
Interpolation has many usage, in Machine Learning we often deal with missing data in a dataset, interpolation is often used to substitute those values.
This method of filling values is called imputation.
Apart from imputation, interpolation is often used where we need to smooth the discrete points in a dataset.

How to Implement it in SciPy?

SciPy provides us with a module called scipy.interpolate which has many functions to deal with interpolation:

1D Interpolation
The function interp1d() is used to interpolate a distribution with 1 variable.
It takes x and y points and returns a callable function that can be called with new x and returns corresponding y.
"""

# Example
# For given xs and ys interpolate values from 2.1, 2.2... to 2.9:

from scipy.interpolate import interp1d
import numpy as np

xs = np.arange(10)
ys = 2*xs + 1

interp_func = interp1d(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)

# Result:
 [5.2  5.4  5.6  5.8  6.   6.2  6.4  6.6  6.8]

# Note: that new xs should be in same range as of the old xs, meaning that we cant call interp_func() with values higher than 10, or less than 0.

# Spline Interpolation
# In 1D interpolation the points are fitted for a single curve whereas in Spline interpolation the points are fitted against a piecewise function defined with polynomials called splines.
# The UnivariateSpline() function takes xs and ys and produce a callable funciton that can be called with new xs.
# Piecewise function: A function that has different definition for different ranges.

# Example
# Find univariate spline interpolation for 2.1, 2.2... 2.9 for the following non linear points:

from scipy.interpolate import UnivariateSpline
import numpy as np

xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1

interp_func = UnivariateSpline(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)

# Result:
 [5.62826474 6.03987348 6.47131994 6.92265019 7.3939103  7.88514634
   8.39640439 8.92773053 9.47917082]

# Interpolation with Radial Basis Function
# Radial basis function is a function that is defined corresponding to a fixed reference point.
# The Rbf() function also takes xs and ys as arguments and produces a callable function that can be called with new xs.

# Example
# Interpolate following xs and ys using rbf and find values for 2.1, 2.2 ... 2.9:

from scipy.interpolate import Rbf
import numpy as np

xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1

interp_func = Rbf(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)

# Result:
 [6.25748981  6.62190817  7.00310702  7.40121814  7.8161443   8.24773402
   8.69590519  9.16070828  9.64233874]

# Test Yourself With Exercises
# Exercise:
# Insert the missing method to find the univariate spline interpolation:

from scipy.interpolate import UnivariateSpline
import numpy as np

xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1

interp_func = UnivariateSpline(xs, ys)

#%%

# https://www.w3schools.com/python/scipy/scipy_statistical_significance_tests.php

"""
SciPy Statistical Significance Tests

What is Statistical Significance Test?
In statistics, statistical significance means that the result that was produced has a reason behind it, it was not produced randomly, or by chance.
SciPy provides us with a module called scipy.stats, which has functions for performing statistical significance tests.
Here are some techniques and keywords that are important when performing such tests:

Hypothesis in Statistics
Hypothesis is an assumption about a parameter in population.

Null Hypothesis
It assumes that the observation is not statistically significant.

Alternate Hypothesis
It assumes that the observations are due to some reason.
Its alternate to Null Hypothesis.

Example:
For an assessment of a student we would take:

"student is worse than average" - as a null hypothesis, and:
"student is better than average" - as an alternate hypothesis.

One tailed test
When our hypothesis is testing for one side of the value only, it is called "one tailed test".

Example:
For the null hypothesis:

"the mean is equal to k", we can have alternate hypothesis:
"the mean is less than k", or:
"the mean is greater than k"

Two tailed test
When our hypothesis is testing for both side of the values.

Example:
For the null hypothesis:

"the mean is equal to k", we can have alternate hypothesis:
"the mean is not equal to k"

In this case the mean is less than, or greater than k, and both sides are to be checked.

Alpha value
Alpha value is the level of significance.

Example:
How close to extremes the data must be for null hypothesis to be rejected.
It is usually taken as 0.01, 0.05, or 0.1.

P value
P value tells how close to extreme the data actually is.
P value and alpha values are compared to establish the statistical significance.
If p value <= alpha we reject the null hypothesis and say that the data is statistically significant. otherwise we accept the null hypothesis.

T-Test
T-tests are used to determine if there is significant deference between means of two variables. and lets us know if they belong to the same distribution.
It is a two tailed test.
The function ttest_ind() takes two samples of same size and produces a tuple of t-statistic and p-value.
"""

# Example
# Find if the given values v1 and v2 are from same distribution:

import numpy as np
from scipy.stats import ttest_ind

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

res = ttest_ind(v1, v2)

print(res)

# Result:
Ttest_indResult(statistic=0.40833510339674095, pvalue=0.68346891833752133)

# If you want to return only the p-value, use the pvalue property:

# Example
...
res = ttest_ind(v1, v2).pvalue

print(res)

# Result:
0.68346891833752133

"""
KS-Test
KS test is used to check if given values follow a distribution.
The function takes the value to be tested, and the CDF as two parameters.
A CDF can be either a string or a callable function that returns the probability.
It can be used as a one tailed or two tailed test.
By default it is two tailed. We can pass parameter alternative as a string of one of two-sided, less, or greater.
"""

# Example
# Find if the given value follows the normal distribution:

import numpy as np
from scipy.stats import kstest

v = np.random.normal(size=100)

res = kstest(v, 'norm')

print(res)

# Result:
KstestResult(statistic=0.047798701221956841, pvalue=0.97630967161777515)

"""
Statistical Description of Data
In order to see a summary of values in an array, we can use the describe() function.
It returns the following description:
1. number of observations (nobs)
2. minimum and maximum values = minmax
3. mean
4. variance
5. skewness
6. kurtosis

"""

# Example
# Show statistical description of the values in an array:

import numpy as np
from scipy.stats import describe

v = np.random.normal(size=100)
res = describe(v)

print(res)

# Result:
DescribeResult(
    nobs=100,
    minmax=(-2.0991855456740121, 2.1304142707414964),
    mean=0.11503747689121079,
    variance=0.99418092655064605,
    skewness=0.013953400984243667,
    kurtosis=-0.671060517912661
  )

"""
Normality Tests (Skewness and Kurtosis)
Normality tests are based on the skewness and kurtosis.
The normaltest() function returns p value for the null hypothesis:
"x comes from a normal distribution".

Skewness:
A measure of symmetry in data.
For normal distributions it is 0.
If it is negative, it means the data is skewed left.
If it is positive it means the data is skewed right.

Kurtosis:
A measure of whether the data is heavy or lightly tailed to a normal distribution.
Positive kurtosis means heavy tailed.
Negative kurtosis means lightly tailed.
"""

# Example
# Find skewness and kurtosis of values in an array:

import numpy as np
from scipy.stats import skew, kurtosis

v = np.random.normal(size=100)

print(skew(v))
print(kurtosis(v))

# Result:
0.11168446328610283
-0.1879320563260931

# Example
# Find if the data comes from a normal distribution:

import numpy as np
from scipy.stats import normaltest

v = np.random.normal(size=100)

print(normaltest(v))

# Result:
NormaltestResult(statistic=4.4783745697002848, pvalue=0.10654505998635538)

# Test Yourself With Exercises
# Exercise:
# Insert the missing method to meassure the summetry in data:

import numpy as np
from scipy.stats import skew, kurtosis

v = np.random.normal(size=100)

print(skew(v))

# output - -0.04162060230341259
# it is negative, so skew to the left

# The end