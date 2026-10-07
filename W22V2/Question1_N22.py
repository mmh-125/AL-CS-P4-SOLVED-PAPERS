#1a

#DECLARE Jobs :ARRAY[0:99,0:1] OF INTEGER
#DECLARE NumberOfJobs: INTEGER
global Jobs
Jobs = []

global NumberOfJobs
NumberOfJobs = 0

#1b

def Initialise():
    for index in range(100):

        Jobs.append([-1,-1])
    NumberOfJobs = 0

#1c

def AddJob(JobNum, priority):
    global NumberOfJobs
    index = 0

    while Jobs[index][0] != -1 and index < 100:
        index = index +1

    if index > 99:
        print("Not Added")
    else:
        Jobs[index][0] = JobNum
        Jobs[index][1] = priority
        print("Added")
        NumberOfJobs = NumberOfJobs +1

#1d

Initialise()
AddJob(12,10)
AddJob(526,9)
AddJob(33,8)
AddJob(12,9)
AddJob(78,1)

#1e
def InsertionSort():
    global Jobs

    for index in range(1,NumberOfJobs):
        lastIndex = index -1
        ThisPriority = Jobs[index][1]
        ThisJob = Jobs[index][0]

        while lastIndex > -1 and ThisPriority < Jobs[lastIndex][1] :


            Jobs[lastIndex+1][1] = Jobs[lastIndex][1]
            Jobs[lastIndex+1][0] = Jobs[lastIndex][0]
            lastIndex = lastIndex -1

        Jobs[lastIndex + 1][1] = ThisPriority
        Jobs[lastIndex +1][0] = ThisJob
        index = index +1

#1f

def PrintArray():
    index = 0
    while Jobs[index][0] != -1:
        print(f"{Jobs[index][0]} priority {Jobs[index][1]}")
        index = index +1

#1gi

InsertionSort()
PrintArray()

#1gii
#ss


















