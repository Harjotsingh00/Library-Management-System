def login():
    print("\n-----Library Access-----")
    print("1. Admin Login")
    print("2. Continue as User")

    choice = input("Enter choice: ")

    if choice == "1":
        username = input("Enter admin username: ")
        password = input("Enter password: ")

        if username == "admin" and password == "admin123":
            print("Admin login successful")
            return ("admin", "Admin")
        else:
            print("Invalid admin credentials")
            return (None, None)

    elif choice == "2":
        name = input("Enter your name: ")
        print(f"Welcome, {name}")
        return ("user", name)

    else:
        print("Invalid choice")
        return (None, None)