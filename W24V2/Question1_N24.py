#1a

class EventItem():
    #PRIVATE EventName : STRING
    #PRIVATE Type : STRING
    #PRIVATE Difficulty : INTEGER
    def __init__(self,name, type, difficulty):
        self.__EventName = name
        self.__Type = type
        self.__Difficulty = difficulty


#1aii
    def GetName(self):
        return self.__EventName
    def GetDifficulty(self):
        return self.__Difficulty
    def GetEventType(self):
        return self.__Type

#1b
Group = [] # ARRAY [0:4] OF EventItem

#1bii
Group.append(EventItem("Bridge", "jump",3))
Group.append(EventItem("Water wade", "swim",4))
Group.append(EventItem("100 mile run", "run",5))
Group.append(EventItem("Gridlock", "drive",2))
Group.append(EventItem("Wall on Wall", "jump",4))

#1c

class Character():
    #PRIVATE CharacterName : STRING
    #PRIVATE Jump : INTEGER
    #PRIVATE Swim : INTEGER
    #PRIVATE Run: INTEGER
    #PRIVATE Drive : INTEGER
    def __init__(self, Name, Jump, Swim, Run, Drive):
        self.__Jump = Jump
        self.__Drive = Drive
        self.__Swim = Swim
        self.__CharacterName = Name
        self.__Run = Run

    def GetName(self):
        return self.__CharacterName

#1d
    def CalculateScore(self, difficulty, type):
        if type == "jump":
            level = self.__Jump
        if type == "run":
            level = self.__Run
        if type == "drive":
            level = self.__Drive
        if type == "swim":
            level = self.__Swim

        difference = difficulty - level

        if difference <= 0:
            return 100
        elif difference > 4:
            return 0
        else:
            return 100 * ((5- difference) /5)

#1e
Tarz = Character("Tarz",5,3,5,1)
Geni = Character("Geni", 2,2,3,4)

#1eii

TarzScore = 0
GeniScore = 0
for event in range(5):
    difficulty = Group[event].GetDifficulty()
    type = Group[event].GetEventType()
    TarzChance = Tarz.CalculateScore(difficulty, type)
    GeniChance = Geni.CalculateScore(difficulty, type)
    thisevent = Group[event].GetName()

    if TarzChance == GeniChance:
        print("Draw")
    elif TarzChance > GeniChance:
        TarzScore = TarzScore +1

        print("Tarz won ", thisevent)
    else:
        GeniScore = GeniScore +1
        print("Geni won ", thisevent)

if TarzScore > GeniScore:
    print(f"Tarz won with {TarzScore} points")
elif GeniScore > TarzScore:
    print(f"Geni won with {GeniScore} points")
else:
    print("It is a draw")






