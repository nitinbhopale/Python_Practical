N = int(input("How many fib terms u want:"))
a,b=0,1
while N:
    print(a,end=' ')
    a,b=b,a+b
    N-=1
