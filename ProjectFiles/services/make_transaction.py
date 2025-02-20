from utils import set_transaction_id
from datetime import datetime
from contextlib import contextmanager
from dbmanager import get_users, get_transactions, save_users, save_transactions
from copy import deepcopy
from models.transaction import Transaction
from dbmanager import USERS_FILE, TRANSACTIONS_FILE

def make_transaction(user):
    choice = 0
    print("""
\n\nMake transaction by:
1. Account number
2. Phone number
3. Personal ID
4. Exit
    """)
    try:
        choice = int(input("Enter choice (1-4): "))
        while choice < 1 or choice > 4:
            print("Invalid choice!")
            choice = int(input("Enter choice again (1-4): "))
    except ValueError as e:
        print("Value error: ", str(e))

    users_data = get_users(USERS_FILE)
    if choice == 1:
        print("Enter account number: ", end="")
        to_user = get_valid_user(user, "account_number")
        money = get_valid_money(user)
        process_transaction(user, to_user, money, users_data)
    elif choice == 2:
        print("Enter phone number: ", end="")
        to_user = get_valid_user(user, "phone_number")
        money = get_valid_money(user)
        process_transaction(user, to_user, money, users_data)
    elif choice == 3:
        print("Enter personal ID: ", end="")
        to_user = get_valid_user(user, "personal_id")
        money = get_valid_money(user)
        process_transaction(user, to_user, money, users_data)
    elif choice == 4:
        pass

@contextmanager
def transaction(database):
    backup = deepcopy(database)
    try:
        yield database
    except Exception:
        print("\n\n\033[1mSomething went wrong! Transaction failed!\033[0m\n\n")
        database.clear()
        database.extend(backup)

def process_transaction(from_user, to_user, money, users_data):
    transactions_data = get_transactions(TRANSACTIONS_FILE)

    with transaction(users_data) as db:
        from_user.make_transaction(to_user, money, db)

        transaction_id = set_transaction_id()
        while transaction_id in [transaction.id for transaction in transactions_data]:
            transaction_id = set_transaction_id()
        transaction_date = datetime.now().strftime("%Y-%m-%d")
        transactions_data.append(Transaction(transaction_id, from_user.id, to_user.id, money, transaction_date))

        save_users(USERS_FILE, db)
        save_transactions(TRANSACTIONS_FILE, transactions_data)
        print(f"\n\n\033[1mTransaction made sucessfully to {to_user.cardholder}!\033[0m\n\n")

# check if user with given key and proper value is already in database or same as active user
def get_valid_user(check_user, key):
    users_data = get_users(USERS_FILE)
    user_info = input()
    while not any(getattr(user, key, None) == user_info for user in users_data) or getattr(check_user, key, None) == user_info:
        user_info = input("User not found! Try again: ")
    
    return next((user for user in users_data if getattr(user, key, None) == user_info), None)

# check if money is negative or more than active user's balance
def get_valid_money(from_user):
    money = 0
    try:
        money = int(input("Enter money: "))
    except ValueError as e:
        print("Value error: ", str(e))
    
    while money <= 0 or money > from_user.balance:
        if money <= 0:
            print("Invalid input!")
        elif money > from_user.balance:
            print("You do not have enough balance to make transaction!")

        money = int(input("Enter money: "))

    return money