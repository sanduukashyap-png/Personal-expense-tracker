import csv

income = []
expenses = []

def add_income():
    source = input("Enter income source: ")
    amount = float(input("Enter income amount: "))

    income.append({
        "source": source,
        "amount": amount
    })

    print("Income added successfully!\n")


def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))

    expenses.append({
        "category": category,
        "amount": amount
    })

    print("Expense added successfully!\n")


def view_summary():
    total_income = sum(item["amount"] for item in income)
    total_expense = sum(item["amount"] for item in expenses)
    balance = total_income - total_expense

    print("\n------ SUMMARY ------")
    print(f"Total Income  : {total_income}")
    print(f"Total Expense : {total_expense}")
    print(f"Balance       : {balance}\n")


def save_to_csv():
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Source/Category", "Amount"])

        for item in income:
            writer.writerow(["Income", item["source"], item["amount"]])

        for item in expenses:
            writer.writerow(["Expense", item["category"], item["amount"]])

    print("Data saved successfully in expenses.csv\n")


while True:
    print("===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Save to CSV")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_income()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        view_summary()
    elif choice == "4":
        save_to_csv()
    elif choice == "5":
        print("Thank you for using Personal Expense Tracker!")
        break
    else:
        print("Invalid choice! Please try again.\n")