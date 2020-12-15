from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(r'C:\Users\armin\PycharmProjects\toplearn\venv\chromedriver')
####################################################### example 1 ######################################################
# driver.get('http://google.com')
###################### method 1
# driver.find_element_by_name('q').send_keys('تاپ لرن' + Keys.ENTER)
#####################
# driver.find_element_by_name('btnK').click() # in eleman ro peyda nakard bry hamin click nakard va error dad
###################### method 2
# driver.find_element_by_name('q').send_keys('تاپ لرن')
# driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').send_keys(Keys.ENTER) # or .click()
########################################################################################################################

####################################################### example 2 ######################################################
# driver.get('https://toplearn.com/')
# time.sleep(2)
# driver.execute_script('window.scrollTo(0,2000)')
# time.sleep(2)
# driver.execute_script('window.scrollTo(0,300)')
########################################################################################################################

####################################################### example 3 ######################################################
driver.get('https://maktabkhooneh.org/')
se = driver.find_element_by_xpath('//*[@id="navbar"]/div/form/input')
time.sleep(0.5)
se.clear()
time.sleep(2)
se.send_keys('python')
driver.find_element_by_xpath('//*[@id="navbar"]/div/form/button').click()  # or : .send_keys(Keys.ENTER)
time.sleep(2)
# driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[5]/div[1]/div/a/div[2]/div[1]').click()
driver.find_element_by_xpath('//div[@title="آموزش رایگان پایتون (Python)"]').click()
########################################################################################################################

####################################################### example 4 ######################################################
# driver.get('https://www.instagram.com/')
# print('OK')
# driver.find_element_by_xpath('//input[@name="username"]').send_keys("armin.azarakhsh10")
# driver.find_element_by_xpath('//input[@name="password"]').send_keys("mr.green10"+Keys.ENTER)

time.sleep(10)
# driver.quit()
