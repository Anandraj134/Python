import random

FLAG = True
MODS = []
PRIME = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47']
P = input("Enter string you want to find :- ")

T = input("Enter the string :- ")
q = int(PRIME[random.randint(0, 14)])

FINAL_MOD = int(P) % int(q)

for i in range(int(len(T)-1)):
    temp = (int(T[i])*10 + int(T[i + 1]))
    MODS.append(temp % q)

for i in range(len(MODS)):
    if MODS[i] == FINAL_MOD:
        if T[i] == P[0] and T[i+1] == P[1]:
            FLAG = False
            print("Matching found at index no.{}".format(i))

if FLAG:
    print("Sorry, your string is not found")



