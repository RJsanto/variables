#Ricky Santos
#Fahrenheit to Centigrade
#12/09/2014

import math
import time

fahrenheit = int(input("please enter the temperature in degrees Fahrenheit: "))
#float allows decimal numbers. int is only for whole numbers

centigrade = (fahrenheit - 32)*(5/9)
centigrade = round(centigrade,0)
#round(,2) rounds the number to two decimal places asmost temperatures come out
#as recurring decimals.

print ("calculating...")
time.sleep(1)
# Delay for 1 seconds

print ("{1} degrees fahrenheit is {0} degrees celsius".format(centigrade,fahrenheit))
