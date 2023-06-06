print("Total marks each subject is 100")
marks = [int(x) for x in input("Enter Marks separeted by Space:").split(' ')]
print(f"{sum(marks)/(len(marks))}%")