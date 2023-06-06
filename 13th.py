list = [int(x) for x in input("Enter Numbers sepateted by comma:").split(',')]
if list==sorted(list):
    print("Items are sorted in Ascending Order")
elif list==sorted(list,reverse=True):
    print("Items are sorted in Descending Order")
else:
    print("Items in list are not sorted")