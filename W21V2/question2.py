#part a
class Picture():
    #DECLARE Description: STRING
    #DECLARE Width : INTEGER
    #DECLARE Height: INTEGER
    #DECLARE FrameColour : STRING
    def __init__(self, desc, width, height, colour):
        self.__Description = desc
        self.__Width = width
        self.__Height = height
        self.__FrameColour = colour


#part b
    def GetDescription(self):
        return self.__Description

    def GetHeight(self):
        return self.__Height
    def GetWidth(self):
        return self.__Width
    def GetColour(self):
        return self.__FrameColour

#partc
    def SetDescription(self, thisdesc):
        self.__Description = thisdesc

#partd
#DECLARE PictureArray[0:99] OF Picture


global PictureArray
PictureArray  = []

#part e

def ReadData():
    global PictureArray
    linecount = 0
    try:
        with open("Pictures.txt", "r") as file:
            for count in range(4):
                thisdesc = file.readline()
                thisheight = int(file.readline())
                thiswidth = int(file.readline())

                thiscolour = file.readline()

                PictureArray.append(Picture(thisdesc,thisheight,thiswidth, thiscolour))
                linecount = linecount+1

    except FileNotFoundError:
        print("File couldn't be found")

    return linecount

#part f

picCount = ReadData()

#part g
reqColour = input("What Colour do you want: ").lower()
maxWidth =int(input("What is the maximum width of pictures that you want: "))
maxHeight = int(input("What is the maximum height of picture you want: "))

for index in range(picCount):
    if PictureArray[index].GetColour() == reqColour:
        print(f"Description: {PictureArray[index].GetDescription()}")
        print(f" Width: {PictureArray[index].GetWidth()} ")
        print(f" Width: {PictureArray[index].GetHeight()} ")


#part h screenshots BLACK,100,100 and silver,25,25



