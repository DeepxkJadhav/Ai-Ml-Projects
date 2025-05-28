import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the dataset
df = pd.read_csv('expense_data.csv')

# Extract the expense descriptions
texts = df['Description']

# Initialize the TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Fit the vectorizer to the texts and transform them into vectors
X = vectorizer.fit_transform(texts)

# Check the shape of the result (rows = samples, cols = features)
print(f"Vectorized text shape: {X.shape}")

# Show the first 10 feature names (words)
print("First 10 feature names:", vectorizer.get_feature_names_out()[:10])
