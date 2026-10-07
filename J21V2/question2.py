#parta  cp

#DECLARE arrayData : ARRAY[0:9] OF INTEGER


global arrayData
arrayData = []
values = [10,5,6,7,1,12,13,15,21,8]
for insert in range(10):
    arrayData.append(values[insert])

#part bi cp
def linearSearch(searchVal):
    index = 0

    while index < 10:
        if searchVal == arrayData[index]:
            return True
        else:
            index = index +1
    return False

#part b ii cp
inputVal = int(input("Enter a value to search: "))
if linearSearch(inputVal) == True:
    print("Value was found.")
else:
    print("value is not in the array.")

#part biii ss


#Part c

def bubbleSort():
    for x in range(len(arrayData),0, -1):
        for y in range(x-1):
            if arrayData[y] < arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y + 1] = temp
bubbleSort()
