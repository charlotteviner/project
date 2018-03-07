#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 16:57:26 2017

@author: charlotteviner

Create agents to provide methods for visualising drainage networks.

Build raindrops as agents in a space. Read in environmental data and get
the agents to move downslope. Display the movement of raindrops as an 
animation contained within a GUI. Display plots of the drainage paths 
taken by the raindrops within a GUI. Calculate the total volume of water
that has reached an outlet point and append this to a file.

Args:
    num_of_drops (int) -- Number of raindrops.
    num_of_steps (int) -- Number of iterations.
    radius (float) -- Radius of the raindrops.
    length (int) -- Size of the environment to be used.
    
Returns:
    animation -- Animates the model.
    total_vol (float) -- Total volume of water that has reached an
        outlet point.
    outlet_vol (.csv) -- File containing total volume of water that has 
        reached an outlet point.
    Scatter plot showing all coordinates of the raindrops for all 
        iterations of the model.
    Scatter plot showing coordinates where 3 or more raindrops have 
        moved through.
"""

import csv
import matplotlib.pyplot
import matplotlib.animation
import rainframework
import tkinter
import matplotlib.backends.backend_tkagg


# Read in environment data and append to new list 'land'.
f = open('in.txt', newline = '') 
land = []
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []
    for item in row:
        rowlist.append(item)
    land.append(rowlist)
f.close()


# Set up parameters.
num_of_drops = 100
num_of_steps = 100
radius = 0.3 # Allow user to set the radius of the droplets.

# Set length to determine size of environment to be used.
length = 99
# Do not set to greater than len(land) - 1.
# Allows the program to be used for different environmental datasets.

# Set up list of raindrops as agents.
raindrops = []

# Set up list of all raindrop coordinates for all model iterations.
all_drops = []

# Set up list of elevations in the landscape.
elevs = []

# Set up list of coordinates making up the landscape.
coords = []

# Set up list of coordinates with minimum elevation in the landscape.
min_coords = []


# Append all elevation values to a list.
# Ranges are 0 - 100 as this is the range which will be plotted.
for i in range(0, length + 1):
    for j in range(0, length + 1):
        elevs.append(land[i][j])
          
min_elev = min(elevs) # Find the minimum elevation in the 'elevs' list.

# Append coordinates associated with each elevation value to a list.
# Ranges are 0 - 100 as this is the range which will be plotted.
for j in range(0, length + 1):
    for i in range(0, length + 1):
        coords.append((i, j))

    
# Find the coordinates associated with the minimum elevation.
# Append these coordinates to 'min_coords' list.
# The following code is altered from that at:
# https://stackoverflow.com/questions/3873361/   
for position, item in enumerate(elevs):
    if item <= min_elev:
        min_coords.append(coords[position])



# Set up the figure for later use in the animation.
fig = matplotlib.pyplot.figure(figsize = (7, 7))
ax = fig.add_axes([0, 0, 1, 1])



# Append coordinates of the raindrops to the 'raindrops' list.
for i in range(num_of_drops):
    y = 0
    x = 0
    raindrops.append(rainframework.Rain(land, raindrops, all_drops, length, 
                                        x, y))



def plot_init():
    """
    Set-up the plot figure.
    
    Set-up the plot figure by providing the limits for the x-axis and
    y-axis, and displaying the environment data in the plot.
    """
    
    matplotlib.pyplot.ylim(0, length) # Set limit of y axis.
    matplotlib.pyplot.xlim(0, length) # Set limit of x axis.
    matplotlib.pyplot.imshow(land) # Display environment in plot.


  
carry_on = True   


def update(frame_number):
    """
    Move raindrops and create frames for use in animation.
    
    Move the raindrops downslope in the environment. Provide a stopping
    condition for the model. Create frames for use in the animation.
    
    Args:
        frame_number (int) -- Number of each frame generated.
        
    Returns:
        Scatter plot of raindrops in the environment for each iteration.
    """
    
    fig.clear()
    global carry_on
    
    for agent in raindrops:
        agent.move() # Move the raindrops downslope.

    # Create stopping condition.
    stop = all(land[agent.x][agent.y] == min_elev for agent in raindrops)
    
    # Model stops running if all raindrops reach a minimum elevation.
    if stop is True:
        carry_on = False
        print("All raindrops have reached a point of minimum elevation.")
    
 
    plot_init() # Set up plot.
    
    # Plot points of minimum elevation in the colour black.
    matplotlib.pyplot.scatter(*zip(*min_coords), color = 'black')


    for agent in raindrops:
        # Plot all agents on a scatter graph in the colour blue.
        matplotlib.pyplot.scatter(agent.y, agent.x, color = 'blue')



def gen_function(b = [0]):
    """
    Stop creating frames when stopping condition is met.
    
    Generator function that determines when frames should stop being 
    created by checking whether the maximum number of iterations and/or 
    the stopping condition has been met.
    """
    
    a = 0
    global carry_on
    while (a < num_of_steps) & (carry_on):
        yield a # Return control and wait next call.
        a = a + 1
    
    if carry_on == True:
        print("Not all raindrops were able to reach a point of minimum \
elevation. Stagnant or oscillating raindrops have reached a sink in the \
landscape.")
        
    print("End of model run.")



def run():
    """
    Run the animation.
    
    Run the animation, using the generator function to determine the 
    number of frames. Provide enable/disable condition for menu options 
    in the GUI.
    
    Returns:
        animation -- Animates the model.
    """
    
    animation = matplotlib.animation.FuncAnimation(fig, update, repeat = False,
                                                   frames = gen_function)
    # Number of frames in animation determined by generator function.
    
    canvas.show() # Show animation in matplotlib canvas.
    
    # Provide conditions for enabling/disabling menu options in the GUI.
    # The following code is altered from that at:
    # http://code.activestate.com/lists/python-tkinter-discuss/204/
    if model_menu.entrycget(0, "state") == "normal":
        model_menu.entryconfig("Calculate...", state = "disabled")
        model_menu.entryconfig("Run model", state = "normal")
        model_menu.entryconfig("Drainage network", state = "disabled")
    else:
        model_menu.entryconfig("Calculate...", state = "normal")
        model_menu.entryconfig("Run model", state = "disabled")
        model_menu.entryconfig("Drainage network", state = "normal")
     


def volume():
    """
    Calculate volume of water that has reached an outlet point.
    
    Calculate the number of raindrops and total volume of water that has 
    reached an outlet point in cm**3. Append this total, the number of 
    raindrops contributing to this total, the total number of raindrops 
    used in the model run, and the radius of the raindrops to a .csv 
    file.
    
    Returns:
        total_vol (float) -- Total volume of water that has reached an 
            outlet point.
        outlet_vol (.csv) -- File containing calculated total and
            parameters.
    """
    
    outlet = [] # Make empty list.
    
    for agent in raindrops:
        for i in range(len(min_coords)):
            # Find raindrops with same coordinates as minimum elevation.
            if agent.y == min_coords[i][0] and agent.x == min_coords[i][1]:
                # Append these coordinates to a list.
                outlet.append(agent)
    
    # Calculate volume of water that has reached a minimum elevation.
    total_vol = (4/3) * 3.14159 * (radius**3) * len(outlet)
    # Assumes all the raindrops are spherical with equal radii.
    
    vol = "%.2f" % total_vol # Total volume to 2 d.p.
    
    print("Volume of water that reached an outlet = " + str(vol) + " cm^3")
    
    # Append total volume and parameters to file 'outlet_vol.csv'.
    with open('outlet_vol.csv', 'a') as f1:
        f1.write(str(total_vol) + "," + str(len(outlet)) + "," + 
                 str(num_of_drops) + "," + str(radius) + "\n")



def all_network():
    """
    Plot all coordinates of the raindrops to visualise the whole 
    drainage network produced in the model run.
    
    Returns:
        Scatter plot showing all coordinates of the raindrops across all 
            iterations of the model.
    """
    
    plot_init() # Set up plot.

    # Plot all raindrop coordinates across all iterations in red.    
    matplotlib.pyplot.scatter(*zip(*all_drops), color = 'red')
    matplotlib.pyplot.show()
    
    
    
def common_network():
    """
    Plot coordinates where 3 or more raindrops have moved through.
    
    Returns:
        Scatter plot showing coordinates on the landscape where 3 or
            more raindrops have moved through.
    """
    
    # Find coordinates that 3 or more raindrops have moved through.
    # Create list of these coordinates.
    # The following code is altered from that at:
    # https://stackoverflow.com/questions/9835762/
    duplicates = set([x for x in all_drops if all_drops.count(x) >= 3])
    
    plot_init() # Set up plot.
    
    matplotlib.pyplot.scatter(*zip(*duplicates), color = 'yellow')
    matplotlib.pyplot.show()
    
    
   
# Create GUI. 
# GUI created with help from the code found at:
# http://code.activestate.com/lists/python-tkinter-discuss/204/  
 
root = tkinter.Tk() # Build the main GUI window.

root.wm_title("Project") # Set the main window title.

# Create a matplotlib canvas embedded within the GUI window.
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master = 
                                                             root)
canvas._tkcanvas.pack(side = tkinter.TOP, fill = tkinter.BOTH, expand = 1)

# Create a menu.
menu_bar = tkinter.Menu(root)

root.config(menu = menu_bar)

model_menu = tkinter.Menu(menu_bar)

# Create sub-menus.
sub_menu = tkinter.Menu(model_menu)

sub_menu_2 = tkinter.Menu(model_menu)

menu_bar.add_cascade(label = "Project", menu = model_menu)

# Provide user with the option to calculate parameters.
model_menu.add_cascade(label = "Calculate...", menu = sub_menu, state = 
                       "disabled")

# Provide user with the option to calculate the total water volume.
sub_menu.add_command(label = "Water volume", command = volume)

# Provide user with the option to view drainage networks.
model_menu.add_cascade(label = "Drainage network", menu = sub_menu_2, state = 
                       "disabled")

# Provide user with the option to show the whole drainage network.
sub_menu_2.add_command(label = "Show whole network", command = all_network)

# Provide user with the option to show the common drainage network.
sub_menu_2.add_command(label = "Show common network", command = common_network)

# Provide user with the option to run the model.
model_menu.add_command(label = "Run model", command = run)

# Provide user with the option to exit the program.
model_menu.add_command(label = "Exit", command = root.quit)
  
tkinter.mainloop() # Set the GUI to wait for events.
