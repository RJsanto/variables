#Ricky Santos
#currency
#18/9/2014

totalmoney = float(input("please enter your amount: "))

twenty = totalmoney // 20
money1 = totalmoney % 20
#// gives no deciamls
#%

ten = money1 // 10
money2 = money1 % 10

five = money2 // 5
money3 = money2 % 5

two = money3 // 2
money4 = money3 % 2

one = money4 // 1



print ("there are {0} twenty pound notes".format(twenty))
print ("there are {0} ten pound notes".format(ten))
print ("there are {0} five pound notes".format(five))
print ("there are {0} two pound notes".format(two))
print ("there are {0} one pound notes".format(one))
