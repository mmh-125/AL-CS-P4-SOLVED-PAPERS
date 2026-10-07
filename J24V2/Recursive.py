NumberArray = [100,85,644,22,15,8,1]

def RecursiveInsertion(IntegerArray, NumberElements):
    #LastItem : INT
    if NumberElements <=1:
        return IntegerArray

    RecursiveInsertion(IntegerArray, NumberElements -1)
    LastItem = IntegerArray[NumberElements-1]
    CheckItem = NumberElements -2
    LoopAgain = True

    if CheckItem <0:
        LoopAgain = False
    elif IntegerArray[CheckItem] < LastItem:
            LoopAgain = False

    while LoopAgain == True:
        IntegerArray[CheckItem +1] = IntegerArray[CheckItem]
        CheckItem -=1
        if CheckItem < 0:
            LoopAgain = False
        elif IntegerArray[CheckItem] < LastItem:
            LoopAgain = False

    IntegerArray[CheckItem +1] = LastItem

    return IntegerArray

SortedArray = RecursiveInsertion(NumberArray, len(NumberArray))
print("Recursive: ", SortedArray)

def IterativeInsertion(IntegerArray, NumberElements):

    for index in range(NumberElements -2, -1, -1):
        sorted = False
        endpointer = index +1
        InsertObject = IntegerArray[index]
        while endpointer <= NumberElements-1  and sorted == False:
            if InsertObject > IntegerArray[endpointer]:
                IntegerArray[endpointer -1] = IntegerArray[endpointer]
                endpointer +=1
            else:
                sorted = True
        IntegerArray[endpointer-1] = InsertObject

    return IntegerArray


Sorted2 = IterativeInsertion([5,7,1,56,45,34], 6)
print(Sorted2)

def BinarySearch(IntegerArray, First, Last, ToFind):
    if First > Last:
        return -1
    Mid = (First + Last) // 2

    if IntegerArray[Mid] == ToFind:
        return Mid

    elif IntegerArray[Mid] > ToFind:
        return BinarySearch(IntegerArray, First, Mid -1, ToFind)
    else:
        return BinarySearch(IntegerArray, Mid +1, Last, ToFind)

print(BinarySearch(Sorted2, 0,5,34))

















