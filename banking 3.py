from datetime import datetime

# Function to withdraw money from account
def withdraw(account, amount):
    # Check for daily transaction limit
    today_transactions = [t for t in account['transactions'] if t[1] == datetime.now().date()]
    if len(today_transactions) >= 5:
        print("Daily transaction limit reached!")
        return
    # Check for withdrawal limit
    if amount > 10000:
        print("Cannot withdraw more than $10000 per transaction!")
        return
    # Check for sufficient funds
    if amount > account['balance']:
        print("Insufficient funds!")
        return
    # Perform withdrawal
    account['balance'] -= amount
    account['transactions'].append(("Withdrawal", amount, datetime.now().date()))
    print(f"Withdrawal successful. Remaining balance: ${account['balance']}")

# Function to deposit money into account
def deposit(account, amount):
    # Check for daily transaction limit
    today_transactions = [t for t in account['transactions'] if t[1] == datetime.now().date()]
    if len(today_transactions) >= 5:
        print("Daily transaction limit reached!")
        return
    # Perform deposit
    account['balance'] += amount
    account['transactions'].append(("Deposit", amount, datetime.now().date()))
    print(f"Deposit successful. Remaining balance: ${account['balance']}")

# Function to get account balance
def get_balance(account):
    return account['balance']

# Function to get transaction history
def get_transaction_history(account):
    return account['transactions']

# Create an account dictionary for each user
accounts = {
    'sathvik': {'balance': 1000, 'transactions': []},
    'tagore': {'balance': 2000, 'transactions': []},
    'zeeshan': {'balance': 3000, 'transactions': []}
}

# User login
umail = input("Enter mailid: ")
upassword = int(input("Enter password: ")) 

# Check if mail and password match
for mail, account in accounts.items():
    if mail == umail and account['password'] == upassword:
        print("Login successful")
        # Dictionary to map user choices to functions
        choices = {
            '1': deposit,
            '2': withdraw,
            '3': get_balance,
            '4': get_transaction_history
        }

        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transaction History")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '5':
                print("Exiting program.")
                break

            if choice in choices:
                if choice == '1' or choice == '2':
                    amount = float(input("Enter amount: "))
                    choiceschoice
                else:
                    result = choiceschoice
                    if choice == '4':  # Transaction history
                        for transaction in result:
                            print(f"{transaction[0]} of ${transaction[1]} on {transaction[2]}")
                    else:
                        print(result)
            else:
                print("Invalid choice. Please try again.")
        break
else:
    print("Invalid mailid or password")
