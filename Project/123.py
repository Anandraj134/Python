with open('1000000-password-seclists.txt') as f:
    f1 = open("passwords.txt", "a")
    for i in range(1000001):
        line = f.readline()
        if len(line) > 7:
            f1.write(line)
            print(line)
print("\n\n\n\nDone")
