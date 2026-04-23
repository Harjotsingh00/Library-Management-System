from datetime import datetime, timedelta
from utisils import library, issued
from suggest import recommend_books

def issue(library):
    print("\n-----Issue Books-----")

    bookid = input("Enter the Book ID or Title: ").lower()
    username = input("Enter your name: ")

    # max 2 books per user
    count = 0
    for record in issued:
        if record["user"] == username:
            count += 1

        if count >= 2:
            print("You can only issue 2 books!")
            return

    for book in library:
        if book["id"] == bookid or book["title"] == bookid:
            if book["quantity"] > 0:
                issue_date = datetime.now()
                due_date = issue_date + timedelta(days=14)

                book["quantity"] -= 1

                if book["quantity"] == 0:
                    book["status"] = "Issued"

                issued.append({
                    "bookid" : bookid,
                    "title": book["title"],
                    "user": username,
                    "issue_date": issue_date.strftime("%Y-%m-%d"),
                    "due_date": due_date.strftime("%Y-%m-%d")
                })

                print("Book issued successfully!")
                print(f"Return by: {due_date.strftime('%Y-%m-%d')}")

                recommend_books(book["category"])
                return
                
            else:
                print("Book not available!")
                return
                

    print("Book not found!")

    

