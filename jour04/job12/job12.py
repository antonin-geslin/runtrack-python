def length(list):
    compteur = 0
    
    for i in list:
        compteur+=1
    return (compteur)

def tri(L):
    i = 0
    size = length(L)
    while i < size - 1:
            if L[i] >= L[i+1]:
                temp = L[i+1]
                L[i+1] = L[i]
                L[i] = temp
                i = 0
            else:
                i += 1
    return(L)
                
            
            
L = [36, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

print(tri(L))