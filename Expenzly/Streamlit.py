import streamlit as st
import pickle

# Load model and vectorizer
with open('model.pkl', 'rb') as f:
    clf = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

st.title("Smart Expense Categorizer")

desc = st.text_area("Enter your expense description:")

if st.button("Categorize"):
    if desc.strip() == "":
        st.warning("Please enter an expense description!")
    else:
        desc_vec = vectorizer.transform([desc])
        prediction = clf.predict(desc_vec)[0]
        st.success(f"Category: {prediction}")
