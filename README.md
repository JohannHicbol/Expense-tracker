# Expense-tracker
Main Functionalities:

1. Ask the user for their monthly budget
(Handled by get_budget())

2. Get an expense from the user

  Name ("Coffee")

  Amount (3.50)

  Category (food, home, work...)
  (Handled by get_user_expense())

3. Save the expense to a CSV file
  (expenses.csv)
  (Handled by save_expense_to_file())

4. Summarize the expenses

  Read all expenses from the file

  Group them by category

  Calculate total spent and budget remaining

  Show remaining days in the month

  Calculate daily budget for the rest of the month
  (Handled by summarize_expenses())
