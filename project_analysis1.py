import mysql.connector as sql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from openpyxl.workbook import Workbook

connect = sql.connect(host="localhost",user = "root",password = "omarahmed123@",database = "company")
cursor = connect.cursor()
statement = "select c.customer_name,p.product_name,s.quantity,p.price from customers c join sales s join products p on c.customer_id = s.customer_id and p.product_id = s.product_id"
cursor.execute(statement)
columns = [col[0] for col in cursor.description]
data = cursor.fetchall()
df = pd.DataFrame(data, columns = columns)
print(df)

sales_by_quantity = df.groupby("product_name")["quantity"].sum()
print(sales_by_quantity)
best_five_products = df.nlargest(5,"quantity")
print(best_five_products)


df.dropna(inplace = True)
df.drop_duplicates(inplace = True)
print(df.dtypes)
df["revenue"] = df["price"] * df["quantity"]

sum_of_revenue = df.groupby("product_name")["revenue"].sum()
print(sum_of_revenue)
best_customers = df.groupby("customer_name")["revenue"].sum().sort_values(ascending=False)
print(best_customers)
print(df["revenue"].sum())
print(df["revenue"].mean())
print(df.loc[df["quantity"].idxmax(),"product_name"])
best_customer = (df.groupby("customer_name")["revenue"].sum().idxmax())
print(best_customer)

revenue_by_product = df.groupby("product_name")["quantity"].sum()
revenue_by_product.plot(kind="line")
plt.title("Quantity Sold By Product")
plt.xlabel("Product Name")
plt.ylabel("Revenue")
plt.show()

plt.figure(figsize=(10,6))
top_five_products = (df.groupby("product_name")["quantity"].sum().nlargest(5))
top_five_products.plot(kind="bar")
plt.title("Top 5 Selling Products")
plt.xlabel("Product Name")
plt.xticks(rotation=0)
plt.ylabel("Quantity Sold")
plt.show()

"""
df.to_excel("sales_analysis_excel.xlsx",index=False)
summary = pd.DataFrame({
    "Total_Revenue":[df["revenue"].sum()],
    "Average_Revenue":[df["revenue"].mean()]
})


summary.to_excel("sales_summary_excel.xlsx",index=False)
"""
