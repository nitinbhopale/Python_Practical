# def add(x,y):
#     return x+y

# print(add(y=5,x=3))


# def add(a,b,c=0,d=0):
#     return a+b+c+d

# print(add(10,20))


# def avg(*arg):
#     return sum(arg)/len(arg)


# print(avg(10,20,30,40,50))



# def name_marks(**args):
#     for name in args:
#         print(name,args[name])

# name_marks(sanjay=90,vijay=70,hari=86)



# x=20
# def scope():
#     x=10
#     gb=globals()
#     print(x)    #Local var
#     print(gb['x'])  #Global Var

# scope()


#Generator
# def genera_prime(N):
#     x=2
#     while N:
#         for i in range(2,x):
#             if x%i==0:
#                 break
#         else:
#             yield x
#             N-=1
#         x+=1

# for num in genera_prime(10):
#     print(num,end=' ')


#Iterator
list=[1,2,3,4,5,6]
it=iter(list)
while True:
    try:
        print(next(it))
    except StopIteration:
        break




# Decorator
# def decor_result(result_mark):
#     def distinction(marks):
#         for mark in marks:
#             if mark>=75:
#                 print("Distinction")
#         else:
#             result_mark(marks)
#     return distinction

# @decor_result
# def result(marks):
#     for mark in marks:
#         if mark>33:
#             pass
#         else:
#             print("Fail")
#             break
#     else:
#         print("Pass")


# result([34,32,66,55,76])