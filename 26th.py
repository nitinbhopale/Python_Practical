def genera_fib(N):
    a,b=0,1
    while N:
        yield a
        a,b=b,a+b
        N-=1

for x in genera_fib(10):
    print(x)