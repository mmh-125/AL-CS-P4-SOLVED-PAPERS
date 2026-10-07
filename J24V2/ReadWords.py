def Play():
    global WordArray
    global NumberWords
    CorrectWords = 0

    print("Main Word: ", WordArray[0])
    print("Number of Answers with 3 or more letters: ", NumberWords)
    Answer = ""
    while Answer != "no" and CorrectWords != NumberWords:
        found = False
        counter = 1
        Answer = input("Enter an answer or enter no to exit: ").strip().lower()
        while found == False and counter <= NumberWords:
            if WordArray[counter] == Answer:
                found = True
            counter +=1
        if found == True:
            WordArray[WordArray.index(Answer)] = "0"
            print("Answer is Correct!")
            CorrectWords +=1
        else:
            if Answer != "no":
                print("Answer is not a word!")

    print("You got: ", (CorrectWords/NumberWords)*100 , "% correct", sep="")
    if (CorrectWords/NumberWords)*100 == 100:
        print("The remaining words are: ")
        for index in WordArray:
            if index == "0":
                print(index)

def ReadWords(filename):
    global WordArray
    global NumberWords
    with open(filename,'r') as file:
        for line in file:
            WordArray.append(line.strip())
    print(WordArray)
    NumberWords = len(WordArray)-1
    Play()

WordArray = []
NumberWords  = 0
choice = input("Enter difficulty(easy/medium/hard): ").strip()
file = choice.title() + ".txt"
print(file)
ReadWords(file)
















