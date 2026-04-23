from utisils import library
def search(library):
    print("\n----- SEARCH -----")
    keyword = input("Enter ID, title, author, or category: ").lower()

    found = False 

    for book in library:
        if (keyword in book["id"].lower() or
            keyword in book["title"].lower() or
            keyword in book["author"].lower() or
            keyword in book["category"].lower()):

            print(f"""
                  ID : {book['id']}
                  Title : {book['title']}
                  Author : {book['author']}
                  Category : {book['category']}
                  Quantity : {book['quantity']}
                  Status : {book['status']}
                """)

            found = True 

    if not found:
        print("No matching books found.")