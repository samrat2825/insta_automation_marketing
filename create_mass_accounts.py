from modules.create_gmail_account import create_account_on_gmail
from modules.enable_less_secure import enable_less_secure_apps
from modules.create_insta import create_account_on_insta
import modules.utility_methods as utils
import time


def accountCreator():
    print("Creation Started")
    account_info = create_account_on_gmail()
    utils.store_credentials(account_info)
    print(" Gmail Account created with email",
          account_info['email'], "and pass", account_info['password'])

    time.sleep(5)

    enable_less_secure_apps(account_info["email"], account_info["password"])
    print('Enabled Less secure apps for {}', account_info['email'])

    create_account_on_insta(account_info)


print("Creating...")
accountCreator()
