# Function to withdraw money from account
def withdraw(account, amount):
    if amount > account['balance']:
        print("Insufficient funds!")
    else:
        account['balance'] -= amount
        account['transactions'].append(f"Withdrawal: ${amount}")
        print(f"Withdrawal successful. Remaining balance: ${account['balance']}")
        file = open('transactions.txt', 'a')
        file.write(f"Withdrawal: ${amount}\n")
        file.close()
    
# Function to deposit money into account
def deposit(account, amount):
    account['balance'] += amount
    account['transactions'].append(f"Deposit: ${amount}")
    print(f"Deposit successful. Remaining balance: ${account['balance']}")
    file = open('transactions.txt', 'a')
    file.write(f"Deposit: ${amount}\n")
    file.close()

# Function to get account balance
def get_balance(account):
    return account['balance'] 

# Function to get transaction history
def get_transaction_history(account):
    file = open('transactions.txt', 'r')
    transactions = file.readlines()
    file.close()
    return transactions

# Create an account dictionary
account = {
    'balance': 1000,
    'transactions': []
}
#login
mail=["sathvik","tagore","zeeshan"]
password=[123,456,789]
umail=str(input("enter mailid "))
upassword=int(input("enter password ")) 
for i in range(0,3):
    if(mail[i] == umail):
        if(password[i] == upassword):
            print("Login successfull")
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
                        choices[choice](account, amount)
                    else:
                        print(choices[choice](account))
                else:
                    print("Invalid choice. Please try again.")
        else:
             print("Invalid mailid or password")
