#Ricky Santos
#Fahrenheit to Centigrade
#12/09/2014

import math
import time

fahrenheit = float(input("please enter the temperature in degrees Fahrenheit: "))
#float allows decimal numbers.

centigrade = (fahrenheit - 32)*(5/9)
centigrade = round(centigrade,1)
#round(,2) rounds the number to two decimal places asmost temperatures come out
#as recurring decimals.

print ("calculating.")
time.sleep(5)
# Delay for 1 minute (5 seconds)
       
print ("{1} degrees fahrenheit is {0} degrees celsius".format(centigrade,fahrenheit))
