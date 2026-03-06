#py --version
#py -m pip install pandas
#py -m pip install matplotlib
#py -m pip install seaborn
#py -m pip install scikit-learn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create synthetic data
data = {
    "Advertising_Spend": [10, 20, 30, 40, 50, 60, 70, 80],
    "Sales_Revenue": [15, 25, 35, 45, 55, 65, 78, 90]
}

# Create DataFrame
df = pd.DataFrame(data)

# Print dataset
print(df)

# Independent variable (X) and Dependent variable (y)
X = df[["Advertising_Spend"]]
y = df["Sales_Revenue"]

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Predict values
y_pred = model.predict(X)

# Print model parameters
print("Slope (m):", model.coef_[0])
print("Intercept (c):", model.intercept_)

# Plot graph
plt.figure(figsize=(7,5))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred, color='red', label='Regression Line')

plt.xlabel("Advertising Spend")
plt.ylabel("Sales Revenue")
plt.title("Linear Regression on Data Warehouse Sales Data")
plt.legend()
plt.show()
