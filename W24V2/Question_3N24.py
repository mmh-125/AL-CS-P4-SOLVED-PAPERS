#1a
HighScores = [["","", ""] for _ in range(7)]

#1b
def ReadData():
    Data = []
    try:
        with open("HighScoreTable.txt", "r") as file:
            for index in range(7):
                Id = file.readline().strip()
                Level = file.readline().strip()
                Score = file.readline().strip()
                Data.append([Id, Level, Score])
    except FileNotFoundError:
        print("File couldnt be found")

    return Data

#1c
def OutputHighScores(Array):
    index =0
    while index < 7 and  Array[index][0] != "" :
        print(index)
        print(f"{Array[index][0]} reached level {Array[index][1]} with a score of {Array[index][2]}")
        index = index + 1

#1d

def SortScores(Array):
    Pointer = 6

    while Pointer >= 0  :

        for Index in range(Pointer):

            if Array[Index][1] < Array[Index +1][1]:
                tempArray = Array[Index]
                Array[Index] = Array[Index +1]

                Array[Index +1] = tempArray

            elif Array[Index][1] == Array[Index +1][1]:
                if Array[Index][2] < Array[Index+1][2]:
                    tempArray = Array[Index]
                    Array[Index] = Array[Index + 1]
                    Array[Index + 1] = tempArray


        Pointer = Pointer -1
    return Array


#ei
HighScores = ReadData()

print("Before")
OutputHighScores(HighScores)
HighScores = SortScores(HighScores)
print("After")
OutputHighScores(HighScores)


