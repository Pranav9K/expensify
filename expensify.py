import json

class FinanceManager:
    def __init__(self):
        self.users = self.load_users()

    def load_users(self):
        try:
            with open("users.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_users(self):
        with open("users.json", "w") as file:
            json.dump(self.users, file)

    def register_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username not in self.users:
            self.users[username] = {"password": password, "expenses": [], "income": []}
            self.save_users()
            print("Registration Successful: Account created successfully. You can now login.")
        else:
            print("Registration Failed: Username already exists.")

    def login_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in self.users and self.users[username]["password"] == password:
            print("Login Successful")
            return username
        else:
            print("Login Failed: Invalid username or password.")
            return None

    def add_expense(self, username):
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        expense_name = input("Enter expense name: ")
        amount = input("Enter amount: ")
        if username in self.users:
            self.users[username]["expenses"].append({"date": date, "category": category, "name": expense_name, "amount": amount})
            self.save_users()
            print("Expense added successfully.")
        else:
            print("User not found.")

    def add_income(self, username):
        date = input("Enter date (YYYY-MM-DD): ")
        source = input("Enter source of income: ")
        amount = input("Enter amount: ")
        if username in self.users:
            self.users[username]["income"].append({"date": date, "source": source, "amount": amount})
            self.save_users()
            print("Income added successfully.")
        else:
            print("User not found.")

    def calculate_total_expenses(self, username):
        if username in self.users:
            total_expenses = sum(float(expense["amount"]) for expense in self.users[username]["expenses"])
            print(f"Total Expenses for {username}: ${total_expenses:.2f}")
        else:
            print("User not found.")

    def calculate_total_income(self, username):
        if username in self.users:
            total_income = sum(float(income["amount"]) for income in self.users[username]["income"])
            print(f"Total Income for {username}: ${total_income:.2f}")
        else:
            print("User not found.")

def main():
    finance_manager = FinanceManager()

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Add Expense")
        print("4. Add Income")
        print("5. Calculate Total Expenses")
        print("6. Calculate Total Income")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            finance_manager.register_user()
        elif choice == "2":
            username = finance_manager.login_user()
            if username:
                while True:
                    inner_choice = input("\n1. Add Expense\n2. Add Income\n3. Calculate Total Expenses\n4. Calculate Total Income\n5. Logout\nEnter your choice: ")
                    if inner_choice == "1":
                        finance_manager.add_expense(username)
                    elif inner_choice == "2":
                        finance_manager.add_income(username)
                    elif inner_choice == "3":
                        finance_manager.calculate_total_expenses(username)
                    elif inner_choice == "4":
                        finance_manager.calculate_total_income(username)
                    elif inner_choice == "5":
                        break
                    else:
                        print("Invalid choice.")
        elif choice == "7":
            finance_manager.save_users()
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
