<div align="center">

# 💰 Smart Finance Insights

### 🤖 AI-Powered Personal Finance Management Platform

Manage your income, expenses, budgets, investments, financial goals, and AI-driven financial insights through one elegant dashboard.

<br>

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Cloud-000000?style=for-the-badge)
![AI](https://img.shields.io/badge/AI-GPT--OSS%2020B-7C3AED?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-1.0.0-orange?style=for-the-badge)

<br>

**🌐 Live Demo:**  
https://moumitadev.pythonanywhere.com/

</div>

---

# 📖 Overview

**Smart Finance Insights** is a modern AI-powered personal finance management platform developed using **Python, Flask, SQLite, JavaScript, and AI technologies**.

The platform helps users manage their personal finances from a centralized dashboard. Users can track income and expenses, create budgets, manage investments, monitor financial goals, analyze spending patterns, generate reports, and receive AI-powered financial assistance.

The application combines **financial management, data analytics, artificial intelligence, machine learning, and reporting** into a single web-based platform.

---

# ✨ Key Features

## 💵 Income Management

- Add monthly income
- Update income records
- Delete income records
- Income overview
- Monthly statistics

---

## 💸 Expense Tracking

- Add expenses
- Edit expenses
- Delete expenses
- Category-wise expense tracking
- Monthly expense analysis
- Spending insights

---

## 📊 Interactive Dashboard

- Financial summary
- Income vs Expense
- Monthly financial charts
- Savings overview
- Budget status
- Financial Health Score

---

## 🎯 Budget Planning

- Create monthly budgets
- Category-wise budgeting
- Track budget utilization
- Remaining budget calculation
- Budget alerts
- AI Budget Advisor

---

## 🤖 AI Financial Assistant

The platform includes an AI-powered conversational financial assistant.

Users can ask normal financial questions and receive intelligent responses.

### AI capabilities include:

- General financial questions
- Saving recommendations
- Spending analysis
- Financial suggestions
- Budget-related guidance
- Personalized financial insights

The deployed application uses **Ollama Cloud with the GPT-OSS 20B model**.

---

## 🧠 AI Financial Insights

The AI module analyzes financial information and provides useful insights based on the user's financial activity.

### Features include:

- Spending insights
- Savings recommendations
- Financial health suggestions
- Budget recommendations
- Investment-related insights

---

## 📈 Financial Analytics

Interactive financial visualizations help users understand their financial behavior.

### Analytics include:

- Income vs Expense
- Expense category analysis
- Budget analysis
- Spending trends
- Investment portfolio analysis
- Financial health analysis

---

## 💼 Investment Portfolio

Users can manage their investment portfolio through the platform.

### Features include:

- Add investments
- Edit investments
- Track invested amount
- Track current value
- Purchase date
- Investment notes
- Portfolio analytics
- Asset allocation

---

## 🎯 Financial Goals

Users can create and monitor their financial goals.

### Features include:

- Create financial goals
- Set target amounts
- Track progress
- Update saved amounts
- Goal completion percentage
- Active/Achieved status

---

## 🛡️ Fraud Detection

The platform includes a machine-learning-based fraud prediction module.

### Features include:

- Transaction analysis
- Fraud prediction
- Machine learning model
- Prediction history
- Fraud analysis dashboard

---

## 📄 Financial Reports

Users can generate financial reports based on their financial data.

### Supported reports include:

- Financial summaries
- PDF reports
- Excel reports
- Income reports
- Expense reports
- Investment information

---

## 📅 Financial Calendar

The financial calendar helps users organize and view important financial activities and dates in one place.

---

## 🔔 Notifications

The platform provides financial notifications and alerts for important activities.

Examples include:

- Budget-related notifications
- Savings notifications
- Spending notifications
- Financial achievement notifications

---

## 👤 User Management

The application provides a complete user authentication and profile system.

### Includes:

- User registration
- Login
- Logout
- OTP verification
- Forgot password
- Reset password
- Profile management
- User settings

---

## 🌙 Dark Mode

The platform includes a modern dark-mode interface for a comfortable user experience.

---

# 🛠️ Technologies Used

<div align="center">

| Category | Technologies |
|---|---|
| **Programming Language** | Python |
| **Web Framework** | Flask |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Database** | SQLite |
| **Data Visualization** | Chart.js |
| **AI** | Ollama Cloud, GPT-OSS 20B |
| **Machine Learning** | Python ML Models |
| **Document Processing** | PDFPlumber, EasyOCR |
| **Reporting** | PDF, Excel |
| **Package Management** | pip, npm |
| **Version Control** | Git & GitHub |
| **Deployment** | PythonAnywhere |

</div>

---

# 🏗️ Project Architecture

```text
                         ┌─────────────────────┐
                         │       USER          │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Web Interface     │
                         │ HTML/CSS/JavaScript │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Flask Backend    │
                         └──────────┬──────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
              ▼                     ▼                     ▼
      ┌───────────────┐     ┌───────────────┐     ┌───────────────┐
      │   Financial   │     │   Analytics   │     │   AI / ML     │
      │   Management  │     │    Engine     │     │    Engine     │
      └───────┬───────┘     └───────┬───────┘     └───────┬───────┘
              │                     │                     │
              ▼                     ▼                     ▼
        Income/Expense         Charts & Reports      AI Assistant
        Budget                 Spending Analysis      Budget Advisor
        Investments            Portfolio Analytics   Fraud Prediction
        Goals                  Financial Health      AI Insights
              │                     │                     │
              └─────────────────────┼─────────────────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      SQLite DB      │
                         └─────────────────────┘

📁 Project Structure
SmartFinanceInsights/
│
├── ai/
│   ├── finance_ai.py
│   ├── fraud_analysis.py
│   ├── model.py
│   ├── predictor.py
│   └── train_model.py
│
├── database/
│   ├── create_db.py
│   ├── db.py
│   └── schema.sql
│
├── finance_ai/
│   ├── chart_engine.py
│   ├── chat_engine.py
│   ├── config.py
│   ├── database_manager.py
│   ├── document_processor.py
│   ├── finance_ai.py
│   ├── memory_manager.py
│   ├── prompt_builder.py
│   ├── report_engine.py
│   ├── tool_router.py
│   └── utils.py
│
├── models/
│   ├── encoders.pkl
│   └── fraud_model.pkl
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│
├── app.py
├── package.json
├── package-lock.json
├── .gitignore
├── LICENSE
├── README.md
└── TODO.md
🔄 Application Workflow
User
  │
  ▼
Login / Registration
  │
  ▼
Dashboard
  │
  ├── Income Management
  │
  ├── Expense Management
  │
  ├── Budget Planning
  │
  ├── Investment Portfolio
  │
  ├── Financial Goals
  │
  ├── Analytics
  │
  ├── Financial Health
  │
  ├── Reports
  │
  ├── Fraud Prediction
  │
  └── AI Financial Assistant
            │
            ▼
       Ollama Cloud
            │
            ▼
       GPT-OSS 20B
            │
            ▼
     Intelligent Response
🤖 AI Assistant Architecture
User Question
      │
      ▼
Chat Assistant Interface
      │
      ▼
Flask Backend
      │
      ▼
Chat Engine
      │
      ▼
Ollama Cloud API
      │
      ▼
GPT-OSS 20B
      │
      ▼
AI Generated Response

The AI API credentials are stored securely using environment variables and are not included in this repository.
