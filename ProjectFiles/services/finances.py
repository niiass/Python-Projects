from datetime import datetime
from dateutil.relativedelta import relativedelta
from dbmanager import get_transactions
from dbmanager import TRANSACTIONS_FILE

def my_finances(user):
    print("""
View your finances in the last:
• 1 month
• 3 months
• 6 months
• 12 months
• Since card creation
    """)

    choice = -1
    try:
        choice = int(input("Enter your choice (1/3/6/12/0): "))
        while choice not in [0, 1, 3, 6, 12]:
            choice = int(input("Enter your choice again (1/3/6/12/0): "))
    except ValueError as e:
        print("Value error: ", str(e))

    if choice == -1:
        print("Invalid input!")
    elif choice == 0:
        get_finances(user, 48)
    else:
        get_finances(user, choice)

def get_finances(user, months_range):
    transactions = get_transactions(TRANSACTIONS_FILE)
    current_date = datetime.now().date()
    date_months_ago = current_date - relativedelta(months=months_range)

    print("\n\nDebits:")
    total_debits = 0
    for transaction in transactions:
        total_debits += transaction.get_debits(user.id, date_months_ago)

    print("\n\nCredits:")
    total_credits = 0
    for transaction in transactions:
        total_credits += transaction.get_credits(user.id, date_months_ago)
    
    print(f"\n\n\033[1mTotal debits: {total_debits}\033[0m")
    print(f"\033[1mTotal credits: {total_credits}\033[0m\n\n")