import os

Queue=[]

def instruction():
    print("\n1.Insertion")
    print("2.Deletion")
    print("3.Exit")
    choice = int(input("Enter Ur Choice:"))
    return choice

while True:
    os.system('cls')
    for x in Queue:
        print(x,end=' ')
    choice = instruction()
    match(choice):
        case 1:
            num1=int(input("Enter Number:"))
            Queue.insert(0,num1)
        case 2:
            if len(Queue)!=0:
                element =Queue[0]
                del Queue[0]
        case 3:
            exit()
    




