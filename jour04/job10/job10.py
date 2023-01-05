L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

result = 1

for i in range(len(L)-1):
    if 25 < L[i] < 90:
        result *= L[i]
        i+=1
    else:
        i+=1
        
print(result)