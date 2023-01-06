def draw_lines(n):
    i = 0
    j = 0
    k = n
    while i <= n+2:
        if i == 0:
            print("+", end="")
            i+=1
        elif i == n+2:
            print("+")
            i+=1
        else:
            print("-", end="")
            i+=1
    i=0
    while i <= n:
        while j <= n+2:
            if j == 0:
                print("|",end="")
                j+=1
            elif j == n + 2:
                print("|")
                j+=1
            elif j == k + 1:
                print(" ", end="")
                k -=1
                j+=1
            else:
                print("#", end="")
                j+=1
        i+=1
        j = 0   
    i=0
    while i <= n+2:
        if i == 0:
            print("+", end="")
            i+=1
        elif i == n+2:
            print("+")
            i+=1
        else:
            print("-", end="")
            i+=1

draw_lines(10)