for i in range(1,5):
    for j in range(1,5):
        if j<=5-i:
            print(5-i,end='')
        else:
            print(' ',end='')
    print()