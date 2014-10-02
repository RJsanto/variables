#Ricky Santos
#Garden cost
#18/9/2014

import math
import time

print ("NOTE : All measurements should be entered in metres. Eg. 9.5 = nine and a half metres ")
print()

garden_length = float(input("Please enter the length of your garden, including the boarder: "))
garden_width = float(input("Please enter the width of your garden including the boarder: "))
border_width = float(input("Please enter the width of the border: "))

print()

garden_area = garden_length * garden_width
print ("The area of your garden is {0} metres squared.".format(garden_area))

print ()

turf_area = (garden_length - (border_width * 2)) * (garden_width - (border_width * 2))
turf_area = round(turf_area,2)

print ("The actual area of the lawn is {0} metres squared.".format(turf_area))

turf_cost = turf_area * 10
turf_cost = round(turf_cost,2)
#rounded to 2 as it is dealing with money and you cannot have 100th of a penny

print ("The total cost of turfing the lawn is {0} pounds.".format(turf_cost))
