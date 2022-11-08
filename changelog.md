# 0.0.10
- Migrated to Python 3.11
- Fixed type annotations for some arguments
- Fixed purple color
- Added more colors
- Added a new method to the OrientedPoint class that transforms an instance to a homogeneous transformation matrix and viceversa
- Changed linewidth argument to just width
- Changed the add_point representation from scatter to plot
- Changed repr for some classes

# 0.0.9
- Fixed matplotlib version to 3.5.2
- Fixed a bug where using show after update did not work
- Added linewidth argument for plotting multiple points
- Added new entity: oriented point
- Added an all import on bgplot entities
- Changed the add oriented point methods to include the new oriented point entity
- Added a brand new logo

# 0.0.8
- Implemented bgpColors for cuter representations
- Changed the default line range value in the add line function
- Changed the default length value of vectors
- Implemented a new method that can disable plot settings as ticks, grid, background...
- Changed module name from 'op' to 'ops'
- Implemented background color change method
- Changed the default colors to use the bgp ones
- Added line width parameter to the add line functions

# 0.0.7
- Fixed a big where the update method didn't maintain the aspect ratio
- Added a set view method where the view of the figure can be changed
- Added more operations use cases for future implementations

# 0.0.6
- Fixed a bug where the aspect ratio did not work for all figures

# 0.0.5
- Added test code on operations module
- Documented all functions and classes
- Instantiating a plane with a null vector is now a localized error
- Added logger to the public API
- Added the option to return degrees instead of radians in the get angle function
- Added more default values to add functions

# 0.0.4
- Added lock aspect ratio by default for figures
- Changed angle between two vectors using atan2
- Changed API to be more modular
- Changed graphics to be more modular
- Improved tests
- Merged show and clear (provisional change)
- Fixed bug where set_limits was a mandatory method to use
- Added figures titles
- Implemented add functions for plotting multiple oriented points, lines and planes
- Added some default positions for some add functions
- Implemented unfinished constructors for plane entity
- Added vector addition and subtraction overrides

# 0.0.3
- Implemented logger class
- Added get_intersection_of_line_and_plane function
- Fixed line projection on plane
- Added (0, 0, 0) as default parameter on some plot functions
- Changed names of graphics "plot" functions to "add" functions

# 0.0.2
- Fixed unexisting import on __init__

# 0.0.1
- First version of the library