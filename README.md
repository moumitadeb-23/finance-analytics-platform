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

**Smart Finance Insights** is a modern AI-powered personal finance management platform developed using **Python, Flask, SQLite, HTML, CSS, JavaScript, Machine Learning, and AI technologies**.

The platform enables users to manage their personal finances from a centralized dashboard. Users can track income and expenses, create budgets, manage investments, monitor financial goals, analyze spending patterns, generate financial reports, detect potentially fraudulent transactions, and receive AI-powered financial assistance.

The application combines **financial management, data analytics, artificial intelligence, machine learning, reporting, and visualization** into one web-based platform.

---

# ✨ Key Features

## 💵 Income Management

- Add monthly income
- Update income records
- Delete income records
- Income overview
- Monthly statistics
- Income history

---

## 💸 Expense Tracking

- Add expenses
- Edit expenses
- Delete expenses
- Category-wise expense tracking
- Monthly expense analysis
- Spending insights
- Expense history

---

## 📊 Interactive Dashboard

- Complete financial summary
- Income vs Expense analysis
- Monthly financial charts
- Savings overview
- Budget status
- Financial Health Score
- Quick financial insights

---

## 🎯 Budget Planning

- Create monthly budgets
- Category-wise budgeting
- Track budget utilization
- Remaining budget calculation
- Budget alerts
- Budget analysis
- AI Budget Advisor

---

## 🤖 AI Financial Assistant

The platform includes an AI-powered conversational financial assistant that allows users to ask natural-language questions about finance.

### AI capabilities include:

- General financial questions
- Saving recommendations
- Spending-related questions
- Budget guidance
- Financial suggestions
- Personalized financial insights
- Natural-language conversations

The deployed application uses **Ollama Cloud with the GPT-OSS 20B model**.

---

## 🧠 AI Financial Insights

The AI module analyzes financial information and provides useful recommendations based on the user's financial activity.

### Features include:

- Spending insights
- Savings recommendations
- Financial health suggestions
- Budget recommendations
- Personalized financial guidance
- Financial behavior analysis

---

## 📈 Financial Analytics

Interactive visualizations help users understand their financial behavior.

### Analytics include:

- Income vs Expense
- Expense category analysis
- Budget analysis
- Spending trends
- Investment portfolio analysis
- Portfolio allocation
- Financial health analysis
- Monthly financial statistics

---

## 💼 Investment Portfolio

Users can manage and analyze their investment portfolio.

### Features include:

- Add investments
- Edit investments
- Track invested amount
- Track current value
- Purchase date
- Investment notes
- Portfolio analytics
- Asset allocation
- Investment history

---

## 🎯 Financial Goals

Users can create and monitor financial goals.

### Features include:

- Create financial goals
- Set target amounts
- Track saved amounts
- Track progress
- Goal completion percentage
- Active/Achieved status
- Goal tracking

---

## 🛡️ Fraud Detection

The platform includes a machine-learning-based fraud prediction module.

### Features include:

- Transaction analysis
- Fraud prediction
- Machine learning model
- Prediction history
- Fraud analysis
- Fraud prediction dashboard

---

## 📄 Financial Reports

Users can generate financial reports based on their financial data.

### Supported reports include:

- Financial summaries
- PDF reports
- Excel reports
- Income information
- Expense information
- Investment information
- Financial analysis

---

## 📅 Financial Calendar

The financial calendar helps users organize and view important financial activities and dates.

### Features include:

- Financial event tracking
- Important financial dates
- Calendar-based organization
- Easy financial planning

---

## 🔔 Notifications

The platform provides financial notifications and alerts for important activities.

Examples include:

- Budget notifications
- Spending notifications
- Savings notifications
- Financial achievement notifications
- Financial status updates

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

The platform includes a modern dark-mode interface for a comfortable and visually appealing user experience.

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
                         │        USER         │
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
│   ├── images/
│   └── charts/
│
├── templates/
│
├── app.py
├── expenses.csv
├── package.json
├── package-lock.json
├── .gitignore
├── LICENSE
├── README.md
└── TODO.md

