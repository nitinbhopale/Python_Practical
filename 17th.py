import os

stack = []
element=0

def instruction():
    print("\n1.Push")
    print("2.Pop")
    print('3.Peek')
    print("4.Exit")
    choice = int(input("Enter Ur Choice:"))
    return choice

while True:
    os.system('cls')
    if element!=0:
        print(element)
        element=0
    else:
        for x in stack:
            print(x,end=' ')
    choice = instruction()
    match(choice):
        case 1:
            num1=int(input("Enter Number:"))
            stack.append(num1)
        case 2:
            if len(stack)!=0:
                element =stack[0]
                del stack[0]
        case 3:
            index = int(input("Enter Index:"))
            element=stack[index]
        case 4:
            exit()
    




