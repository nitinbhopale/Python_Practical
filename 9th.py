str1={x for x in input("Enter 1st string:")}
str2={x for x in input("Enter 2nd string:")}
for x in str1.intersection(str2):
    print(x)

