from utisils import library, issued
def stats():
    print("\n-----STATS-----")
    print("Total number of books: ",len(library))
    print("Books now available: ",len(library) - len(issued))
    print("Issued books: ",len(issued))

    print("List of issued books:- ", issued)