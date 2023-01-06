def draw_rectangle(width, height):
    i = 0
    j = 0
    while i <= height - 1:
        while j <= width - 1:
            if i == 0 or i == height - 1:
                if j == 0:
                    print("|", end="")
                    j+=1
                elif j == width - 1:
                    print("|")
                    j+=1
                else:
                    print("-", end="")
                    j+=1
            else:
                    if j == 0:
                        print("|", end="")
                        j+=1
                    elif j == width - 1:
                        print("|")
                        j+=1
                    else:
                        print(" ", end="")
                        j+=1
        i+=1
        j=0

draw_rectangle(10, 3)
draw_rectangle(15, 6)
