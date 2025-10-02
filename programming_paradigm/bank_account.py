# Bank account


class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance
        
    # Add or deposit the amount to account_balance
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        else:
            print("Deposit amout must be positive")
            return False
        
    # Deduct the amount from account_balance if funds are sufficient
    def withdraw(self, amount):
        if amount <=0:
            print("Withdrawal amount must be positive")
            return False
        elif amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
        
    # Print the current balance in a user-friendly format
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")