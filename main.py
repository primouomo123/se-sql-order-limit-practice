import pandas as pd
import sqlite3


conn = sqlite3.connect('data.sqlite')
# products table
print(pd.read_sql("""
SELECT *
 FROM products;
""", conn))

# Step 1
# Order the data by product code in descending order.
print(pd.read_sql("""
SELECT *
 FROM products
ORDER BY productCode DESC;
""", conn))
print("\n")

# Step 2
# Select the product code, product name, product line, and product vendor.
 # Sort by product line and then product name.
print(pd.read_sql("""
SELECT productCode, productLine, productName, productVendor
 FROM products
ORDER BY productLine, productName;
""", conn))
print("\n")

# Step 3
# Count how many distinct product lines there are.
print(pd.read_sql("""
SELECT COUNT(DISTINCT productLine) AS productLineCount
 FROM products
""", conn))
print("\n")

# Step 4
# Select the product name, quantity in stock, the MSRP, the buy price, and find the difference between
# the MSRP and buy price.
 # Call this difference difference.
 # Order by the difference from the greatest to the least, and then by quantity in stock from least to greatest.
print(pd.read_sql("""
SELECT productName, quantityInStock, MSRP, buyPrice, MSRP - buyPrice AS difference
 FROM products
ORDER BY difference DESC, CAST(quantityInStock AS INTEGER) ASC;
""", conn))
print("\n")

# Step 5
# Select the product name, product line, the MSRP, and the buy price.
 # Find the difference between the buy price and MSRP, but use the absolute value to make the difference positive.
 # Call this difference abs_difference.
 # Order by the difference from the greatest to the least.
 # Only select the "Classic Cars" product line.
 # Limit the results to the top 10.
print(pd.read_sql("""
SELECT productName, productLine, MSRP, buyPrice, abs(buyPrice - MSRP) AS abs_difference
 FROM products
 WHERE productLine ="Classic Cars"
ORDER BY abs_difference DESC
LIMIT 10;
""", conn))
print("\n")

conn.close()