# add_income.py - function to add income


def add_income():
    source = input("Enter income source (e.g. Salary, Pocket Money): ")
    if source == "":
        source = "Other"

    while True:
        text = input("Enter your income: ₹")
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

        amount = float(text)   # type conversion

        if amount == 0:
            print("Amount must be greater than 0.")
            continue

        break

    # Storing
    entry = {"source": source, "amount": amount}
    return entry
