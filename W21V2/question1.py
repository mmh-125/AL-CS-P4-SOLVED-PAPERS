#part a
def Unknown(X,Y):
    if X < Y:
        print(X+Y)
        return Unknown(X+1,Y) *2
    elif X == Y:
        return 1
    else:
        print(X+Y)
        return Unknown(X-1,Y) // 2

#part bi

print(10, 15)
print(Unknown(10,15))

print(10,10)
print(Unknown(10,10))

print(15,10)
print(Unknown(15,10))



#Part b ii
# ss of prev output

# part c

def IterativeUnknown(X,Y):
    retval = 1
    while X!= Y:
        if X < Y:
            print(X+Y)
            X = X+1
            retval = retval *2
        elif X >Y :
            X = X-1
            print(X+Y)
            retval = retval // 2
    return retval

print(10, 15)
print(IterativeUnknown(10,15))

print(10,10)
print(IterativeUnknown(10,10))

print(15,10)
print(IterativeUnknown(15,10))









#part di




