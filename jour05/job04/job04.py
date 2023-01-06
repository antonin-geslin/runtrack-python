def cesar(string, decalage, sens):
    result = ""
    for i in string:
        if i != " ":
            if 97 <= ord(i) + decalage * sens <= 122:
                result += chr(ord(i) + decalage * sens)
            elif ord(i) + decalage * sens >= 122:
                result += chr((ord(i) - 26) + decalage * sens)
            elif ord(i) + decalage * sens <= 97:
                result += chr((ord(i) + 26) + decalage * sens)
        else:
            result += " "
    
    return(result)

print(cesar("je suiz antonin", 3, 1))
print(cesar("je suiz antonin", 3, -1))