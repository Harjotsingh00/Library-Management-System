from utisils import library


def add():
    print("\n----ADD NEW BOOK----")

    bookid = input("Enter Book ID : ")
    title = input("Enter book title : ")
    author = input("Enter author of the book : ")
    category = input("Enter category of the book: ")
    quantity = int(input("Enter the quantity: "))

    

    if title == "" or author == "" or quantity <= 0:
        print("Invalid input! Fill all fields correctly.")

    for book in library:
        if book["id"] == bookid:
            book["quantity"] += quantity
            print("Book already exists. Quantity updated.")
        
    new_book = {
        "id": bookid,
        "title": title,
        "author": author,
        "category": category,
        "quantity": quantity,
        "status": "Available"
    }

    library.append(new_book)
    
        
