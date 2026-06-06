import mysql.connector

expensesList = []

# DATABASE CONNECT
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abcd@1234",
    database="expense_tracker"
)

cursor = conn.cursor()

print("Welcome to Expense Tracker")

while True:

    print("\n===== MENU =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Kharcha")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":

        day = input("Enter Date: ")
        month = input("Enter Month: ")
        year = input("Enter Year: ")

        date = f"{day}/{month}/{year}"
        category = input("Category: ")
        description = input("Description: ")

        try:
            amount = float(input("Amount: "))

        except ValueError:
            print("Please enter a valid amount.")
            continue

        # DATABASE INSERT
        cursor.execute(
    """
    INSERT INTO expenses
    (date, category, description, amount)
    VALUES (%s, %s, %s, %s)
    """,
    (date, category, description, amount)
)

        conn.commit()

        print("Expense Added Successfully!")

    elif choice == "2":

        # DATABASE FETCH
        cursor.execute("SELECT * FROM expenses")

        records = cursor.fetchall()

        if len(records) == 0:
            print("No expenses found.")

        else:
            print("\n===== ALL EXPENSES =====")

            for i, expense in enumerate(records, start=1):

                print(
                    f"{i}. Date: {expense[0]}, "
                    f"Category: {expense[1]}, "
                    f"Description: {expense[2]}, "
                    f"Amount: ₹{expense[3]}"
                )

    elif choice == "3":

        # TOTAL FROM DATABASE
        cursor.execute("SELECT SUM(amount) FROM expenses")

        total = cursor.fetchone()[0]

        print(f"Total Kharcha = ₹{total}")

    elif choice == "4":

        conn.close()

        print("Thank You For Using Expense Tracker")
        break

    else:
        print("Invalid Choice! Enter 1, 2, 3 or 4.")