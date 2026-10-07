#PART A
class TreasureChest:
    #DECLARE question: STRING
    #DECLARE answer : INTEGER
    #DECLARE points : INTEGER

    def __init__(self, qstn, answer, pts):
        self.__question = qstn
        self.__answer = answer
        self.__points = pts

    #part c i
    def getQuestion(self):
        return self.__question

    #part cii
    def checkAnswer(self, userAnswer):
        if userAnswer == self.__answer:
            return True
        else:
            return False

    #part ciii

    def getPoints(self, attempts):
        if attempts ==1:
            return self.__points
        elif attempts == 2:
            return self.__points // 2
        elif attempts > 4:
            return 0
        else:
            return self.__points // 4







#partb  CP
 #DECLARE arrayTreasure : ARRAY [0:4] OF TreasureChest
global arrayTreasure
arrayTreasure = []

def readData():

    global arrayTreasure
    try:
        with open("TreasureChestData.txt", 'r') as file:
            for index in range(5):
                thisquestion = file.readline().strip()
                thisanswer = int(file.readline().strip())
                thispoints = int(file.readline().strip())
                arrayTreasure.append(TreasureChest(thisquestion, thisanswer,thispoints))
    except FileNotFoundError:
        print("The accessed file could not be found.")

#part ci CP
#above

#part cii CP Above

#part ciii CP Above

#part civ CP
readData()
Qnum = int(input("Enter a question number(1-5): "))

print(arrayTreasure[Qnum -1].getQuestion())

ThisAnswer = int(input("Answer: "))
attempts = 1

Correct = arrayTreasure[Qnum -1].checkAnswer(ThisAnswer)

while not(Correct):
    ThisAnswer = int(input("Try again:  "))
    attempts = attempts +1
    Correct = arrayTreasure[Qnum - 1].checkAnswer(ThisAnswer)

print(f"User got: {arrayTreasure[Qnum -1].getPoints(attempts)} points.")

#c partv
#ss qstn 1 correct in 1
#ss qstn 5 correct in 2









