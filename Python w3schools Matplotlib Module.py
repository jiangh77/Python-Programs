# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 18:45:58 2022

@author: jiang
"""

# Python w3schools Matplotlib Module

# https://www.w3schools.com/python/matplotlib_intro.asp

"""
Matplotlib Tutorial

What is Matplotlib?
Matplotlib is a low level graph plotting library in python that serves as a visualization utility.
Matplotlib was created by John D. Hunter.
Matplotlib is open source and we can use it freely.
Matplotlib is mostly written in python, a few segments are written in C, Objective-C and Javascript for Platform compatibility.

Where is the Matplotlib Codebase?
The source code for Matplotlib is located at this github repository https://github.com/matplotlib/matplotlib
"""

#%%

# https://www.w3schools.com/python/matplotlib_getting_started.asp

"""
Matplotlib Getting Started

Installation of Matplotlib
If you have Python and PIP already installed on a system, then installation of Matplotlib is very easy.
"""

# Install it using this command:

C:\Users\Your Name>pip install matplotlib

# If this command fails, then use a python distribution that already has Matplotlib installed,  like Anaconda, Spyder etc.

# Import Matplotlib

# Once Matplotlib is installed, import it in your applications by adding the import module statement:

import matplotlib

# Now Matplotlib is imported and ready to use:

# Checking Matplotlib Version
# The version string is stored under __version__ attribute.

# Example

import matplotlib

print(matplotlib.__version__)

# output - 3.2.2

# Note: two underscore characters are used in __version__.

#%%

# https://www.w3schools.com/python/matplotlib_pyplot.asp

"""
Matplotlib Pyplot

Pyplot
Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:
import matplotlib.pyplot as plt
Now the Pyplot package can be referred to as plt.
"""

# Example
# Draw a line in a diagram from position (0,0) to position (6,250):

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

# Result:

#%%

# https://www.w3schools.com/python/matplotlib_plotting.asp

"""
Matplotlib Plotting

