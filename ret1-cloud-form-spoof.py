from sre_parse import SPECIAL_CHARS
import requests
import random
import json
import string
import secrets

email_domains = [
    'gmail.com',
    'yahoo.com',
    'hotmail.com',
    'morar.net',
    'schmidt.biz',
]
seps = [
    '',
    '.',
    '_',
    '-'
]
decor = [
    'poop'
    'asdf'
    'uwu',
    '1990',
]
num_requests = 10
url = "https://44b5k.quest/amorlapaz/post.php"
with open ('./names.json', 'r') as f:
    names = json.load(f)
    utf_valid_region_indices = [3, 11, 19, 27, 28, 30, 32, 35, 37, 38, 39, 40, 41, 43, 52, 57]
with open('./10k-most-common-pws.txt', 'r') as f:
    passwords = f.readlines()

def flip_coin():
    return secrets.choice([0, 1]) == 0

def one_in_(this_many):
    return random.randint(0, this_many) == 0

def generate_email_from_name(firstname, lastname):
    # case 1 Firstname_Lastname (where _ is any separator)
    # case 2 Flastname (where it's first initial, last name)
    newfirstname = firstname if flip_coin() else firstname[0]
    newlastname = lastname if flip_coin() else lastname[0]
    newdecoration = '' if flip_coin() else secrets.choice(decor)
    new2decoration = '' if flip_coin() else secrets.choice(decor)
    random_sep = secrets.choice(seps)

    new_email = newfirstname + newdecoration + random_sep + newlastname + new2decoration
    return new_email

def generate_password():
    pwd_length = 3
    letters = string.ascii_letters
    digits = string.digits
    # special_chars = string.punctuation
    special_chars = '!$'
    alphabet = letters + digits + special_chars
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
    
    common_pw = secrets.choice(passwords).rstrip()
    return common_pw + ('' if flip_coin() else pwd)


if __name__ == '__main__':
    for i in range(num_requests):
        gender = 'male' if flip_coin() else 'female'
        region_index = secrets.choice(utf_valid_region_indices)
        email_index = random.randint(0, len(email_domains) - 1)

        payload={
            'username': 'pazusa'
        }

        firstname = secrets.choice(names[region_index][gender])
        lastname = secrets.choice(names[region_index]['surnames'])
        payload['email'] = generate_email_from_name(firstname, lastname) + '@' + email_domains[email_index]

        password = generate_password()
        payload['pass'] = password

        print(payload)
        response = requests.request("POST", url, data=payload)
        print('success' if response.status_code == 200 else 'failure')
