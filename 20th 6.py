num=1
for i in range(1,5):
    reg=0
    var=num
    for j in range(1,5):
        if j<=i:
            print(var,end=' ')
            if var==0:var=1
            else: var =0

            if reg==0:
                if num==1:num=0
                else:num=1
                reg=1
        else:
            print(" ",end=' ')
    print()
