#Ricky Santos
#23/9/2014
#spot check

import math

width = int(input("please enter the width of the pool: ."))
length = int(input("please enter the length of the pool: ."))
depth = int(input("please enter the depth of the pool: ."))

main_section = length*width*depth

circleRadius = width/2
circleArea = 3.14 * (circleRadius * circleRadius)
halfCircleVolume = (circleArea/2) * depth

poolVolume = main_section + halfCircleVolume

print ()
print ("The volume of the pool is {0}.".format(poolVolume))
