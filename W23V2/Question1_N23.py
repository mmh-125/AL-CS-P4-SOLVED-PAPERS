#DECLARE StackVowel : ARRAY[0:99] OF STRING
#DECLARE StackConsonant : ARRAY[0:99] OF STRING

global StackVowel
global StackConsonant

StackVowel = ["" for _ in range(100)]
StackConsonant = ["" for _ in range(100)]

#1aii

VowelTop = 0 #INTEGER
ConsonantTop = 0 #INTEGER

#1bi
def PushData(Char):
    global VowelTop
    global ConsonantTop

    if Char.lower() in["a","e","i","o","u"]:
        if VowelTop >99:
            print("Vowel Stack is full, cannot be pushed.")
        else:
            StackVowel[VowelTop] = Char
            VowelTop = VowelTop+1
    elif ConsonantTop > 99:
        print("Consonant Stack is full, cannot be pushed.")
    else:
        StackConsonant[ConsonantTop] = Char
        ConsonantTop +=1


#1bii

def ReadData():
    try:
        with open("StackData.txt", "r") as file:
            for index in range(100):
                thischar = file.readline().strip()
                PushData(thischar)
    except FileNotFoundError:
        print("File does not exist.")



#1c

def PopVowel():
    global VowelTop

    if VowelTop == 0:
        return("No data")
    else:
        VowelTop = VowelTop -1
        return StackVowel[VowelTop]

def PopConsonant():

    global ConsonantTop
    if ConsonantTop == 0:
        return("No data")
    else:
        ConsonantTop = ConsonantTop -1
        return StackConsonant[ConsonantTop]


#d
ReadData()
retvals = ["" for _ in range(5)]
count = 0
thisval = ""
while count<5:
    search = input("Vowel or Consonant?: ").strip().lower()
    if search == "vowel":

        thisval = PopVowel()
        if thisval == "No data":
            print("This stack is empty")
        else:
            retvals[count] = thisval
            count = count + 1

    elif search == "consonant":
        thisval = PopConsonant()
        if thisval== "No data":
            print("This stack is empty")
        else:
            retvals[count] = thisval
            count = count +1


for char in retvals:
    print(char, end = "")




