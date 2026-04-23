from add import library
def display():

    print("\n----Library Books----")

    if len(library) == 0:
        print("No Books available. Sorry for the inconvenience.")

    else:
        for book in library:
            print(f"""
                -------------------
                ID : {book["id"]}
                TITLE : {book["title"]}
                AUTHOR : {book["author"]}
                CATEGORY : {book["category"]}
                QUANTITY : {book["quantity"]}
                STATUS : {book["status"]}
                --------------------
                """)
            
            