import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select


def connection(code1, code2):
    # options = Options()
    # options.add_argument('--headless')
    #
    # driver = webdriver.Firefox(options=options,
    #                            executable_path="D:/Anand/OneDrive/Python/Automation/geckodriver/geckodriver.exe")
    driver = webdriver.Firefox(executable_path="D:/Anand/OneDrive/Python/Automation/geckodriver/geckodriver.exe")
    driver.get(
        "https://www.google.com/search?q=currency+converter&rlz=1C1RXQR_enIN988IN988&oq=currency+converter&aqs=chrome"
        "..69i57.2865j0j1&sourceid=chrome&ie=UTF-8")
    select1 = Select(driver.find_element(By.XPATH,
                                         '//*[@id="knowledge-currency__updatable-data-column"]/div[3]/table/tbody/tr['
                                         '1]/td[3]/div/select'))
    select1.select_by_value(code1)
    # select1.select_by_visible_text(code1)

    select2 = Select(driver.find_element(By.XPATH,
                                         '//*[@id="knowledge-currency__updatable-data-column"]/div[3]/table/tbody/tr['
                                         '3]/td[3]/div/select'))

    select2.select_by_visible_text(code2)
    time.sleep(5)
    selected1 = driver.find_element(By.CLASS_NAME, 'vLqKYe').get_attribute("data-name")

    selected2 = driver.find_element(By.CLASS_NAME, 'MWvIVe').get_attribute("data-name")
    currency_value = driver.find_element(By.XPATH,
                                         '//*[@id="knowledge-currency__updatable-data-column"]/div[3]/table/tbody/tr['
                                         '3]/td[1]/input').get_property(
        "value")
    driver.close()
    return selected1, selected2, currency_value


def dec():
    print("=" * 50)


def calculator(se1, se2, val, uval):
    final_value = float(val) * uval
    print("{} :- {}".format(se1, uval))
    print("{} :- {}".format(se2, final_value))
    dec()


class ConverterSelector:
    def __init__(self, amount, s1, s2):
        self.amount = amount
        self.s1 = s1
        self.s2 = s2

    def R2D(self):
        sel1, sel2, cv = connection(self.s1, self.s2)
        calculator(sel1, sel2, cv, self.amount)

    def R2E(self):
        sel1, sel2, cv = connection(self.s1, self.s2)
        calculator(sel1, sel2, cv, self.amount)

    def R2P(self):
        sel1, sel2, cv = connection(self.s1, self.s2)
        calculator(sel1, sel2, cv, self.amount)

    def R2Y(self):
        sel1, sel2, cv = connection(self.s1, self.s2)
        calculator(sel1, sel2, cv, self.amount)

    def D2R(self):
        sel1, sel2, cv = connection(self.s1, self.s2)
        calculator(sel1, sel2, cv, self.amount)

    def D2E(self):
        sel1, sel2, cv = connection(self.s1, self.s2)
        calculator(sel1, sel2, cv, self.amount)

    def D2P(self):
        sel1, sel2, cv = connection(self.s1, self.s2)
        calculator(sel1, sel2, cv, self.amount)

    def D2Y(self):
        sel1, sel2, cv = connection(self.s1, self.s2)
        calculator(sel1, sel2, cv, self.amount)

    def E2R(self):
        sel1, sel2, cv = connection(self.s1, self.s2)
        calculator(sel1, sel2, cv, self.amount)

    def E2D(self):
        sel1, sel2, cv = connection(self.s1, self.s2)
        calculator(sel1, sel2, cv, self.amount)

    def E2P(self):
        sel1, sel2, cv = connection(self.s1, self.s2)
        calculator(sel1, sel2, cv, self.amount)

    def E2Y(self):
        sel1, sel2, cv = connection(self.s1, self.s2)
        calculator(sel1, sel2, cv, self.amount)

    def P2R(self):
        sel1, sel2, cv = connection(self.s1, self.s2)
        calculator(sel1, sel2, cv, self.amount)

    def P2D(self):
        sel1, sel2, cv = connection(self.s1, self.s2)
        calculator(sel1, sel2, cv, self.amount)

    def P2E(self):
        sel1, sel2, cv = connection(self.s1, self.s2)
        calculator(sel1, sel2, cv, self.amount)

    def P2Y(self):
        sel1, sel2, cv = connection(self.s1, self.s2)
        calculator(sel1, sel2, cv, self.amount)

    def Y2R(self):
        sel1, sel2, cv = connection(self.s1, self.s2)
        calculator(sel1, sel2, cv, self.amount)

    def Y2D(self):
        sel1, sel2, cv = connection(self.s1, self.s2)
        calculator(sel1, sel2, cv, self.amount)

    def Y2E(self):
        sel1, sel2, cv = connection(self.s1, self.s2)
        calculator(sel1, sel2, cv, self.amount)

    def Y2P(self):
        sel1, sel2, cv = connection(self.s1, self.s2)
        calculator(sel1, sel2, cv, self.amount)


def main():
    list_currency = ['Indian Rupee', 'United States Dollar', 'Euro', 'Pound sterling', 'Japanese Yen']
    for i in range(len(list_currency)):
        print("{}. {}".format(i + 1, list_currency[i]))
    dec()
    sel1 = int(input("Select your currency :- "))
    dec()

    for i in range(len(list_currency)):
        if sel1 - 1 != i:
            print("{}. {}".format(i + 1, list_currency[i]))
    dec()
    sel2 = int(input("Select currency you want to convert :- "))
    dec()
    convert = ConverterSelector(int(input("Enter Amount :- ")), list_currency[sel1 - 1], list_currency[sel2 - 1])
    dec()

    if sel1 == 1:
        if sel2 == 2:
            convert.R2D()
        elif sel2 == 3:
            convert.R2E()
        elif sel2 == 4:
            convert.R2P()
        elif sel2 == 5:
            convert.R2Y()
        else:
            print("Please select proper option")
    elif sel1 == 2:
        if sel2 == 1:
            convert.D2R()
        elif sel2 == 3:
            convert.D2E()
        elif sel2 == 4:
            convert.D2P()
        elif sel2 == 5:
            convert.D2Y()
        else:
            print("Please select proper option")
    elif sel1 == 3:
        if sel2 == 1:
            convert.E2R()
        elif sel2 == 2:
            convert.E2D()
        elif sel2 == 4:
            convert.E2P()
        elif sel2 == 5:
            convert.E2Y()
        else:
            print("Please select proper option")
    elif sel1 == 4:
        if sel2 == 1:
            convert.P2R()
        elif sel2 == 2:
            convert.P2D()
        elif sel2 == 3:
            convert.P2E()
        elif sel2 == 5:
            convert.P2Y()
        else:
            print("Please select proper option")
    elif sel1 == 5:
        if sel2 == 1:
            convert.Y2R()
        elif sel2 == 2:
            convert.Y2D()
        elif sel2 == 3:
            convert.Y2E()
        elif sel2 == 4:
            convert.Y2P()
        else:
            print("Please select proper option")
