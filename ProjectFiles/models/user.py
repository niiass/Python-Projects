class User:
    def __init__(self, id, balance, cardholder, card_number, exp_date, cvv, acc_number, phone_number, personal_id, username, password):
        self.id = id
        self.balance = balance
        self.cardholder = cardholder
        self.card_number = card_number
        self.expiration_date = exp_date
        self.cvv = cvv
        self.account_number = acc_number
        self.phone_number = phone_number
        self.personal_id = personal_id
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            "Balance": self.balance,
            "Cardholder": self.cardholder,
            "Card number": self.card_number,
            "Expiration date": self.expiration_date,
            "CVV": self.cvv,
            "Account number": self.account_number,
            "Phone number": self.phone_number,
            "Personal ID": self.personal_id,
            "Username": self.username,
            "Password": self.password
        }

    def convert(self, rate, currency):
        try:
            return f"You have {round(self.balance/rate, 2)} {currency}"
        except ZeroDivisionError:
            print("Rate is 0!")
            return None
    
    def get_card_details(self):
        print(f"\n\n\033[1mCard number: {self.card_number}\033[0m")
        print(f"\033[1mExpiration date: {self.expiration_date}\033[0m")
        print(f"\033[1mCVV: {self.cvv}\033[0m\n\n")

    def make_transaction(self, to_user, money, database):
        for user in database:
            if self.id == user.id:
                user.balance -= money
            if to_user.id == user.id:
                user.balance += money
    
    def __str__(self):
         return f"Balance: {self.balance}, Cardholder: {self.cardholder}, Card number: {self.card_number}, Expiration date: {self.expiration_date}, CVV: {self.cvv}, Account number: {self.account_number}, Phone number: {self.phone_number}, Personal ID: {self.personal_id}, Username: {self.username}, Password: {self.password}"
