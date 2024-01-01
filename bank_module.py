# bank_module.py

class Bank:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful. Current balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful. Current balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

# main_script.py

from bank_module import Bank

def display_menu():
    print("\nMenu:")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Initialize the initial balance to 50000
initial_balance = 50000.0

my_bank = Bank(initial_balance)

while True:
    user_choice = display_menu()

    if user_choice == 1:
        # Check Balance
        print(f"Current balance: ${my_bank.check_balance()}")

    elif user_choice == 2:
        # Withdraw
        try:
            withdraw_amount = float(input("Enter the amount to withdraw: $"))
            my_bank.withdraw(withdraw_amount)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif user_choice == 3:
        # Deposit
        try:
            deposit_amount = float(input("Enter the amount to deposit: $"))
            my_bank.deposit(deposit_amount)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif user_choice == 4:
        # Exit
        print("Exiting the program. Thank you!")
        break
