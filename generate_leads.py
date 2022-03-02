import modules.config as config
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from modules.utility_methods import fetch_comments, fetch_credentials, fetch_leads, store_posts, store_leads
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
        if href.find('/p/') != -1:
            output.append(href)
    return output


def fetch_liked_by(driver):
    # print("fetching likes")
    time.sleep(8)
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[2]/div/div/div/a').click()
    time.sleep(4)

    try:
        users = []

        height = driver.find_element_by_xpath(
            "/html/body/div[6]/div/div/div[2]/div/div").value_of_css_property("padding-top")
        match = False
        while match == False:
            lastHeight = height

            # step 1
            elements = []
            elements = driver.find_elements_by_xpath(
                "//a[@class='notranslate']")

            # step 2
            # print(elements)
            for element in elements:
                if element.get_attribute('title') not in users:
                    users.append(element.get_attribute('title'))

            # step 3
            driver.execute_script(
                "return arguments[0].scrollIntoView();", elements[-1])
            time.sleep(1)

            # step 4
            height = driver.find_element_by_xpath(
                "/html/body/div[6]/div/div/div[2]/div/div").value_of_css_property("padding-top")
            if lastHeight == height:
                match = True

        store_leads(users)
        # print(users)
        # print(len(users))
    except Exception as e:
        print(e)


def save_post(driver):
    save_button = WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[4]/div/div/button')))
    save_button.click()


def like_post(driver):
    like_button = WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button')))
    like_button.click()


def generate_leads(driver, tags):
    for tag in tags:
        tag = tag[1:]  # remove #
        tag = tag[:-1]  # remove \n
        print(tag)
        posts_links = generate_posts_by_tag(driver, tag)
        store_posts(posts_links)
        # print(posts_links)
        for post_link in posts_links:
            try:
                url = post_link
                driver.get(url)
                driver.refresh()
                sleep(3)

                # print('Commenting')
                # comment_box = WebDriverWait(driver, 20).until(
                #     expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')))
                # comment = random.choice(comments)
                # comment_box.send_keys(comment)

                # sleep(5)
                # driver.find_element_by_xpath(
                #     '//*[@id="react-root"]/section/main/div/div/article/div/div[2]/div/div[2]/section[3]/div/form/button').click()
                # print('Commented on', url)
                fetch_liked_by(driver)

                # driver.find_element_by_xpath(
                #     '/html[1]/body[1]/div[1]/section[1]/main[1]/div[1]/div[1]/article[1]/div[1]/div[2]/div[1]/div[1]/div[1]/header[1]/div[2]/div[1]/div[1]/div[1]/a[1]').click()

                # sleep(3)
                # output.add(driver.current_url.split('/')[-2:-1][0])
                # driver.close()
            except Exception as e:
                print("\n###########################")
                print("Error", post_link, e)


def login_instagram(driver, username, password):
    driver.get('https://www.instagram.com/')
    enter_username = WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.NAME, 'username')))
    enter_username.send_keys(username)
    enter_password = WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.NAME, 'password')))
    enter_password.send_keys(password)
    enter_password.send_keys(Keys.RETURN)


def generate_leads():
    credentials = fetch_credentials()[0]
    tags = fetch_leads()
    for tag in tags:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=chrome_options)

        print(credentials[0], credentials[1])
        login_instagram(driver, credentials[0], credentials[1])
        time.sleep(5)
        generate_leads(driver, tags)
        driver.close()
