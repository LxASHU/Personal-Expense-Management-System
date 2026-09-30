# add_expense.py - function to add an expense
CATEGORIES = ("Food", "Travel", "Shopping", "Bills", "Education", "Other")


def add_expense():
    print("\nSelect a category:")
    for i in range(len(CATEGORIES)):
        print(i + 1, ".", CATEGORIES[i])

    choice = input("Enter category number: ")

    category = "Other"
    for i in range(len(CATEGORIES)):
        if choice == str(i + 1):
            category = CATEGORIES[i]

    while True:
        text = input("Enter your expense: ₹")
        valid = True
        dots = 0
        digits = 0

        # Check every character of the input
        for ch in text:
            if ch == ".":
                dots = dots + 1
            elif ch in "0123456789":
                digits = digits + 1
            else:
                valid = False

        if dots > 1 or digits == 0:
            valid = False

        if valid == False:
            print("Invalid input! Enter a positive number using digits only.")
            continue

        amount = float(text)   # type conversion: str -> float

        if amount == 0:
            print("Amount must be greater than 0.")
            continue

        break

    # Store the entry as a dictionary
    entry = {"category": category, "amount": amount}
    return entry
