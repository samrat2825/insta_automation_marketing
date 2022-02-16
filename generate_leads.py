import modules.config as config
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from modules.utility_methods import store_usernames

tags = ['mentalhealthtips', 'music']


def generate_posts_by_tag(tag):
    url = 'https://www.instagram.com/explore/tags/'+str(tag)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        executable_path=config.Config['chromedriver_path'], options=chrome_options)
    driver.get(url)
    all_a_tags = driver.find_elements_by_tag_name('a')
    output = []
    for elem in all_a_tags:
        href = elem.get_attribute("href")
        if href.find('/p/') != -1:
            output.append(href)
    driver.close()
    return output


def generate_leads():
    output = set()
    for tag in tags:
        posts_links = generate_posts_by_tag(tag)
        for post_link in posts_links:
            try:
                url = post_link
                chrome_options = Options()
                chrome_options.add_argument("--headless")
                driver = webdriver.Chrome(
                    executable_path=config.Config['chromedriver_path'], options=chrome_options)
                driver.get(url)
                sleep(3)
                driver.find_element_by_xpath(
                    '/html[1]/body[1]/div[1]/section[1]/main[1]/div[1]/div[1]/article[1]/div[1]/div[2]/div[1]/div[1]/div[1]/header[1]/div[2]/div[1]/div[1]/div[1]/a[1]').click()
                sleep(3)
                output.add(driver.current_url.split('/')[-2:-1][0])
                driver.close()
            except:
                print(post_link)
    store_usernames(output)


generate_leads()
