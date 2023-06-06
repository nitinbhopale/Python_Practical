char = 65
for i in range(1,5):
    character=char
    reg=0
    for j in range(1,5):
        if j<=i:
            print(chr(character),end='')
            character+=1
            if reg==0:
                char+=1
                reg=1
        else:
            print(" ",end='')
    print()