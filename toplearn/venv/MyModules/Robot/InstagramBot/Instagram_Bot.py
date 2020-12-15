from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import randint


class InstagramBot:

    def __init__(self, Username, Password):
        self.username = Username
        self.password = Password
        self.driver = webdriver.Chrome(r'C:\Users\armin\PycharmProjects\toplearn\venv\chromedriver')
        self.driver.maximize_window()

    def Quit(self):
        print('Done!')
        time.sleep(5)
        self.driver.quit()

    def Login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(2)
        user_name = self.driver.find_element_by_xpath('//input[@name="username"]')
        user_name.clear()
        user_name.send_keys(self.username)
        time.sleep(0.5)
        pass_word = self.driver.find_element_by_xpath('//input[@name="password"]')
        pass_word.clear()
        pass_word.send_keys(self.password)
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//button[@type = "submit"]').click()
        time.sleep(2)
        # self.driver.find_element_by_xpath('//button[@class="aOOlW   HoLwm "]').click()
        self.driver.get(f'https://www.instagram.com/{self.username}/')
        # time.sleep(5)
        print(f"{self.username} is Login! ")

    def Like(self, hashtag, num=1, bool_Comment=False, Comment='❤'):
        tags = hashtag.split(",")
        for tag in tags:
            self.driver.get(f'https://www.instagram.com/explore/tags/{tag}/')
            time.sleep(1)
            link_list = []
            a = 0
            while (len(link_list) <= num):
                time.sleep(2)
                link = self.driver.find_elements_by_tag_name('a')  # bebin khodet mitoni code behtr az in bezani
                link_list = [l.get_attribute('href') for l in link if
                             ('.com/p/' in l.get_attribute('href') and l.get_attribute('href') not in link_list)]
                # print(len(link_list), '\n' + 10 * '*')
                self.driver.execute_script(f'scroll({a},{a + 10 ** 5})')
                a += 10 ** 5
            time.sleep(2)
            for i in range(len(link_list)):
                self.driver.get(link_list[i])
                self.driver.execute_script('scroll(0,110)')
                time.sleep(0.1)
                self.driver.find_element_by_class_name('wpO6b ').click()
                time.sleep(randint(1, 5))
                if bool_Comment:
                    self.Comment(Comment=Comment)
                if i == num - 1:
                    break;

    def Comment(self, Comment):
        self.driver.find_element_by_xpath('//span[@class="_15y0l"]').click()
        time.sleep(0.5)
        self.driver.find_element_by_tag_name('textarea').send_keys(Comment + Keys.ENTER)
        time.sleep(2)


######################################################### main #########################################################
# GUI --> sakht format bry gereftan vorodi !
# test = InstagramBot('mrblack.10', 'aza9724373')
# test.Login()
# btn_comment = False
# test.Like('life', bool_Comment=btn_comment, num=2)
#
# test.Quit()