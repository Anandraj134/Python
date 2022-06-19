T_Sum = 0
i = 1
item = int(input("Enter the total number of items :- "))
while i <= item:

    print("=" * 50)
    print("""    1. Electronic
    2. Footwear
    3. Vehicle""")
    print("=" * 50)

    choice = int(input("Enter the choice for the GST Calculation :- "))
    i += 1
    print("=" * 50)

    if choice == 1:
        print("You selected the Electronic Section")
        print("=" * 50)
        price = float(input("Enter the original price of the product :- "))
        GST_E = price + ((18 * price) / 100)
        print("=" * 50)
        print("Final price of the product is {0}\n".format(GST_E))
        T_Sum += (GST_E + price)

    elif choice == 2:
        print("You selected the Footwear Section")
        print("=" * 50)
        price = float(input("Enter the original price of the product :- "))
        GST_E = price + ((12 * price) / 100)
        print("=" * 50)
        print("Final price of the product is {0}\n".format(GST_E))
        T_Sum += (GST_E + price)

    elif choice == 3:
        print("You selected the Vehicle Section")
        print("=" * 50)
        price = float(input("Enter the original price of the product :- "))
        GST_E = price + ((28 * price) / 100)
        print("=" * 50)
        print("Final price of the product is {0}\n".format(GST_E))
        T_Sum += (GST_E + price)

    else:
        i -= 1
        print("Enter Proper number")

print("=" * 50)
print("Total Price of all the product with the GST :- {0}".format(T_Sum))
print("=" * 50)
