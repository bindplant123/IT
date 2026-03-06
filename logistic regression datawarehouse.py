#py --version
#py -m pip install pandas
#py -m pip install matplotlib
#py -m pip install seaborn
#py -m pip install scikit-learn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Sample synthetic data
data = {
    "Age": [22, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    "Income": [15, 18, 25, 30, 35, 45, 50, 60, 65, 70],
    "Purchase": [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display dataset
print(df)

# Independent variables
X = df[["Age", "Income"]]

# Dependent variable
y = df["Purchase"]

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Create Logistic Regression model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Model evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Create mesh grid for decision boundary
x_min, x_max = X["Age"].min() - 1, X["Age"].max() + 1
y_min, y_max = X["Income"].min() - 1, X["Income"].max() + 1

xx, yy = np.meshgrid(
    np.arange(x_min, x_max, 0.5),
    np.arange(y_min, y_max, 0.5)
)

# Convert grid to DataFrame to avoid warning
grid = pd.DataFrame(
    np.c_[xx.ravel(), yy.ravel()],
    columns=["Age", "Income"]
)

Z = model.predict(grid)
Z = Z.reshape(xx.shape)

# Plot decision boundary
plt.figure(figsize=(7,5))

plt.contourf(xx, yy, Z, alpha=0.3, cmap="coolwarm")

plt.scatter(
    X["Age"],
    X["Income"],
    c=y,
    edgecolor="k",
    cmap="coolwarm"
)

plt.xlabel("Age")
plt.ylabel("Income")
plt.title("Logistic Regression – Purchase Prediction")
plt.show()
