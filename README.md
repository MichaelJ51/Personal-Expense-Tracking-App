# Expense Tracker

## 🎯 Overview
This is a simple command-line Expense Tracker program that allows users to record and categorize expenses while tracking their budget. The application reads and writes expenses to a CSV file and provides a summary of spending by category, total expenses, and remaining budget.

## 🛠 Features
- Allows users to input a valid budget.
- Records user expenses with a name, amount, and category.
- Saves expense data in a CSV file.
- Summarizes expenses by category.
- Calculates total spending and remaining budget.
- Suggests a daily spending limit based on the remaining days in the month.

## 🚀 Installation
### Prerequisites
Ensure you have Python 3 installed on your system.

### Clone the Repository
```sh
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
```

### Install Dependencies
This script relies on an `Expense` class, which should be defined in an `expense.py` file.
Ensure you have the required module:

```sh
pip install -r requirements.txt
```

## 📌 Usage
Run the program using:
```sh
expense_tracker.py
```

### How It Works
1. **Enter Your Budget**: The program prompts you to enter a budget.
2. **Record an Expense**: Input the expense name, amount, and select a category from the available options.
3. **Save Expenses**: The program writes your expense to a CSV file (`expenses.csv`).
4. **View Summary**: The program calculates and displays expenses by category, total spending, and remaining budget.
5. **Daily Budget Suggestion**: The program estimates a daily budget based on the remaining days in the month.

## 📁 File Structure
```
expense-tracker/
│── Excel.png            # Linking csv file to Excel
│── Output.png           # Example output
│── README.md            # Documentation
│── expense.py           # Expense class definition
│── expense_tracker.py   # Main application logic
│── expenses.csv         # File where expenses are stored

```

## 🔗 Linking to Excel
The expense data is stored in a CSV file (`expenses.csv`), which can be easily opened and analyzed using Microsoft Excel, Google Sheets, or any spreadsheet software.

### Steps to Open CSV in Excel:
1. Open Microsoft Excel.
2. Click on **File** > **Open**.
3. Select **Browse** and locate `expenses.csv`.
4. Ensure **All Files (
*.*
)** is selected in the file type dropdown.
5. Click **Open** and select **Comma Delimited (CSV)** if prompted.
6. The data will be displayed in a structured table format.

### Benefits of Linking to Excel:
- Use Excel formulas to analyze expenses.
- Create graphs and charts for better visualization.
- Filter and sort expenses by category.
- Export reports for financial planning.

## 🔥 Example Output
```
🎯 Running Expense Tracker!!
Please enter your budget: 1000
🎯 Getting User Expense!!
Enter expense name: Lunch
Enter expense amount: 15
Please select a category:
 1. 🍕 Food
 2. 🏡 Home
 3. 📅 Work
 4. 🥳 Fun
 5. 👀 Misc
 6. ✈️ Travel
Enter a category number [1-6]: 1
🎯 Saving User Expense: Lunch, $15.00 to expenses.csv
🎯 Summarizing User Expense
📈 Expenses By Category:
 🍕 Food: $15.00
💵 Total Spent: $15.00
✅ Budget Remaining: $985.00
👉 Budget Per Day: $35.00
```

