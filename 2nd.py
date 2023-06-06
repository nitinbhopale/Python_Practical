# year=int(input("Enter Year:"))
# if year%100==0:
#     if year%400==0:
#         print("Leap Year")
#     else:
#         print("Not leap year")
# else:
#     if year%4==0:
#         print("Leap Year")
#     else:
#         print("Not Leap Year")

year=int(input("Enter Year:"))
print("Leap Year") if year%400==0 or year%4==0 else print("Not Leap Year")


# print(sum([int(x) for x in input("Enter Number:")]))
