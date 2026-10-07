import datetime


#3ai

class Character():
    #PRIVATE CharacterName : STRING
    #PRIVATE DateOfBirth : DATE
    #PRIVATE Intelligence : REAL
    #PRIVATE Speed : INTEGER
    def __init__(self, cname, dob, intel, speed):
        self.__CharacterName = cname
        self.__DateOfBirth = dob
        self.__Intelligence = intel
        self.__Speed = speed

#3aii
    def GetIntelligence(self):
        return self.__Intelligence


    def GetName(self):
        return self.__CharacterName

#3AIII

    def SetIntelligence(self, intel):
        self.__Intelligence = intel

#3aiv
    def Learn(self):
        self.__Intelligence = self.__Intelligence * 1.1


#3av
    def ReturnAge(self):
        return 2023 - self.__DateOfBirth.year

#3bi

FirstCharacter = Character("Royal", datetime.date(2019,1,1),70,30)

#bii
FirstCharacter.Learn()
print("Name: ", FirstCharacter.GetName())
print("Age: ", FirstCharacter.ReturnAge())
print("Intelligence: ", FirstCharacter.GetIntelligence())

#biii ss

#c
class MagicCharacter(Character):

    def __init__(self,cname, dob, intel, speed, element):
        # PRIVATE CharacterName : STRING
        # PRIVATE DateOfBirth : DATE
        # PRIVATE Intelligence : REAL
        # PRIVATE Speed : INTEGER
        #PRIVATE Element : STRING
        super().__init__(cname,dob,intel,speed)

        self.__Element = element

#cii
    def Learn(self):
        if self.__Element== "fire" or self.__Element == "water":
            super().SetIntelligence(super().GetIntelligence() *1.2)
        elif self.__Element == "earth":
            super().SetIntelligence(super().GetIntelligence()*1.3)
        else:
            super().SetIntelligence(super().GetIntelligence() *1.1)

#di

FirstMagic = MagicCharacter("Light", datetime.date(2018,3,3), 75, 22, "fire")

#dii
FirstMagic.Learn()
print("Name: ", FirstMagic.GetName())
print("Age: ", FirstMagic.ReturnAge())
print("Intelligence: ", FirstMagic.GetIntelligence())

#diii ss

