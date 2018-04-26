# project

## Core Skills: Individual Project

For my individual project, I built a program, in Python, that models rainfall in a landscape. The model is designed to:
* randomly create raindrops as agents in the landscape;
* move them downslope, and;
* trace the paths of the raindrops to allow visualisation of the drainage network in the environment.

The program also provides the user with the option to calculate the total volume of water that reaches an outlet point in the landscape.

### Ongoing Issues with the Code

Some of the menu items in the GUI have been programmed to be disabled before the model is run, and then are subsequently enabled once it is run. However, the way this has been coded only appears to work on Mac computers and not Windows. The reason for this issue is unknown and has not yet been resolved.

### Future Development

Possible future development for the model could include the calculation of the volume of water at *each* outlet point (if more than one exists on the landscape). This development was attempted but unfortunately the model only, currently, calculates the total volume of water across *all* outlet points.

The model could also potentially be programmed to delineate watersheds and calculate the drainage area. This would be useful for more quantitative analysis of river environments.
