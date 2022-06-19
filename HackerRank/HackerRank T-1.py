# Designer Door Mat

n1 = input()
z = n1.split(" ")
n = int(z[0])
m = n * 3

flag = True
for i in range(n):
    div1 = int((m - (3 + (6 * i))) / 2)
    div2 = int((m - (3 + (6 * ((n-1)-i)))) / 2)
    div3 = int((m - 7) / 2)
    if i == int(n/2):
        flag = False
        for temp in range(div3):
            print("-", end="")
        print("WELCOME", end="")
        for temp in range(div3):
            print("-", end="")
        print("")

    elif flag:
        for temp in range(div1):
            print("-", end="")
        for temp in range(int(1 + (2 * i))):
            print(".|.", end="")
        for temp in range(div1):
            print("-", end="")
        print("")
    else:
        for temp in range(div2):
            print("-", end="")
        for temp in range(int(1 + (2 * ((n-1) - i)))):
            print(".|.", end="")
        for temp in range(div2):
            print("-", end="")
        print("")
