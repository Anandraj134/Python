import datetime
import Automation.CurrencyConverter as cc


def dec():
    print("=" * 50)


def age(bdate):
    today = datetime.date.today()
    Age = today.year - bdate.year - ((today.month, today.day) < (bdate.month, bdate.day))
    return Age


def BMI(hi, hf, wi):
    height = (hi * 0.0254) + (hf * 0.3048)
    bmi_calc = wi / (height * height)
    if bmi_calc <= 18.5:
        return bmi_calc, "Underweight"
    elif 18.5 < bmi_calc <= 25:
        return bmi_calc, "Normal"
    elif 25 < bmi_calc <= 30:
        return bmi_calc, "Overweight"
    else:
        return bmi_calc, "Obese"


def converter(select1, select2, data):
    if select1 == 1:  # Byte
        if select2 == 2:  # KB
            return data / 1000
        elif select2 == 3:  # MB
            return data / 1048576
        elif select2 == 4 or select2 == 5:  # GB / TB
            return 0
    elif select1 == 2:  # KB
        if select2 == 1:  # Byte
            return data * 1024
        elif select2 == 3:  # MB
            return data / 1024
        elif select2 == 4:  # GB
            return data / 1048576
        elif select2 == 5:
            return 0
    elif select1 == 3:
        if select2 == 1:
            return data * 1048576
        if select2 == 2:
            return data * 1024
        if select2 == 4:
            return data / 1024
        if select2 == 5:
            return data / 1048576
    elif select1 == 4:
        if select2 == 1:
            return data * 1073741824
        elif select2 == 2:
            return data * 1048576
        elif select2 == 3:
            return data * 1024
        elif select2 == 5:
            return data / 1024
    elif select1 == 5:
        if select2 == 1:
            return data * 1099511627776
        elif select2 == 2:
            return data * 1073741824
        elif select2 == 3:
            return data * 1048576
        elif select2 == 4:
            return data * 1024


def DateDifference(start_d, end_d):
    return abs((start_d - end_d).days)


def discount_calculator(price, discount):
    disc_value = (price * discount) / 100
    final_value = price - disc_value
    return price, disc_value, final_value


def length_calculator(s1, s2, user_length):
    pass #TODO



dec()
print("""1. Age\t\t\t\t\t2. Area
3. BMI\t\t\t\t\t4. Data
5. Date\t\t\t\t\t6. Discount
7. Length\t\t\t\t8. Mass
9. Numeric System\t\t10.Speed
11.Temperature\t\t\t12.Time
13.Volume\t\t\t\t14.Currency Converter""")
dec()
user_choice = int(input("Choose any one option from above :- "))
dec()

if user_choice == 1:
    day = int(input("Enter day :- "))
    month = int(input("Enter month :- "))
    year = int(input("Enter year :- "))
    date = age(datetime.date(year, month, day))
    dec()
    print("Age difference = {} years".format(date))
    dec()

elif user_choice == 2:
    pass
    # TODO fill up this function later

elif user_choice == 3:
    print("Height:")
    h_inch = int(input("Enter inches :- "))
    h_feet = int(input("Enter feets :- "))
    weight = int(input("Enter weight in kg :- "))
    bmi, message = BMI(h_inch, h_feet, weight)
    dec()
    print("BMI = {0:.2f}\nBMI class = {1}".format(bmi, message))
    dec()

elif user_choice == 4:
    list_data = ["Bytes", "KB", "MB", "GB", "TB"]
    for i in range(len(list_data)):
        print("{0}. {1}".format(i + 1, list_data[int(i)]))
    sel1 = int(input("Select your data type :- "))
    print("You selected '{}'".format(list_data[sel1 - 1]))
    dec()
    for i in range(len(list_data)):
        if i != sel1 - 1:
            print("{0}. {1}".format(i + 1, list_data[int(i)]))
    sel2 = int(input("Select data type you want to convert :- "))
    print("You selected '{}'".format(list_data[sel2 - 1]))
    dec()
    user_data = float(input("Enter your data :- "))
    dec()
    converted_data = converter(sel1, sel2, user_data)
    print("{0} --> {1} = {2}".format(list_data[sel1 - 1], list_data[sel2 - 1], converted_data))

elif user_choice == 5:
    print("For Starting date:")
    dec()
    s_day = int(input("Enter day :- "))
    s_month = int(input("Enter month :- "))
    s_year = int(input("Enter year :- "))
    dec()
    print("For Ending date:")
    dec()
    e_day = int(input("Enter day :- "))
    e_month = int(input("Enter month :- "))
    e_year = int(input("Enter year :- "))
    dec()
    s_date = datetime.date(s_year, s_month, s_day)
    e_date = datetime.date(e_year, e_month, e_day)
    date_diff = DateDifference(s_date, e_date)
    print(date_diff)

elif user_choice == 6:
    amount = float(input("Enter the amount :- "))
    disc = float(input("Enter discount percentage :- "))
    o_price, disc_price, final_price = discount_calculator(amount, disc)
    print("""
    Amount :- \t\t\t\t{0}
    Discount :- \t\t\t{1}%
    Discount(In Amount) :- \t{2}
    ------------------------------------
    Final Price :- \t\t\t{3}
    """.format(o_price, disc, disc_price, final_price))

elif user_choice == 7:
    list_length = ["MM", "CM", "DM", "M", "KM", "MI", "YD", "FT", "IN", "FT|IN"]
    for i in range(len(list_length)):
        print("{}. {}".format(i + 1, list_length[i]))
    sel1 = int(input("Please select one UNIT :- "))

    for i in range(len(list_length)):
        if i != sel1 - 1:
            print("{}. {}".format(i + 1, list_length[i]))
    sel2 = int(input("Please select one UNIT which you want to convert :- "))

elif user_choice == 14:
    cc.main()
