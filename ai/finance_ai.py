# ==========================================================
# Finance Analytics Platform
# AI FINANCE ENGINE 4.0
# PART 1
# ==========================================================

import os
import io
import json
import sqlite3
from datetime import datetime

import ollama
import pandas as pd
import pdfplumber
import matplotlib.pyplot as plt

from PIL import Image
import easyocr


class FinanceAI:

    # ======================================================
    # INITIALIZATION
    # ======================================================

    def __init__(self):

        # Ollama model
        self.model = "llama3.1:8b"

        # Conversation memory
        self.chat_memory = {}

        # OCR Engine
        self.reader = easyocr.Reader(
            ["en"],
            gpu=False
        )

        # Upload folder
        self.upload_folder = "uploads"

        os.makedirs(
            self.upload_folder,
            exist_ok=True
        )

    # ======================================================
    # DATABASE CONNECTION
    # ======================================================

    def connect(self):

        conn = sqlite3.connect("finance.db")

        conn.row_factory = sqlite3.Row

        return conn

    # ======================================================
    # MEMORY MANAGEMENT
    # ======================================================

    def get_memory(self, user_id):

        if user_id not in self.chat_memory:

            self.chat_memory[user_id] = []

        return self.chat_memory[user_id]

    def save_memory(self, user_id, role, content):

        history = self.get_memory(user_id)

        history.append({

            "role": role,

            "content": content

        })

        # Keep only last 15 messages
        if len(history) > 15:

            history = history[-15:]

        self.chat_memory[user_id] = history

    def clear_memory(self, user_id):

        self.chat_memory[user_id] = []

    # ======================================================
    # LOAD USER DATA
    # ======================================================

    def load_user_data(self, user_id):

        conn = self.connect()

        cur = conn.cursor()

        data = {}

        tables = [

            "income",

            "expense",

            "budget",

            "investments",

            "financial_goals",

            "notifications"

        ]

        for table in tables:

            try:

                cur.execute(

                    f"""

                    SELECT *

                    FROM {table}

                    WHERE user_id=?

                    """,

                    (user_id,)

                )

                data[table] = cur.fetchall()

            except:

                data[table] = []

        conn.close()

        return data

    # ======================================================
    # BASIC CALCULATIONS
    # ======================================================

    def total_income(self, data):

        return sum(

            float(x["amount"])

            for x in data["income"]

        )

    def total_expense(self, data):

        return sum(

            float(x["amount"])

            for x in data["expense"]

        )

    def total_savings(self, data):

        return (

            self.total_income(data)

            -

            self.total_expense(data)

        )

    def budget_amount(self, data):

        if len(data["budget"]) == 0:

            return 0

        try:

            return float(

                data["budget"][0]["monthly_budget"]

            )

        except:

            return 0

    def budget_used(self, data):

        budget = self.budget_amount(data)

        if budget == 0:

            return 0

        return round(

            (

                self.total_expense(data)

                /

                budget

            )

            * 100,

            2

        )

    # ======================================================
    # FINANCIAL HEALTH SCORE
    # ======================================================

    def health_score(self, data):

        score = 100

        savings = self.total_savings(data)

        usage = self.budget_used(data)

        if savings < 0:

            score -= 40

        elif savings == 0:

            score -= 20

        if usage > 100:

            score -= 30

        elif usage > 80:

            score -= 10

        return max(score, 0)

    # ======================================================
    # BUILD CONTEXT
    # ======================================================

    def build_context(self, user_id):

        data = self.load_user_data(user_id)

        context = f"""
Finance Analytics Platform

Financial Summary

Total Income:
₹{self.total_income(data):,.2f}

Total Expense:
₹{self.total_expense(data):,.2f}

Savings:
₹{self.total_savings(data):,.2f}

Monthly Budget:
₹{self.budget_amount(data):,.2f}

Budget Used:
{self.budget_used(data)}%

Financial Health Score:
{self.health_score(data)}/100
"""

        return context, data

        # ======================================================
    # EXPENSE CATEGORY ANALYSIS
    # ======================================================

    def expense_by_category(self, data):

        categories = {}

        for row in data["expense"]:

            try:

                category = row["category"]

                amount = float(row["amount"])

            except:

                continue

            if category not in categories:

                categories[category] = 0

            categories[category] += amount

        return categories


    # ======================================================
    # HIGHEST EXPENSE CATEGORY
    # ======================================================

    def highest_expense_category(self, data):

        categories = self.expense_by_category(data)

        if not categories:

            return ("None", 0)

        highest = max(

            categories,

            key=categories.get

        )

        return (

            highest,

            categories[highest]

        )


    # ======================================================
    # TOP EXPENSES
    # ======================================================

    def top_expenses(self, data, limit=5):

        try:

            expenses = sorted(

                data["expense"],

                key=lambda x: float(x["amount"]),

                reverse=True

            )

            return expenses[:limit]

        except:

            return []


    # ======================================================
    # INVESTMENT SUMMARY
    # ======================================================

    def investment_summary(self, data):

        invested = 0

        current = 0

        profit = 0

        for item in data["investments"]:

            try:

                invested += float(item["invested_amount"])

                current += float(item["current_value"])

            except:

                continue

        profit = current - invested

        return {

            "invested": invested,

            "current": current,

            "profit": profit

        }


    # ======================================================
    # GOAL PROGRESS
    # ======================================================

    def goal_progress(self, data):

        goals = []

        for goal in data["financial_goals"]:

            try:

                target = float(goal["target_amount"])

                saved = float(goal["saved_amount"])

            except:

                continue

            percentage = 0

            if target > 0:

                percentage = round(

                    (saved / target) * 100,

                    2

                )

            goals.append({

                "goal": goal["goal_name"],

                "target": target,

                "saved": saved,

                "progress": percentage

            })

        return goals


    # ======================================================
    # NOTIFICATION SUMMARY
    # ======================================================

    def notification_summary(self, data):

        unread = 0

        for n in data["notifications"]:

            try:

                if int(n["is_read"]) == 0:

                    unread += 1

            except:

                continue

        return unread


    # ======================================================
    # SMART INSIGHTS
    # ======================================================

    def smart_insights(self, data):

        insights = []

        income = self.total_income(data)

        expense = self.total_expense(data)

        savings = self.total_savings(data)

        budget = self.budget_amount(data)

        usage = self.budget_used(data)

        category, amount = self.highest_expense_category(data)

        if income == 0:

            insights.append(

                "No income records found."

            )

        if expense > income:

            insights.append(

                "Your expenses are higher than your income."

            )

        if savings > 0:

            insights.append(

                f"You have saved ₹{savings:,.2f}."

            )

        if usage > 100:

            insights.append(

                "You have exceeded your monthly budget."

            )

        elif usage > 80:

            insights.append(

                "Your budget usage is above 80%."

            )

        if category != "None":

            insights.append(

                f"Highest spending category is {category} (₹{amount:,.2f})."

            )

        investment = self.investment_summary(data)

        if investment["profit"] > 0:

            insights.append(

                f"Investment profit: ₹{investment['profit']:,.2f}"

            )

        elif investment["profit"] < 0:

            insights.append(

                f"Investment loss: ₹{abs(investment['profit']):,.2f}"

            )

        if not insights:

            insights.append(

                "Your financial profile looks stable."

            )

        return insights


    # ======================================================
    # PERSONALIZED RECOMMENDATIONS
    # ======================================================

    def recommendations(self, data):

        advice = []

        savings = self.total_savings(data)

        usage = self.budget_used(data)

        score = self.health_score(data)

        if savings < 0:

            advice.append(

                "Reduce unnecessary spending immediately."

            )

        if usage > 90:

            advice.append(

                "Avoid additional purchases this month."

            )

        if score < 60:

            advice.append(

                "Improve your savings ratio."

            )

        if score >= 80:

            advice.append(

                "Excellent financial discipline. Keep it up!"

            )

        if len(data["investments"]) == 0:

            advice.append(

                "Consider starting a SIP or mutual fund investment."

            )

        if len(data["financial_goals"]) == 0:

            advice.append(

                "Create financial goals to track your savings."

            )

        return advice

        # ======================================================
    # CREATE SYSTEM PROMPT
    # ======================================================

    def create_prompt(self, user_id, question):

        context, data = self.build_context(user_id)

        insights = self.smart_insights(data)

        advice = self.recommendations(data)

        memory = self.get_memory(user_id)

        history = ""

        for item in memory:

            history += f"""

{item['role'].upper()}:
{item['content']}
"""

        prompt = f"""
You are Finance AI Assistant.

You are a professional financial assistant.

Always answer politely.

Always use Indian Rupees (₹).

Always answer in a structured format.

==================================

USER FINANCIAL DATA

{context}

==================================

SMART INSIGHTS

{chr(10).join(insights)}

==================================

PERSONALIZED ADVICE

{chr(10).join(advice)}

==================================

CHAT HISTORY

{history}

==================================

USER QUESTION

{question}

"""

        return prompt


    # ======================================================
    # OLLAMA RESPONSE
    # ======================================================

    def ollama_response(self, prompt):

        try:

            response = ollama.chat(

                model=self.model,

                messages=[

                    {

                        "role": "user",

                        "content": prompt

                    }

                ]

            )

            return response["message"]["content"]

        except Exception as e:

            return f"AI Error: {str(e)}"


    # ======================================================
    # NORMAL CHAT
    # ======================================================

    def chat(self, user_id, question):

        prompt = self.create_prompt(

            user_id,

            question

        )

        answer = self.ollama_response(

            prompt

        )

        self.save_memory(

            user_id,

            "user",

            question

        )

        self.save_memory(

            user_id,

            "assistant",

            answer

        )

        return answer


    # ======================================================
    # QUICK SUMMARY
    # ======================================================

    def quick_summary(self, user_id):

        context, data = self.build_context(

            user_id

        )

        summary = f"""

Financial Summary

Income:
₹{self.total_income(data):,.2f}

Expense:
₹{self.total_expense(data):,.2f}

Savings:
₹{self.total_savings(data):,.2f}

Budget Used:
{self.budget_used(data)}%

Health Score:
{self.health_score(data)}/100

"""

        return summary


    # ======================================================
    # FINANCIAL HEALTH
    # ======================================================

    def get_health_score(self, user_id):

        _, data = self.build_context(

            user_id

        )

        return {

            "score":

            self.health_score(data)

        }


    # ======================================================
    # AI RECOMMENDATIONS
    # ======================================================

    def get_ai_suggestions(self, user_id):

        _, data = self.build_context(

            user_id

        )

        return self.recommendations(

            data

        )

        # ======================================================
    # UNIVERSAL DOCUMENT ANALYZER
    # ======================================================

    def analyze_uploaded_file(self, filepath):

        if not os.path.exists(filepath):

            return {

                "success": False,

                "analysis": "Uploaded file not found."

            }

        extension = os.path.splitext(filepath)[1].lower()

        try:

            # ---------------------------------------
            # PDF
            # ---------------------------------------

            if extension == ".pdf":

                extracted_text = self.extract_pdf_text(

                    filepath

                )

            # ---------------------------------------
            # EXCEL
            # ---------------------------------------

            elif extension in [".xlsx", ".xls"]:

                extracted_text = self.extract_excel_text(

                    filepath

                )

            # ---------------------------------------
            # CSV
            # ---------------------------------------

            elif extension == ".csv":

                extracted_text = self.extract_csv_text(

                    filepath

                )

            # ---------------------------------------
            # IMAGE
            # ---------------------------------------

            elif extension in [

                ".png",

                ".jpg",

                ".jpeg"

            ]:

                extracted_text = self.extract_image_text(

                    filepath

                )

            else:

                return {

                    "success": False,

                    "analysis": "Unsupported file type."

                }

            # ---------------------------------------
            # EMPTY FILE
            # ---------------------------------------

            if extracted_text.strip() == "":

                return {

                    "success": False,

                    "analysis": "No readable content found."

                }

            # ---------------------------------------
            # AI ANALYSIS
            # ---------------------------------------

            analysis = self.document_ai_analysis(

                extracted_text

            )

            return {

                "success": True,

                "analysis": analysis,

                "text": extracted_text

            }

        except Exception as e:

            return {

                "success": False,

                "analysis": str(e)

            }

        # ======================================================
    # PDF TEXT EXTRACTION
    # ======================================================

    def extract_pdf_text(self, filepath):

        text = ""

        try:

            with pdfplumber.open(filepath) as pdf:

                for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:

                        text += page_text + "\n"

        except Exception as e:

            text = f"Unable to read PDF: {str(e)}"

        return text.strip()


    # ======================================================
    # EXCEL TEXT EXTRACTION
    # ======================================================

    def extract_excel_text(self, filepath):

        text = ""

        try:

            excel = pd.ExcelFile(filepath)

            for sheet in excel.sheet_names:

                df = pd.read_excel(

                    filepath,

                    sheet_name=sheet

                )

                text += f"\n\n===== Sheet: {sheet} =====\n"

                text += df.to_string(index=False)

        except Exception as e:

            text = f"Unable to read Excel file: {str(e)}"

        return text.strip()


    # ======================================================
    # CSV TEXT EXTRACTION
    # ======================================================

    def extract_csv_text(self, filepath):

        text = ""

        try:

            df = pd.read_csv(filepath)

            text = df.to_string(index=False)

        except Exception as e:

            text = f"Unable to read CSV file: {str(e)}"

        return text.strip()

        # ======================================================
    # IMAGE OCR
    # ======================================================

    def extract_image_text(self, filepath):

        text = ""

        try:

            result = self.reader.readtext(

                filepath,

                detail=0,

                paragraph=True

            )

            text = "\n".join(result)

        except Exception as e:

            text = f"Unable to read image: {str(e)}"

        return text.strip()


    # ======================================================
    # AI DOCUMENT ANALYSIS
    # ======================================================

    def document_ai_analysis(self, document_text):

        if not document_text:

            return "No readable content found."

        prompt = f"""
You are Finance AI Assistant.

Analyze the following document professionally.

Provide your response in this format:

============================

DOCUMENT SUMMARY

• Short summary

============================

IMPORTANT DETAILS

• Important values
• Important dates
• Transactions
• Categories

============================

FINANCIAL INSIGHTS

• Spending pattern
• Savings opportunity
• Suspicious transactions
• Budget suggestions

============================

AI RECOMMENDATIONS

• Personalized recommendations

============================

DOCUMENT

{document_text}

"""

        try:

            response = ollama.chat(

                model=self.model,

                messages=[

                    {

                        "role":"user",

                        "content":prompt

                    }

                ]

            )

            return response["message"]["content"]

        except Exception as e:

            return f"AI Error : {str(e)}"


    # ======================================================
    # QUICK DOCUMENT SUMMARY
    # ======================================================

    def summarize_document(self, filepath):

        result = self.analyze_uploaded_file(filepath)

        if result["success"]:

            return result["analysis"]

        return result["analysis"]


    # ======================================================
    # DOCUMENT TYPE DETECTION
    # ======================================================

    def detect_document_type(self, filepath):

        extension = os.path.splitext(filepath)[1].lower()

        mapping = {

            ".pdf": "PDF",

            ".csv": "CSV",

            ".xlsx": "Excel",

            ".xls": "Excel",

            ".png": "Image",

            ".jpg": "Image",

            ".jpeg": "Image"

        }

        return mapping.get(

            extension,

            "Unknown"

        )


    # ======================================================
    # DOCUMENT INFORMATION
    # ======================================================

    def file_information(self, filepath):

        return {

            "filename": os.path.basename(filepath),

            "type": self.detect_document_type(filepath),

            "size_kb": round(

                os.path.getsize(filepath)/1024,

                2

            )

        }

        # ======================================================
    # DOCUMENT STATISTICS
    # ======================================================

    def document_statistics(self, text):

        if not text:

            return {

                "characters": 0,

                "words": 0,

                "lines": 0

            }

        return {

            "characters": len(text),

            "words": len(text.split()),

            "lines": len(text.splitlines())

        }


    # ======================================================
    # DOCUMENT KEYWORDS
    # ======================================================

    def extract_keywords(self, text, limit=15):

        if not text:

            return []

        stop_words = {

            "the","is","are","was","were","a","an","and","or",

            "to","of","for","in","on","at","by","with","from",

            "this","that","it","be","as","if","into","your"

        }

        words = []

        for word in text.lower().split():

            word = "".join(

                c for c in word

                if c.isalnum()

            )

            if len(word) < 3:

                continue

            if word in stop_words:

                continue

            words.append(word)

        frequency = {}

        for word in words:

            frequency[word] = frequency.get(word, 0) + 1

        sorted_words = sorted(

            frequency.items(),

            key=lambda x: x[1],

            reverse=True

        )

        return [w[0] for w in sorted_words[:limit]]


    # ======================================================
    # FINANCIAL VALUE EXTRACTION
    # ======================================================

    def detect_currency_values(self, text):

        import re

        values = re.findall(

            r'₹\s?[\d,]+(?:\.\d+)?',

            text

        )

        values += re.findall(

            r'\b\d[\d,]*(?:\.\d+)?\b',

            text

        )

        return values[:100]


    # ======================================================
    # COMPLETE DOCUMENT ANALYSIS
    # ======================================================

    def complete_document_analysis(self, filepath):

        result = self.analyze_uploaded_file(filepath)

        if not result["success"]:

            return result

        text = result["text"]

        return {

            "success": True,

            "analysis": result["analysis"],

            "statistics": self.document_statistics(text),

            "keywords": self.extract_keywords(text),

            "financial_values": self.detect_currency_values(text),

            "file": self.file_information(filepath)

        }


    # ======================================================
    # CHAT ATTACHMENT CONTEXT
    # ======================================================

    def document_context(self, filepath):

        result = self.complete_document_analysis(filepath)

        if not result["success"]:

            return ""

        context = f"""

Uploaded Document

Filename:
{result['file']['filename']}

Type:
{result['file']['type']}

Statistics:
{result['statistics']}

Keywords:
{', '.join(result['keywords'])}

Analysis:
{result['analysis']}

"""

        return context

    # ======================================================
    # DOCUMENT QUESTION ANSWERING
    # ======================================================

    def ask_document(self, filepath, question):

        result = self.complete_document_analysis(filepath)

        if not result["success"]:

            return result["analysis"]

        context = result["analysis"]

        prompt = f"""
You are Finance AI Assistant.

The user uploaded a financial document.

Use ONLY the information below to answer the question.

===========================
DOCUMENT ANALYSIS
===========================

{context}

===========================
QUESTION
===========================

{question}

Answer clearly using bullet points whenever possible.
"""

        try:

            response = ollama.chat(

                model=self.model,

                messages=[

                    {

                        "role":"user",

                        "content":prompt

                    }

                ]

            )

            return response["message"]["content"]

        except Exception as e:

            return str(e)


    # ======================================================
    # DOCUMENT + USER FINANCE CONTEXT
    # ======================================================

    def merge_document_with_finances(

            self,

            user_id,

            filepath

    ):

        financial_context, data = self.build_context(

            user_id

        )

        document = self.complete_document_analysis(

            filepath

        )

        if not document["success"]:

            return financial_context

        return f"""

=========================
USER FINANCIAL PROFILE
=========================

{financial_context}

=========================
DOCUMENT ANALYSIS
=========================

{document["analysis"]}

"""


    # ======================================================
    # AI DOCUMENT ADVISOR
    # ======================================================

    def document_financial_advice(

            self,

            user_id,

            filepath

    ):

        context = self.merge_document_with_finances(

            user_id,

            filepath

        )

        prompt = f"""
You are an expert Financial Advisor.

Study both

1. User Financial Data
2. Uploaded Document

Provide

• Summary

• Risks

• Spending Pattern

• Savings Suggestions

• Investment Advice

• Fraud Warning (if any)

• Budget Recommendation

• Final Conclusion

=========================

{context}

"""

        try:

            response = ollama.chat(

                model=self.model,

                messages=[

                    {

                        "role":"user",

                        "content":prompt

                    }

                ]

            )

            return response["message"]["content"]

        except Exception as e:

            return str(e)


    # ======================================================
    # DOCUMENT CACHE
    # ======================================================

    def cache_document(

            self,

            filepath

    ):

        if not hasattr(

                self,

                "document_cache"

        ):

            self.document_cache = {}

        result = self.complete_document_analysis(

            filepath

        )

        self.document_cache[filepath] = result

        return result


    # ======================================================
    # GET CACHED DOCUMENT
    # ======================================================

    def get_cached_document(

            self,

            filepath

    ):

        if not hasattr(

                self,

                "document_cache"

        ):

            self.document_cache = {}

        return self.document_cache.get(

            filepath,

            None

        )

        # ======================================================
    # INTENT DETECTION
    # ======================================================

    def detect_intent(self, message):

        message = message.lower().strip()

        chart_keywords = [

            "chart",

            "graph",

            "plot",

            "pie",

            "bar chart",

            "line chart",

            "visualize",

            "analytics"

        ]

        report_keywords = [

            "report",

            "summary pdf",

            "financial report",

            "download report",

            "generate report"

        ]

        document_keywords = [

            "pdf",

            "document",

            "receipt",

            "bill",

            "invoice",

            "excel",

            "csv",

            "analyze file",

            "upload"

        ]

        navigation_keywords = {

            "dashboard":"/dashboard",

            "reports":"/reports",

            "analytics":"/analytics",

            "budget":"/budget",

            "expenses":"/expenses",

            "income":"/income",

            "goals":"/financial-goals",

            "investments":"/investments",

            "notifications":"/notifications",

            "settings":"/settings"

        }

        greeting_keywords = [

            "hi",

            "hello",

            "hey",

            "good morning",

            "good evening"

        ]

        # -----------------------
        # Greetings
        # -----------------------

        if any(

            word in message

            for word in greeting_keywords

        ):

            return {

                "type":"greeting"

            }

        # -----------------------
        # Charts
        # -----------------------

        if any(

            word in message

            for word in chart_keywords

        ):

            return {

                "type":"chart"

            }

        # -----------------------
        # Reports
        # -----------------------

        if any(

            word in message

            for word in report_keywords

        ):

            return {

                "type":"report"

            }

        # -----------------------
        # Documents
        # -----------------------

        if any(

            word in message

            for word in document_keywords

        ):

            return {

                "type":"document"

            }

        # -----------------------
        # Navigation
        # -----------------------

        for page,url in navigation_keywords.items():

            if page in message:

                return {

                    "type":"navigation",

                    "url":url,

                    "page":page.title()

                }

        # -----------------------
        # Finance Questions
        # -----------------------

        finance_words = [

            "income",

            "expense",

            "saving",

            "budget",

            "investment",

            "health score",

            "goal",

            "money"

        ]

        if any(

            word in message

            for word in finance_words

        ):

            return {

                "type":"finance"

            }

        # -----------------------
        # Default Chat
        # -----------------------

        return {

            "type":"chat"

        }

        # ======================================================
    # BUILD CONVERSATION CONTEXT
    # ======================================================

    def build_chat_prompt(self, user_id, question):

        # Financial Context
        financial_context, data = self.build_context(user_id)

        # AI Insights
        insights = self.smart_insights(data)

        # Recommendations
        recommendations = self.recommendations(data)

        # Conversation Memory
        memory = self.get_memory(user_id)

        history = ""

        if len(memory) > 0:

            history += "\nPrevious Conversation\n"

            history += "-------------------------\n"

            for item in memory:

                role = item["role"].upper()

                history += f"{role}: {item['content']}\n"

        prompt = f"""
You are Finance AI Assistant.

You are an intelligent AI financial assistant like ChatGPT.

Your job is to help users understand their finances,
answer questions,
give investment suggestions,
budget advice,
expense analysis,
goal tracking,
and financial education.

Rules:

1. Always answer politely.

2. Always use ₹ for currency.

3. Keep answers short unless user requests details.

4. Use bullet points whenever possible.

5. Never invent financial data.

6. Base answers on the user's actual financial information.

===================================================

USER FINANCIAL PROFILE

{financial_context}

===================================================

SMART INSIGHTS

{chr(10).join(insights)}

===================================================

PERSONALIZED RECOMMENDATIONS

{chr(10).join(recommendations)}

===================================================

CHAT HISTORY

{history}

===================================================

CURRENT QUESTION

{question}

===================================================

Now answer the user's question professionally.
"""

        return prompt

        # ======================================================
    # OLLAMA RESPONSE ENGINE
    # ======================================================

    def generate_ai_response(self, user_id, question):

        prompt = self.build_chat_prompt(

            user_id,

            question

        )

        try:

            response = ollama.chat(

                model=self.model,

                messages=[

                    {

                        "role": "system",

                        "content":
                        """
You are Finance AI Assistant.

Behave exactly like ChatGPT.

You are friendly.

Professional.

Helpful.

Provide financial guidance.

Use markdown formatting.

Use bullet points.

Never make up financial information.

If you don't know something, say so politely.
                        """

                    },

                    {

                        "role": "user",

                        "content": prompt

                    }

                ]

            )

            if (

                "message" in response

                and

                "content" in response["message"]

            ):

                answer = response["message"]["content"]

            else:

                answer = (

                    "Sorry, I couldn't generate a response."

                )

            answer = answer.strip()

            if answer == "":

                answer = (

                    "I couldn't understand that request."

                )

            return {

                "success": True,

                "response": answer

            }

        except Exception as e:

            return {

                "success": False,

                "response":

                f"AI Error: {str(e)}"

            }

        # ======================================================
    # UPDATE CHAT MEMORY
    # ======================================================

    def update_chat_memory(

            self,

            user_id,

            user_message,

            ai_response

    ):

        history = self.get_memory(user_id)

        history.append({

            "role": "user",

            "content": user_message,

            "timestamp": datetime.now().strftime(

                "%Y-%m-%d %H:%M:%S"

            )

        })

        history.append({

            "role": "assistant",

            "content": ai_response,

            "timestamp": datetime.now().strftime(

                "%Y-%m-%d %H:%M:%S"

            )

        })

        MAX_HISTORY = 20

        if len(history) > MAX_HISTORY * 2:

            history = history[-MAX_HISTORY * 2:]

        self.chat_memory[user_id] = history


    # ======================================================
    # GET CHAT HISTORY
    # ======================================================

    def get_chat_history(

            self,

            user_id

    ):

        return self.get_memory(user_id)


    # ======================================================
    # CLEAR CHAT HISTORY
    # ======================================================

    def clear_chat_history(

            self,

            user_id

    ):

        self.chat_memory[user_id] = []

        return True


    # ======================================================
    # LAST AI RESPONSE
    # ======================================================

    def last_ai_response(

            self,

            user_id

    ):

        history = self.get_memory(user_id)

        for item in reversed(history):

            if item["role"] == "assistant":

                return item["content"]

        return ""


    # ======================================================
    # LAST USER MESSAGE
    # ======================================================

    def last_user_message(

            self,

            user_id

    ):

        history = self.get_memory(user_id)

        for item in reversed(history):

            if item["role"] == "user":

                return item["content"]

        return ""

        # ======================================================
    # COMPLETE CHAT RESPONSE
    # ======================================================

    def chat_response(self, user_id, question):

        result = self.generate_ai_response(

            user_id,

            question

        )

        if not result["success"]:

            return {

                "success": False,

                "response": result["response"]

            }

        ai_answer = result["response"]

        self.update_chat_memory(

            user_id,

            question,

            ai_answer

        )

        return {

            "success": True,

            "response": ai_answer,

            "history": self.get_chat_history(

                user_id

            )

        }


    # ======================================================
    # STREAM RESPONSE (Future Ready)
    # ======================================================

    def stream_chat_response(

            self,

            user_id,

            question

    ):

        response = self.chat_response(

            user_id,

            question

        )

        return response


    # ======================================================
    # QUICK GREETING
    # ======================================================

    def greeting(self):

        return """
👋 Hello!

I'm your Finance AI Assistant.

I can help you with:

• Income Analysis

• Expense Tracking

• Budget Planning

• Investment Advice

• Financial Goals

• Reports

• Charts

• Receipt OCR

• PDF Analysis

• Excel Analysis

• Financial Health

How can I help you today?
"""


    # ======================================================
    # UNKNOWN QUESTION
    # ======================================================

    def unknown_response(self):

        return """
Sorry, I couldn't understand your request.

Try asking things like:

• Show my expenses

• Show my budget

• Generate expense chart

• Generate financial report

• Analyze this PDF

• Analyze my receipt

• Give investment advice

• Financial health score

• Show savings
"""


    # ======================================================
    # RESET AI
    # ======================================================

    def reset_ai(self, user_id):

        self.clear_chat_history(

            user_id

        )

        return {

            "success": True,

            "message":

            "Conversation has been reset."

        }

    