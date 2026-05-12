Library Book Borrowing System

A simple Python-based library management system that tracks books, clients, 
and borrowing activity — storing all data persistently in a JSON file that 
updates itself in real time.



 Overview

This project models a real-world library workflow using Object-Oriented 
Programming (OOP) in Python. Clients can borrow and return books, and every 
action is recorded with an accurate datetime stamp. All data is saved to a 
local JSON file so the system remembers its state even after the program stops.



 Features

- Register clients with a unique ID and name
- Borrow and return books with real-time datetime tracking
- Automatic availability status updates per book
- Per-client borrowing history stored on their profile
- Full transaction audit log (every borrow and return event)
- JSON file updates itself after every action — no manual saving needed



 Project Structure

library-system/
│
├── library_system.py     # Main application logic
├── library_data.json     # Auto-generated data file (created on first run)
└── README.md



 How It Works

The system is built around three core classes:

- `Base` — Parent class that gives every object a unique ID and 
  `created_at` / `updated_at` timestamps
- `Book` — Represents a book with title, author, year, and availability status
- `User` — Represents a client who can borrow and return books

All object state is converted to plain dictionaries via `to_dict()` methods 
and written to `library_data.json` using Python's built-in `json` module. 
The file is overwritten with the latest state after every action.

---

 Getting Started

Requirements: Python 3.x — no external libraries needed.

Run the demo:

python3 library_system.py


A `library_data.json` file will be created automatically on the first run 
and updated live from that point forward.

---

 JSON Data Structure

json
{
    "last_updated": "2026-05-12T10:15:30",
    "books": [
        {
            "id": 1,
            "title": "The Great Gatsby",
            "is_available": false,
            "borrower_id": 1,
            "updated_at": "2026-05-12T10:15:30"
        }
    ],
    "users": [
        {
            "id": 1001,
            "name": "Alice",
            "borrowed_book_ids": [1],
            "updated_at": "2026-05-12T10:15:30"
        }
    ]
}



 Concepts Practiced

- Object-Oriented Programming (classes, inheritance, instance methods)
- JSON serialization with Python's `json` module
- Datetime handling with `datetime.datetime.now()`
- Persistent file storage without a database
- Separation of concerns (data, display, and logic in separate classes)


 Author

Built as a learning project to explore OOP design patterns and JSON-based 
data persistence in Python.
