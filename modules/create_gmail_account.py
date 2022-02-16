import modules.config as config
from selenium import webdriver
from time import sleep
import modules.generateaccountinformation as accnt


def create_account_on_gmail():
    url = 'https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp'
    driver = webdriver.Chrome(
        executable_path=config.Config['chromedriver_path'])
    driver.get(url)

    account_info = accnt.new_account()
    driver.find_element_by_id('firstName').send_keys(
        str(account_info['name'].split(' ')[0]))
    driver.find_element_by_id('lastName').send_keys(
        str(account_info['name'].split(' ')[1]))
    driver.find_element_by_id('username').send_keys(
        str(account_info['username']))
    driver.find_element_by_xpath(
        "//input[@name='Passwd']").send_keys(str(account_info['password']))
    driver.find_element_by_xpath(
        "//input[@name='ConfirmPasswd']").send_keys(str(account_info['password']))
    driver.find_element_by_id("i3").click()
    driver.find_element_by_xpath(
        "//span[normalize-space()='Next']").click()
    sleep(4)
    driver.find_element_by_xpath(
        "//input[@id='phoneNumberId']").send_keys(str(config.Config['mobile']))
    driver.find_elements_by_tag_name("button")[0].click()
    print("Enter OTP:")
    otp = input()
    driver.find_element_by_xpath("//input[@id='code']").send_keys(otp)
    driver.find_elements_by_tag_name("button")[1].click()

    # dob and submit left

    driver.close()

    return account_info
