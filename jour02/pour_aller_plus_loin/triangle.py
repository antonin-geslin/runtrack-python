def triangle(a,b,c):
    maximum = max(a,b,c)
    minimum = min(a,b,c)
    if a > minimum and a < maximum:
        mid = a
    elif b > minimum and b < maximum:
        mid = b
    else:
        mid = c

    if maximum > minimum + mid:
        print("On ne peut pas construire de triangle avec ces longueurs") 
        return(False)
    
    if pow(maximum, 2) == pow(minimum, 2) + pow(mid, 2):
        print("On peut construire ce triangle, c'est un triangle rectangle")
        if maximum == minimum or minimum == mid or mid == maximum:
            print("En plus de ca il est isocèle !")
    elif maximum == mid and maximum == minimum:
        print("On peut construire ce triangle, c'est un triangle équilateral")
    elif maximum == minimum or minimum == mid or mid == maximum:
        print("On peut construire ce triangle, c'est un triangle isocèle")
    else:
        print("On peut construire ce triangle, c'est un triangle quelquonque")

triangle(10, 6, 6)