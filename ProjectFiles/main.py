from register import register
from login import login

def main_menu():
    exit_session = False
    while not exit_session:
        print("1. Register\n2. Log In\n3. Exit")
        choice = 0
        try:
            while choice not in [1, 2, 3]:
                choice = int(input("Enter your choice: "))
        except ValueError as e:
            print("Value error: ", str(e))

        if choice == 1:
            register()
        elif choice == 2:
            login()
        elif choice == 3:
            exit_session = True

def main():
    print("Welcome to eBank - Mobile Bank!")
    main_menu()

if __name__ == "__main__":
    main()