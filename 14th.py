x=[1,2,3,4,5,6,7,8]
num = int(input("Which number u want to search:"))
for no in x:
    if no==num:
        print("Success")
        break
else:
    print("Failure")