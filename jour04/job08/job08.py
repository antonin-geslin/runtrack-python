L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

compteur = 0
for i in range(len(L)):
    if L[i] % 2 == 0:
        compteur+=1
        i+=1
    else:
        i+=1
print(compteur)