import modules.config as config
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from modules.utility_methods import fetch_comments, fetch_credentials, fetch_leads, store_posts
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import os
import random


def generate_posts_by_tag(driver, tag):
    time.sleep(5)
    url = 'https://www.instagram.com/explore/tags/'+str(tag)
    driver.get(url)
    driver.refresh()
    time.sleep(10)
    all_a_tags = driver.find_elements_by_tag_name('a')
    output = []
    for elem in all_a_tags:
        href = elem.get_attribute("href")
        print(href)
        if href.find('/p/') != -1:
            output.append(href)
    # driver.close()
    return output


def fetch_liked_by(driver):
    print("fetching likes")
    time.sleep(8)
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[2]/div/div/div/a').click()
    all_a_tags = driver.find_elements_by_tag_name('a')
    output = []
    for elem in all_a_tags:
        href = elem.get_attribute("href")
        # if href.find('/p/') != -1:
        output.append(href)
    # driver.close()
    print(output)
    # return output


def save_post(driver):
    save_button = WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[4]/div/div/button')))
    save_button.click()


def like_post(driver):
    like_button = WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button')))
    like_button.click()


def generate_leads(driver, tags):
    comments = fetch_comments()
    # output = set()
    for tag in tags:
        tag = tag[1:]
        tag = tag[:-1]
        print(tag)
        posts_links = generate_posts_by_tag(driver, tag)
        store_posts(posts_links)
        print(posts_links)
        posts_links = posts_links[:1]
        for post_link in posts_links:
            try:
                url = post_link
                # chrome_options = Options()
                # chrome_options.add_argument("--headless")
                # driver = webdriver.Chrome(
                #     executable_path=config.Config['chromedriver_path'], options=chrome_options)
                driver.get(url)
                driver.refresh()
                sleep(3)

                print('Commenting')
                comment_box = WebDriverWait(driver, 20).until(
                    expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')))
                print(random.choice(comments))
                comment_box.send_keys(random.choice(comments))

                sleep(5)
                driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div/div/article/div/div[2]/div/div[2]/section[3]/div/form/button').click()
                print('Commented on', url)
                # fetch_liked_by(driver)

                # driver.find_element_by_xpath(
                #     '/html[1]/body[1]/div[1]/section[1]/main[1]/div[1]/div[1]/article[1]/div[1]/div[2]/div[1]/div[1]/div[1]/header[1]/div[2]/div[1]/div[1]/div[1]/a[1]').click()

                # sleep(3)
                # output.add(driver.current_url.split('/')[-2:-1][0])
                # driver.close()
            except:
                print(post_link)


def login_instagram(driver, username, password):
    driver.get('https://www.instagram.com/')
    enter_username = WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.NAME, 'username')))
    enter_username.send_keys(username)
    enter_password = WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.NAME, 'password')))
    enter_password.send_keys(password)
    enter_password.send_keys(Keys.RETURN)


credentials = fetch_credentials()
tags = fetch_leads()
tags = tags[:1]
for i, credential in enumerate(credentials):
    if i == 0:
        continue
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # driver = webdriver.Chrome(
    #     executable_path=config.Config['chromedriver_path'], options=chrome_options)
    driver = webdriver.Chrome(
        executable_path=config.Config['chromedriver_path'])

    print(credential[0], credential[1])
    login_instagram(driver, credential[0], credential[1])
    generate_leads(driver, tags)
    time.sleep(5)
    driver.close()
