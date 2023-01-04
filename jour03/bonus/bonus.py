string = input("Ecrivez la string que vous voulez inversez : ")
i = len(string)
result = ""

while i > 0:
    result += string[i-1]
    i-= 1


print(result)
