#Demonstration of Encapsulation

class BankAccount:
    def __init__(self, name, balance):
        self.name = name          # Public attribute
        self.__balance = balance  # Private attribute

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    # Public method to access private data
    def get_balance(self):
        return self.__balance


# Creating an object
account = BankAccount("Shriram", 5000)

# Accessing methods
account.deposit(2000)
account.withdraw(1000)

# Display balance
print("Current Balance:", account.get_balance())