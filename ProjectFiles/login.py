from services.convert import convert
from services.make_transaction import make_transaction
from services.finances import my_finances
from services.money_request import ask_for_money
from dbmanager import get_users
from services.money_request import check_requests
from services.card_details import card_details
from dbmanager import USERS_FILE
import time

def login():
    users_data = get_users(USERS_FILE)
    if users_data:
        user_username = input("Enter username: ")
        while user_username not in [user.username for user in users_data]:
            print("Username not found!")
            user_username = input("Enter username again: ")
        
        for user in users_data:
            if user.username == user_username:
                current_user = user

        password = input("Enter password: ")
        while password != current_user.password:
            print("Password is incorrect!")
            password = input("Enter password again: ")

        print("Log in successful!\n")
        
        login_menu(current_user)
    else:
        print("There are no users!")

def login_menu(user):
    choice = 0
    while choice != 6:
        choice = 0
        # refresh user's data after each service
        users_data = get_users(USERS_FILE)
        user = next((u for u in users_data if u.id == user.id), user)

        print(f"Your balance: {user.balance}₾")
        print(f"Your account number: {user.account_number}\n")
        check_requests(user)
        time.sleep(2)
        print("1. Convert")
        print("2. My finances")
        print("3. Card details")
        print("4. Make transaction")
        print("5. Ask for money")
        print("6. Exit")
        try:
            while choice not in [1, 2, 3, 4, 5, 6]:
                choice = int(input("Enter your choice: "))
        except ValueError as e:
            print("Value error: ", str(e))
            
        if choice == 1:
            convert(user)
        elif choice == 2:
            my_finances(user)
        elif choice == 3:
            card_details(user)
        elif choice == 4:
            make_transaction(user)
        elif choice == 5:
            ask_for_money(user)
        elif choice == 6:
            continue
        time.sleep(2)