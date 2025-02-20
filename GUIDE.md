# eBank – Mobile Bank

**eBank** is a mobile banking application that offers users a variety of features.
At the initial stage, users must register or log in with an existing account.

---

# Project Description


## 📝 1. Registration

During registration, users must enter the following information:
- **Cardholder's Name**  
- **Personal ID Number**  
- **Phone Number**  
- **Username**  
- **Password** (must meet specific requirements)

After successful registration, the system **automatically generates**:
- Card expiration date (4 years from the creation date)
- Random card number
- Three-digit CVV code
- Account number in the format: `GE##EB################`  
- Unique twelve-symbol alphanumeric ID
- 1,000 GEL balance

---

## 🔑 2. Login

Users log into the system using their pre-registered **username and password**. After logging in, the screen displays:
- Available balance on the card (in GEL)
- Card account number
- A menu with various functionalities

---

### 📋 2.1. Currency Conversion
- Convert money to the desired currency based on the current exchange rate of the National Bank of Georgia.

---

### 📊 2.2. My Finances
- View income and expenses for the following periods:
  - Last **1 month**
  - Last **3 months**
  - Last **6 months**
  - Last **12 months**
  - From the date of card creation.

---

### 💳 2.3. Card Details
- The user re-enters the password.
- The screen displays the card details:
  - **Card number**  
  - **Expiration Date**  
  - **CVV code**

---

### 💸 2.4. Transaction Execution
Transactions can be made using the following methods:
1. **By account number**  
2. **By phone number**  
3. **By personal ID number**

---

### 🤝 2.5. Request Money
- Request money from another user or receive a money request.

---

# Project Structure

**🛠️The system structure is divided into several folders and files, each serving a specific purpose🛠️**

1. **Main Folders and Their Purpose 📂**
- ***database/ 💾***
  - This folder stores information related to users, transactions, and requests. 🗂️
It consists of three `.json` files:

  - **users.json**: 📋 Stores registered user data (*balance, name, card number, expiration date, CVV code, account number, phone number, personal ID, username, password*).

  - **transactions.json**: 💸 Stores transaction details (*sender, receiver, amount, transaction date*).

  - **requests.json**: 📨 Stores money request data (*request sender, request recipient, amount, message*).

- ***models/ 🧩***

  - This folder contains files describing the project's "core components."
  - **user.py**: 👤 Defines user profiles (e.g., name, card number, balance).
  - **transaction.py**: 🔄 Describes transactions (money transfers between users).
  - **request.py**: 📩 Defines money requests.

- ***services/ 🛠️***

  - This folder contains the main functionality of the application.
  - **card_details.py**: 💳 Retrieves card details (card number, expiration date, CVV code).
  - convert.py: 🔄 Converts currency based on the exchange rate.
  - **finances.py**: 💰 Provides financial details for a selected period.
  - **make_transaction.py**: ✉️ Handles transaction execution.
  - **money_request.py**: 📨 Manages money requests.
  - **utils.py**: ⚙️ Contains helper functions used across different files.

2. **Other Files and Their Purpose 🗃️**

- ***dbmanager.py 🗄️***

  - Manages the project's "database" (`users.json`, `transactions.json`, `requests.json`).
  - Ensures data storage and updates.

- ***utils.py ⚙️***
  - Contains functions for random data generation during registration and shared logic for various files.

- ***login.py and register.py 👥***

  - login.py: Handles user authentication and service selection. 🔑
  - register.py: Handles user registration. 📝

- ***main.py 🌐***

  - The main file that integrates all components and functionalities.

- ***GUIDE.md 📘***

  - A guide to help users understand and use the program, providing a complete project overview. 💡

---

# Appendix
📦 Required Python modules for the project:
 - **python-dateutil 🗓️**
   - ❗ Needs to be installed: pip install python-dateutil
   - 📊 Used for retrieving financial data within a specific period
 - **time ⏳**
   - 🖥️ Used for convenient output formatting
   - ⏸️ Delays program execution by two seconds to display service results
 - **datetime 📅**
   - 🛠️ Used for handling card expiration dates
 - **json 📂**
   - 📋 Used for managing database files

---

# Contact 

- 👤 **Developer:** Nia Gogilidze  
- 📧 **Gmail:** gogilidzenia@gmail.com
- 🐱‍💻 **GitHub:** [niiass](https://github.com/niiass)  
- 🌐 **Social Media:** [Nia Gogilidze](https://www.linkedin.com/in/nia-gogilidze/) 

---
## 🌟 **eBank** – A fast and convenient way to manage your finances! 🌟