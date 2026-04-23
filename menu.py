from utisils import library, issued
import login, add, issue, display, search, stats, returnbook

print("\n-----WELCOME TO THE LIBRARY MENU-----")

print("""
Library Fine Rules:
- First week delay: ₹10/day
- Second week: ₹20/day
- Third week: ₹60/day
- Fine increases progressively each week
""")

# First login OUTSIDE loop
role, current_user = login.login()

while role:
    print(f"\n===== Library Menu ({role.upper()}) =====")

    if role == "admin":
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books")
        print("4. Check Stats")
        print("5. Switch to User")
        print("6. Exit")

    elif role == "user":
        print("1. View Books")
        print("2. Search Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Switch to Admin")
        print("6. Exit")

    choice = input("Enter choice: ")

    # ADMIN MENU
    if role == "admin":
        if choice == "1":
            add.add()
        elif choice == "2":
            display.display()
        elif choice == "3":
            search.search(library)
        elif choice == "4":
            stats.stats()
        elif choice == "5":
            role, current_user = login.login()  # switch role properly
        elif choice == "6":
            break

    # USER MENU
    elif role == "user":
        if choice == "1":
            display.display()
        elif choice == "2":
            search.search(library)
        elif choice == "3":
            issue.issue(library)
        elif choice == "4":
            returnbook.return_book(library)
        elif choice == "5":
            role, current_user = login.login()  # switch role properly
        elif choice == "6":
            break