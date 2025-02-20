class Request:
    def __init__(self, id, from_user, to_user, amount, message, status):
        self.id = id
        self.from_user_id = from_user
        self.to_user_id = to_user
        self.amount = amount
        self.message = message
        self.status = status
    
    def to_dict(self):
        return {
            "From": self.from_user_id,
            "To": self.to_user_id,
            "Amount": self.amount,
            "Message": self.message,
            "Status": self.status
        }
    
    def __str__(self):
        return f"Money requested: {self.amount}\nMessage: {self.message}"