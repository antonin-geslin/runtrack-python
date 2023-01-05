L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

max = L[1]
min = L[1]
i = 0
for i in range(len(L)-1):
    if max < L[i-1]:
        max = L[i-1]
        i+=1
    else:
        i+=1
    if min > L[i-1]:
        min = L[i-1]
        i+=1
    else:
        i+=1
        
print(max)
print(min)