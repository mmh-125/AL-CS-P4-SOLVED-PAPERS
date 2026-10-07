#ai
class Employee:
    #PRIVATE HourlyPay: REAL
    #PRIVATE EmployeeNumber: STRING
    #PRIVATE JobTitle: STRING

    def __init__(self, Pay, Num, Title):
        self.__HourlyPay = Pay
        self.__EmployeeNumber = Num
        self.__JobTitle = Title
        self.__PayYear2022 = [0.0 for _ in range(52)]


#aii
    def getEmployeeNumber(self):
        return self.__EmployeeNumber

#aiii
    def SetPay(self, weeknum, hours):
        Pay = hours * self.__HourlyPay
        self.__PayYear2022[weeknum -1] = Pay


#aiv
    def GetTotalPay(self):
        total = 0
        for sum in range(52):
            total = total + self.__PayYear2022[sum]
        return total

#bi

class Manager(Employee):
    # PRIVATE HourlyPay: REAL
    # PRIVATE EmployeeNumber: STRING
    # PRIVATE JobTitle: STRING
    # PRIVATE BonusValue : REAL
    def __init__(self, Pay, Num,Bonus, Title):
        self.__BonusValue = Bonus
        super().__init__(Pay, Num, Title)

#bii
    def SetPay(self,weeknum, hours):
        hours = hours + (hours* self.__BonusValue/100)
        super().SetPay(weeknum,hours)
        print(super().GetTotalPay())

#c

EmployeeArray = []


with open("Employees.txt", "r") as file:

    for count in range(8):
        IsManager = True

        pay = file.readline().strip()
        id = file.readline().strip()
        third = file.readline().strip()
        try:
            third = float(third)
            Title = file.readline().strip()

        except ValueError:

            IsManager = False

        if IsManager == True:
             EmployeeArray.append(Manager(float(pay), id, float(third), Title))

        else:
             EmployeeArray.append(Employee(float(pay), id, third))

#d
print(EmployeeArray[2].SetPay(2,5))
def EnterHours():
    with open("HoursWeek1.txt", "r") as file:
        for count in range(8):
            id = file.readline().strip()

            hours = float(file.readline().strip())
            index = 0
            found = False
            while found == False:


                if EmployeeArray[index].getEmployeeNumber() == id:
                    found = True
                else:
                    index = index + 1
            EmployeeArray[index].SetPay(1,hours)

#ei

EnterHours()

for count in range(8):
    pay = EmployeeArray[count].GetTotalPay()
    id =  EmployeeArray[count].getEmployeeNumber()
    print("Employee Number: ", id)
    print("Total Pay: ", pay)

