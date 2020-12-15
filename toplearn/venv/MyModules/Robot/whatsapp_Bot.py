from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r'C:\Users\armin\PycharmProjects\toplearn\venv\chromedriver')
driver.get('https://web.whatsapp.com/')

msg = input("Enter message : ")
num = int(input("Enter number of messages : "))
names = input("Enter names : ").split(',')

input("Please press Enter to run!")
for user in names:
    input(user)
    selectUser = driver.find_element_by_xpath(f'//span[@title="{user}"]')
    selectUser.click()
    msgToUser = driver.find_element_by_class_name('_1Plpp')
    for i in range(num):
        msgToUser.send_keys(msg)
        time.sleep(2)
        driver.find_element_by_class_name('_35EW6').click()

time.sleep(5)
driver.quit()
