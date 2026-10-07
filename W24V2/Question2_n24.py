#1a

class Queue():
    def __init__(self,head, tail, arrayval ):
        self.QueueArray = [arrayval for _ in range(100)] #ARRAY[0:99] OF INTEGER
        self.HeadPointer = head #INTEGER
        self.TailPointer = tail #INTEGER

#1B
TheQueue = Queue(-1,0,-1)


#1c
def Enqueue(AQueue,TheData):
    if AQueue.HeadPointer == -1:
        AQueue.QueueArray[AQueue.TailPointer] = TheData
        AQueue.HeadPointer = 0
        AQueue.TailPointer = AQueue.TailPointer +1
        return 1
    elif AQueue.TailPointer >  98:
        return -1
    else:
        AQueue.QueueArray[AQueue.TailPointer] = TheData
        AQueue.TailPointer += 1
        return 1

#1d

def ReturnAllData():
    global TheQueue
    OutStr = ""
    for count in range(TheQueue.HeadPointer, TheQueue.TailPointer ):
        OutStr = OutStr + str(TheQueue.QueueArray[count])

    return OutStr

#1ei
index = 0
inserted = 1
while index < 10 and inserted != -1:
    value = int(input("Enter an integer greater or equal to zero: "))
    while value < 0:
        value = int(input("Enter an integer greater or equal to zero: "))
    inserted = Enqueue(TheQueue,value)
    if inserted == -1:
        print("Queue is full")
    else:
        print("Item added to Queue")
    index = index +1

print(ReturnAllData())

    #1eii ss 10 9 -1 8 7 6 5 4 3 2 1

#f
def Dequeue():
    global TheQueue
    if TheQueue.HeadPointer == -1:
        return -1
    else:
        TheQueue.TailPointer =  TheQueue.TailPointer -1
        return TheQueue.QueueArray[TheQueue.TailPointer]


#gi
for count in range(2):
    dequeued = Dequeue()
    if dequeued == -1:
        print("Queue Empty")
    else:
        print(dequeued)
ReturnAllData()


#gii 10 9 8 7 6 5 4 3 2 1





