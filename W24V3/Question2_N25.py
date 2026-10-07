#A
Queue = ["" for _ in range(100)] #ARRAY OF STRING
QueueHead = -1 #INTEGER
QueueTail = -1 #INTEGER
NumberItems = 0 #INTEGER
global Queue
global QueueHead
global QueueTail
global NumberItems



#B
def Enqueue(instr):
    global QueueTail
    global NumberItems
    global QueueHead
    if NumberItems == 100:
        return False
    else:
        QueueTail +=1
        if QueueHead == -1:
            QueueHead = 0
        Queue[QueueTail] = instr
        NumberItems = NumberItems +1
        return True

#C
def Dequeue():
    global NumberItems
    global QueueHead
    if NumberItems == 0:
        return "False"
    else:
        NumberItems -=1
        retval = Queue[QueueHead]
        return retval

#D
def ReadData():
    try:
        with open("BinaryData.txt", "r") as file:
            for line in file:
                thisdigit = int(line.strip())
                Enqueue(thisdigit)

    except FileNotFoundError:
        print("File couldnt be found")


#E
def Compress():
    global NumberItems

    NewString = ""
    for count in range(NumberItems):
        thisdigit = 0
        previdigit = 0
        itercount = 0

        thisdigit = Dequeue()
        while thisdigit == prevdigit:
            itercount + =1
            prevdigit






