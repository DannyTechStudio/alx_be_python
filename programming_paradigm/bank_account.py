
"""
CLASS BankAccount:

    METHOD __init__(initial_balance = 0):
        TRY:
            account_balance ← load_balance()
        EXCEPT FileNotFoundError:
            account_balance ← initial_balance
            save_balance()

    METHOD load_balance():
        TRY:
            OPEN "balance.txt" in read mode
            READ content and remove extra spaces
            IF content is empty:
                RETURN 0
            ELSE:
                RETURN content converted to float
        EXCEPT FileNotFoundError:
            RETURN 0

    METHOD save_balance():
        OPEN "balance.txt" in write mode
        WRITE account_balance to file
        CLOSE file

    METHOD deposit(amount):
        account_balance ← account_balance + amount
        CALL save_balance()

    METHOD withdraw(amount):
        IF amount <= account_balance:
            account_balance ← account_balance - amount
            CALL save_balance()
            RETURN True
        ELSE:
            RETURN False

    METHOD display_balance():
        PRINT "Your current balance is $" + account_balance

"""

class BankAccount:
    
    def __init__(self, initial_balance=0):
        try:
            self.account_balance = self.load_balance()
        except FileNotFoundError:
            self.account_balance = initial_balance
            self.save_balance()
        
    def load_balance(self):
        try:
            with open("balance.txt", "r") as file:
                content = file.read().strip()
                if content == '':
                    return 0
                return float(content)
        except FileNotFoundError:
            return 0
            
    def save_balance(self):
        with open("balance.txt", "w") as file:
            file.write(str(self.account_balance))
    
    def deposit(self, amount):
        self.account_balance += amount
        self.save_balance()
    
    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            self.save_balance()
            return True
        else:
            return False
    
    def display_balance(self):
        print(f"Your current balance is ${self.account_balance}")