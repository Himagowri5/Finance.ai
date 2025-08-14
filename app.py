# app.py
import streamlit as st
import json
from finance_logic import calculate_income_tax, analyze_expenses, investment_advice
from chatbot_api import get_chatbot_response

st.set_page_config(page_title="Personal Finance Chatbot", layout="wide")

st.title("💰 Personal Finance Chatbot")

# User Input Section
st.sidebar.header("Enter Your Financial Data")
income = st.sidebar.number_input("Monthly Income (INR)", min_value=0, value=50000)
rent = st.sidebar.number_input("Rent / Housing", min_value=0, value=10000)
food = st.sidebar.number_input("Food / Groceries", min_value=0, value=8000)
transport = st.sidebar.number_input("Transport", min_value=0, value=3000)
other = st.sidebar.number_input("Other Expenses", min_value=0, value=5000)
mf = st.sidebar.number_input("Mutual Funds Investment", min_value=0, value=10000)
ppf = st.sidebar.number_input("PPF Investment", min_value=0, value=5000)

expenses = {"Rent": rent, "Food": food, "Transport": transport, "Other": other}
investments = {"Mutual Funds": mf, "PPF": ppf}

if st.sidebar.button("Analyze Finance"):
    # Tax calculation
    tax = calculate_income_tax(income)
    st.subheader("🧾 Tax Analysis")
    st.write(f"Your estimated income tax: **₹{tax}**")

    # Expense analysis
    st.subheader("💸 Expense Analysis")
    expense_advice = analyze_expenses(expenses)
    for adv in expense_advice:
        st.write(f"- {adv}")

    # Investment advice
    st.subheader("📈 Investment Advice")
    invest_advice = investment_advice(income, expenses, investments)
    for adv in invest_advice:
        st.write(f"- {adv}")

    # Chatbot Interaction
    st.title("💰 Personal Finance Chatbot")
st.subheader("🤖 Chatbot Advice")

# Input box for user question
user_question = st.text_input("Ask the chatbot for financial tips:")

# Display response only if user entered something
if user_question:
    hf_response = get_chatbot_response(user_question)
    st.write(hf_response)

    # Save data locally
    user_data = {
        "income": income,
        "expenses": expenses,
        "investments": investments
    }
    with open("data/user_data.json", "w") as f:
        json.dump(user_data, f)
