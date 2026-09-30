# Personal Expense Management System

## Overview

The Personal Expense Management System is a menu-driven command-line program written in Python. It helps a user record income and expenses and see a simple summary of their finances: total income, total expense, balance, savings rate and expenses by category.

It is built using concepts from the Python Essentials course and needs no external libraries.

## Features

- Add income with a source (Salary, Pocket Money, etc.)
- Add expenses with a category (Food, Travel, Shopping, Bills, Education, Other)
- View all income and expense entries
- Financial analysis: total income, total expense, balance, approximate savings rate and category-wise expenses
- Status message: saved money, broke even, or overspent
- Input validation for amounts and menu choices

## Technologies / Tools Used

- Python 3 (no external libraries)
- GitHub 
- VS code

## Steps to Install and Run

### Step 1: Install Python 3

Download and install Python 3 from https://www.python.org/downloads/ (on Windows, tick "Add Python to PATH"). Check it with `python --version`.

### Step 2: Open a terminal inside the project folder

Open a terminal (command prompt) inside the project folder that contains `main.py`. On Windows, you can open the folder in File Explorer, type `cmd` in the address bar and press Enter.

### Step 3: Run the program

```
python main.py
```

On some systems use `python3 main.py` (macOS / Linux) or `py main.py` (Windows).

The main menu will appear:

```
===== Personal Expense Management System =====
1. Add Income
2. Add Expense
3. View History
4. Show Analysis
5. Exit
Enter your choice:
```

### Step 4: Use the program

Type the number of the option you want and press **Enter**. After every action the main menu appears again, so you can keep adding entries. Data is kept in memory only, so it is cleared when the program closes.

**Option 1: Add Income**

1. Type `1` and press Enter.
2. Enter where the money came from, for example `Salary`. If you press Enter without typing, it is saved as `Other`.
3. Enter the amount, for example `20000`. Only digits and one decimal point are allowed. If the amount is wrong, the program shows an error and asks again.
4. `Income added successfully.` is shown and you return to the menu.

```
Enter your choice: 1
Enter income source (e.g. Salary, Pocket Money): Salary
Enter your income: ₹20000
Income added successfully.
```

**Option 2: Add Expense**

1. Type `2` and press Enter.
2. A list of categories is shown. Type the number of the category, for example `1` for Food. A wrong number saves the expense under `Other`.
3. Enter the amount you spent, for example `4000`. It follows the same amount rules as income.
4. `Expense added successfully.` is shown and you return to the menu.

```
Enter your choice: 2

Select a category:
1 . Food
2 . Travel
3 . Shopping
4 . Bills
5 . Education
6 . Other
Enter category number: 1
Enter your expense: ₹4000
Expense added successfully.
```

**Option 3: View History**

1. Type `3` and press Enter.
2. Every income and expense entered so far is listed with a number.
3. If nothing has been added yet, it shows `No income added yet.` or `No expenses added yet.`

```
Enter your choice: 3

----- Transaction History -----

Income:
1 . Salary      : ₹ 20000.0

Expenses:
1 . Food        : ₹ 4000.0
2 . Travel      : ₹ 3500.0
```

**Option 4: Show Analysis**

1. Type `4` and press Enter.
2. The program shows:
   - **Total Income:** the sum of all income entries
   - **Total Expense:** the sum of all expense entries
   - **Balance:** total income minus total expense
   - **Savings Rate:** balance as a  approximate percentage of income, as a whole number
   - **Expense by category:** how much was spent in each category, with an approximate percentage
   - **Status:** whether you saved money, broke even or overspent

```
Enter your choice: 4

----- Finance Analysis -----
Total Income  : ₹ 20000.0
Total Expense : ₹ 7500.0
Balance       : ₹ 12500.0
Savings Rate  : approx 62 %

Expense by category:
Food    : ₹ 4000.0 (approx 53 %)
Travel  : ₹ 3500.0 (approx 46 %)

Status: You have saved money.
```

| Situation | Status message |
|---|---|
| Income is more than expense | `Status: You have saved money.` |
| Income equals expense | `Status: Your income and expense are equal.` |
| Expense is more than income | `Status: You have spent more than your income.` |

**Option 5: Exit**

Type `5` and press Enter. The program shows `Thank you for using the system!` and closes. Any other menu input shows `Invalid choice! Please try again.`

**Example session from start to finish**

1. Run `python main.py`.
2. Choose `1`, enter `Salary` and `20000`.
3. Choose `1`, enter `Pocket Money` and `2000`.
4. Choose `2`, category `1` (Food), amount `4000`.
5. Choose `2`, category `2` (Travel), amount `3500`.
6. Choose `3` to check the history.
7. Choose `4` to see the analysis: Total Income ₹ 22000.0, Total Expense ₹ 7500.0, Balance ₹ 14500.0.
8. Choose `5` to exit.

No packages need to be installed, and all files must stay in the same folder.

## Instructions for Testing

1. Run `python main.py`.
2. Follow the **Steps** of each test in the table below.
3. Check that the program shows the **Expected result**.

| No. | Test | Steps | Expected result |
|---|---|---|---|
| 1 | Invalid menu choice | Enter `9` at the menu | `Invalid choice! Please try again.` |
| 2 | Letters as amount | Option 1, enter `abc` as amount | `Invalid input! Enter a positive number using digits only.` and asks again |
| 3 | Negative amount | Option 1, enter `-5` | Invalid input message, asks again |
| 4 | Zero amount | Option 1, enter `0` | `Amount must be greater than 0.` and asks again |
| 5 | Two decimal points | Option 1, enter `1.2.3` | Invalid input message, asks again |
| 6 | Empty amount | Option 1, press Enter without typing | Invalid input message, asks again |
| 7 | Decimal amount | Option 1, enter `250.50` | Accepted, `Income added successfully.` |
| 8 | Wrong category number | Option 2, enter `9` as category | Saved with category `Other` |
| 9 | History with no data | Option 3 right after starting | `No income added yet.` and `No expenses added yet.` |
| 10 | Overspending | Add income `1000`, expense `1500`, then option 4 | Balance `-500.0` and `You have spent more than your income.` |
