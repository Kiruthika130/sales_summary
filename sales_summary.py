import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="093616",
    database="sales_analysis"
)

# Step 2: Run SQL query
query = """
SELECT 
    product_id, 
    COUNT(*) AS total_orders, 
    SUM(amount) AS total_revenue 
FROM online_sales 
GROUP BY product_id

"""
df = pd.read_sql(query, conn)

# Step 3: Print results
print("📦 Basic Sales Summary:")
print(df)

# Step 4: Plot revenue by product
df.plot(kind='bar', x='product_id',
        y='total_revenue', color='teal', legend=False)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")  # Optional
plt.show()

# Step 5: Close connection
conn.close()
