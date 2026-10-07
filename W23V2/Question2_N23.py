#ai
def IterativeCalculation(Number):
    Total = 0
    ToFind = Number
    while Number != 0:
        if ToFind % Number == 0:
            Total = Total + Number

        Number = Number -1
    return Total

#2aii
print(IterativeCalculation(10))

#2aiii

#2b
def RecursiveValue(Number, ToFind):
    if Number == 0:
        return 0
    elif ToFind % Number == 0:
        return Number + RecursiveValue(Number -1, ToFind)
    else:
        return RecursiveValue(Number-1,ToFind)



#2bii
print(RecursiveValue(50,50))

#2biii ss
