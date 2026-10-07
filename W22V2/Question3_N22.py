



HeadPointer = 0

TailPointer = -1
Queue = [0 for _ in range(100)]

#3b
def Enqueue(insert):
    global TailPointer
    global HeadPointer


    if (HeadPointer == (TailPointer) +1 and HeadPointer !=0) or (HeadPointer == 0 and TailPointer == 99 ):
        return False
    else:
        TailPointer = TailPointer +1
        if TailPointer == 100:
            TailPointer = 0

        Queue[TailPointer] =  insert
        return True

#3c

for count in range(20):
    inserted = Enqueue(count +1 )

if inserted:
    print('Successful')
else:
    print("Unsuccesful")

#3d



def RecursiveOutput(index):
    if index + 1 == 100:
        index = 0
    if index == TailPointer:
        return Queue[index]
    else:
        RecursiveOutput(index +1)



print (RecursiveOutput(HeadPointer))

#EII ss




