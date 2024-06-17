class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance
        self.transaction_stack = Stack()

    def deposit(self, amount):
        self.balance += amount
        self.transaction_stack.push(("Deposit", amount))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            self.transaction_stack.push(("Withdrawal", amount))

    def get_balance(self):
        return self.balance

    def get_statement(self):
        statement = []
        temp_stack = Stack()
        while not self.transaction_stack.is_empty():
            transaction = self.transaction_stack.pop()
            statement.append(transaction)
            temp_stack.push(transaction)
        while not temp_stack.is_empty():
            self.transaction_stack.push(temp_stack.pop())
        return statement

def main():
    account = BankAccount("1234567890", 100)

    while True:
        print("\nBanking System Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Statement")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 3:
            print(f"Current Balance: {account.get_balance()}")
        elif choice == 4:
            print("Statement:")
            statement = account.get_statement()
            for transaction in statement:
                print(f"{transaction[0]}: {transaction[1]}")
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
