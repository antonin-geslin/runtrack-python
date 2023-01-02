target = "e"
i = 0
bool = False
string = input("Entrez la chaine de caractère dans laquelle vous voulez vérifier la présence d'un e: ")

for i in range(len(string)):
    if string[i] == target:
        print("Il y'a bien un e dans la chaine de caractère, il est en", (i+1),"ème position")
        bool = True
        break
    else:
        i+=1

if bool == False:
    print("Il n'y a pas de e dans la chaine de caractère")

