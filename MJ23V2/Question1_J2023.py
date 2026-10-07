#1a

global Animals
Animals = ["" for _ in range(10)]

#1b

temp = ["horse",
        "lion",
        "rabbit",
        "mouse",
        "bird",
        "deer",
        "whale",
        "elephant",
        "kangaroo",
        "tiger"]

for insert in range(10):
    Animals[insert] = temp[insert]

#1c
def SortDescending():
    ArrayLength = len(Animals)
    Temp = ""
    for X in range(ArrayLength-1):
        for Y in range(ArrayLength - X-1):
            if Animals[Y][0] > Animals[Y+1][0]:
                Temp = Animals[Y]
                Animals[Y] = Animals[Y+1]
                Animals[Y+1] = Temp


#1d

SortDescending()
for output in range(len(Animals)):
    print(Animals[output])

#1dii
#ss
