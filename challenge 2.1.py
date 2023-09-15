class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name} (Account #{self.__account_number}): ${self.__account_balance:.2f}"

# Example usage:
if __name__ == "__main__":
    # Create a BankAccount instance
    my_account = BankAccount("12345", "uzumaki naruto", 1000.0)

    # Deposit and display balance
    my_account.deposit(900.0)
    print(my_account.display_balance())  # Output: "Account Balance for uzumaki naruto(Account #12345): $1500.00"

    # Withdraw and display balance
    my_account.withdraw(200.0)
    print(my_account.display_balance())  # Output: "Account Balance for uzumaki naruto(Account #12345): $1300.00"
