string = "abcdefghijklmnopqrstuvwxyz" * 10
k = 0
for i in range(0,22):
    for j in range(0, i+1):
        print(string[k], end=" ")
        j+=1
        k += 1
    i+=1
    print()
        