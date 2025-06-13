# Bank Management System in Python

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = str(hash(account_holder))[:10]  # Generate a unique account number based on account holder's name

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited: ",amount, "Current balance: ",self.balance)

        else:
            print("Deposit amount should be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount should be positive.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Withdrew: ",amount , "Current balance: " , self.balance)

    def check_balance(self):
        print("Account balance:", self.balance)

    def get_account_details(self):
        print("Account Holder:",self.account_holder)
        print("Account Number:",self.account_number)
        print("Account Balance:",self.balance)


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name):
        if name not in self.accounts:
            account = BankAccount(name)
            self.accounts[name] = account
            print("Account created for",name)
        else:
            print("Account already exists for this holder.")

    def get_account(self, name):
        if name in self.accounts:
            return self.accounts[name]
        else:
            print("Account not found.")
            return None

    def display_all_accounts(self):
        if len(self.accounts) == 0:
            print("No accounts available.")
        else:
            for account in self.accounts.values():
                account.get_account_details()


# Main Function to interact with Bank Management System
def main():
    bank = Bank()

    while True:
        print("\n--- Bank Management System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Account Details")
        print("6. View All Accounts")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter account holder's name: ")
            bank.create_account(name)

        elif choice == '2':
            name = input("Enter account holder's name: ")
            account = bank.get_account(name)
            if account:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)

        elif choice == '3':
            name = input("Enter account holder's name: ")
            account = bank.get_account(name)
            if account:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)

        elif choice == '4':
            name = input("Enter account holder's name: ")
            account = bank.get_account(name)
            if account:
                account.check_balance()

        elif choice == '5':
            name = input("Enter account holder's name: ")
            account = bank.get_account(name)
            if account:
                account.get_account_details()

        elif choice == '6':
            bank.display_all_accounts()

        elif choice == '7':
            print("Exiting Bank Management System. Thank you!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
