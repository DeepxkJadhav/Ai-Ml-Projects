<h1 align="center">💸 Expenzly</h1>
<p align="center">
    Smart AI-Powered Expense Classifier & Financial Toolkit<br>
    <strong>Built with Streamlit, Scikit-learn, and Love ❤️</strong>
</p>

<p align="center">
    <img src="https://img.shields.io/badge/Streamlit-%F0%9F%93%8A-red?style=for-the-badge" alt="Streamlit badge">
    <img src="https://img.shields.io/badge/ScikitLearn-%F0%9F%96%A5-blue?style=for-the-badge" alt="Scikit-learn badge">
    <img src="https://img.shields.io/badge/Finance%20AI-%F0%9F%92%B0-success?style=for-the-badge" alt="Finance AI badge">
    <img src="https://img.shields.io/badge/Status-Stable-green?style=for-the-badge" alt="Status Stable badge">
</p>

---

## 🧠 About the Project

**Expenzly** is a production-ready, AI-enhanced financial assistant designed to:
- 🧠 Automatically **classify your expenses** using NLP and Machine Learning.
- 🧮 Help you **plan budgets** and track **monthly savings**.
- 📊 Visualize insights like **spending trends** and **category distributions**.
- 📂 Handle real-time inputs, batch predictions, and CSV uploads seamlessly.

> Imagine a personal finance coach + accountant in one. That’s Expenzly.

---

## 🚀 Features

- 🔮 **AI Expense Categorization**  
    Classify expenses into categories like Rent, Transport, Dining, Insurance, etc., using a trained ML model.

- 📥 **Single & Batch Inputs**  
    Paste one item or hundreds — Expenzly scales!

- 📁 **CSV Upload Support**  
    Upload your financial data and get categorized results + download CSV reports.

- 💰 **Budget Calculator**  
    Enter income, customize expenses, and track real-time savings.

    ![Budget planner interface showing categorized expenses, input fields for income and expenses, and summary of savings. The interface is clean and modern, with a positive and encouraging tone.](image.png)

- 📊 **Insight Dashboard**  
    Interactive visual breakdowns with pie charts, line graphs, and smart tips.

---

## 🛠️ Tech Stack

| Tool / Library        | Purpose                      |
|-----------------------|------------------------------|
| `Streamlit`           | Frontend & UI                |
| `Scikit-learn`        | ML Model for classification  |
| `Pickle`              | Serialized model handling    |
| `Matplotlib`          | Visualizations               |
| `Pandas`              | Data handling + CSV support  |
| `Pillow`              | Logo/image rendering         |

---

🏁 Getting Started
🔧 Install Dependencies
bash
Copy code
pip install -r requirements.txt
▶️ Run Locally
bash
Copy code
streamlit run app.py
App will be live at: http://localhost:8501


📦 Model Training (Optional)
python
Copy code
# Train a classifier from your labeled expense data (CSV format)
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

pipeline.fit(X_train, y_train)
# Save with pickle

📫 Contact
Developer: Deepak Jadhav
Email : deepak.s.jadhav07@example.com
LinkedIn: linkedin.com/in/deepakjadhav
Portfolio: In progess

⭐ Hiring Managers, TL;DR:
✅ Full-stack ML-powered finance app

✅ Production-ready UI/UX with custom styling

✅ Handles NLP + classification + file processing

✅ Deployable, extensible, and polished

👉 Let's talk. I build things that work — smart, usable, and beautiful.

<p align="center"> Made with 💸 by <strong>[Deepak]</strong> — 2025 </p> ```