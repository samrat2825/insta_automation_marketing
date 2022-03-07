import modules.config as config
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from modules.utility_methods import fetch_comments, fetch_credentials, fetch_posts, store_posts, store_leads
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import os
import random


def save_post(driver):
    save_button = WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[4]/div/div/button')))
    save_button.click()


def like_post(driver):
    like_button = WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button')))
    like_button.click()


def start_posting(driver, comment, post_links):
    url = random.choice(post_links)
    while len(url) < 1:
        url = random.choice(post_links)
    try:
        driver.get(url)
        driver.refresh()
        sleep(3)

        print('Commenting', comment)
        sleep(8)
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/article/div/div[2]/div/div[2]/section[3]/div/form/textarea').send_keys(comment)
        # comment_box = WebDriverWait(driver, 30).until(
        #     expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')))
        # comment_box.send_keys(comment)

        sleep(5)
        print('Comment Send')
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/article/div/div[2]/div/div[2]/section[3]/div/form/button').click()
        print('Commented on', url)
        sleep(5)

        # x = random.random()
        # if x > 0.5:
        #     like_post(driver)
        # else:
        #     save_post(driver)

    except Exception as e:
        print("\n###########################")
        print("Error", url, e)
        start_posting(driver, comment, post_links)


def login_instagram(driver, username, password):
    driver.get('https://www.instagram.com/')
    enter_username = WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.NAME, 'username')))
    enter_username.send_keys(username)
    enter_password = WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.NAME, 'password')))
    enter_password.send_keys(password)
    enter_password.send_keys(Keys.RETURN)


def post_comments():
    credentials = fetch_credentials()
    comments = fetch_comments()
    post_links = fetch_posts()
    for i, credentail in enumerate(credentials):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=chrome_options)

        print(credentail[0], credentail[1])
        time.sleep(5)
        login_instagram(driver, credentail[0], credentail[1])
        time.sleep(20)
        signed_in = "onetap"
        if signed_in in driver.current_url:
            start_posting(driver, random.choice(comments), post_links)
        driver.close()
