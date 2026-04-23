from utisils import library

def recommend_books(category):
    print("\nRecommended Books:")

    found = False

    for book in library:
        if book["category"].lower() == category.lower() and book["quantity"] > 0:
            print(f"- {book['title']} by {book['author']}")
            found = True

    if not found:
        print("No recommendations available.")