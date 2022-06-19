# String Formatting

n = int(input())


for i in range(1, n+1):
    binary = bin(i)
    hexa = hex(i).upper()
    octal = oct(i)

    print("{0} {1} {2} {3}".format(str(i).rjust(len(bin(n))-2), octal[2:].rjust(len(bin(n))-2),
                                   hexa[2:].rjust(len(bin(n))-2), binary[2:].rjust(len(bin(n))-2)))