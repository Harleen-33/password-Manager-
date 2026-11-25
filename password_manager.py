
import json
import os

FILE_NAME = "passwords.json"


# Load saved accounts
def load_accounts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []


# Save accounts
def save_accounts(accounts):
    with open(FILE_NAME, "w") as file:
        json.dump(accounts, file, indent=4)


# Add a new account
def add_account():
    print("\n--- ADD NEW ACCOUNT ---")

    website = input("Website/App name: ").strip()
    username = input("Username/Email: ").strip()
    password = input("Password (use dummy data): ").strip()

    if not website or not username or not password:
        print("All fields are required!")
        return

    accounts = load_accounts()

    account = {
        "website": website,
        "username": username,
        "password": password
    }

    accounts.append(account)
    save_accounts(accounts)

    print("Account added successfully!")


# View all accounts
def view_accounts():
    print("\n--- SAVED ACCOUNTS ---")

    accounts = load_accounts()

    if not accounts:
        print("No accounts found.")
        return

    for number, account in enumerate(accounts, start=1):
        print("\nAccount:", number)
        print("Website:", account["website"])
        print("Username:", account["username"])
        print("Password:", account["password"])


# Search an account
def search_account():
    print("\n--- SEARCH ACCOUNT ---")

    accounts = load_accounts()
    search = input("Enter website name: ").strip().lower()

    found = False

    for account in accounts:
        if search == account["website"].lower():
            print("\nAccount found!")
            print("Website:", account["website"])
            print("Username:", account["username"])
            print("Password:", account["password"])
            found = True

    if not found:
        print("Account not found.")


# Update an account
def update_account():
    print("\n--- UPDATE ACCOUNT ---")

    accounts = load_accounts()
    website = input("Enter website name: ").strip().lower()

    for account in accounts:
        if account["website"].lower() == website:

            print("1. Update Username")
            print("2. Update Password")

            choice = input("Enter your choice: ")

            if choice == "1":
                account["username"] = input("New username: ").strip()
            elif choice == "2":
                account["password"] = input("New password: ").strip()
            else:
                print("Invalid choice.")
                return

            save_accounts(accounts)
            print("Account updated successfully!")
            return

    print("Account not found.")


# Delete an account
def delete_account():
    print("\n--- DELETE ACCOUNT ---")

    accounts = load_accounts()
    website = input("Enter website name: ").strip().lower()

    for account in accounts:
        if account["website"].lower() == website:

            confirm = input("Confirm deletion? (yes/no): ").lower()

            if confirm == "yes":
                accounts.remove(account)
                save_accounts(accounts)
                print("Account deleted successfully!")
            else:
                print("Deletion cancelled.")

            return

    print("Account not found.")


# Main menu
def main():
    while True:
        print("\n" + "=" * 35)
        print("         PASSWORD MANAGER")
        print("=" * 35)

        print("1. Add New Account")
        print("2. View Saved Accounts")
        print("3. Search Account")
        print("4. Update Account")
        print("5. Delete Account")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            add_account()

        elif choice == "2":
            view_accounts()

        elif choice == "3":
            search_account()

        elif choice == "4":
            update_account()

        elif choice == "5":
            delete_account()

        elif choice == "6":
            print("Thank you for using Password Manager!")
            break

        else:
            print("Invalid choice! Please try again.")


main()
