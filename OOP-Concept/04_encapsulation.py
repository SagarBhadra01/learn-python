'''
Encapsulation is about protecting data inside a class.
It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.
This prevents accidental changes to your data and hides the internal details of how your class works. 
'''

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder      #public attribute
        self.__balance = balance                  #private attribute
        self.__transaction_history = []          #private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transaction_history.append(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

    def get_transaction_history(self):
        return self.__transaction_history
    
# Example usage
account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())
print(account.get_transaction_history())
#print(account.__balance)  # This will raise an AttributeError      
#print(account.__transaction_history)  # This will raise an AttributeError
# Accessing private attributes using name mangling (not recommended)
#print(account._BankAccount__balance)
#print(account._BankAccount__transaction_history)
