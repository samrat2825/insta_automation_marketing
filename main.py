from generate_leads import *
from post_comments import *
from datetime import datetime
from modules.utility_methods import *
import time


def pre_process_posts_links():
    post_links = fetch_posts()

    new_post_links = []
    for post_link in post_links:
        if len(post_link) > 2:
            new_post_links.append(post_link)
    # print(len(new_post_links))
    store_updated_posts(new_post_links)


def start():
    today = datetime.now()
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    current_time = current_time[:2]
    if today.day == 7 and current_time == "11":
        generate_leads()
        pre_process_posts_links()
    post_comments()


start()
