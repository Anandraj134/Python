from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def dollor():
    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Firefox(options=options, executable_path="geckodriver/geckodriver.exe")
    driver.get(
        "https://www.google.com/search?q=dollor+price&rlz=1C1RXQR_enIN988IN988&oq=dollor+price+&aqs=chrome..69i57.4721j0j1&sourceid=chrome&ie=UTF-8")

    driver.implicitly_wait(2)
    dollor = driver.find_element_by_xpath(
        "//*[@id=\"knowledge-currency__updatable-data-column\"]/div[3]/table/tbody/tr[3]/td[1]/input").get_property(
        "value")
    return dollor


user_inp = int(input("Enter value in dollor"))
print(float(dollor()) * user_inp)

