# Finance Analytics Platform for Financial Reporting and Budget Tracking

## 📌 Project Overview

The **Finance Analytics Platform for Financial Reporting and Budget Tracking** is a web-based financial management and analytics application developed using Python and Flask.

The platform helps users manage their personal finances by tracking income, expenses, budgets, investments, financial goals, and financial reports. It also provides interactive analytics, AI-powered financial assistance, fraud prediction, and personalized financial insights.

---

## 🎯 Objectives

The main objectives of this project are:

- To provide a centralized platform for managing personal financial information.
- To track income and expenses efficiently.
- To help users create and monitor budgets.
- To provide financial analytics through interactive charts.
- To manage investments and financial goals.
- To generate financial reports.
- To provide AI-powered financial recommendations.
- To assist users in making better financial decisions.
- To provide fraud prediction and financial analysis features.

---

## ✨ Key Features

### 💰 Financial Management

- Income tracking
- Expense tracking
- Budget management
- Bill management
- Savings tracking
- Financial goals
- Investment portfolio management

### 📊 Financial Analytics

- Spending analysis
- Income vs. expense analysis
- Budget analysis
- Portfolio analytics
- Financial health analysis
- Interactive charts and visualizations

### 🤖 AI-Powered Features

- AI Financial Assistant
- Budget Advisor
- AI-powered financial insights
- Financial report generation
- Document analysis
- Personalized financial recommendations

### 🛡️ Fraud Detection

- Fraud prediction
- Machine learning based analysis
- Prediction history

### 📄 Reporting

- Financial report generation
- PDF reports
- Excel reports
- Financial summaries

### 🔔 Additional Features

- User authentication
- OTP verification
- Notifications
- Profile management
- Dark mode
- Financial calendar
- Savings tips
- Dataset management

---

## 🛠️ Technologies Used

### Backend

- Python
- Flask
- SQLite

### Frontend

- HTML5
- CSS3
- JavaScript
- Chart.js

### Artificial Intelligence & Machine Learning

- Ollama Cloud
- GPT-OSS 20B
- Python-based AI modules
- Machine Learning models
- EasyOCR for document processing

### Database

- SQLite

### Development & Deployment

- Visual Studio Code
- Git
- GitHub
- PythonAnywhere

---

## 🏗️ Project Structure

```text
finance-analytics-platform/
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
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore


🔄 Application Workflow
User
  │
  ▼
Web Interface
  │
  ▼
Flask Application
  │
  ├── Financial Management
  │       ├── Income
  │       ├── Expenses
  │       ├── Budget
  │       ├── Investments
  │       └── Financial Goals
  │
  ├── Analytics Engine
  │       ├── Spending Analysis
  │       ├── Budget Analysis
  │       └── Portfolio Analysis
  │
  ├── AI Engine
  │       ├── AI Assistant
  │       ├── Budget Advisor
  │       └── Financial Insights
  │
  ├── ML Module
  │       └── Fraud Prediction
  │
  └── Reporting Module
          ├── PDF Reports
          └── Excel Reports


🤖 AI Financial Assistant

The platform includes an AI-powered financial assistant that can answer general financial questions and provide personalized financial insights.

The application uses Ollama Cloud with the GPT-OSS 20B model for AI-powered conversational responses.

API credentials are stored securely using environment variables and are not included in the GitHub repository.

📊 Financial Analytics

The analytics module provides visual representations of financial data using interactive charts.

Examples include:

Income vs. Expense
Expense category analysis
Budget utilization
Investment portfolio analysis
Financial health indicators

These visualizations help users understand their financial patterns and make informed decisions.

🛡️ Security and Privacy

Sensitive information is not included in the public repository.

The project uses:

Environment variables for API credentials
.gitignore for sensitive files
SQLite database for application data
Authentication and OTP verification

The .env file and database files are excluded from the GitHub repository.

🚀 Deployment

The application has been deployed using PythonAnywhere.

The deployed application provides access to the Finance Analytics Platform through a web browser.

📋 Requirements

Install the required Python packages using:

pip install -r requirements.txt

For local development, configure the required environment variables in a .env file.

Example:

OLLAMA_HOST=https://ollama.com
OLLAMA_MODEL=gpt-oss:20b
OLLAMA_API_KEY=your_api_key_here

Never commit your actual API key to GitHub.

▶️ Running the Application Locally

Clone the repository:

git clone https://github.com/moumitadeb-23/finance-analytics-platform.git

Navigate into the project:

cd finance-analytics-platform

Install dependencies:

pip install -r requirements.txt

Configure your environment variables and then run:

python app.py

The application can then be accessed through the local Flask server.

👩‍💻 Developer

Moumita Deb

GitHub:
https://github.com/moumitadeb-23

📜 License

This project is licensed under the MIT License.

See the LICENSE file for details.

⭐ Acknowledgement

This project was developed as an academic project to demonstrate the practical application of web development, financial analytics, artificial intelligence, machine learning, database management, and reporting technologies.
