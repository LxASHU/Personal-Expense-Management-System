# main.py - Personal Expense Management System
# Run this file to start the program:  python main.py

from add_income import add_income
from add_expense import add_expense
from view_history import view_history
from Analysis import analysis

incomes = []  
expenses = []  
while True:
    print("\n===== Personal Expense Management System =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View History")
    print("4. Show Analysis")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        incomes.append(add_income())
        print("Income added successfully.")
    elif choice == "2":
        expenses.append(add_expense())
        print("Expense added successfully.")
    elif choice == "3":
        view_history(incomes, expenses)

    elif choice == "4":
        analysis(incomes, expenses)

    elif choice == "5":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice! Please try again.")
