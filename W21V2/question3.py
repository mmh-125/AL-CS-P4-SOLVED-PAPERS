#part a

#DECLARE ARRAYNODES : ARRAY[0:20,0:2] OF INTEGER
#DECLARE RootPointer: INTEGER
#DECLARE FreeNode : INTEGER
global ArrayNodes

ArrayNodes = []
global RootPointer
RootPointer = -1
global FreeNode
FreeNode = 0

#part b

def AddNode():
    global FreeNode
    global RootPointer
    global ArrayNodes


    NodeData = int(input("Enter node data: "))

    if FreeNode <= 19:

        ArrayNodes.append([-1,NodeData, -1])

        if RootPointer == -1:
            RootPointer = 0

        else:
            Placed = False
            CurrentNode = RootPointer
            while Placed == False:

                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]

                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]

        FreeNode = FreeNode +1
    else:
        print("Tree is full")


#part c

def PrintAll():
    print("LeftPointer Data RightPointer")
    for index in range(len(ArrayNodes)):
        print(f"     {ArrayNodes[index][0]}       {ArrayNodes[index][ 1]}     {ArrayNodes[index][ 2]}" )

#part di enter data 10,5,15,18,12,6,20,11,9,4

for index in range(10):

    AddNode()
PrintAll()


#part dii ss

#part ei
def InOrder(CurrentNode):
    if ArrayNodes[CurrentNode][0] != -1:
        return InOrder(ArrayNodes[CurrentNode][0])

    print(ArrayNodes[CurrentNode][1])

    if ArrayNodes[CurrentNode][2] != -1:
        return InOrder(ArrayNodes[CurrentNode][2])

print(InOrder(0))
























