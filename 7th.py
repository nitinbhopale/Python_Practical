def add(N):
    se=0
    so=0
    for x in range(1,N+1):
        if x%2:
            so+=x
        else:
            se+=x
    print("Sum of Even Numbers:",se)
    print("Sum of Odd Numbers:",so)

add(10)
