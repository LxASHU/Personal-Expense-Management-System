# Personal Expense Management system -  Project Statement

## Problem Statement

Many students and beginners do not keep a record of their money. They receive income from different sources such as pocket money, salary or part-time work, and spend it on food, travel, shopping and bills, but they do not note it down anywhere. By the end of the month they cannot say how much they earned, how much they spent, how much is left, or which category took most of their money.

Existing budgeting apps are often too complex, need internet access or an account, and are not suitable for someone who only wants a quick, simple summary. There is a need for a small, easy-to-use tool that records income and expenses and shows a clear picture of the user's finances.

## Scope of the Project

**Included in the project**

- A command-line program written in Python 3 that runs on the user's own computer, with no internet connection or external libraries
- Recording income entries with a source
- Recording expense entries with a category
- Viewing all recorded income and expense entries
- Analysis of finances: total income, total expense, balance, approximate savings rate and expenses by category
- Validation of amounts and menu choices

**Not included in the project**

- Saving data permanently (entries are kept in memory and cleared when the program is closed)
- Editing or deleting entries after they are added
- Graphical interface, mobile app or web version
- Multiple users, login or bank account connection
- Currencies other than the rupee (₹)

## Target Users

- Students who want to track their pocket money and daily spending
- Beginners and first-time earners who want a simple way to see where their money goes
- Anyone who prefers a small, offline tool over a full budgeting app

## High-Level Features

- **Add income:** record money received along with its source (Salary, Pocket Money, etc.)
- **Add expense:** record money spent under a category (Food, Travel, Shopping, Bills, Education, Other)
- **View history:** see every income and expense entry added so far
- **Finance analysis:** total income, total expense, balance, approximate savings rate and category-wise expenses
- **Status message:** tells the user whether they saved money, broke even or overspent
- **Input validation:** only positive numbers are accepted as amounts, and invalid menu choices are handled
- **Menu-driven interface:** simple numbered menu, so any number of entries can be added before exiting