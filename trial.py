import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="varchasva",database="bank_management")

def create_account():
    name = input("Enter account holder's name: ")
    balance = float(input("Enter initial deposit amount: "))
    cursor = mydb.cursor()
    query = "insert into accounts (name, balance) values (%s, %s)"
    cursor.execute(query, (name, balance))
    mydb.commit()
    print("Account created successfully!")

def deposit_amount():
    account_number = int(input("Enter account number: "))
    deposit = float(input("Enter deposit amount: "))
    cursor = mydb.cursor()
    query = "update accounts set balance = balance + %s where account_number = %s"
    cursor.execute(query, (deposit, account_number))
    mydb.commit()
    print("Amount deposited successfully!")

def withdraw_amount():
    account_number = int(input("Enter account number: "))
    withdraw = float(input("Enter withdrawal amount: "))
    cursor = mydb.cursor()
    query = "select balance from accounts where account_number = %s"
    cursor.execute(query, (account_number,))
    result = cursor.fetchone()
    if result and result[0] >= withdraw:
        update_query = "update accounts set balance = balance - %s where account_number = %s"
        cursor.execute(update_query, (withdraw, account_number))
        mydb.commit()
        print("Amount withdrawn successfully!")
    else:
        print("Insufficient balance or account not found!")

def check_balance():
    account_number = int(input("Enter account number: "))
    cursor = mydb.cursor()
    query = "select balance from accounts where account_number = %s"
    cursor.execute(query, (account_number,))
    result = cursor.fetchone()
    if result:
        print(f"Account Balance: {result[0]}")
    else:
        print("Account not found!")

def delete_account():
    account_number = int(input("Enter account number to delete: "))
    confirm = input(f"Are you sure you want to delete account {account_number}? (yes/no): ").lower()
    if confirm == "yes":
        cursor = mydb.cursor()
        query = "delete from accounts where account_number = %s"
        cursor.execute(query, (account_number,))
        mydb.commit()
        if cursor.rowcount > 0:
            print("Account deleted successfully!")
        else:
            print("Account not found!")
    else:
        print("Account deletion cancelled.")

def transfer_money():
    from_account = int(input("Enter the account number to transfer from: "))
    to_account = int(input("Enter the account number to transfer to: "))
    amount = float(input("Enter the amount to transfer: "))

    cursor = mydb.cursor()
    
    query = "select balance from accounts where account_number = %s"
    cursor.execute(query, (from_account,))
    result = cursor.fetchone()
    
    if result and result[0] >= amount:
        update_from_query = "update accounts set balance = balance - %s where account_number = %s"
        cursor.execute(update_from_query, (amount, from_account))

        update_to_query = "update accounts set balance = balance + %s where account_number = %s"
        cursor.execute(update_to_query, (amount, to_account))

        mydb.commit()
        print(f"Transferred {amount} from account {from_account} to account {to_account}.")
    else:
        print("Insufficient balance or invalid account number!")

while True:
    print("\nBank Management System")
    print("1. Create Account")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Check Balance")
    print("5. Delete Account")
    print("6. Transfer Money")
    print("7. Exit")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        create_account()
    elif choice == 2:
        deposit_amount()
    elif choice == 3:
        withdraw_amount()
    elif choice == 4:
        check_balance()
    elif choice == 5:
        delete_account()
    elif choice == 6:
        transfer_money()
    elif choice == 7:
        print("Exiting the program.")
        mydb.close()
        break
    else:
        print("Invalid choice. Please try again.")