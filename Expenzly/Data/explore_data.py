import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('expense_data.csv')

# Print first 5 rows to see what data looks like
print("Sample data:")
print(df.head())

# Show count of samples per category
print("\nCategory distribution:")
print(df['Category'].value_counts())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())
