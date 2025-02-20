import json
from models.user import User
from models.transaction import Transaction
from models.request import Request

USERS_FILE = "ProjectFiles/database/users.json"
TRANSACTIONS_FILE = "ProjectFiles/database/transactions.json"
REQUESTS_FILE = "ProjectFiles/database/requests.json"

def get_users(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            if not content.strip():
                return []
            users_dict = json.loads(content)

            users = []
            for id, user_data in users_dict.items():
                user = User(
                    id,
                    user_data["Balance"],
                    user_data["Cardholder"],
                    user_data["Card number"],
                    user_data["Expiration date"],
                    user_data["CVV"],
                    user_data["Account number"],
                    user_data["Phone number"],
                    user_data["Personal ID"],
                    user_data["Username"],
                    user_data["Password"]
                )
                users.append(user)
            return users
    except FileNotFoundError:
        print("Error occcurred: File not found!")
        return []

def get_transactions(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            if not content.strip():
                return []
            transactions_dict = json.loads(content)

            transactions = []
            for id, transactions_data in transactions_dict.items():
                transaction = Transaction(
                    id,
                    transactions_data["From"],
                    transactions_data["To"],
                    transactions_data["Amount"],
                    transactions_data["Date"]
                )
                transactions.append(transaction)
            return transactions
    except FileNotFoundError:
        print("Error occcurred: File not found!")
        return []

def get_requests(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            if not content.strip():
                return []
            requests_dict = json.loads(content)

            requests = []
            for id, requests_data in requests_dict.items():
                request = Request(
                    id,
                    requests_data["From"],
                    requests_data["To"],
                    requests_data["Amount"],
                    requests_data["Message"],
                    requests_data["Status"]
                )
                requests.append(request)
            return requests
    except FileNotFoundError:
        print("Error occcurred: File not found!")
        return []

def save_users(file_name, users):
    users_data = {user.id: user.to_dict() for user in users}
    try:
        with open(file_name, 'w') as file:
            json.dump(users_data, file, indent=4)
    except FileNotFoundError:
        print("Error occcurred: File not found!")


def save_transactions(file_name, transactions):
    transactions_data = {transaction.id: transaction.to_dict() for transaction in transactions}
    try:
        with open(file_name, 'w') as file:
            json.dump(transactions_data, file, indent=4)
    except FileNotFoundError:
        print("Error occcurred: File not found!")

def save_requests(file_name, requests):
    reqeusts_data = {request.id: request.to_dict() for request in requests}
    try:
        with open(file_name, 'w') as file:
            json.dump(reqeusts_data, file, indent=4)
    except FileNotFoundError:
        print("Error occcurred: File not found!")