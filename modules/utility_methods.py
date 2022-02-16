from csv import DictWriter

field_names = ['name', 'username', 'password',
               'email', 'gender', 'birthday']


def store_credentials(user):
    with open('Assets/username.csv', 'a') as csvfile:
        dictwriter_object = DictWriter(csvfile, fieldnames=field_names)
        dictwriter_object.writerow(user)
        csvfile.close()


def store_usernames(leads):
    print(leads)
    new_leads = set()
    with open('Assets/leads.txt', 'r') as leadsFile:
        curr_leads = leadsFile.readlines()
        for lead in curr_leads:
            new_leads.add(lead)
        leadsFile.close()

    for lead in leads:
        new_leads.add(lead)

    print(new_leads)

    with open('Assets/leads.txt', 'w') as leadsFile:
        L = list(new_leads)
        leadsFile.writelines(L)
        leadsFile.close()


def fetch_leads():
    new_leads = []
    with open('Assets/leads.txt', 'r') as leadsFile:
        curr_leads = leadsFile.readlines()
        for lead in curr_leads:
            new_leads.append(lead)
        leadsFile.close()
    return new_leads
