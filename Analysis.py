# analysis.py - function to calculate and show the finance summary


def analysis(incomes, expenses):
    total_income = 0
    total_expense = 0

    for item in incomes:
        total_income = total_income + item["amount"]

    for item in expenses:
        total_expense = total_expense + item["amount"]

    balance = total_income - total_expense

    print("\n----- Finance Analysis -----")
    print("Total Income  : ₹", total_income)
    print("Total Expense : ₹", total_expense)
    print("Balance       : ₹", balance)

    if total_income > 0:
        savings_percent = balance / total_income * 100
        print("Savings Rate  : approx", int(savings_percent), "%")

    # Category-wise expenses using a dictionary
    if len(expenses) > 0:
        category_totals = {}
        for item in expenses:
            category = item["category"]
            if category in category_totals:
                category_totals[category] = category_totals[category] + item["amount"]
            else:
                category_totals[category] = item["amount"]

        print("\nExpense by category:")
        for category in category_totals:
            percent = category_totals[category] / total_expense * 100
            print(category, "\t: ₹", category_totals[category], "(approx", int(percent), "%)")

    # Status message
    print()
    if balance > 0:
        print("Status: You have saved money.")
    elif balance == 0:
        print("Status: Your income and expense are equal.")
    else:
        print("Status: You have spent more than your income.")