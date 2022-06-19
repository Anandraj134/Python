def fact(x):
    factorial = 1
    for i in range(x):
        factorial *= (i+1)
    return factorial


def EO(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"


def prime(x):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                return "Not Prime"
            else:
                return "Prime"
    else:
        return "Not Prime"


n = int(input("Enter a number :- "))
factorial = fact(n)
evenOdd = EO(n)
pri = prime(n)

print("Factorial of {0} = {1}\n{0} is {2} Number\n{0} is {3} Number".format(n, factorial, evenOdd, pri))