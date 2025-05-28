import pandas as pd

# Sample data - transaction descriptions with categories
data = {
    'Description': [
        'Walmart Grocery Store',
        'Electricity Bill Payment',
        'Netflix Subscription',
        'Starbucks Coffee',
        'Monthly Rent',
        'Uber Ride',
        'Gas Station',
        'Amazon Purchase',
        'Water Bill',
        'Gym Membership',
        'Apple Store',
        'Movie Theater',
        'Internet Provider',
        'Taxi Fare',
        'Restaurant Dinner'
    ],
    'Category': [
        'Groceries',
        'Utilities',
        'Entertainment',
        'Dining',
        'Rent',
        'Transport',
        'Transport',
        'Shopping',
        'Utilities',
        'Health',
        'Shopping',
        'Entertainment',
        'Utilities',
        'Transport',
        'Dining'
    ]
}

df = pd.DataFrame(data)
df.to_csv('expense_data.csv', index=False)
print("Sample dataset saved as 'expense_data.csv'")
