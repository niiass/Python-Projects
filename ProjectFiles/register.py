from datetime import datetime
from utils import set_expriration_date, set_account_number, set_card_number, set_cvv, set_user_id, password_checker, is_in_db
from dbmanager import get_users, save_users
from models.user import User
from dbmanager import USERS_FILE

def register():
    balance = 1000

    cardholder = input("Enter cardholder name: ")
    while not cardholder or cardholder.isspace():
        print("Cardholder name is not valid!")
        cardholder = input("Enter cardholder name again: ")

    personal_id = input("Enter personal ID: ")
    while len(personal_id) != 11 or not personal_id.isdecimal() or is_in_db(personal_id, "personal_id"):
        if is_in_db(personal_id, "personal_id"):
            print("Personal ID already exists!")
        else:
            print("Personal ID must have 11 digits!")
        personal_id = input("Enter personal ID again: ")

    phone_number = input("Enter phone number: ")
    while len(phone_number) !=  9 or not phone_number.isdecimal() or is_in_db(phone_number, "phone_number"):
        if is_in_db(phone_number, "phone_number"):
            print("Phone number already exists!")
        else:
            print("Phone number must have 9 digits!")
        phone_number = input("Enter phone number again: ")

    username = input("Enter username: ")
    while len(username) < 5 or username.isspace() or is_in_db(username, "username"):
        if is_in_db(username, "username"):
            print("Username already exists!")
        else:
            print("Username must have at least 5 characters!")
        username = input("Enter username again: ")

    print("Password requirements:")
    print("➙ At least one uppercase letter")
    print("➙ At least one lowercase letter")
    print("➙ At least one number (0-9)")
    print("➙ At least eight characters")
    password = input("Enter password: ")
    while not password_checker(password):
        print("Password must meet the requirements!")
        password = input("Enter password again: ")

    creation_time = datetime.now()
    exp_date = set_expriration_date(creation_time.month, creation_time.year)

    card_number = set_card_number()
    while is_in_db(card_number, "card_number"):
        card_number = set_card_number()

    cvv = set_cvv()
    while is_in_db(cvv, "cvv"):
        cvv = set_cvv()

    acc_number = set_account_number()
    while is_in_db(acc_number, "account_number"):
        acc_number = set_account_number()

    id = set_user_id()
    while is_in_db(acc_number, "id"):
        id = set_user_id()

    users_data = get_users(USERS_FILE)
    users_data.append(User(id, balance, cardholder, card_number, exp_date, cvv, acc_number, phone_number, personal_id, username, password))
    save_users(USERS_FILE, users_data)

    print("\n\n\033[1mRegistered successfully!\033[0m\n\n")