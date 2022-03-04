from datetime import date
from generate_leads import *
from post_comments import *
from datetime import datetime


def start():
    today = datetime.now()
    if today.day == 4:
        generate_leads()
    post_comments()


start()
