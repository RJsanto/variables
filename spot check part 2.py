#Ricky Santos
#23/9/2014
#spot check part 2

startWeight = int(input("please insert weight in grams."))

onehundreds = startWeight // 100
onehundredsRemainder =startWeight % 100

fiftys = onehundredsRemainder // 50
fiftysRemainder = onehundredsRemainder % 50

tens = fiftysRemainder // 10
tensRemainder = fiftysRemainder % 10

fives = tensRemainder // 5
fivesRemainder = tensRemainder % 5


twos = fivesRemainder // 2
twosRemainder = fivesRemainder % 2

ones = twosRemainder // 1



print ("there are {0} 100g weights.".format(onehundreds))
print ("there are {0} 50g weights.".format(fiftys))
print ("there are {0} 10g weights.".format(tens))
print ("there are {0} 5g weights.".format(fives))
print ("there are {0} 2g weights.".format(twos))
print ("there are {0} 1g weights.".format(ones))

