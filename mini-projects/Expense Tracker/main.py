List_Expenses = []

# add_expense function for adding expenses to the list
def add_expense():
    amount = int(input("Enter the amount: "))
    category = input("Enter the category: ")
    description = input("Enter the description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }
    List_Expenses.append(expense)

# view_expenses function for viewing the expenses in the list
def view_expenses():
    print("Expenses : ")
    for expense in List_Expenses:
        print(f"Amount: {expense['amount']}, "
              f"Category: {expense['category']}, "
              f"Description: {expense['description']} ")

# total_spending function for calculating the total spending
def total_spending():
    total = 0 
    for expense in List_Expenses:
        total += expense["amount"]
    print("Total spending is : ", total)

# spending_by_category function for calculating the total spending by category
def spending_by_category():
    category = input("Enter the category to check the spending : ")
    total = 0
    for expense in List_Expenses:
        if expense["category"] == category:
            total += expense["amount"]
    print(f"Total spending in {category} is : {total}")

# highest_expense function for finding the highest expense
def highest_expense():
    for expense in List_Expenses:
        if expense["amount"] == max(expense["amount"] for expense in List_Expenses):
            print("Highest expense is : ", expense["amount"])

def main():
    print("------------ Expense Tracker -----------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Spending by Category")
    print("5. Highest Expense")
    print("6. Exit")

    while True:
        choice = int(input("\nEnter your choice : "))
        match choice:
            case 1 :
                add_expense()
            case 2 :
                view_expenses()
            case 3 :
                total_spending()
            case 4 :    
                spending_by_category()
            case 5 :
                highest_expense()
            case 6 :
                break

    with open("expenses.txt","w") as f:
        f.write(str(List_Expenses))

main()
