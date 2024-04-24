# Define a function to load user data from a file
def load_user_data(filename):
    users = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                email, password, balance, *transactions = line.strip().split(',')
                users[email] = {
                    'password': password,
                    'balance': float(balance),
                    'transactions': transactions
                }
    except FileNotFoundError:
        pass
    return users

# Define a function to save user data to a file
def save_user_data(filename, users):
    with open(filename, 'w') as file:
        for email, data in users.items():
            transactions = ','.join(data['transactions'])
            file.write(f"{email},{data['password']},{data['balance']},{transactions}\n")

# Define the banking operations functions
# ... (Your existing functions here)

# Define the main function
def main():
    users = load_user_data('users.txt')
    umail = input("Enter mailid: ")
    upassword = input("Enter password: ")
    user = users.get(umail)
    if user and user['password'] == upassword:
        print("Login successful")
        account = user
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
    save_user_data('users.txt', users)

# Run the main function
if __name__ == "__main__":
    main()
