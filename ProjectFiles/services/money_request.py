from services.make_transaction import get_valid_user, process_transaction
from models.request import Request
from dbmanager import get_requests, save_requests, get_users, save_users
from dbmanager import REQUESTS_FILE, USERS_FILE
from utils import set_request_id


# because of the same logic here are used some functions from make_transaction.py file
def ask_for_money(user):
    choice = 0
    print("""
\n\nMake request by:
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

    if choice == 1:
        print("Enter account number: ", end="")
        to_user = get_valid_user(user, "account_number")
        process_request(user, to_user)
    elif choice == 2:
        print("Enter phone number: ", end="")
        to_user = get_valid_user(user, "phone_number")
        process_request(user, to_user)
    elif choice == 3:
        print("Enter personal ID: ", end="")
        to_user = get_valid_user(user, "personal_id")
        process_request(user, to_user)
    elif choice == 4:
        pass

def process_request(from_user, to_user):
    money = 0
    try:
        money = int(input("Enter money to request: "))
    except ValueError as e:
        print("Value error: ", str(e))
    
    while money <= 0:
        print("Invalid input!")
        money = int(input("Enter money to request: "))

    message = input("Leave a message: ")

    requests_data = get_requests(REQUESTS_FILE)
    request_id = set_request_id()
    while request_id in [request.id for request in requests_data]:
        request_id = set_request_id()

    # status gets 0 means that request is not responded
    requests_data.append(Request(request_id, from_user.id, to_user.id, money, message, 0))
    save_requests(REQUESTS_FILE, requests_data)
    print(f"\n\n\033[1mRequest sent sucessfully to {to_user.cardholder}!\033[0m\n\n")

def check_requests(request_getter):
    requests_data = get_requests(REQUESTS_FILE)
    users_data = get_users(USERS_FILE)
    received_requests = []
    for request in requests_data:
        if request_getter.id == request.to_user_id and request.status == 0:
            received_requests.append(request)
    
    if received_requests:
        for received_request in received_requests:
            request_sender = next(user for user in users_data if user.id == received_request.from_user_id)
            print(f"Request from: {request_sender.cardholder}\n{received_request}")
            choice = 'n'
            try:
                choice = input("Will you accept the request? (y/n): ")
                while choice.lower() not in ['y', 'n']:
                    choice = input("Incorrect input! Try again (y/n): ")
            except ValueError:
                print("Invalid input! Request has been declined!")
            
            if choice == 'y':
                process_transaction(request_getter, request_sender, received_request.amount, users_data)
                save_users(USERS_FILE, users_data)
            elif choice == 'n':
                print("Request declined!")
                continue
            
            # mark request as responded
            received_request.status = 1
        save_requests(REQUESTS_FILE, requests_data)
    else:
        print("\033[1mNo requests!\033[0m\n\n")