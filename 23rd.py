names = input("Enter Name separeted by Comma:").split(',')
names1=names
names.sort()
print("Sorting using sort Function:",names)
print("Sorting without using sort Function:",sorted(names1))