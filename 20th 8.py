for i in range(1,9):
    for j in range(1,16):
        if j<=9-i or j>=7+i:
            print("*",end='')
        else:
            print("-",end='')
    print()