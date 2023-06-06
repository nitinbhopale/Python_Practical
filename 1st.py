# print("Even") if int(input("Enter Number:"))%2==0 else print("Odd")


x=int(input("Enter Number:"))
y=int(input("Enter 2nd Number:"))
for H in range(min(x,y),1,-1):
    if x%H==0 and y%H==0:
        print("GCD is",H)
        break


















