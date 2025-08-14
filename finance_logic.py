# finance_logic.py

def calculate_income_tax(income):
    tax = 0
    # Simplified Indian tax slabs FY 2024-25 for individuals <60 yrs
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = 12500 + (income - 500000) * 0.20
    else:
        tax = 112500 + (income - 1000000) * 0.30
    return round(tax, 2)

def analyze_expenses(expenses):
    total = sum(expenses.values())
    advice = []
    for k, v in expenses.items():
        perc = (v / total) * 100
        if perc > 40:
            advice.append(f"High spending on {k}. Consider reducing it.")
    if not advice:
        advice.append("Your expenses seem balanced.")
    return advice

def investment_advice(income, expenses, investments):
    savings = income - sum(expenses.values()) - sum(investments.values())
    advice = []
    if savings < 0:
        advice.append("You are overspending! Reduce expenses immediately.")
    elif savings < income * 0.1:
        advice.append("Try to save at least 10% of your income.")
    else:
        advice.append("Your savings are good. Consider diversifying investments.")
    return advice
