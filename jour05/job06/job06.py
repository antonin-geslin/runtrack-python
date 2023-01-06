def luke(L):
    result = []
    i = 0
    while i < len(L):
        if L[i] <= 40:
            result.append(L[i])
        else:
            a = L[i] % 10
            if a == 3 or a == 4:
                result.append(L[i] + 5 - a)
            elif a == 8 or a == 9:
                result.append(L[i] + 10 - a)
            else:
                result.append(L[i])
        i+=1
    return(result)




L = [32, 40,45, 68, 69, 54,83,82,65, 90]
print(L)
print(luke(L))


