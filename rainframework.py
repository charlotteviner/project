#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 10:52:22 2017

@author: charlotteviner
"""

import random


class Rain():
    """
    Set up and provide methods for raindrops as agents.
    
    Set up raindrop coordinates and provide methods to allow the 
    raindrops to interact with the landscape. Implement property 
    attributes for the x and y coordinates.
    
    __init__ -- Set up agent coordinates.
    getx -- Get the x-coordinate of an agent.
    setx -- Set the x-coordinate of an agent.
    gety -- Get the y-coordinate of an agent.
    sety -- Set the y-coordinate of an agent.
    move -- Move the agents downslope.
    """
    
    def __init__(self, land, raindrops, all_drops, length, x, y):
        """
        Set up agent coordinates.
        
        Set up coordinates for the raindrops and create a boundary 
        condition to stop the rain from flowing out of the environment.
        
        Args:
            land (list) -- Environment coordinate list.
            raindrops (list) -- Agent coordinate list.
            all_drops (list) -- List of all raindrop coordinates across 
                all iterations of the model.
            length (int) -- Size of the environment to be used.
            y (int) -- Agent y-coordinate.
            x (int) -- Agent x-coordinate.
        """
        
        # Allow raindrops to access the size of the environment.
        self.length = length
        
        # Set up y-coordinate to be a random integer 0 - 99.
        self._y = random.randint(0, length)
        
        # Set up x-coordinate to be a random integer 0 - 99.
        self._x = random.randint(0, length)
        
        # Create a boundary condition for the rain, so it can't flow out
        # of the environment.
        if self._y < 0:
            self._y = 0
            
        if self._y > length:
            self._y = length
            
        if self._x < 0:
            self._x = 0
            
        if self._x > length:
            self._x = length
        
        # Allow raindrops to access the land data.
        self.land = land
        
        # Allow raindrops to access other raindrop data.
        self.raindrops = raindrops
        
        # Allow raindrops to access all raindrops data.
        self.all_drops = all_drops

        
    # Implement a property attribute for x.
    
    def getx(self):
        """
        Get the x-coordinate of an agent.
        
        Returns:
            The x-coordinate of an agent.
        """
        
        return self._x
    
    
    def setx(self, value):
        """
        Set the x-coordinate of an agent.
        
        Args:
            value -- An integer.
        """
        
        self._x = value
    

    # Define the property of x.    
    x = property(getx, setx)
    
    
    # Implement a property attribute for y.
    
    def gety(self):
        """
        Get the y-coordinate of an agent.
        
        Returns:
            The y-coordinate of an agent.
        """
        
        return self._y
    
    
    def sety(self, value):
        """
        Set the y-coordinate of an agent.
        
        Args:
            value -- An integer.
        """
        
        self._y = value
        
        
    # Define the property of y.    
    y = property(gety, sety)
    

    
    def move(self):
        """
        Move the raindrops downslope.
        
        Move the raindrops downslope by assessing the lowest elevation 
        surrounding the current position of a raindrop and moving the
        raindrop to this position.

        Returns:
            neighbours (list) -- List of neighbouring coordinates.
            heights (list) -- List of neighbouring elevations.
            y (int) -- New y-coordinate.
            x (int) -- New x-coordinate.
        """
        
        # Multiple 'if' statements are required to resolve issues with
        # index ranges.
        
        if 1 <= self._x <= (self.length - 1) and \
        1 <= self._y <= (self.length - 1):
        # Condition for coordinates from (1, 1) to (98, 98).
            
            # Find coordinates of the 8 neighbouring pixels.
            neighbours = [(self._x - 1, self._y - 1), (self._x - 1, self._y), \
                          (self._x - 1, self._y + 1), (self._x, self._y - 1), \
                          (self._x, self._y + 1), (self._x + 1, self._y - 1), \
                          (self._x + 1, self._y), (self._x + 1, self._y + 1)]
        
            # Find the elevation data of the 8 neighbouring pixels.
            heights = [self.land[self._x - 1][self._y - 1], \
                       self.land[self._x - 1][self._y], \
                       self.land[self._x - 1][self._y + 1], \
                       self.land[self._x][self._y - 1], \
                       self.land[self._x][self._y + 1], \
                       self.land[self._x + 1][self._y - 1], \
                       self.land[self._x + 1][self._y], \
                       self.land[self._x + 1][self._y + 1]]
        
        
        elif self._x == 0 and 1 <= self._y <= (self.length - 1):
        # Condition for coordinates sitting on the x-axis boundary.
            
            # Find coordinates of the 5 neighbouring pixels.
            neighbours = [(self._x, self._y - 1), (self._x, self._y + 1), \
                          (self._x + 1, self._y - 1), (self._x + 1, self._y), \
                          (self._x + 1, self._y + 1)]
        
            # Find the elevation data of the 5 neighbouring pixels.
            heights = [self.land[self._x][self._y - 1], \
                       self.land[self._x][self._y + 1], \
                       self.land[self._x + 1][self._y - 1], \
                       self.land[self._x + 1][self._y], \
                       self.land[self._x + 1][self._y + 1]]
         
            
        elif self._x == self.length and 1 <= self._y <= (self.length - 1):
        # Condition for coordinates sitting on the boundary line x = 99.
            
            # Find coordinates of the 5 neighbouring pixels.            
            neighbours = [(self._x - 1, self._y - 1), (self._x - 1, self._y), \
                          (self._x - 1, self._y + 1), (self._x, self._y - 1), \
                          (self._x, self._y + 1)]
        
            # Find the elevation data of the 5 neighbouring pixels.
            heights = [self.land[self._x - 1][self._y - 1], \
                       self.land[self._x - 1][self._y], \
                       self.land[self._x - 1][self._y + 1], \
                       self.land[self._x][self._y - 1], \
                       self.land[self._x][self._y + 1]]
         
            
        elif 1 <= self._x <= (self.length - 1) and self._y == 0:
        # Condition for coordinates sitting on the y-axis boundary.

            # Find coordinates of the 5 neighbouring pixels.             
            neighbours = [(self._x - 1, self._y), (self._x - 1, self._y + 1), \
                          (self._x, self._y + 1), (self._x + 1, self._y), \
                          (self._x + 1, self._y + 1)]
        
            # Find the elevation data of the 5 neighbouring pixels.
            heights = [self.land[self._x - 1][self._y], \
                       self.land[self._x - 1][self._y + 1], \
                       self.land[self._x][self._y + 1], \
                       self.land[self._x + 1][self._y], \
                       self.land[self._x + 1][self._y + 1]]
        
        
        elif 1 <= self._x <= (self.length - 1) and self._y == self.length:
        # Condition for coordinates sitting on the boundary line y = 99.    
        
            # Find coordinates of the 5 neighbouring pixels.            
            neighbours = [(self._x - 1, self._y - 1), (self._x - 1, self._y), \
                          (self._x, self._y - 1), (self._x + 1, self._y - 1), \
                          (self._x + 1, self._y)]
        
            # Find the elevation data of the 5 neighbouring pixels.
            heights = [self.land[self._x - 1][self._y - 1], \
                       self.land[self._x - 1][self._y], \
                       self.land[self._x][self._y - 1], \
                       self.land[self._x + 1][self._y - 1], \
                       self.land[self._x + 1][self._y]]
         
            
        elif self._x == 0 and self._y == 0:
        # Condition for coordinate (0, 0).

            # Find coordinates of the 3 neighbouring pixels.            
            neighbours = [(self._x, self._y + 1), (self._x + 1, self._y), \
                          (self._x + 1, self._y + 1)]
        
            # Find the elevation data of the 3 neighbouring pixels.
            heights = [self.land[self._x][self._y + 1], \
                       self.land[self._x + 1][self._y], \
                       self.land[self._x + 1][self._y + 1]]
         
            
        elif self._x == 0 and self._y == self.length:
        # Condition for coordinate (0, 99).

            # Find coordinates of the 3 neighbouring pixels.
            neighbours = [(self._x, self._y - 1), (self._x + 1, self._y - 1), \
                          (self._x + 1, self._y)]
        
            # Find the elevation data of the 3 neighbouring pixels.
            heights = [self.land[self._x][self._y - 1], \
                       self.land[self._x + 1][self._y - 1], \
                       self.land[self._x + 1][self._y]]
         
            
        elif self._x == self.length and self._y == 0:
        # Condition for coordinate (99, 0).

            # Find coordinates of the 3 neighbouring pixels.            
            neighbours = [(self._x - 1, self._y), (self._x - 1, self._y + 1), \
                          (self._x, self._y + 1)]
        
            # Find the elevation data of the 3 neighbouring pixels.
            heights = [self.land[self._x - 1][self._y], \
                       self.land[self._x - 1][self._y + 1], \
                       self.land[self._x][self._y + 1]]
          
            
        elif self._x == self.length and self._y == self.length:
        # Condition for coordinate (99, 99).

            # Find coordinates of the 3 neighbouring pixels.            
            neighbours = [(self._x - 1, self._y - 1), (self._x - 1, self._y), 
                          (self._x, self._y - 1)]
        
            # Find the elevation data of the 3 neighbouring pixels.
            heights = [self.land[self._x - 1][self._y - 1], \
                       self.land[self._x - 1][self._y], \
                       self.land[self._x][self._y - 1]]

        
        # The following code is altered from that at:
        # https://stackoverflow.com/questions/364621/
        # Get position of the minimum elevation of the neighbouring 
        # coordinates.
        for position, item in enumerate(heights):
            if item == min(heights):
                min_neighbour = neighbours[position]


        # If a neighbouring coordinate has a lower elevation:       
        if self.land[self._x][self._y] >= min(heights):
            # Move agent to position of the neighbour.
            self._x = min_neighbour[0]
            self._y = min_neighbour[1]
            # Append the new coordinate to list 'all_drops'.
            self.all_drops.append((min_neighbour[1], min_neighbour[0]))      
        else:
            pass # Else, do nothing. 