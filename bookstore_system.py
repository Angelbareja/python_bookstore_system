import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_sample_datasets():
    if not os.path.exists("inventory.csv"):
        inventory_data = {
            "Title": [
                "The Great Gatsby",
                "To Kill a Mockingbird",
                "1984",
                "Pride and Prejudice",
                "The Catcher in the Rye",
            ],
            "Author": [
                "F. Scott Fitzgerald",
                "Harper Lee",
                "George Orwell",
                "Jane Austen",
                "J.D. Salinger",
            ],
            "Genre": ["Fiction", "Classic", "Dystopian", "Romance", "Classic"],
            "Price": [10.99, 12.50, 15.00, 9.99, 11.25],
            "Quantity": [50, 30, 40, 25, 35],
        }
        pd.DataFrame(inventory_data).to_csv("inventory.csv", index=False)

    if not os.path.exists("sales.csv"):
        dates = pd.date_range(start="2026-01-01", periods=12, freq="ME").strftime(
            "%Y-%m-%d"
        )
        sales_data = {
            "Date": np.random.choice(dates, size=30),
            "Title": np.random.choice(
                [
                    "The Great Gatsby",
                    "To Kill a Mockingbird",
                    "1984",
                    "Pride and Prejudice",
                    "The Catcher in the Rye",
                ],
                size=30,
            ),
            "Quantity Sold": np.random.randint(1, 10, size=30),
        }
        df_sales = pd.DataFrame(sales_data)
        price_map = {
            "The Great Gatsby": 10.99,
            "To Kill a Mockingbird": 12.50,
            "1984": 15.00,
            "Pride and Prejudice": 9.99,
            "The Catcher in the Rye": 11.25,
        }
        df_sales["Total Revenue"] = (
            df_sales["Title"].map(price_map) * df_sales["Quantity Sold"]
        )
        df_sales.to_csv("sales.csv", index=False)


# 1. & 2. BOOKSTORE CLASS

class Bookstore:
    def __init__(self, inventory_file="inventory.csv", sales_file="sales.csv"):
        self.inventory_file = inventory_file
        self.sales_file = sales_file
        self.inventory = {}
        self.load_inventory()

    def load_inventory(self):
        if os.path.exists(self.inventory_file):
            df = pd.read_csv(self.inventory_file)
            for _, row in df.iterrows():
                self.inventory[row["Title"]] = {
                    "Author": row["Author"],
                    "Genre": row["Genre"],
                    "Price": float(row["Price"]),
                    "Quantity": int(row["Quantity"]),
                }

    def add_book(self, title, author, genre, price, quantity):
        
        if price <= 0 or quantity < 0:
            print("Error: Price must be positive and Quantity non-negative.")
            return False

        if title in self.inventory:
            self.inventory[title]["Quantity"] += quantity
        else:
            self.inventory[title] = {
                "Author": author,
                "Genre": genre,
                "Price": price,
                "Quantity": quantity,
            }
        print(f"Successfully added/updated '{title}'.")
        return True

    def update_inventory(self, title, quantity):

        if title in self.inventory:
            if quantity < 0:
                print("Error: Quantity cannot be negative.")
                return False
            self.inventory[title]["Quantity"] = quantity
            print(f"Updated '{title}' inventory stock to {quantity}.")
            return True
        else:
            print(f"Error: Book '{title}' not found in inventory.")
            return False

    def record_sale(self, title, quantity, sale_date):
        
        if title not in self.inventory:
            print(f"Error: Book '{title}' not found in inventory.")
            return False

        if self.inventory[title]["Quantity"] < quantity:
            print(f"Error: Insufficient stock for '{title}'.")
            return False

        # Deduct stock
        self.inventory[title]["Quantity"] -= quantity
        revenue = self.inventory[title]["Price"] * quantity

        # Append to sales
        new_sale = pd.DataFrame(
            [
                {
                    "Date": sale_date,
                    "Title": title,
                    "Quantity Sold": quantity,
                    "Total Revenue": revenue,
                }
            ]
        )
        new_sale.to_csv(
            self.sales_file,
            header=not os.path.exists(self.sales_file),
            index=False,
        )
        print(f"Sale recorded: {quantity} units of '{title}' for total {revenue:.2f}.")
        
        return True

    def generate_report(self):
        
        total_items = sum(item["Quantity"] for item in self.inventory.values())
        total_val = sum(
            item["Quantity"] * item["Price"] for item in self.inventory.values()
        )
        print("\n--- INVENTORY REPORT ---")
        print(f"Total Unique Titles: {len(self.inventory)}")
        print(f"Total Book Units Stocked: {total_items}")
        print(f"Total Inventory Valuation: {total_val:.2f}\n")


# 3. SALES ANALYSIS & COMPUTATIONS

def analyze_sales(sales_file="sales.csv", inventory_file="inventory.csv"):
    df_sales = pd.read_csv(sales_file)
    df_inv = pd.read_csv(inventory_file)

    df_merged = pd.merge(df_sales, df_inv, on="Title", how="left")

    revenues = df_merged["Total Revenue"].to_numpy()
    prices = df_inv["Price"].to_numpy()

    total_revenue = np.sum(revenues)
    avg_price = np.mean(prices)

    print("\n--- NUMPY ANALYSIS ---")
    print(f"Total Revenue Generated: ${total_revenue:.2f}")
    print(f"Average Book Price: ${avg_price:.2f}")

    best_sellers = df_sales.groupby("Title")["Quantity Sold"].sum().sort_values(ascending=False)
    genre_revenue = df_merged.groupby("Genre")["Total Revenue"].sum()

    print("\n--- PANDAS ANALYSIS ---")
    print("Best-Selling Books (Units Sold):")
    print(best_sellers)
    print("\nRevenue Distribution by Genre:")
    print(genre_revenue)

    return df_merged


# 4. DATA VISUALIZATION

def create_visualizations(df_merged, inventory_file="inventory.csv"):
    df_inv = pd.read_csv(inventory_file)
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # 1. Bar Chart
    genre_sales = df_merged.groupby("Genre")["Total Revenue"].sum().reset_index()
    sns.barplot(x="Genre", y="Total Revenue", data=genre_sales, ax=axes[0, 0], palette="viridis")
    axes[0, 0].set_title("Total Sales by Genre")
    axes[0, 0].set_ylabel("Revenue ")

    # 2. Line Graph
    df_merged["Date"] = pd.to_datetime(df_merged["Date"])
    monthly_sales = df_merged.resample("ME", on="Date")["Total Revenue"].sum().reset_index()
    sns.lineplot(x="Date", y="Total Revenue", data=monthly_sales, marker="o", ax=axes[0, 1], color="b")
    axes[0, 1].set_title("Monthly Sales Trends")
    axes[0, 1].set_ylabel("Revenue ")

    # 3. Pie Chart
    axes[1, 0].pie(
        genre_sales["Total Revenue"],
        labels=genre_sales["Genre"],
        autopct="%1.1f%%",
        startangle=140,
    )
    axes[1, 0].set_title("Revenue Share by Genre")

    # 4. Heatmap
    correlation_data = df_merged[["Price", "Quantity Sold", "Total Revenue"]].corr()
    sns.heatmap(correlation_data, cmap="coolwarm", ax=axes[1, 1])
    axes[1, 1].set_title("Price vs. Sales Volume Correlation")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":

    generate_sample_datasets()

    store = Bookstore()

    store.add_book("Dune", "Frank Herbert", "Sci-Fi", 14.99, 20)
    store.record_sale("1984", 2, "2026-09-04")
    store.generate_report()

    merged_data = analyze_sales()

    create_visualizations(merged_data)
