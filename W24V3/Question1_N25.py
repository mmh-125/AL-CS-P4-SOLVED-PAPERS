#ai
class BoardObject:
    def __init__(self,thiscode,thisval):
        #self.__Code : STRING
        #self.__Value: INTEGER
        self.__Code = thiscode
        self.__Value = thisval

#aii
     def GetCode(self):

         return self.__Code
     def GetValue(self):
         return self.__Value

#aiii

Object1 = BoardObject("A", 2)
Object2 = BoardObject("B",3)
Object3 = BoardObject("C",5)
Object4 = BoardObject("D", 2)
Object5 = BoardObject("E",7)

#bi
class Board:
    #self.__TheBoard : ARRAY[0:9,0:9] OF BoardObject
    def __init__(self):
        self.__TheBoard = []

        for x in range(10):
            self.__TheBoard.append([])

            for y in range(10):
                self.__TheBoard[x].append(BoardObject("-",0))

#bii
    def GetObject(self,row,col):
        return self.__TheBoard[row][col]

#biii
    def SetObject(self, Board, row,col):
        self.__TheBoard[row][col] = Board

#biv
    def DisplayBoard(self):
        for rowprint in range(10):
            for colprint in range(10):
                print(self.__TheBoard[rowprint][colprint].GetCode(), end =" ")
            print()

SetObject(Object1,0,0)


#ci
