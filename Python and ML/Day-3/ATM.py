class ATM:

    def __init__(self, amt, idx, amount):
        self.amt = amt
        self.idx = idx
        self.amount = amount

    def dep(self):
        self.amount[self.idx] += self.amt
        print("You have {0} in your account".format(self.amount[self.idx]))

    def withdraw(self):
        self.amount[self.idx] -= self.amt
        print("You have {0} in your account".format(self.amount[self.idx]))


username = input("Enter username :- ")

uname = ["abc", "xyz", "pqr"]
upin = [123, 456, 789]
amount = [12300, 45600, 78900]

if username in uname:
    pin = int(input("Hello {0}, Enter your pin :- ".format(username)))
    idx = uname.index(username)
    if pin == upin[idx]:
        print("1. Deposit\n2. Withdraw")
        choice = int(input("Enter Choice :- "))
        amt = int(input("Enter amount :- "))
        p1 = ATM(amt, idx, amount)
        if choice == 1:
            p1.dep()
        elif choice == 2:
            p1.withdraw()

    else:
        print("Invalid")
else:
    print("Invalid")