Plotting x and y points
The plot() function is used to draw points (markers) in a diagram.
By default, the plot() function draws a line from point to point.
The function takes parameters for specifying points in the diagram.
Parameter 1 is an array containing the points on the x-axis.
Parameter 2 is an array containing the points on the y-axis.
If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.
"""

# Example
# Draw a line in a diagram from position (1, 3) to position (8, 10):

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()

# Result:

# The x-axis is the horizontal axis.
# The y-axis is the vertical axis.

# Plotting Without Line
# To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.

# Example
# Draw two points in the diagram, one at position (1, 3) and one in position (8, 10):

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()

# Result:

# You will learn more about markers in the next chapter.

# Multiple Points
# You can plot as many points as you like, just make sure you have the same number of points in both axis.

# Example
# Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

# Result:

"""
Default X-Points
If we do not specify the points in the x-axis, they will get the default values 0, 1, 2, 3, (etc. depending on the length of the y-points.
So, if we take the same example as above, and leave out the x-points, the diagram will look like this:
"""

# Example
# Plotting without x-points:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()

# Result:

# The x-points in the example above is [0, 1, 2, 3, 4, 5].

#%%

# https://www.w3schools.com/python/matplotlib_markers.asp

"""
Matplotlib Markers

Markers
You can use the keyword argument marker to emphasize each point with a specified marker:
"""

# Example
# Mark each point with a circle:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()

# Result:

# Example
# Mark each point with a star:
...
plt.plot(ypoints, marker = '*')
...

# Result:

"""
Format Strings fmt
You can use also use the shortcut string notation parameter to specify the marker.
This parameter is also called fmt, and is written with this syntax:
marker|line|color
"""

# Example
# Mark each point with a circle:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()

# Result:

# The marker value can be anything from the Marker Reference above.
# The line value can be one of the following:

# Line Reference

# Note: If you leave out the line value in the fmt parameter, no line will be plotted.
# The short color value can be one of the following:

# Color Reference

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, '*-b')
plt.show()

# Marker Size
# You can use the keyword argument markersize or the shorter version, ms to set the size of the markers:

# Example
# Set the size of the markers to 20:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

# Result:

# Marker Color
# You can use the keyword argument markeredgecolor or the shorter mec to set the color of the edge of the markers:

# Example
# Set the EDGE color to red:

# ms = Marker Size, mec = Marker Edge Color, mfc = Marker Face Color

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()

# Result:

# You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers:

# Example
# Set the FACE color to red:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()

# Result:

# Use both the mec and mfc arguments to color of the entire marker:

# Example
# Set the color of both the edge and the face to red:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
plt.show()

# Result:

# You can also use Hexadecimal color values:

# Example
# Mark each point with a beautiful green color:
...
plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
...

# Result:

# Or any of the 140 supported color names.

# Example
# Mark each point with the color named "hotpink":
...
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
...
# Result:

# Example
# marker = '*', ms = 10, mec = 'b', mfc = 'r'

#%%

# https://www.w3schools.com/python/matplotlib_line.asp

"""
Matplotlib Line
Linestyle
You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line:
"""

# Example
# Use a dotted line:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()

# Result:

# Example
# Use a dashed line:

plt.plot(ypoints, linestyle = 'dashed')

# Result:

"""
Shorter Syntax

The line style can be written in a shorter syntax:
linestyle can be written as ls.
dotted can be written as :.
dashed can be written as --.
"""
# Example
# Shorter syntax:

plt.plot(ypoints, ls = ':')

# Result:

# Line Styles
# You can choose any of these styles:

# Line Color
# You can use the keyword argument color or the shorter c to set the color of the line:

# Example
# Set the line color to red:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'r')
plt.show()

# Result:

# You can also use Hexadecimal color values:

# Example
# Plot with a beautiful green line:
...
plt.plot(ypoints, c = '#4CAF50')
...

# Result:

# Or any of the 140 supported color names.

# Example
# Plot with the color named "hotpink":
...
plt.plot(ypoints, c = 'hotpink')
...

# Result:

# Line Width
# You can use the keyword argument linewidth or the shorter lw to change the width of the line.
# The value is a floating number, in points:

# Example
# Plot with a 20.5pt wide line:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20.5')
plt.show()

# Result:

# linestyle = ls
# dotted = ':'
# dashed = '--'
# color = c
    
# Multiple Lines
# You can plot as many lines as you like by simply adding more plt.plot() functions:

# Example
# Draw two lines by specifying a plt.plot() function for each line:

import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()

# Result:

# You can also plot many lines by adding the points for the x- and y-axis for each line in the same plt.plot() function.
# (In the examples above we only specified the points on the y-axis, meaning that the points on # the x-axis got the the default values (0, 1, 2, 3).)
# The x- and y- values come in pairs:

# Example
# Draw two lines by specifiyng the x- and y-point values for both lines:

import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()

# Result:

#%%

# https://www.w3schools.com/python/matplotlib_labels.asp

"""
Matplotlib Labels and Title

Create Labels for a Plot
With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.
"""

# Example
# Add labels to the x- and y-axis:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()

# Result:

# Create a Title for a Plot
# With Pyplot, you can use the title() function to set a title for the plot.

# Example
# Add a plot title and labels for the x- and y-axis:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()

# Result:

# Set Font Properties for Title and Labels
# You can use the fontdict parameter in xlabel(), ylabel(), and title() to set font properties for the title and labels.

# Example
# Set font properties for the title and labels:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x, y)
plt.show()

# Result:

# Position the Title
# You can use the loc parameter in title() to position the title.
# Legal values are: 'left', 'right', and 'center'. Default value is 'center'.

# Example
# Position the title to the left:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data", loc = 'left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.show()

# Result:

#%%

# https://www.w3schools.com/python/matplotlib_grid.asp

"""
Matplotlib Adding Grid Lines

Add Grid Lines to a Plot
With Pyplot, you can use the grid() function to add grid lines to the plot.
"""

# Example
# Add grid lines to the plot:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid()

plt.show()

# Result:

# Specify Which Grid Lines to Display
# You can use the axis parameter in the grid() function to specify which grid lines to display.
# Legal values are: 'x', 'y', and 'both'. Default value is 'both'.

# Example
# Display only grid lines for the x-axis:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'x')

plt.show()

# Result:

# Example
# Display only grid lines for the y-axis:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'y')

plt.show()

# Result:

# Set Line Properties for the Grid
# You can also set the line properties of the grid, like this: grid(color = 'color', linestyle = 'linestyle', linewidth = number).

# Example
# Set the line properties of the grid:

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()

# Result:

# color, linestyle, linewidth
    
#%%

# https://www.w3schools.com/python/matplotlib_subplot.asp

"""
Matplotlib Subplot

Display Multiple Plots
With the subplot() function you can draw multiple plots in one figure:
"""
# Example
# Draw 2 plots:

import matplotlib.pyplot as plt
import numpy as np

# plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

# plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()

# Result:

"""
The subplot() Function

The subplot() function takes three arguments that describes the layout of the figure.
The layout is organized in rows and columns, which are represented by the first and second argument.

The third argument represents the index of the current plot.
"""

plt.subplot(1, 2, 1)
# the figure has 1 row, 2 columns, and this plot is the first plot.

plt.subplot(1, 2, 2)
# the figure has 1 row, 2 columns, and this plot is the second plot.

# So, if we want a figure with 2 rows an 1 column (meaning that the two plots will be displayed on top of each other instead of side-by-side), we can write the syntax like this:

# Example
# Draw 2 plots on top of each other:

import matplotlib.pyplot as plt
import numpy as np

# plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
plt.plot(x,y)

# plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x,y)

plt.show()

# Result:

# You can draw as many plots you like on one figure, just descibe the number of rows, columns, and the index of the plot.

# Example
# Draw 6 plots:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()

# Result:

# Title
# You can add a title to each plot with the title() function:

# Example
# 2 plots, with titles:

import matplotlib.pyplot as plt
import numpy as np

# plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

# plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")

plt.show()

# Result:

# Super Title
# You can add a title to the entire figure with the suptitle() function:

# Example
# Add a title for the entire figure:

import matplotlib.pyplot as plt
import numpy as np

# plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

# plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show()

# Result:

#%%

# https://www.w3schools.com/python/matplotlib_scatter.asp

"""
Matplotlib Scatter

Creating Scatter Plots
With Pyplot, you can use the scatter() function to draw a scatter plot.
The scatter() function plots one dot for each observation. It needs two arrays of the same length, one for the values of the x-axis, and one for values on the y-axis:
"""

# Example
# A simple scatter plot:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()

# Result:

"""
The observation in the example above is the result of 13 cars passing by.
The X-axis shows how old the car is.
The Y-axis shows the speed of the car when it passes.
Are there any relationships between the observations?
It seems that the newer the car, the faster it drives, but that could be a coincidence, after all we only registered 13 cars.
"""

# Example
# Draw two plots on the same figure:

import matplotlib.pyplot as plt
import numpy as np

# day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

# day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()

# Result:

# Note: The two plots are plotted with two different colors, by default blue and orange, you will learn how to change colors later in this chapter.
# By comparing the two plots, I think it is safe to say that they both gives us the same conclusion: the newer the car, the faster it drives.

# Colors
# You can set your own color for each scatter plot with the color or the c argument:

# Example
# Set your own color of the markers:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')

plt.show()

# Result:

# Color Each Dot
# You can even set a specific color for each dot by using an array of colors as value for the c argument:
# Note: You cannot use the color argument for this, only the c argument.

# Example
# Set your own color of the markers:
    
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x, y, c=colors)

plt.show()

# Result:

"""
ColorMap

The Matplotlib module has a number of available colormaps.
A colormap is like a list of colors, where each color has a value that ranges from 0 to 100.
Here is an example of a colormap:

This colormap is called 'viridis' and as you can see it ranges from 0, which is a purple color, and up to 100, which is a yellow color.

How to Use the ColorMap
You can specify the colormap with the keyword argument cmap with the value of the colormap, in this case 'viridis' which is one of the built-in colormaps available in Matplotlib.
In addition you have to create an array with values (from 0 to 100), one value for each of the point in the scatter plot:
"""

# Example
# Create a color array, and specify a colormap in the scatter plot:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.show()

# Result:

# You can include the colormap in the drawing by including the plt.colorbar() statement:

# Example
# Include the actual colormap:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.colorbar()

plt.show()

# Result:

# Available ColorMaps
# You can choose any of the built-in colormaps:

# Size
# You can change the size of the dots with the s argument.
# Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:

# Example
# Set your own size for the markers:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes)

plt.show()

# Result:

# Alpha

# You can adjust the transparency of the dots with the alpha argument.
# Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:

# Example
# Set your own size for the markers:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes, alpha=0.5)

plt.show()

# Result:

# Combine Color Size and Alpha
# You can combine a colormap with different sizes on the dots. This is best visualized if the dots are transparent:

# Example
# Create random arrays with 100 values for x-points, y-points, colors and sizes:

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()

# Result:

# color, c, cmap, plt.colorbar(), s, alpha

#%%

# https://www.w3schools.com/python/matplotlib_bars.asp

"""
Matplotlib Bars

Creating Bars
With Pyplot, you can use the bar() function to draw bar graphs:
"""

# Example
# Draw 4 bars:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

# Result:

# The bar() function takes arguments that describes the layout of the bars.
# The categories and their values represented by the first and second argument as arrays.

# Example

x = ["APPLES", "BANANAS"]
y = [400, 350]
plt.bar(x, y)

# Result:

# Horizontal Bars
# If you want the bars to be displayed horizontally instead of vertically, use the barh() function:

# Example
# Draw 4 horizontal bars:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()

# Result:

# Bar Color
# The bar() and barh() takes the keyword argument color to set the color of the bars:

# Example
# Draw 4 red bars:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red")
plt.show()

# Result:

# Color Names
# You can use any of the 140 supported color names.

# Example
# Draw 4 "hot pink" bars:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "hotpink")
plt.show()

# Result:

# Color Hex
# Or you can use Hexadecimal color values:

# Example
# Draw 4 bars with a beautiful green color:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "#4CAF50")
plt.show()

# Result:

# Bar Width
# The bar() takes the keyword argument width to set the width of the bars:

# Example
# Draw 4 very thin bars:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1)
plt.show()

# Result:

# The default width value is 0.8
# Note: For horizontal bars, use height instead of width.

# Bar Height
# The barh() takes the keyword argument height to set the height of the bars:

# Example
# Draw 4 very thin bars:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y, height = 0.1)
plt.show()

# Result:

# The default height value is 0.8

# bar(), barh(), color, color names, color Hex, width, height

#%%

# https://www.w3schools.com/python/matplotlib_histograms.asp

"""
Matplotlib Histograms

Histogram
A histogram is a graph showing frequency distributions.
It is a graph showing the number of observations within each given interval.
Example: Say you ask for the height of 250 people, you might end up with a histogram like this:
"""

"""
You can read from the histogram that there are approximately:
2 people from 140 to 145cm
5 people from 145 to 150cm
15 people from 151 to 156cm
31 people from 157 to 162cm
46 people from 163 to 168cm
53 people from 168 to 173cm
45 people from 173 to 178cm
28 people from 179 to 184cm
21 people from 185 to 190cm
4 people from 190 to 195cm
"""

"""
Create Histogram

In Matplotlib, we use the hist() function to create histograms.
The hist() function will use an array of numbers to create a histogram, the array is sent into the function as an argument.
For simplicity we use NumPy to randomly generate an array with 250 values, where the values will concentrate around 170, and the standard deviation is 10. Learn more about Normal Data Distribution in our Machine Learning Tutorial.
"""

# Example
# A Normal Data Distribution by NumPy:

import numpy as np

x = np.random.normal(170, 10, 250)

print(x)

# Result:
# This will generate a random result, and could look like this:

"""
output
[174.07895656 164.47979584 173.52370368 172.96748384 171.17830113
 162.66673612 187.25434179 172.66616924 166.16757413 189.7459029
 167.97408048 173.96538816 182.79668409 156.45887619 163.81449393
 165.7905241  184.71943275 170.81264217 185.44847581 171.31999511
 181.44722805 164.04234865 186.97394163 172.03338277 172.5741924
 179.26917448 162.10339644 183.12557746 167.45707661 180.09904993
 174.80106572 179.43021467 166.59511702 163.54061197 174.05964767
 164.66278947 184.5132701  176.9105219  170.06151329 170.3803787
 193.63289871 162.8984176  172.00131222 191.51805839 170.34797031
 177.79395507 173.98904476 173.17593805 179.43589345 172.53449739
 173.45049078 157.18710144 163.91948323 164.57279371 182.86287728
 174.38721398 160.680502   165.0591434  174.63115205 152.05999881
 159.87047938 186.05514301 165.68259037 174.48119137 145.57352218
 155.31913023 158.62554508 169.55079215 172.62946311 169.45494556
 162.08465885 166.91196307 170.10701539 159.97371909 167.59805118
 168.92254565 153.41066907 165.09024726 154.60660004 183.69931238
 167.55199576 175.14734672 153.22647764 160.14629413 166.10767793
 163.17405436 172.53703788 163.08752491 178.02903762 177.22605389
 172.76650558 151.30948297 178.19879147 171.2623022  175.01345256
 177.71597543 164.53286161 173.00658987 163.14778145 176.11800573
 183.08976423 173.93564542 152.97581982 176.88480138 191.15155242
 196.3429236  183.640936   158.73090884 181.47679826 167.16411261
 184.71529644 176.51822706 187.79233472 159.95672614 172.76763544
 179.08919953 154.92487583 172.68780576 170.33757854 165.26766833
 185.70427902 170.64807441 160.9691295  167.96441933 162.03232916
 182.81676942 167.9122352  179.8680989  160.95684697 178.53829732
 163.65111757 183.62434638 165.99974014 183.8996859  171.79950989
 162.06159007 174.00309044 179.78031708 149.79927717 185.8076299
 189.08818851 181.28374275 170.50840041 166.83614237 170.63769175
 178.16344311 172.31911069 166.71513789 164.04070107 171.82056183
 165.0470729  190.96741004 167.57609593 176.50607649 137.37069791
 167.078733   168.06583099 185.08385238 177.46835154 173.67419973
 155.38928683 168.33066884 167.08981403 165.23614334 170.0358243
 175.58436055 166.93312928 177.23060619 170.30623719 156.81500922
 182.96193377 156.24714405 180.36649339 174.49934387 167.04257104
 168.87319702 171.39979429 162.91194897 178.88681163 173.4514929
 154.76873218 156.62896057 173.00145262 161.87957711 169.87990384
 169.9378134  176.47189801 165.05877088 165.70629441 171.72161545
 162.79761208 189.09020483 169.25966333 177.50064805 173.16996422
 174.55221694 172.04898339 161.42096884 174.75127115 190.50621564
 186.14589797 167.77804715 176.81867877 183.611925   178.87931796
 177.72159549 154.00508563 153.63421197 178.12138819 153.3584975
 172.38319411 180.19096311 156.84451272 174.23176565 176.06990939
 174.17989238 157.95101454 180.79909666 189.43025326 176.9752828
 167.15266355 174.96617152 156.99106635 162.27135297 154.98808855
 168.08317514 162.99321931 173.64947152 158.78094663 155.92915216
 190.7351743  180.07446073 165.63064145 166.37422752 175.17359542
 173.6466313  156.5920316  165.37714232 161.93486058 163.54483477
 171.89748555 178.4072202  163.31181909 171.78106103 163.25334059
 157.77673075 165.4464919  181.10691412 165.72422942 166.77493502]
"""

# The hist() function will read the array and produce a histogram:

# Example
# A simple histogram:

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 

# Result:

#%%

# https://www.w3schools.com/python/matplotlib_pie_charts.asp

"""
Matplotlib Pie Charts

Creating Pie Charts
With Pyplot, you can use the pie() function to draw pie charts:
"""

# Example
# A simple pie chart:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show() 

# Result:

# As you can see the pie chart draws one piece (called a wedge) for each value in the array (in this case [35, 25, 25, 15]).
# By default the plotting of the first wedge starts from the x-axis and move counterclockwise:

# Note: The size of each wedge is determined by comparing the value with all the other values, by using this formula:
# The value divided by the sum of all values: x/sum(x)

# Labels
# Add labels to the pie chart with the label parameter.
# The label parameter must be an array with one label for each wedge:

# Example
# A simple pie chart:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 

# Result:

# Start Angle
# As mentioned the default start angle is at the x-axis, but you can change the start angle by specifying a startangle parameter.
# The startangle parameter is defined with an angle in degrees, default angle is 0:

# Example
# Start the first wedge at 90 degrees:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show() 

# Result:

"""
Explode
Maybe you want one of the wedges to stand out? The explode parameter allows you to do that.
The explode parameter, if specified, and not None, must be an array with one value for each wedge.
Each value represents how far from the center each wedge is displayed:
"""

# Example
# Pull the "Apples" wedge 0.2 from the center of the pie:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show() 

# Result:

# Shadow
# Add a shadow to the pie chart by setting the shadows parameter to True:

# Example
# Add a shadow:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show() 

# Result:

# Colors
# You can set the color of each wedge with the colors parameter.
# The colors parameter, if specified, must be an array with one value for each wedge:

# Example
# Specify a new color for each wedge:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show() 

# Result:

"""
You can use Hexadecimal color values, any of the 140 supported color names, or one of these shortcuts:
'r' - Red
'g' - Green
'b' - Blue
'c' - Cyan
'm' - Magenta
'y' - Yellow
'k' - Black
'w' - White
"""

# Legend
# To add a list of explanation for each wedge, use the legend() function:

# Example
# Add a legend:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show() 

# Result:

# Legend With Header
# To add a header to the legend, add the title parameter to the legend function.

# Example
# Add a legend with a header:

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show() 

# Result:

# The end