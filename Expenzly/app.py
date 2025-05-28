import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from PIL import Image

# === Load Model and Vectorizer ===
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# === Load Logo ===
logo = Image.open("logo/logo.png")

# === Category Icons ===
category_icons = {
    "Groceries": "🛒",
    "Utilities": "💡",
    "Entertainment": "🎬",
    "Dining": "🍽️",
    "Rent": "🏠",
    "Transport": "🚗",
    "Shopping": "🛍️",
    "Health": "💪",
    "Travel": "✈️",
    "Education": "📚",
    "Insurance": "🛡️",
    "Other": "📁"
}

# === Page Config ===
st.set_page_config(page_title="Expenzly", page_icon="💸", layout="wide")

# === Style ===
st.markdown("""
    <style>
        .main { background-color: #f9fafc; }
        h1, h2, h3 {
            background: linear-gradient(to right, #1f3c88, #39b385);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .box {
            background-color: white;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }
        .small {
            font-size: 0.9rem;
            color: gray;
        }
    </style>
""", unsafe_allow_html=True)

# === Header ===
col1, col2 = st.columns([0.1, 0.9])
with col1:
    st.image(logo, width=60)
with col2:
    st.title("Expenzly")
    st.markdown("Smart AI-powered expense categorizer and finance toolkit.")

# === Sidebar Navigation ===
st.sidebar.header("🔍 Explore")
page = st.sidebar.radio("Go to", [
    "📥 Single Input",
    "📋 Batch Input",
    "📁 CSV Upload",
    "🧮 Budget Calculator",
    "📊 Insights"
])

# === Prediction Function ===
def predict_category(desc_list):
    vec = vectorizer.transform(desc_list)
    preds = model.predict(vec)
    confidences = model.predict_proba(vec).max(axis=1) * 100
    return preds, confidences

# === Single Input ===
if page == "📥 Single Input":
    st.markdown("### 📝 Single Expense Prediction")
    desc = st.text_input("Enter an expense description:")
    if st.button("🔮 Predict"):
        if not desc.strip():
            st.warning("Please enter something.")
        else:
            pred, conf = predict_category([desc])
            icon = category_icons.get(pred[0], "📁")
            st.success(f"{icon} Category: **{pred[0]}**  |  Confidence: **{conf[0]:.2f}%**")

