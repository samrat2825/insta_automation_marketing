from csv import DictWriter
import csv

field_names = ['username', 'password']


def store_credentials(user):
    with open('Assets/username.csv', 'a') as csvfile:
        dictwriter_object = DictWriter(csvfile, fieldnames=field_names)
        dictwriter_object.writerow(user)
        csvfile.close()


def store_posts(post_links):
    # print(post_links)
    new_posts = set()
    with open('Assets/posts.txt', 'r') as postsFile:
        curr_posts = postsFile.readlines()
        for post_link in curr_posts:
            new_posts.add(post_link)
        postsFile.close()

    for post_link in post_links:
        if len(post_link) > 0:
            new_posts.add(post_link)

    # print(new_posts)

    with open('Assets/posts.txt', 'w') as postsFile:
        for post_link in new_posts:
            postsFile.write(post_link + "\n")
        postsFile.close()


def store_leads(leads):
    new_posts = set()
    with open('Assets/leads.txt', 'r') as postsFile:
        curr_posts = postsFile.readlines()
        for post_link in curr_posts:
            new_posts.add(post_link)
        postsFile.close()

    for lead in leads:
        if len(lead) > 0:
            new_posts.add(lead)

    # print(new_posts)

    with open('Assets/leads.txt', 'w') as postsFile:
        for post_link in new_posts:
            postsFile.write(post_link + "\n")
        postsFile.close()


def preprocess_leads():
    new_leads = []
    with open('Assets/hashtags.txt', 'r') as leadsFile:
        curr_leads = leadsFile.readlines()
        for lead in curr_leads:
            new_leads.append(lead)
        leadsFile.close()

    leads = str(new_leads[0])
    new_leads = leads.split(' ')
    leads = new_leads
    new_leads = []
    for lead in leads:
        if (lead[1:]).isalpha():
            new_leads.append(lead)
        else:
            print(lead)

    with open('Assets/hashtags.txt', 'w') as leadsFile:
        for lead in new_leads:
            leadsFile.write(lead + "\n")
        leadsFile.close()
    print(new_leads)


def fetch_comments():
    print("Fetching Comments")
    with open('Assets/comments.txt', 'r', encoding='utf-8') as commentsfile:
        comments = commentsfile.readlines()
        data = []
        for comment in comments:
            comment = comment[:-1]
            data.append(comment)
        commentsfile.close()
        # print(data)
        return data


def fetch_leads():
    print("Fetching Hastags")
    with open('Assets/hashtags.txt', 'r', encoding='utf-8') as leadsFile:
        curr_leads = leadsFile.readlines()
        new_leads = []
        for lead in curr_leads:
            new_leads.append(lead)
        leadsFile.close()
        return new_leads


def fetch_posts():
    print("Fetching Post Links")
    with open('Assets/posts.txt', 'r', encoding='utf-8') as leadsFile:
        curr_leads = leadsFile.readlines()
        new_leads = []
        for lead in curr_leads:
            new_leads.append(lead)
        leadsFile.close()
        return new_leads


def fetch_credentials():
    print("Fetching Credentials")
    with open('Assets/username.csv', 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        rows = []
        for row in csvreader:
            if len(row) > 0:
                rows.append(row)
        file.close()
        return rows


# print(fetch_credentials())
# fetch_comments()
# fetch_leads()
