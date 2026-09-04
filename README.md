# 📚 Bookstore Management & Sales Analysis

A professional Python project that combines **bookstore inventory management, sales recording, data analysis, and data visualization** using Pandas, NumPy, Matplotlib, and Seaborn.

## 📌 Project Overview

This project provides a simple bookstore management system that can:

- Manage book inventory
- Add new books and update stock
- Record book sales
- Calculate revenue
- Generate inventory reports
- Analyze sales data
- Identify best-selling books
- Analyze revenue by genre
- Visualize sales trends and relationships

The project uses CSV files for storing inventory and sales data, making it easy to understand and suitable for a beginner-to-intermediate Python portfolio.

## ✨ Key Features

### 1. Bookstore Management

The `Bookstore` class manages the store's inventory and sales files.

- Load inventory from `inventory.csv`
- Add or update books
- Update inventory quantities
- Record sales
- Prevent sales when stock is insufficient
- Generate inventory reports

### 2. Data Analysis

The project uses **NumPy** and **Pandas** to perform:

- Total revenue calculation
- Average book price calculation
- Best-selling book analysis
- Revenue analysis by genre
- Data merging between sales and inventory datasets

### 3. Data Visualization

The project creates a 2×2 visualization dashboard containing:

- **Bar Chart:** Total Sales by Genre
- **Line Graph:** Monthly Sales Trends
- **Pie Chart:** Revenue Share by Genre
- **Heatmap:** Correlation between price, quantity sold, and revenue

## 🛠️ Technologies Used

- **Python 3**
- **Pandas** – data manipulation and CSV processing
- **NumPy** – numerical calculations
- **Matplotlib** – data visualization
- **Seaborn** – statistical visualization

## 📂 Project Structure

```text
Bookstore-Management/
│
├── bookstore_system.py     # Main Python application
├── inventory.csv           # Book inventory data
├── sales.csv               # Sales transaction data
└── README.md               # Project documentation
````

## 📊 Dataset Details

### `inventory.csv`

Contains information such as:

* Book title
* Author
* Genre
* Price
* Quantity in stock

### `sales.csv`

Contains:

* Sale date
* Book title
* Quantity sold
* Total revenue

If the CSV files do not exist, the program can generate sample inventory and sales datasets automatically.

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Bookstore-Management
```

### 2. Install dependencies

```bash
pip install numpy pandas matplotlib seaborn
```

### 3. Run the project

```bash
python bookstore_system.py
```

## 🔍 Example Operations

The main program demonstrates:

```python
store.add_book("Dune", "Frank Herbert", "Sci-Fi", 14.99, 20)
store.record_sale("1984", 2, "2026-09-04")
store.generate_report()
```

The project then performs sales analysis and displays the visualization dashboard.

## 📈 Skills Demonstrated

This project showcases practical skills in:

* Object-Oriented Programming (OOP)
* Python file handling
* CSV data processing
* Data cleaning and merging
* NumPy calculations
* Pandas DataFrame operations
* GroupBy analysis
* Data visualization
* Inventory management logic
* Sales and revenue analysis
* Basic data analytics workflow

## 🎯 Project Purpose

This project was developed as a **professional portfolio/showcase project** to demonstrate the practical use of Python programming and data analytics concepts in a real-world bookstore scenario.

It is suitable for showcasing skills in:

* Python Development
* Data Analysis
* Data Visualization
* Beginner Data Science
* OOP-based application development

## 🚀 Future Improvements

Possible enhancements include:

* Add a graphical user interface (GUI)
* Add user authentication
* Add a database such as MySQL or SQLite
* Add customer management
* Add search and filtering functionality
* Export analytical reports
* Add automated low-stock alerts
* Build an interactive dashboard using Streamlit

## 👤 Author

**Angel Bareja**
