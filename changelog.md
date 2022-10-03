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