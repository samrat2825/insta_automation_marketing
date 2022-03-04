from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import os
from selenium import webdriver
from modules.utility_methods import fetch_leads


class bot:
    def __init__(self, username, password, user, message, driver):
        self.username = username
        self.password = password
        self.user = user
        self.message = message
        self.base_url = 'https://www.instagram.com/'
        self.bot = driver
        self.login()

    def login(self):
        self.bot.get(self.base_url)

        enter_username = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)

        # first pop-up
        self.bot.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(5)

        try:
            # 2nd pop-up
            self.bot.find_element_by_xpath(
                '/html/body/div[5]/div/div/div/div[3]/button[2]').click()
            time.sleep(4)
        except all as e:
            print(e)
            self.bot.find_element_by_xpath(
                '/html/body/div[5]/div/div/div/div[3]/button[2]').click()

        # direct button
        self.bot.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        time.sleep(3)

        # clicks on pencil icon
        self.bot.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
        time.sleep(2)
        for i in self.user:

            # enter the username
            self.bot.find_element_by_xpath(
                '/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i)
            time.sleep(2)

            # click on the username
            self.bot.find_element_by_xpath(
                '/html/body/div[6]/div/div/div[2]/div[2]/div/div').click()
            time.sleep(2)

            # next button
            self.bot.find_element_by_xpath(
                '/html/body/div[6]/div/div/div[1]/div/div[2]/div/button').click()
            time.sleep(8)

            # click on message area
            send = self.bot.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

            # types message
            send.send_keys(self.message)
            time.sleep(1)

            # send message
            send.send_keys(Keys.RETURN)
            time.sleep(2)

            # clicks on direct option or pencl icon
            self.bot.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
            time.sleep(2)


def send_dms(insta_username, insta_password):
    raw_leads = fetch_leads()
    leads = []
    for lead in raw_leads:
        leads.append(lead[:-1])

    driver = webdriver.Chrome(ChromeDriverManager().install())

    # enter receiver user name
    user = leads
    message = ("final test")
    print("Logging In")
    bot(insta_username, insta_password, user, message, driver)

    # when our program ends it will show "done".
    print("DONE")
