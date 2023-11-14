import os
import datetime

main_expense_list = []

#Function to add expenses
def add_expense():
    date = datetime.datetime.now()
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Write a brief description: ")

    expense = {
        "Date": date.strftime("%Y-%m-%d %H:%M:%S"),
        "Amount": amount,
        "Category": category,
        "Description": description,
    }
    
    main_expense_list.append(expense)
    print("Expense added successfully!")

#Function to display all the expenses
def list_expenses():
    if len(main_expense_list) == 0:
        print("No expenses found.")
    else:
        print("\nExpense List:")
        for i, expense in enumerate(main_expense_list, start=1):
            print(f"{i}. Date: {expense['Date']}")
            print(f"   Amount: Rs{expense['Amount']}")
            print(f"   Category: {expense['Category']}")
            print(f"   Description: {expense['Description']}\n")

#Function to get total amount of all expenses for a particular time period
#strptime function formats time stamp from string format to date-time object
#strftime function formats time stamp from date-time object to string format  
def total_expenses():
    try:
        start_date = datetime.datetime.strptime(input("Enter start date (YYYY-MM-DD): "), "%Y-%m-%d")
        end_date = datetime.datetime.strptime(input("Enter end date (YYYY-MM-DD): "), "%Y-%m-%d")
        amount = 0
        for expense in main_expense_list:
            if (start_date <= datetime.datetime.strptime(expense['Date'], "%Y-%m-%d %H:%M:%S") <= end_date):
                amount += expense["Amount"]
        print(f"The Total Amount from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')} is : {amount}")
    except ValueError:
        print("You have entered the wrong date format. Please use YYYY-MM-DD.")

#This function gives monthly report of expenses in category-wise
def monthly_report():
    try:
        report_month = datetime.datetime.strptime(input("Enter report month in (YYYY-MM): "), "%Y-%m")
        monthly_expenses = []
        categories = set()
        category_amount = 0
        for expense in main_expense_list:
            if (datetime.datetime.strptime(expense['Date'], "%Y-%m-%d %H:%M:%S").month == report_month.month):
                monthly_expenses.append(expense)
        
        if len(monthly_expenses) == 0:
            print("No expenses found for the mentioned month.")
        else:
            print(f"\nMonthly Report for {report_month.strftime('%B %Y')}:")
            for expense in monthly_expenses:
                categories.add(expense['Category'])
                
            for category in categories:
                for expense in monthly_expenses:
                    if expense['Category'] == category:
                        category_amount += expense['Amount']
                print(f"{category}: Rs{category_amount}")
                category_amount = 0
    except ValueError:
        print("Invalid date format. Please use YYYY-MM.")

#Function to save expenses to a text file 
def save_expenses():
    with open("expenses.txt", "w") as file:
        for expense in main_expense_list:
            file.write(f"{expense['Date']},{expense['Amount']},{expense['Category']},{expense['Description']}\n")
    print("Expenses saved to 'expenses.txt'.")

# Function to load expenses from a text file
def load_expenses():
    if os.path.exists("expenses.txt"):
        with open("expenses.txt", "r") as file:
            for line in file:
                date, amount, category, description = line.strip().split(",")
                main_expense_list.append({
                    "Date": date,
                    "Amount": float(amount),
                    "Category": category,
                    "Description": description
                })
        print("Expenses loaded from 'expenses.txt'.")

# Main loop
def main():
    load_expenses()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Calculate Total Expenses for a given Time")
        print("4. Generate Monthly Report")
        print("5. Save Expenses")
        print("6. Load Expenses")
        print("7. Quit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            monthly_report()
        elif choice == "5":
            save_expenses()
        elif choice == "6":
            load_expenses()
        elif choice == "7":
            print("Thank you!!")
            break
        else:
            print("Invalid choice!!")

if __name__ == "__main__":
    main()