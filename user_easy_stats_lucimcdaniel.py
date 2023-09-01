"""

Purpose: Illustrate the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpreter
Must be 3.10 or greater to get the correlation and linear regression.

Uses only Python Standard Library modules.

@ uses statistics module for descriptive stats
@ uses sys module for checking Python version

Name: Luci McDaniel
Date: 8/31/2023
I am using the easy_stats file from module one to create a file that will chart data on 
foster care. 
I pulled data from this link https://www.acf.hhs.gov/sites/default/files/documents/cb/afcars-report-29.pdf 

"""
# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------


# Import from Python Standard Library

import statistics
import sys

# univariant time series data (one variable over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
# below xtimes is the age of the child and yvalues is percentage of children that age in foster care
xtimes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
yvalues = [7, 9, 8, 7, 6, 5, 5, 5, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 2, 1, 1]

mean = statistics.mean(yvalues)
median = statistics.median(yvalues)
mode = statistics.mode(yvalues)

var = statistics.variance(yvalues)
stdev = statistics.stdev(yvalues)
smallest = min(yvalues)
largest = max(yvalues)
range = largest - smallest 

logger.info(f"mean = {mean:.2f}")
logger.info(f"median = {median: .2f}")
logger.info(f"mode = {mode: .2f}")

logger.info(f"variance = {var: .2f}")
logger.info(f"standard deviation = {stdev: .2f}")
logger.info(f"smallest = {smallest: .2f}")
logger.info(f"largest = {largest: .2f}")
logger.info(f"range = {range: .2f}")

"""
The below is from module one and not needed for now

# if the lists are not the same size,
# log an error and quit the program
if len(xtimes) != len(yvalues):
    logger.error("ERROR: The related sets are not the same size.")
    logger.error(f"      {len(xtimes)}!={len(yvalues)}")
    quit()

# check the Python version before using the correlation function
logger.warn("Correlation requires Python version 3.10 or greater.")
logger.warn(f"Your version is {sys.version_info.major}.{sys.version_info.minor}")

# if the Python version is too old, we can quit now
if sys.version_info.minor < 10:
    logger.error("Please update Python to 3.10 or greater")
    logger.error("or use View / Command Palette / Python: Select Interpreter")
    logger.error("to get a newer one.")
    quit()

# If we're still here, use the new correlation function from the statistics module
xx_corr = statistics.correlation(xtimes, xtimes)
xy_corr = statistics.correlation(xtimes, yvalues)

# log the information
logger.info("Here's some time series data:")
logger.info(f"xtimes:{xtimes}")
logger.info(f"yvalues:{yvalues}")
logger.info(f"correlation between xtimes and xtimes = {xx_corr:.2f}")
logger.info(f"correlation between xtimes and yvalues = {xy_corr:.2f}")

# Calculate slope and intercept of a line

# Here's some bivariant data (two series of data)

arrayX = [-200, -150, -100, 50, 0, 50, 100, 150]
arrayY = [-240, -165, -99, 35, 19, 75, 130, 125]

# Call linear_regression() function -
# and get back 2 values: slope and intercept
# describing the 'best fit' line through the data
slope, intercept = statistics.linear_regression(arrayX, arrayY)

# Choose an x value off in the future (future x)
future_x = 200

# Extend the line out into the unknown future
# and read the value (of future y)
future_y = round(slope * future_x + intercept)

logger.info("Here's some bivariant data (2 variables, together):")
logger.info(f"x:{arrayX}")
logger.info(f"y:{arrayY}")
logger.info("Calculate the slope and intercept of a best fit straight line:")
logger.info(f"   slope = {slope:.2f}")
logger.info(f"   intercept = { intercept:.2f}")
logger.info("Let's use our best fit line to PREDICT a future value.")
logger.info(f"   At future x = {future_x:d},")
logger.info(f"   we predict the value of y will be { future_y:d}.")
logger.info("How'd we do? Does this make sense given the data?")
"""
