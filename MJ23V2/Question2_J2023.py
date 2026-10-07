#1a
class SaleData:
    #DECLARE SaleID : STRING
    #DECLARE SaleQuantity : INTEGER
    def __init__(self, id, quantity):
        self.SaleID =id
        self.SaleQuantity = quantity

#1b
global CircularQueue
CircularQueue = [SaleData("", -1) for _ in range(5)]
Head = 0
Tail = 0
NumberOfItems = 0

#c
def Enqueue(record):
    global NumberOfItems
    global Head
    global Tail
    if NumberOfItems == 5:
        return -1
    else:
        CircularQueue[Tail] = record
        Tail = Tail +1
        if Tail == 5:
            Tail = 0
        NumberOfItems =  NumberOfItems +1
        return 1

#d
def Dequeue():
    global NumberOfItems
    global Head
    if NumberOfItems == 0:
        return[]
    else:
        CurrentNode = Head
        Head = Head +1
        if Head == 5:
            Head = 0
        NumberOfItems = NumberOfItems -1
        return CircularQueue[CurrentNode]

#E
def EnterRecord():
    Id = input("Enter the Sale Id: ").upper()
    Quantity = int(input("Enter Sale Quantity: "))
    inserted = Enqueue(SaleData(Id, Quantity))

    if inserted == -1:
        print("Full")
    else:

        print("Stored")


#fI ADF 10, OOP 1, BXW 5, XXZ 22, HQR 6, LLP 3
for index in range(6):
    EnterRecord()
node =Dequeue()
if node == []:
    print("Queue is empty.")
else:
    print(node.SaleID)
    print(node.SaleQuantity)
EnterRecord()

for count in range(len(CircularQueue)):
    print(CircularQueue[count].SaleID)
    print(CircularQueue[count].SaleQuantity)

#fii ss
