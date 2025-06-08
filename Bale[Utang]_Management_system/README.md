# 📋 Utang Management System

A simple and intuitive debt tracking (Utang) management system built with Python and Kivy. This app allows users to record, search, view, and delete credit records using a user-friendly GUI and stores the data in a CSV file.

---

## 🚀 Features

- **➕ Create A Record:** Add new entries with name, item, price, and quantity.  
- **📖 Read All Records:** View all stored records in a popup window.  
- **🔍 Search A Record:** Look up records by name and display results.  
- **🗑️ Delete A Record:** Remove a specific record by name.  
- **❌ Exit:** Close the application safely.

---

## 🛠 Technologies Used

- **Python 3**  
- **Kivy** – GUI framework for building interactive applications.  
- **CSV Module** – For storing and retrieving data.

---

## 📁 File Structure

```plaintext
utang-management-system/
├── main.py          # Main application logic
├── utang.kv         # Kivy UI layout definitions
├── bale.csv         # Auto-generated CSV file storing records
└── README.md        # Project documentation
```

---

## 🖥️ Screens Overview

### Main Screen
Provides navigation options to manage records:
- Add
- Read
- Search
- Delete
- Exit

### Add Record
Input fields for:
- Name
- Item
- Price
- Quantity

Automatically calculates total and timestamps the record.

### Search
Search records by name and displays matching entries.

### Delete
Delete records by entering the name.

---

## ▶️ How to Run

1. Make sure you have Python installed.  
2. Install the required module:  
   ```
   pip install kivy
   ```  
3. Run the app:  
   ```
   python main.py
   ```  

> **Note:** A file named `bale.csv` will be created automatically if it doesn’t exist.

---

## 📌 Important Notes

- **Data Persistence:** All records are stored in a CSV file (`bale.csv`) for simplicity and portability.  
- **UI Design:** The `.kv` file handles styling, layout, and theming, providing a consistent user experience.

---

## 💡 Future Improvements

- Add edit/update functionality.  
- Sort and filter records.  
- Integrate a database (e.g., SQLite) for better scalability.  
- Add export/import options (PDF, Excel).

---

## 🧑‍💻 Author

Developed by Vee.

---

## 📄 License

This project is open-source and free to use for educational or personal purposes.
