account1_owner = None
account1_number = None
account1_balance = 0.0

account2_owner = None
account2_number = None
account2_balance = 0.0

account3_owner = None
account3_number = None
account3_balance = 0.0

while True:
    print("\nSimple Banking System")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Account Details")
    print("5. Exit")
    choice = input("Select an option (1-5): ")
    if choice == '1':
        owner = input("Enter account owner's name: ")
        account_number = int(input("Enter account number: "))

        if account1_number == account_number or account2_number == account_number or account3_number == account_number:
            print("Account number already exists.")
        elif account1_owner is None:
            account1_owner = owner
            account1_number = account_number
            print("Account created successfully.")
        elif account2_owner is None:
            account2_owner = owner
            account2_number = account_number
            print("Account created successfully.")
        elif account3_owner is None:
            account3_owner = owner
            account3_number = account_number
            print("Account created successfully.")
        else:
            print("Cannot create more than 3 accounts.")
    elif choice == '2':
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter amount to deposit: "))
        if account1_number == account_number:
            account1_balance += amount
            print("Deposit successful. New balance:", account1_balance)
        elif account2_number == account_number:
            account2_balance += amount
            print("Deposit successful. New balance:", account2_balance)
        elif account3_number == account_number:
            account3_balance += amount
            print("Deposit successful. New balance:", account3_balance)
        else:
            print("Account not found.")
    elif choice == '3':
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter amount to withdraw: "))
        if account1_number == account_number:
            if 0 < amount <= account1_balance:
                account1_balance -= amount
                print(f"${amount} withdrawn successfully. New balance:", account1_balance)
            elif amount > account1_balance:
                print("Insufficient funds.")
            else:
                print("Invalid amount.")
        elif account2_number == account_number:
            if 0 < amount <= account2_balance:
                account2_balance -= amount
                print(f"${amount} withdrawn successfully. New balance:", account2_balance)
            elif amount > account2_balance:
                print("Insufficient funds.")
            else:
                print("Invalid amount.")
        elif account3_number == account_number:
            if 0 < amount <= account3_balance:
                account3_balance -= amount
                print(f"${amount} withdrawn successfully. New balance:", account3_balance)
            elif amount > account3_balance:
                print("Insufficient funds.")
            else:
                print("Invalid amount.")
        else:
            print("Account not found.")

    elif choice == '4':
        account_number = int(input("Enter account number: "))
        if account1_number == account_number:
            print(f"Account Owner: {account1_owner}")
            print(f"Account Number: {account1_number}")
            print(f"Account Balance: ${account1_balance:.2f}")
        elif account2_number == account_number:
            print(f"Account Owner: {account2_owner}")
            print(f"Account Number: {account2_number}")
            print(f"Account Balance: ${account2_balance:.2f}")
        elif account3_number == account_number:
            print(f"Account Owner: {account3_owner}")
            print(f"Account Number: {account3_number}")
            print(f"Account Balance: ${account3_balance:.2f}")
        else:
            print("Account not found.") 
    elif choice == '5':
        print("Exiting the system. Goodbye!")
        break            
    else:
        print("Invalid option. Please try again.")