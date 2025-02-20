from datetime import datetime
import requests

# get current currency rates from currencies json file of national bank of gerogia
def get_currency_rates():
    today_date = datetime.now().strftime("%Y-%m-%d")
    api_url = f"https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/en/json/?date={today_date}"

    try:
        response = requests.get(api_url)
        response.raise_for_status() 
        data = response.json()
        return data
    except ValueError as e:
        print("Value Error: ", str(e))
        return None

# choose and convert in any currency available in national bank
def convert(user):
    rates = get_currency_rates()
    if rates:
        currencies = [currency for currency in rates[0]["currencies"]]
        currencies_size = len(currencies)
        print("\nChoose currency to convert in:")
        for i in range(currencies_size):
            print(f"{i+1}. {currencies[i]['code']} - {currencies[i]['name']}")
        print(f"{currencies_size + 1}. Exit\n")

        choice = currencies_size + 1
        try:
            choice = int(input(f"Enter choice (1-{currencies_size}): "))
            while choice < 1 or choice > currencies_size + 1:
                print("Invalid choice!")
                choice = int(input(f"Enter choice again (1-{currencies_size}): "))
        except ValueError as e:
            print("Invalid input!")
        
        if choice != currencies_size + 1:
            print(f"\n\033[1m{user.convert(currencies[choice-1]['rate'], currencies[choice-1]['code'])}\033[0m\n")