# 📚 Library Management System (Python)

A modular, console-based **Library Management System** built using Python.
This project focuses on implementing real-world library operations using **core programming concepts**, without relying on external databases or file storage.

---

## 🚀 Overview

This system allows:

* **Admins** to manage books
* **Users** to browse, issue, and return books
* Implements **fine calculation**, **search**, and **recommendation logic**

All data is handled **in-memory using Python data structures**, making the project simple, fast, and easy to understand.

---

## 🧩 Features

### 🔐 Role-Based Access

* **Admin**

  * Add books
  * View books
  * Search books
  * View statistics

* **User**

  * View books
  * Search books
  * Issue books
  * Return books

---

### 📚 Book Management

* Add books with:

  * ID, Title, Author, Category, Quantity
* Automatically updates quantity if book already exists
* Tracks book status (`Available` / `Issued`)

---

### 🔍 Smart Search System

* Search by:

  * Book ID
  * Title
  * Author
  * Category
* Supports:

  * Partial matching
  * Case-insensitive search

---

### 📖 Issue Book System

* Issue using Book ID or Title
* Stores:

  * User name
  * Issue date
  * Due date (14 days)
* Prevents:

  * Issuing unavailable books

---

### 🔁 Return Book System

* Matches issued records
* Updates quantity after return
* Removes issued entry
* Applies fine if returned late

---

### 💰 Progressive Fine System

* Fine applied only after due date
* Increasing penalty based on delay:

| Delay Period  | Fine per Day             |
| ------------- | ------------------------ |
| Week 1        | ₹10/day                  |
| Week 2        | ₹20/day                  |
| Week 3        | ₹60/day                  |
| Further weeks | Increasing progressively |

---

### 📊 Statistics Dashboard

* Total books
* Issued records
* Available copies

---

### 🤖 Recommendation System

* Suggests books based on category
* Triggered after issuing a book

---

## ⚠️ Data Handling Note

* All data is stored in **Python variables (lists & dictionaries)**
* No external database or file storage is used
* Data resets when the program is restarted

This design choice keeps the project:

* Simple
* Beginner-friendly
* Easy to demonstrate and explain

---

## 🏗️ Project Structure

```id="r1l9wx"
library_management/
│
├── add.py           # Add book logic
├── display.py       # Display books
├── search.py        # Search functionality
├── issue.py         # Issue book logic
├── returnbook.py    # Return + fine system
├── login.py         # Authentication system
├── stats.py         # Statistics dashboard
├── suggest.py       # Recommendation system
├── utils.py         # Helper functions
├── data.py          # (Optional / future use)
├── menu.py          # Main program flow
```

---

## ⚙️ Technologies Used

* Python
* Built-in modules (`datetime`)

---

## ▶️ How to Run

```bash id="0qz7j3"
python menu.py
```

---

## 🧠 Key Concepts Demonstrated

* Modular Programming
* Lists & Dictionaries
* Function-based design
* Role-based system
* Date & time handling
* Algorithmic logic (fine calculation)

---

## 🎯 Design Philosophy

This project focuses on:

* Keeping the system **simple yet functional**
* Implementing **real-world logic using basic concepts**
* Ensuring everything is **easy to explain and understand**

---

## 📌 Future Improvements

* Add JSON/database storage
* Build GUI using Tkinter
* Add user authentication system
* Implement book reservation

---

## 👨‍💻 Author

**Harjot Singh**
B.Tech – Artificial Intelligence & Data Science

---

## ⭐ Final Note

This project demonstrates how a complete system can be built using
**fundamentals of programming, structured logic, and clean modular design**.
