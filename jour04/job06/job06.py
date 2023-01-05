L = [1,0,0,0,0,2]

temp = L[0]
L[0] = L[len(L)-1]
L[len(L)-1] = temp

print(L)