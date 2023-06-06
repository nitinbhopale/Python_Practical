# large=lambda a,b,c: print(a if a>b>c else(b if b>c else c))

# a,b,c=int(input("Enter 1st Number:")),int(input("Enter 1st Number:")),int(input("Enter 1st Number:"))
# large(a,b,c)



# square=lambda N:print(N*N)

# x=int(input("Enter Number:"))
# square(x)



# filt=lambda x:[ num for num in x if num%2==0]
# print(filt([1,2,3,4,5,6]))


list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
print(list(map(lambda x,y:x*y,list1,list2)))