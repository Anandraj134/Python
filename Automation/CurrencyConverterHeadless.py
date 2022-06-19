import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select


def connection(code1, code2, site):
    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Firefox(options=options,
                               executable_path="D:/Anand/OneDrive/Python/Automation/geckodriver/geckodriver.exe", service_log_path=os.devnull)
    # driver = webdriver.Firefox(executable_path="D:/Anand/OneDrive/Python/Automation/geckodriver/geckodriver.exe")
    driver.get(site)

    # select1.select_by_visible_text(code1)

    time.sleep(5)
    selected1 = driver.find_element(By.CLASS_NAME, 'vLqKYe').get_attribute("data-name")
    cmv = driver.find_element(By.XPATH, "//*[@id=\"knowledge-currency__updatable-data-column\"]/div[1]/div[2]/span[1]").get_attribute("data-value")
    selected2 = driver.find_element(By.CLASS_NAME, 'MWvIVe').get_attribute("data-name")
    currency_value = driver.find_element(By.XPATH,
                                         '//*[@id="knowledge-currency__updatable-data-column"]/div[3]/table/tbody/tr['
                                         '3]/td[1]/input').get_property(
        "value")
    driver.close()
    return selected1, selected2, currency_value, cmv

3
70

def dec():
    print("=" * 50)


def calculator(se1, se2, val, uval, cmv):
    final_value = float(val) * uval
    print("")
    print("")
    print("{} :- {}".format(se1, uval))
    print("{} :- {}".format(se2, final_value))
    print("(1 {} value :- {:.2f})".format(se2, float(cmv)))
    dec()