# === Batch Input ===
elif page == "📋 Batch Input":
    st.markdown("### 🧾 Paste Multiple Expenses")
    multi_input = st.text_area("Enter one expense per line:")
    if st.button("🚀 Predict All"):
        lines = [line.strip() for line in multi_input.split('\n') if line.strip()]
        if not lines:
            st.warning("Please enter valid input.")
        else:
            preds, confs = predict_category(lines)
            result_df = pd.DataFrame({
                "Description": lines,
                "Category": preds,
                "Confidence (%)": [f"{c:.2f}" for c in confs]
            })
            st.dataframe(result_df)

            # Pie chart 
            st.markdown("#### 📊 Category Breakdown")
            fig, ax = plt.subplots(figsize=(3, 3))  # Reduced size
            result_df['Category'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
            ax.set_ylabel('')
            st.pyplot(fig)


# === CSV Upload ===
elif page == "📁 CSV Upload":
    st.markdown("### 📤 Upload CSV")
    file = st.file_uploader("Upload a CSV with a `Description` column", type=["csv"])
    if file:
        df = pd.read_csv(file)
        if 'Description' not in df.columns:
            st.error("Missing 'Description' column.")
        else:
            descs = df['Description'].dropna().astype(str).tolist()
            preds, confs = predict_category(descs)
            result_df = pd.DataFrame({
                "Description": descs,
                "Category": preds,
                "Confidence (%)": [f"{c:.2f}" for c in confs]
            })
            st.dataframe(result_df)
            st.download_button("⬇️ Download Results", result_df.to_csv(index=False), file_name="categorized.csv")

# === Budget Calculator ===
elif page == "🧮 Budget Calculator":
    st.markdown("### 💰 Budget Planner")
    
    income = st.number_input("Monthly Income (₹)", min_value=0)

    st.markdown("#### 📝 Customize Your Expenses")
    with st.form("budget_form"):
        categories = ["Rent", "Groceries & Dining", "Transport & Travel", "Miscellaneous"]
        expenses = {}
        for category in categories:
            expenses[category] = st.number_input(f"{category}", min_value=0.0, key=category)
        submitted = st.form_submit_button("🧾 Calculate Summary")
    
    if submitted:
        total_expense = sum(expenses.values())
        savings = income - total_expense

        # Dynamic message based on savings
        if savings < 0:
            msg = '<span style="color:#d9534f;">⚠️ You are overspending! Try to reduce your expenses.</span>'
            bg = "#fff"  # Changed to white for better contrast
            border = "#d9534f"
        elif savings < 0.2 * income:
            msg = '<span style="color:#f0ad4e;">💡 Your savings are below 20%. Consider adjusting your budget.</span>'
            bg = "#fff"  # Changed to white for better contrast
            border = "#f0ad4e"
        else:
            msg = '<span style="color:#5cb85c;">🎉 Great! You are saving a healthy portion of your income.</span>'
            bg = "#fff"  # Changed to white for better contrast
            border = "#5cb85c"

        st.markdown(f"""
            <div class="box" style="background-color:{bg}; padding:1.5rem; border-radius:12px; 
            box-shadow:0 4px 12px rgba(0,0,0,0.05); border: 2px solid {border};">
            <h4 style="color:#1f3c88;">Total Expenses: ₹{total_expense:.2f}</h4>
            <h4 style="color:#39b385;">Savings: ₹{savings:.2f}</h4>
            <p class="small">{msg}</p>
            </div>
        """, unsafe_allow_html=True)



# === Insights ===
elif page == "📊 Insights":
    st.markdown("### 📊 Finance Insights Dashboard")

    # Simulated placeholder values for demo
    st.markdown("#### 🔍 Expense Category Distribution")
    demo_data = pd.Series({
        "Rent": 25000,
        "Groceries": 8000,
        "Transport": 3000,
        "Entertainment": 2000,
        "Other": 1000
    })
    fig1, ax1 = plt.subplots(figsize=(3, 3))  # Reduced size
    demo_data.plot.pie(autopct='%1.1f%%', ax=ax1)
    ax1.set_ylabel('')
    st.pyplot(fig1)

    st.markdown("#### 📈 Monthly Expense Trend (Mock)")
    months = ["Jan", "Feb", "Mar", "Apr", "May"]
    expenses = [40000, 42000, 39000, 45000, 41000]
    fig2, ax2 = plt.subplots(figsize=(4, 2.5))  # Reduced size
    ax2.plot(months, expenses, marker='o', color='#1f77b4')
    ax2.set_title("Monthly Spending")
    ax2.set_ylabel("Amount (₹)")
    st.pyplot(fig2)

    st.markdown("#### 💡 Tips")
    st.info("Consider using category limits, and track recurring expenses to improve savings.")

# === Footer ===
st.markdown("---")
st.markdown("<center>Made with 💸 by Expenzly · © 2025</center>", unsafe_allow_html=True)

# === Additional Feature: Expense Category Suggestions ===
# Suggests possible categories as user types in Single Input

if page == "📥 Single Input":
    st.markdown("#### 💡 Category Suggestions")
    desc_partial = st.text_input("Start typing an expense description for suggestions:", key="suggest")
    if desc_partial.strip():
        # Use vectorizer to get similar words/categories (simple demo: show top 3 probable categories)
        vec = vectorizer.transform([desc_partial])
        proba = model.predict_proba(vec)[0]
        top_idx = np.argsort(proba)[::-1][:3]
        top_cats = [model.classes_[i] for i in top_idx]
        st.write("Top Suggestions:", ", ".join([f"{category_icons.get(cat, '📁')} {cat}" for cat in top_cats]))

# === Additional Feature: Download Example CSV Template ===
if page == "📁 CSV Upload":
    st.markdown("#### 📄 Download Example CSV Template")
    example_df = pd.DataFrame({"Description": ["Paid rent", "Bought groceries", "Uber ride", "Movie night"]})
    st.download_button("⬇️ Download Example CSV", example_df.to_csv(index=False), file_name="example_expenses.csv")

# === Additional Feature: About & Help Section in Sidebar ===
with st.sidebar.expander("ℹ️ About & Help"):
    st.markdown("""
    **Expenzly** helps you categorize expenses using AI, plan budgets, and gain insights.
    - Use **Single Input** for one expense.
    - Use **Batch Input** or **CSV Upload** for many expenses.
    - **Budget Calculator** helps plan your monthly finances.
    - **Insights** shows trends and tips.
    ---
    **Need help?** Contact: support@expenzly.com
    """)