🔄 Application Workflow
                              ┌──────────────┐
                              │     USER     │
                              └──────┬───────┘
                                     │
                                     ▼
                         ┌─────────────────────┐
                         │ Login / Registration│
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      Dashboard      │
                         └──────────┬──────────┘
                                    │
             ┌──────────────────────┼──────────────────────┐
             │          │            │          │           │
             ▼          ▼            ▼          ▼           ▼
          Income     Expenses      Budget   Investments   Goals
             │          │            │          │           │
             └──────────┴────────────┴──────────┴───────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     Analytics       │
                         └──────────┬──────────┘
                                    │
                  ┌─────────────────┼─────────────────┐
                  │                 │                 │
                  ▼                 ▼                 ▼
             Charts & Reports   Financial Health   Portfolio
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     AI / ML Layer   │
                         └──────────┬──────────┘
                                    │
             ┌──────────────────────┼──────────────────────┐
             │                      │                      │
             ▼                      ▼                      ▼
       AI Assistant          Budget Advisor         Fraud Detection
             │                      │                      │
             └──────────────────────┼──────────────────────┘
                                    │
                                    ▼
                             Ollama Cloud
                                    │
                                    ▼
                              GPT-OSS 20B
                                    │
                                    ▼
                           AI Generated Response


🤖 AI Assistant Architecture

┌──────────────────────┐
│     User Question    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Chat Assistant UI    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    Flask Backend     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│     Chat Engine      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Ollama Cloud API   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│     GPT-OSS 20B      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  AI Generated Reply  │
└──────────────────────┘
The AI API credentials are stored securely using environment variables and are not included in the public repository.

🧠 AI & Machine Learning Modules

The project contains multiple AI and machine-learning components.

🤖 AI Financial Assistant

Provides conversational answers to user financial questions using the Ollama Cloud API and GPT-OSS 20B.

💡 AI Insights

Analyzes financial information and provides recommendations related to spending, savings, and financial health.

🎯 AI Budget Advisor

Provides budget-related suggestions based on financial information.

🛡️ Fraud Prediction

Uses trained machine-learning models to analyze transactions and predict potentially fraudulent activity.

📊 Financial Analysis

Combines financial records, calculations, analytics, and AI-generated insights to help users understand their financial situation.

📊 Data Visualization

The application uses interactive charts to present financial information clearly.

Visualizations include:
📊 Income vs Expense charts
🥧 Expense category charts
📈 Budget analysis charts
💼 Portfolio charts
📊 Investment allocation
📈 Financial trends

Charts are generated dynamically based on the user's financial data.

📄 Document Processing

The platform contains a document-processing module for handling financial documents.

Supported functionality includes:
PDF processing
Financial document extraction
Document analysis
Image-based document processing
Financial information extraction

The deployed PythonAnywhere version disables the EasyOCR runtime initialization because of deployment resource limitations.

🔐 Security & Privacy

The project follows basic security practices to protect sensitive information.

🔑 API keys are stored using environment variables.
🚫 .env files are excluded using .gitignore.
🗄️ Database files are excluded from GitHub.
🐍 Python cache files are excluded.
📦 Backup files are excluded.
🔐 User authentication is implemented.
📱 OTP verification is supported.
🔒 Sensitive credentials are not hard-coded in the public repository.

Important: Never add your real API key to GitHub.

🚀 Deployment

The application has been successfully deployed using PythonAnywhere.

The deployed application includes:

Flask web application
SQLite database
AI financial assistant
Financial analytics
Machine learning modules
Financial reporting
Investment portfolio management
Financial goals
Fraud prediction

🌐 Live Application
<div align="center">
👉 https://moumitadev.pythonanywhere.com/
</div>

💻 Installation
1️⃣ Clone the Repository

