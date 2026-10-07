#Part a (CP)
class Node:
    #DECLARE data : INTEGER
    #DECLARE nextNode: INTEGER

    def __init__(self):
        self.data = 0
        self.nextNode = -1

#DECLARE linkedList : ARRAY[0:9] OF Node
#DECLARE emptyList : INTEGER
#DECLARE startPointer : INTEGER

#PART B CP

#DECLARE startPointer : INTEGER
#DECLARE emptyList : INTEGER
linkedList = [Node() for _ in range(10)]
data = [1,5,6,7,2,0,0,56,0,0]
pointers = [1,4,7,-1,2,6,8,3,9,-1]


for index in range(len(data)):
    linkedList[index].data = data[index]
    linkedList[index].nextNode= pointers[index]

startPointer = 0
emptyList = 5

#PART Ci  CP

def outputNodes(linkedlist, startpointer):

    print(linkedlist[startpointer].data)
    next = linkedlist[startpointer].nextNode
    while next != -1:
        print(linkedlist[next].data)
        next = linkedlist[next].nextNode

#PART Cii SS
outputNodes(linkedList,startPointer)

#PART Di CP




def addNode(mylist, emptyP, startp):
    thisdata = int(input("Enter Data to insert in list: "))
    insert = False
    index = startp
    thisnode = emptyP

    if emptyP < 0 or emptyP > len(mylist):
        return False
    else:
        mylist[emptyP].data = thisdata
        emptyP = mylist[emptyP].nextNode
        mylist[thisnode].nextNode = -1

        insert = False
        while insert == False:
            if mylist[index].nextNode == -1:
                mylist[index].nextNode = thisnode
                insert = True
            else:
                index = mylist[index].nextNode
        return True

print()
outputNodes(linkedList, startPointer)
Inserted = addNode(linkedList, emptyList, startPointer)
if Inserted == True:
    print("Value has been inserted.")
else:
    print("List is full.")

outputNodes(linkedList, startPointer)























