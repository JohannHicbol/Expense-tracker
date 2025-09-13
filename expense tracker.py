from expense import Expense
import calendar
import datetime


def main():
    print(f"Welcome to the Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = get_budget()
    expense = get_user_expense()

    save_expense_to_file(expense, expense_file_path)

    summarize_expenses(expense_file_path, budget)

def get_user_expense():
    print(f"Gettting the user expenses")
    expense_name = input("Enter expense name: ")
    while True:
        try:
            expense_amount = float(input("Enter expense amount: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the expense amount.")
    expense_category = [
        "food",
        "home",
        "Work",
        "Fun",
        "Misc",
    ]

    while True:
        print("select a category: ")
        for i, category_name in enumerate(expense_category):
            print(f"  {i+1}. {category_name}")

        value_range = f"[1 - {len(expense_category)}]"
        selected_index = int(input(f"Select an category number {value_range}: ")) - 1

        if selected_index in range(len(expense_category)):
            selected_category = expense_category[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
            )
            return new_expense
        else:
            print("Invalid selection. Please try again!")


def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving the user expenses:{expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")



def summarize_expenses(expense_file_path, budget):
    print(f"Summzing the user expenses")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category,
            )
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key]+= expense.amount
        else:
            amount_by_category[key] = expense.amount
    print("Expenses by Category")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:,.2}")

    totel_spent = sum(x.amount for x in expenses)
    print(f"Totel Spent: {totel_spent:,.2f} this month")

    remaining_budget = budget - totel_spent
    print(f"Budget remaining: {remaining_budget:,.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    print(f"Remaining days: {remaining_days:,.2f}")
    daily_budget = remaining_budget / remaining_days
    print(green(f" Budget Per Day: ${daily_budget:.2f}"))

def get_budget():
    while True:
        try:
            return float(input("How much is the budget: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def green(text):
    return f"\033[92m{text}\033[0m"

if __name__ == "__main__":
    main()