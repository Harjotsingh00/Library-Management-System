from datetime import datetime
from utisils import issued  

def return_book(library):
    print("\n----- Return Book -----")

    bookid = input("Enter Book ID: ")
    username = input("Enter your name: ")

    for record in issued:
        if record["bookid"] == bookid and record["user"] == username:

            due_date = datetime.strptime(record["due_date"], "%Y-%m-%d")
            return_date = datetime.now()

            late_days = (return_date - due_date).days

            if late_days <= 0:
                return 0

            total_fine = 0

            for day in range(1, late_days + 1):
                week = (day - 1) // 7 + 1  # week number

            # factorial logic
            fact = 1
            for i in range(1, week + 1):
                fact *= i

            daily_fine = 10 * fact
            total_fine += daily_fine

            return total_fine

            for book in library:
                if book["id"] == bookid:
                    book["quantity"] += 1
                    book["status"] = "Available"

            issued.remove(record)

            print("Book returned successfully!")

            if fine > 0:
                print(f"Late return! Fine: ₹{fine}")
            else:
                print("No fine!")
  

            return

    print("Record not found!")