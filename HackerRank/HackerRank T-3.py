# Alphabet Rangoli
import string

n1 = int(input())
n = (n1 * 2) - 1

for i in range(n):
    flag = True
    phase1 = (n - (1 + (2 * i)))
    phase2 = (n - (1 + (2 * (n - i))))

    if flag:
        for temp in range(int(phase1/2)):
            print("-", end="")
        for temp in range(1 + (2 * i)):
            count = 0
            if count == 0 or count % 2 == 0:
                print(string.ascii_lowercase[n1-temp], end="")
            else:
                print("-")
        for temp in range(int(phase1/2)):
            print("-", end="")

    elif phase1 == 0:
        for temp in range()