L = [8, 24,48,2,16]
compteur = 0
for i in range(len(L)):
    if L[i] % 3 == 0:
        compteur+=1
        i+=1
    else:
        i+=1
print(compteur)