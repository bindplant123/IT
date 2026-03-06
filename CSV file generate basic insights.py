#py --version
#py -m pip install pandas
#py -m pip install matplotlib
#py -m pip install seaborn
#py -m pip install scikit-learn

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read CSV file
file_path = "E:\\GUYS\\Code\\BI\\DATA.csv"
data = pd.read_csv(file_path)

# Step 2: Display first few rows
print("First 5 rows of the dataset:")
print(data.head())

# Step 3: Display basic information
print("\nDataset Information:")
data.info()

# Step 4: Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Step 5: Basic statistical analysis
print("\nStatistical Summary:")
print(data.describe())

# Step 6: Generate simple insights
print("\nBasic Insights:")

for column in data.select_dtypes(include=['int64', 'float64']).columns:
    print(f"\nColumn: {column}")
    print(f"Mean: {data[column].mean()}")
    print(f"Maximum: {data[column].max()}")
    print(f"Minimum: {data[column].min()}")

# Step 7: Data Visualization
numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns

if len(numeric_columns) > 0:
    data[numeric_columns[0]].plot(kind='line', title='Basic Line Plot')
    plt.xlabel("Index")
    plt.ylabel(numeric_columns[0])
    plt.show()
else:
    print("No numerical columns available for plotting.")
