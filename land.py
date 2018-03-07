#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 17:37:12 2017

@author: charlotteviner

Credit: Code written by Andrew Evans.

Create elevation data for use in the project.

Provided for background on how the artificial environment 'land' was 
created.

Returns:
    land (list) -- List containing land elevation data.
    land (.txt) -- File containing data for the land elevation.
"""

import matplotlib
import csv


w = 100 # Set width to 100.
h = 100 # Set height to 100.


land = [] # Create empty list called 'land'.


# Plot a 100 x 100 square.
for y in range(0, h): # Cycle through coordinates (0, h) until h = 100.
    row = [] # Create empty list called 'row'.
    for x in range(0, w):
        row.append(0) # Append 0 to 'row' at (0, w) until w = 100.
    land.append(row) # Append each row created to the 'land' list.


# Add relief to the 100 x 100 square.
for y in range(0, h): # Cycle through coordinates (0, h) until h = 100.
    for x in range(0, w): # Cycle through (0, w) until w = 100.
        if (x + y) < w:
            # If (x + y) < w, then the coordinate will = x + y.
            land[y][x] = x + y
        else :
            # If not, the coordinate will = (w - x) + (h - y).
            land[y][x] = (w - x) + (h - y)


# Plot 'land' on a graph.
matplotlib.pyplot.ylim(0, h) # Limit of y axis.
matplotlib.pyplot.xlim(0, w) # Limit of x axis.
matplotlib.pyplot.imshow(land)


print(land)


# Create a new file 'land.txt' which contains the coordinate data.
f = open('land.txt', 'w', newline='') 
writer = csv.writer(f, delimiter=',')
for row in land:		
	writer.writerow(row)
f.close()
