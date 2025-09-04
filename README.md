# 🧾 Expense Tracker

A simple **command-line expense tracking program** that helps you log, view, edit, and analyze your daily expenses.  
The program stores each entry with a **description, amount, and date**, and allows you to filter your history by day, week, month, year, or custom range.  

---

## 📅 Project Timeline
- **Started:** July 25, 2025  
- **Finished:** July 31, 2025  

---

## 🚀 Features

- ➕ **Add entries** with description, amount, and date.  
- ✏️ **Edit or delete entries** anytime.  
- 📖 **View entries** individually or as a full list.  
- ⏱️ **Filter history by time frame** (day, week, month, year, or custom).  
- 💰 **Calculate total spending** automatically.  
- 🖥️ **User-friendly interface** with menus, clear formatting, and feedback messages.  

---

## 🛠️ Tools & Technologies

- **Python 3.13+**
- Standard libraries:
  - `datetime` – for handling dates and ranges
  - `calendar` – for month and year calculations

---

## 📂 Project Structure

```
expense-tracker/
│── history.txt        # Stores logged expenses
│── expense_tracker.py # Main program
│── README.md          # Documentation (this file)
```

---

## 🔮 Future Updates & Features

Planned improvements to make the app more powerful and user-friendly:

- 🎨 **Better UI** with tables, colors, and clear menus.  
- 📊 **Statistics & summaries** (e.g., top categories, monthly averages).  
- 📁 **Export reports** to CSV or PDF.
- ☁️ **Optional database support** (SQLite / PostgreSQL). 

---

## ⚡ Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/expense-tracker.git
   ```
2. Navigate to the project folder:
   ```bash
   cd expense-tracker
   ```
3. Run the program:
   ```bash
   python expense_tracker.py
   ```

---

## 📌 Notes

- All expense history is stored in `history.txt`.  
- Dates must be entered in `dd-mm-yyyy` format.  
- If you enter a wrong date or number, the program will notify you with an error message.  

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request with improvements.  

