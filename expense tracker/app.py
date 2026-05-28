from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abcd@1234",
    database="expense_tracker"
)

cursor = conn.cursor()

# Home Page
@app.route("/", methods=["GET", "POST"])
def home():

    # Add Expense
    if request.method == "POST":

        date = request.form["date"]
        category = request.form["category"]
        description = request.form["description"]
        amount = float(request.form["amount"])

        # Amount Limit
        if amount > 50000:
            return "Amount Limit Exceeded"

        # Insert Data
        cursor.execute(
            """
            INSERT INTO expenses(date, category, description, amount)
            VALUES(%s, %s, %s, %s)
            """,
            (date, category, description, amount)
        )

        conn.commit()

        return redirect("/")

    # Show Data
    cursor.execute("SELECT * FROM expenses")

    data = cursor.fetchall()

    return render_template("index.html", expenses=data)


# Delete Expense
@app.route("/delete/<int:id>")
def delete(id):

    cursor.execute(
        "DELETE FROM expenses WHERE id=%s",
        (id,)
    )

    conn.commit()

    return redirect("/")


# Run Website
if __name__ == "__main__":
    app.run(debug=True)