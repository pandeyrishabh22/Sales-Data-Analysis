import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

df.dropna(inplace=True)

df['Order Date'] = pd.to_datetime(df['Order Date'])

df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()

print("\nTotal Sales:", total_sales)
print("Total Profit:", total_profit)

top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Products:")
print(top_products)

region_sales = df.groupby('Region')['Sales'].sum()
print("\nRegion-wise Sales:")
print(region_sales)

category_sales = df.groupby('Category')['Sales'].sum()
print("\nCategory-wise Sales:")
print(category_sales)

monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

plt.figure()
region_sales.plot(kind='bar')
plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

plt.figure()
category_sales.plot(kind='bar')
plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()