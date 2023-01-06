target = "e"
i = 0
bool = False
string = input("Entrez la chaine de caractère dans laquelle vous voulez vérifier la présence d'un e: ")

while i < len(string) and bool == False:
    if string[i] == target:
        print("Il y'a bien un e dans la chaine de caractère, il est en", (i+1),"ème position")
        bool = True
    else:
        i+=1

if bool == False:
    print("Il n'y à pas de e dans la chaine de caractère")

