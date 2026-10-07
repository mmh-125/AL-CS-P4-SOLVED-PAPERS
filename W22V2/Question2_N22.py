#2a
class Character:
    #DECLARE Name: STRING
    #DECLARE XCoordinate : INTEGER
    #DECLARE YCoordinate: INTEGER
    def __init__(self, name, xval, yval):
        self.__Name = name
        self.__XCoordinate = xval
        self.__YCoordinate = yval


#2b
    def GetName(self):
        return self.__Name
    def GetX(self):
        return self.__XCoordinate
    def GetY(self):
        return self.__YCoordinate

#2c
    def ChangePosition(self,XChange, YChange):
        self.__XCoordinate = self.__XCoordinate + XChange
        self.__YCoordinate = self.__YCoordinate + YChange

#2d

AllCharacters = []
with open("Characters.txt", "r") as file:
    for counter in range(10):
        name = file.readline().strip()
        xval = file.readline()
        yval = file.readline()
        AllCharacters.append(Character(name, int(xval), int(yval)))


#2e
CharacterIndex = 0
Found = False
while Found == False:
    if CharacterIndex == 0:
        Find = input("Enter a characters name : ").strip()

    if AllCharacters[CharacterIndex].GetName().lower() == Find.lower():

        Found = True
    else:

        CharacterIndex = CharacterIndex + 1


        if CharacterIndex == 10:
            CharacterIndex = 0



#2f

print("Enter W to go Up")
print("Enter A to go Left")
print("Enter S to go Down")
print("Enter D to go Right")

moves = ["W", "A", "S", "D"]

move = input("Enter your move: ").strip().upper()
while move not in moves:
    move = input("Enter a correct move: ").strip().upper()

if move == "W":
    AllCharacters[CharacterIndex].ChangePosition(0,1)
elif move == "A":
    AllCharacters[CharacterIndex].ChangePosition(-1, 0)
elif move == "S":
    AllCharacters[CharacterIndex].ChangePosition(0, -1)
else:
    AllCharacters[CharacterIndex].ChangePosition(1, 0)

#gi
print(f"{AllCharacters[CharacterIndex].GetName()} has changed coordinates to X = {AllCharacters[CharacterIndex].GetX()} and Y = {AllCharacters[CharacterIndex].GetY()}")

#gii











