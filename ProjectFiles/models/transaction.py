from datetime import datetime

class Transaction:
    def __init__(self, id, from_user, to_user, amount, date):
        self.id = id
        self.from_user_id = from_user
        self.to_user_id = to_user
        self.amount = amount
        self.date = date
    
    def to_dict(self):
        return {
            "From": self.from_user_id,
            "To": self.to_user_id,
            "Amount": self.amount,
            "Date": self.date
        }
    
    def get_debits(self, user_id, date_months_ago):
        if user_id == self.from_user_id and datetime.strptime(self.date, "%Y-%m-%d").date() > date_months_ago:
            print(f"On {self.date} - {self.amount}")
            return float(self.amount)
        return 0

    def get_credits(self, user_id, date_months_ago):
        if user_id == self.to_user_id and datetime.strptime(self.date, "%Y-%m-%d").date() > date_months_ago:
            print(f"On {self.date} - {self.amount}")
            return float(self.amount)
        return 0
        