class ConverterSelector:
    def __init__(self, amount, s1, s2):
        self.amount = amount
        self.s1 = s1
        self.s2 = s2

    def R2D(self):
        sel1, sel2, cv, cmv = connection(self.s1, self.s2, "https://www.google.com/search?q=rupee+to+dollar&rlz=1C1RXQR_enIN988IN988&oq=rupee+to+dollar&aqs=chrome..69i57.4651j0j1&sourceid=chrome&ie=UTF-8")
        calculator(sel1, sel2, cv, self.amount, cmv)

    def R2E(self):
        sel1, sel2, cv, cmv = connection(self.s1, self.s2, "https://www.google.com/search?q=rupee+to+euro&rlz=1C1RXQR_enIN988IN988&oq=rupee+to+euro&aqs=chrome..69i57.2996j0j1&sourceid=chrome&ie=UTF-8")
        calculator(sel1, sel2, cv, self.amount, cmv)

    def R2P(self):
        sel1, sel2, cv, cmv = connection(self.s1, self.s2, "https://www.google.com/search?q=rupee+to+pound&rlz=1C1RXQR_enIN988IN988&oq=rupee+to+pound&aqs=chrome..69i57.3342j0j1&sourceid=chrome&ie=UTF-8")
        calculator(sel1, sel2, cv, self.amount, cmv)

    def R2Y(self):
        sel1, sel2, cv, cmv = connection(self.s1, self.s2, "https://www.google.com/search?q=rupee+to+japanese+yen&rlz=1C1RXQR_enIN988IN988&oq=rupee+to+japanese+yen&aqs=chrome..69i57.5247j0j1&sourceid=chrome&ie=UTF-8")
        calculator(sel1, sel2, cv, self.amount, cmv)

    def D2R(self):
        sel1, sel2, cv, cmv = connection(self.s1, self.s2, "https://www.google.com/search?q=dollar+to+rupee&rlz=1C1RXQR_enIN988IN988&oq=dollar+to+&aqs=chrome.2.69i57j0i271l3.5220j0j1&sourceid=chrome&ie=UTF-8")
        calculator(sel1, sel2, cv, self.amount, cmv)

    def D2E(self):
        sel1, sel2, cv, cmv = connection(self.s1, self.s2, "https://www.google.com/search?q=dollar+to+euro&rlz=1C1RXQR_enIN988IN988&oq=dollar+to+euro&aqs=chrome..69i57j0i271.12966j0j1&sourceid=chrome&ie=UTF-8")
        calculator(sel1, sel2, cv, self.amount, cmv)

    def D2P(self):
        sel1, sel2, cv, cmv = connection(self.s1, self.s2, "https://www.google.com/search?q=dollar+to+pound&rlz=1C1RXQR_enIN988IN988&oq=dollar+to+po&aqs=chrome.1.69i57j0i271l2.4886j0j1&sourceid=chrome&ie=UTF-8")
        calculator(sel1, sel2, cv, self.amount, cmv)

    def D2Y(self):
        sel1, sel2, cv, cmv = connection(self.s1, self.s2, "https://www.google.com/search?q=dollar+to+yen&rlz=1C1RXQR_enIN988IN988&oq=dollar+to+yen&aqs=chrome..69i57.3202j0j1&sourceid=chrome&ie=UTF-8")
        calculator(sel1, sel2, cv, self.amount, cmv)

    def E2R(self):
        sel1, sel2, cv, cmv = connection(self.s1, self.s2, "https://www.google.com/search?q=euro+to+rupee&rlz=1C1RXQR_enIN988IN988&oq=euro+to+rupee&aqs=chrome..69i57.3814j0j1&sourceid=chrome&ie=UTF-8")
        calculator(sel1, sel2, cv, self.amount, cmv)

    def E2D(self):
        sel1, sel2, cv, cmv = connection(self.s1, self.s2, "https://www.google.com/search?q=euro+to+dollar&rlz=1C1RXQR_enIN988IN988&oq=euro+to+dollar&aqs=chrome..69i57j0i271l2.1814j0j1&sourceid=chrome&ie=UTF-8")
        calculator(sel1, sel2, cv, self.amount, cmv)

    def E2P(self):
        sel1, sel2, cv, cmv = connection(self.s1, self.s2, "https://www.google.com/search?q=euro+to+pound&rlz=1C1RXQR_enIN988IN988&oq=euro+to+pound&aqs=chrome..69i57.2706j0j1&sourceid=chrome&ie=UTF-8")
        calculator(sel1, sel2, cv, self.amount, cmv)

    def E2Y(self):
        sel1, sel2, cv, cmv = connection(self.s1, self.s2, "https://www.google.com/search?q=euro+to+japanese+yen&rlz=1C1RXQR_enIN988IN988&oq=euro+to+japanese+yen&aqs=chrome..69i57.5146j0j1&sourceid=chrome&ie=UTF-8")
        calculator(sel1, sel2, cv, self.amount, cmv)

    def P2R(self):
        sel1, sel2, cv, cmv = connection(self.s1, self.s2, "https://www.google.com/search?q=pound+to+rupee&rlz=1C1RXQR_enIN988IN988&oq=pound+to+rupee&aqs=chrome..69i57.4618j0j1&sourceid=chrome&ie=UTF-8")
        calculator(sel1, sel2, cv, self.amount, cmv)

    def P2D(self):
        sel1, sel2, cv, cmv = connection(self.s1, self.s2, "https://www.google.com/search?q=pound+to+dollar&rlz=1C1RXQR_enIN988IN988&oq=pound+to+doll&aqs=chrome.1.69i57j0i271l2.8681j0j1&sourceid=chrome&ie=UTF-8")
        calculator(sel1, sel2, cv, self.amount, cmv)

    def P2E(self):
        sel1, sel2, cv, cmv = connection(self.s1, self.s2, "https://www.google.com/search?q=pound+to+euro&rlz=1C1RXQR_enIN988IN988&oq=pound+to+euro&aqs=chrome..69i57.4967j0j1&sourceid=chrome&ie=UTF-8")
        calculator(sel1, sel2, cv, self.amount, cmv)

    def P2Y(self):
        sel1, sel2, cv, cmv = connection(self.s1, self.s2, "https://www.google.com/search?q=pound+to+yen&rlz=1C1RXQR_enIN988IN988&oq=pound+to+yen&aqs=chrome..69i57.3558j0j1&sourceid=chrome&ie=UTF-8")
        calculator(sel1, sel2, cv, self.amount, cmv)

    def Y2R(self):
        sel1, sel2, cv, cmv = connection(self.s1, self.s2, "https://www.google.com/search?q=yen+to+rupee&rlz=1C1RXQR_enIN988IN988&oq=yen+to+rupee&aqs=chrome..69i57.3949j0j1&sourceid=chrome&ie=UTF-8")
        calculator(sel1, sel2, cv, self.amount, cmv)

    def Y2D(self):
        sel1, sel2, cv, cmv = connection(self.s1, self.s2, "https://www.google.com/search?q=yen+to+dollar&rlz=1C1RXQR_enIN988IN988&oq=yen+to+doll&aqs=chrome.1.69i57j0i271l3.4266j0j1&sourceid=chrome&ie=UTF-8")
        calculator(sel1, sel2, cv, self.amount, cmv)

    def Y2E(self):
        sel1, sel2, cv, cmv = connection(self.s1, self.s2, "https://www.google.com/search?q=yen+to+euro&rlz=1C1RXQR_enIN988IN988&oq=yen+to+euro&aqs=chrome..69i57.5193j0j1&sourceid=chrome&ie=UTF-8")
        calculator(sel1, sel2, cv, self.amount, cmv)

    def Y2P(self):
        sel1, sel2, cv, cmv = connection(self.s1, self.s2, "https://www.google.com/search?q=yen+to+pound&rlz=1C1RXQR_enIN988IN988&oq=yen+to+pound&aqs=chrome..69i57.6270j0j1&sourceid=chrome&ie=UTF-8")
        calculator(sel1, sel2, cv, self.amount, cmv)


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
