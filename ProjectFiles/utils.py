import random
import string
from dbmanager import get_users, USERS_FILE

def set_expriration_date(month, year):
    return f"{month}/{year+4}"

def set_card_number():
    card_num = "4"
    for i in range(15):
        card_num += str(random.randint(0, 9))
        if i % 4 == 2 and i != 14:
            card_num += " "
    return card_num

def set_cvv():
    return random.randint(100, 999)

def set_account_number():
    acc_number = "GE" + str(random.randint(10, 99)) + "EB"
    for _ in range(16):
        acc_number += str(random.randint(0, 9))
    return acc_number

def set_user_id():
    id = ""
    for i in range(12):
        id += chr(random.choice(list(range(48, 58)) + list(range(97, 123))))
        if i % 4 == 3 and i != 11:
            id += "-"
    return id

def set_transaction_id():
    transaction_id = ""
    for i in range(16):
        transaction_id += chr(random.choice(list(range(48, 58)) + list(range(97, 123))))
        if i % 4 == 3 and i != 15:
            transaction_id += "-"
    return transaction_id

def set_request_id():
    transaction_id = ""
    for i in range(8):
        transaction_id += chr(random.choice(list(range(48, 58)) + list(range(97, 123))))
        if i % 4 == 3 and i != 7:
            transaction_id += "-"
    return transaction_id

def password_checker(password):
    if len(password) < 8:
        return False
    if not any(char in password for char in string.ascii_lowercase):
        return False
    if not any(char in password for char in string.ascii_uppercase):
        return False
    if not any(char in password for char in string.digits):
        return False
    return True


def is_in_db(var, key):
    users_data = get_users(USERS_FILE)
    if users_data:
        return any(getattr(user, key, None) == var for user in users_data)
    return False