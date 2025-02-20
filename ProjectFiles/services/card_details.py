def card_details(user):
    password = input("Enter password again: ")
    while password != user.password:
        print("Incorrect Password!")
        password = input("Try again: ")
    
    user.get_card_details()