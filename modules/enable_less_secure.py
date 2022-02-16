from selenium import webdriver
import imaplib
import email
import re
from selenium import webdriver
import modules.config as config
import time
import traceback


def get_otp(username, password):
    otp = []
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(username, password)

    status, messages = imap.select("Inbox")
    N = 3
    messages = int(messages[0])
    print(messages)

    for i in range(messages, messages - N, -1):
        if i < 1:
            break

        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                content = msg.as_string()
                array = re.findall(r'[0-9]+', content)
                for i in array:
                    if len(i) == 6 and otp.count(i) == 0 and content.find('Instagram') != -1:
                        otp.append(i)

    imap.close()
    imap.logout()
    return otp


def enable_less_secure_apps(username, password):
    try:
        print("Enabling Less secure apps", username, password)

        driver = webdriver.Chrome(
            executable_path=config.Config['chromedriver_path'])
        # driver.get(r'https://accounts.google.com/signin/v2/identifier?continue=' +
        #            'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1' +
        #            '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
        driver.get(r'https://myaccount.google.com/lesssecureapps')
        driver.implicitly_wait(15)

        nextButton = driver.find_elements_by_xpath(
            '//*[@class ="WpHeLc VfPpkd-mRLv6"]')
        nextButton[0].click()

        loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
        loginBox.send_keys(username)

        nextButton = driver.find_elements_by_xpath(
            '//*[@id ="identifierNext"]')
        nextButton[0].click()

        passWordBox = driver.find_element_by_xpath(
            '//*[@id ="password"]/div[1]/div / div[1]/input')
        passWordBox.send_keys(password)

        nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
        nextButton[0].click()

        print('Login Successful...!!')

        driver.refresh()

        time.sleep(8)

        driver.get(r'https://myaccount.google.com/u/0/lesssecureapps')

        time.sleep(3)

        enabled = driver.find_element_by_xpath(
            "//button[@aria-label='Less secure apps turned off']").is_enabled

        if enabled == False:
            secureButton = driver.find_elements_by_xpath(
                "//button[@aria-label='Less secure apps turned off']")
            secureButton[0].click()

        driver.close()
    except:
        traceback.print_exc()
        print('Enabling less secure apps failed')
        driver.close()
