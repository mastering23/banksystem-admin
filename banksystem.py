import os

# Define file paths
user_file = "user.txt"
account_file = "account.txt"
credit_file = "credit.txt"
loan_file = "loan.txt"


# Function to create files if they don't exist
def create_files():
    files = [user_file, account_file, credit_file, loan_file]
    for file in files:
        if not os.path.exists(file):
            with open(file, "w") as f:
                f.write("")  # Create an empty file
            print(f"{file} created.")


# Call the create_files function at the start
create_files()


# Function to handle user login
def userData(user, passwd):
    global password
    while True:
        if user != "user01" or password != "2025":
            print("Incorrect user or password. Please try again.")
            user = input("Enter user: ")
            password = input("Enter password: ")
        else:
            print("Login successful. Welcome!")
            break


# Call the userData function to handle login
user = input("Enter user: ")
password = input("Enter password: ")
userData(user, password)

# Define initial balance
balance = 1000.0


# Admin system to manage user data
def adminSystem():
    print("++++ Admin System ++++")
    while True:
        print("Choose an option: ")
        print("(1) Add new user")
        print("(2) View all users")
        print("(3) Edit user profile")
        print("(4) Delete user account")
        print("(5) Exit admin system")

        choice = input("Enter your choice: ")

        if choice == "1":
            addNewUser()
        elif choice == "2":
            viewUsers()
        elif choice == "3":
            editUserProfile()
        elif choice == "4":
            deleteUserAccount()
        elif choice == "5":
            break
        else:
            print("Invalid option, try again.")


# Function to add a new user
def addNewUser():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    address = input("Enter address: ")
    phone_number = input("Enter phone number: ")
    account_type = input("Enter account type (Credit/Saving/Loan): ")
    account_number = generateUniqueAccountNumber()

    # Save user details in user.txt
    with open(user_file, "a") as f:
        f.write(f"{account_number},{first_name},{last_name},{address},{phone_number},{account_type}\n")

    print(f"User added successfully! Account number: {account_number}")


# Function to generate a unique account number
def generateUniqueAccountNumber():
    if not os.path.exists(account_file):
        return 10001  # First account number

    with open(account_file, "r") as f:
        lines = f.readlines()
        if lines:
            last_account = int(lines[-1].split(",")[0])
            return last_account + 1
        else:
            return 10001


# Function to view all users
def viewUsers():
    if os.path.exists(user_file):
        with open(user_file, "r") as f:
            users = f.readlines()
            for user in users:
                print(user.strip())
    else:
        print("No users found.")


# Function to edit a user profile
def editUserProfile():
    account_number = input("Enter the account number to edit: ")

    if os.path.exists(user_file):
        with open(user_file, "r") as f:
            users = f.readlines()

        with open(user_file, "w") as f:
            for user in users:
                data = user.strip().split(",")
                if data[0] == account_number:
                    print("Editing user profile...")
                    new_first_name = input(f"Enter new first name (current: {data[1]}): ") or data[1]
                    new_last_name = input(f"Enter new last name (current: {data[2]}): ") or data[2]
                    new_address = input(f"Enter new address (current: {data[3]}): ") or data[3]
                    new_phone = input(f"Enter new phone number (current: {data[4]}): ") or data[4]
                    f.write(f"{account_number},{new_first_name},{new_last_name},{new_address},{new_phone},{data[5]}\n")
                    print("User profile updated.")
                else:
                    f.write(user)
    else:
        print("User not found.")


# Function to delete a user account
def deleteUserAccount():
    account_number = input("Enter the account number to delete: ")

    if os.path.exists(user_file):
        with open(user_file, "r") as f:
            users = f.readlines()

        with open(user_file, "w") as f:
            for user in users:
                data = user.strip().split(",")
                if data[0] == account_number:
                    print(f"Deleting account for {data[1]} {data[2]}")
                else:
                    f.write(user)
    else:
        print("No users found.")


# Main prompt for user actions
prompt = input("Type View (1) BALANCE || (2) Deposit || (3) Withdraw || (4) Exit || (00010admin) Admin System: ")

while True:
    match prompt:
        case "1":
            print(f"Your current balance is: ${balance}")
            break
        case "2":
            deposit = float(input("Enter deposit amount: "))
            balance += deposit
            print(f"Deposit successful! New balance: ${balance}")
            break
        case "3":
            withdraw = float(input("Enter withdrawal amount: "))
            if withdraw > balance:
                print("Insufficient funds!")
            else:
                balance -= withdraw
                print(f"Withdrawal successful! New balance: ${balance}")
            break
        case "00010admin":
            adminSystem()
            break
        case "4":
            print("Exiting the system. Goodbye!")
            break
        case _:
            print("Invalid option, please try again.")
            prompt = input("Type View (1) BALANCE || (2) Deposit || (3) Withdraw || (4) Exit || (00010admin) Admin System: ")
