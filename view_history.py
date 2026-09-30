# view_history.py - function to show all entries


def view_history(incomes, expenses):
    print("\n----- Transaction History -----")

    print("\nIncome:")
    if len(incomes) == 0 :
        print("\tNo income added yet.")
    for i in range(len(incomes)) :

        print(i + 1, ".", incomes[i]["source"], "\t: ₹", incomes[i]["amount"])

    print("\nExpenses:")
    if len(expenses) == 0 :
        print("\tNo expenses added yet.")
    for i in range(len(expenses)) :
    
        print(i + 1, ".", expenses[i]["category"], "\t: ₹", expenses[i]["amount"])