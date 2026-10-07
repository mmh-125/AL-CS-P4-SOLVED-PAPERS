class Node:
    #LeftPointer : INTEGER
    #Data : INTEGER
    #RightPointer : INTEGER
    def __init__(self, data):
        self.__Data = data
        self.__LeftPointer = -1
        self.__RightPointer = -1

    def GetLeft(self):
        return self.__LeftPointer
    def GetRight(self):
        return self.__RightPointer
    def GetData(self):
        return self.__Data

    def SetLeft(self, leftp):
        self.__LeftPointer = leftp

    def SetRight(self, rightp):
        self.__RightPointer = rightp

    def SetData(self, thisdata):
        self.__Data = thisdata

class TreeClass:
    #FirstNode : INTEGER
    #NumberNodes : INTEGER
    #Tree : List OF Node

    def __init__(self):
        self.__FirstNode = -1
        self.__NumberNodes =0

        self.__Tree = [Node(-1) for _ in range(20)]

    def InsertNode(self, NewNode):

        if self.__NumberNodes == 0:
            self.__Tree[0] = NewNode
            self.__NumberNodes +=1
            self.__FirstNode = 0
        else:
            self.__Tree[self.__NumberNodes] = NewNode
            thispointer = 0
            prevpointer = -1
            greater = False
            while thispointer != -1:
                prevpointer = thispointer
                if self.__Tree[self.__NumberNodes].GetData() > self.__Tree[thispointer].GetData():

                    greater = True
                    thispointer = self.__Tree[thispointer].GetRight()
                else:
                    greater = False
                    thispointer = self.__Tree[thispointer].GetLeft()

            if greater:
                self.__Tree[prevpointer].SetRight(self.__NumberNodes)
            else:
                self.__Tree[prevpointer].SetLeft(self.__NumberNodes)
            self.__NumberNodes +=1

    def OutputTree(self):
        if self.__NumberNodes == 0:
            print("No Nodes")
        else:
            for count in range(self.__NumberNodes):
                print("Node Data: " , self.__Tree[count].GetData())
                print("Node Left Pointer: ", self.__Tree[count].GetLeft())
                print("Node Right Pointer: ", self.__Tree[count].GetRight())

TheTree = TreeClass()

TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(11))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(1))
TheTree.InsertNode(Node(20))
TheTree.InsertNode(Node(7))
TheTree.InsertNode(Node(15))



TheTree.OutputTree()





















