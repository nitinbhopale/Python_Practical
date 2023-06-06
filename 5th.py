N = int(input("How may prime numbers u want:"))
x=2
while N:
    for y in range(2,x):
        if x%y==0:
            break
    else:
        print(x,end=' ')
        N-=1
    x+=1