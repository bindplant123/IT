# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read sales data from CSV file
data = pd.read_csv("C:\\Users\\abdul\\Downloads\\BI\\BI\\DATA 2.csv")

# Display dataset
print("Sales Data:")
print(data)

# Line Chart - Monthly Sales Trend
plt.figure(figsize=(8,5))
plt.plot(data["Month"], data["Sales"], marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.grid(True)

plt.show()

# Another simple line plot
plt.plot(data["Month"], data["Sales"], marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()