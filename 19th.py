mat1 = [[1,2,3],[4,5,6]]
mat2 = [[10,20,30],[40,50,60]]

ans = [[],[]]

for index in range(3):
    ans[0].append(mat1[0][index]+mat2[0][index])
    ans[1].append(mat1[1][index]+mat2[1][index])

print(ans)
