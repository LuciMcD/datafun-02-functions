"""
Name: Luci McDaniel
Date: 8/31/2023
This module is to explore different math functions. 
I chose Foster Care as my domain in the first Module so I hope to incorporate that in 
this module as well.
I am using data from The AFCARS Report, linked here
 https://www.acf.hhs.gov/sites/default/files/documents/cb/afcars-report-29.pdf
 Also some information was pulled from USDA. 
"""
import math

from util_logger import setup_logger
logger, logname = setup_logger(__file__)

def get_total_in_fostercare(male, female):
    logger.info(f"Calling get_total_in_fostercare {male, female}")
    #adding the total number of male children to the total number of female children to get the total number of children.
    sum = male + female
    logger.info(f"RETURNING {sum}")
    return sum

def get_deficit(cost, allowance):
    logger.info(f"Calling get_deficit{cost, allowance}")
    #Here we are showing that the monthly cost to raise a child is much higher than the allowance given
    deficit = allowance - cost
    logger.info(f"RETURNING {deficit}")
    logger.info(f"Absolute value of the deficit = {math.fabs(deficit)}")
    return deficit

def get_percentage_of_males(male, total):
    logger.info(f"Calling get_percentage_of_males{male, total}")
    #This function is showing the percentage of male children in foster care during 2021
    decimal = male / total
    percentage = decimal*100
    logger.info(f"RETURNING {percentage}")
    logger.info(f"Rounding down the percentage is {math.floor(percentage)}%")
    return percentage

def get_percentage_of_females(female, total):
    logger.info(f"Calling get_percentage_of_females {female, total}")
    #This function is showing the percentage of female children in foster care during 2021
    decimalf = female / total
    percentagef = decimalf*100
    logger.info(f"RETURNING {percentagef}")
    logger.info(f"Rounding up the percentage is {math.ceil(percentagef)}%")
    return percentagef


get_total_in_fostercare(199969, 191037) #numbers in 2021
get_total_in_fostercare(222644, 213912) #number in 2017
get_total_in_fostercare(223042, 214295) #number in 2018
get_deficit(1145.44,503.00)#numbers in 2020
get_percentage_of_males(199969, 391098) #numbers in 2021
get_percentage_of_females(191037, 391098)

if __name__ == "__main__":

    logger.info("Explore some functions in the math module")
    logger.info(f"math.fabs(deficit) = {math.fabs(-642.44)}")
    logger.info(f"math.com(5,1) = {math.comb(5,1)}")
    logger.info(f"math.perm(5,1) = {math.perm(5,1)}")
    logger.info(f"math.floor(9.7) = {math.floor(9.7)}")
    logger.info(f"THIS HAS BEEN FUN!")




    

