import os
import logging

logging.basicConfig(level=logging.INFO)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSET_DIR = os.path.join(BASE_DIR, 'Assets')

Config = {
    "bot_type": 1,
    "chromedriver_path": r"C:\Users\Dell\Documents\GitHub\insta_automation_marketing\chromedriver.exe",
    "use_custom_proxy": False,
    "use_local_ip_address": True,
    "amount_of_account": 1,
    "amount_per_proxy": 1,
    "proxy_file_path": ASSET_DIR + "/proxies.txt",
    "email_domain": "gmail.com",
    "country": "it",
    "mobile": "9990165720",
}