git clone https://github.com/moumitadeb-23/finance-analytics-platform.git

2️⃣ Navigate to the Project
cd finance-analytics-platform
3️⃣ Create a Virtual Environment
python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Activate it on Linux/macOS:

source venv/bin/activate
4️⃣ Install Dependencies
pip install -r requirements.txt
5️⃣ Configure Environment Variables

Create a .env file in the project root.

OLLAMA_HOST=https://ollama.com
OLLAMA_MODEL=gpt-oss:20b
OLLAMA_API_KEY=your_api_key_here

⚠️ Never upload your real API key to GitHub.

The .env file is already excluded through .gitignore.

6️⃣ Run the Application
python app.py

The application can then be accessed through the local Flask server.

🗃️ Database

The application uses SQLite as its database.

The database manages information related to:

Users
Income
Expenses
Budgets
Investments
Financial goals
Notifications
Prediction history
User settings
Financial records

The database is automatically used by the Flask backend for storing and retrieving application data.

🧪 Testing

The application was tested locally before deployment.

Testing included:

User registration
User login
OTP verification
Income management
Expense management
Budget management
Investment management
Financial goals
Analytics
Portfolio analytics
AI financial assistant
AI budget advisor
Fraud prediction
Financial reports
Notifications
Dark mode
Settings
Profile management

The deployed application was also tested on PythonAnywhere.

⚠️ Limitations

Although the application provides several financial management and AI features, there are some limitations.

The platform does not directly connect to bank accounts.
Financial recommendations should not be considered professional financial advice.
AI-generated responses may occasionally contain inaccurate information.
AI functionality depends on availability of the Ollama Cloud service.
The deployed version has limited document OCR functionality due to PythonAnywhere resource limitations.
SQLite is suitable for this project but may not be ideal for very large-scale production systems.
Fraud detection performance depends on the quality of the training dataset.
🔮 Future Enhancements

The following features can be added in future versions:

📱 Dedicated Android/iOS mobile application
☁️ Cloud database integration
🏦 Bank API integration
💳 Automatic transaction synchronization
📧 Email-based financial alerts
📲 SMS financial notifications
📈 Advanced investment prediction
🔮 AI-powered financial forecasting
🔐 Two-factor authentication
🌍 Multi-currency support
💱 Currency conversion
📊 Advanced financial dashboards
🧠 More personalized AI recommendations
📚 Learning Outcomes

This project helped demonstrate practical knowledge of:

Python programming
Flask web development
Frontend development
SQLite database management
REST-style backend development
Data visualization
Machine learning
Artificial intelligence
API integration
Financial analytics
Report generation
Git and GitHub
Cloud deployment
Environment variable management
Software project organization
👩‍💻 Developer
<div align="center">
Moumita Deb

🎓 Student & Developer

💻 Python • Flask • AI • Machine Learning • Web Development

🔗 GitHub

https://github.com/moumitadeb-23

🌐 Live Project

https://moumitadev.pythonanywhere.com/

</div>
⭐ Support

If you found this project useful, please consider giving it a ⭐ Star on GitHub.

Your support motivates further improvements and future releases. 💙

📜 License

This project is licensed under the MIT License.

See the LICENSE file for more details.

The MIT License permits:

✅ Commercial use
✅ Modification
✅ Distribution
✅ Private use

Subject to:

📜 Preservation of the copyright notice
📜 Preservation of the license notice
💙 Thank You for Visiting
<div align="center">
📊 Smart Finance Insights

Smart Finance Insights was developed as an AI-powered personal finance management platform to demonstrate modern web development practices, financial analytics, database management, machine learning, and AI-assisted decision making.

💰 Manage Your Money
📊 Understand Your Finances
🤖 Get AI-Powered Insights
🎯 Achieve Your Financial Goals
<br>
⭐ If you like this project, don't forget to star the repository!
<br>

Made with ❤️ by Moumita Deb

</div> ```
