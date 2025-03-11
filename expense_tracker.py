from expense import Expense
import calendar
import datetime


def main():
    print("🎯 Running Expense Tracker!!")
    expense_file_path = "expenses.csv"

    budget = get_valid_budget()
    
    # User input for expense
    expense = get_user_expense()

    # Write the expense to a file
    expense_to_file(expense, expense_file_path)

    # Read file and summarize expenses
    summarize_expenses(expense_file_path, budget)


def get_valid_budget():
    """Ensures the user inputs a valid positive budget."""
    while True:
        try:
            budget = float(input("Please enter your budget: "))
            if budget > 0:
                return budget
            else:
                print("❌ Budget must be a positive number. Try again.")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")


def get_user_expense():
    print("🎯 Getting User Expense!!")
    expense_name = input("Enter expense name: ")

    while True:
        try:
            expense_amount = float(input("Enter expense amount: "))
            if expense_amount > 0:
                break
            else:
                print("❌ Expense amount must be positive. Try again.")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

    print(f"You've entered {expense_name}, ${expense_amount:.2f}")

    expense_categories = [
        "🍕 Food", 
        "🏡 Home", 
        "📅 Work", 
        "🥳 Fun", 
        "👀 Misc", 
        "✈️ Travel"
    ]

    while True:
        print("Please select a category: ")
        for i, category_name in enumerate(expense_categories, start=1):
            print(f" {i}. {category_name}")

        try:
            selected_index = int(input(f"Enter a category number [1-{len(expense_categories)}]: ")) - 1
            if 0 <= selected_index < len(expense_categories):
                selected_category = expense_categories[selected_index]
                return Expense(name=expense_name, category=selected_category, amount=expense_amount)
            else:
                print("❌ Invalid category. Please try again.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")


def expense_to_file(expense, expense_file_path):
    """Appends the expense details to a CSV file."""
    print(f"🎯 Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expenses(expense_file_path, budget):
    """Reads the expenses from the file and summarizes spending by category."""
    print(f"🎯 Summarizing User Expense")
    expenses = []

    try:
        with open(expense_file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                # Strip leading/trailing whitespace and split by comma
                expense_name, expense_amount, expense_category = line.strip().split(",")
                # Strip any extra whitespace from the amount and category
                expense_amount = expense_amount.strip()
                expense_category = expense_category.strip()
                line_expense = Expense(
                    name=expense_name.strip(),
                    amount=float(expense_amount),
                    category=expense_category,
                )
                expenses.append(line_expense)
    except FileNotFoundError:
        print("⚠️ No expenses recorded yet.")
        return

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        amount_by_category[key] = amount_by_category.get(key, 0) + expense.amount

    print("📈 Expenses By Category:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")

    total_spent = sum(exp.amount for exp in expenses)
    print(f"💵 Total Spent: ${total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"✅ Budget Remaining: ${remaining_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = max(1, days_in_month - now.day)

    daily_budget = remaining_budget / remaining_days
    print(green(f"👉 Budget Per Day: ${daily_budget:.2f}"))


def green(text):
    """Formats text in green for CLI output."""
    return f"\033[92m{text}\033[0m"


if __name__ == "__main__":
    main()
