"""
==========================================================
FINANCE ANALYTICS PLATFORM
FinanceAI v2.0
Configuration File
==========================================================
"""

import os

# ==========================================================
# PROJECT PATHS
# ==========================================================

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

PROJECT_ROOT = os.path.abspath(
    os.path.join(BASE_DIR, "..")
)

DATABASE_PATH = os.path.join(
    PROJECT_ROOT,
    "finance.db"
)

UPLOAD_FOLDER = os.path.join(
    PROJECT_ROOT,
    "uploads"
)

REPORT_FOLDER = os.path.join(
    PROJECT_ROOT,
    "reports"
)

CHART_FOLDER = os.path.join(
    PROJECT_ROOT,
    "static",
    "charts"
)

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)
os.makedirs(CHART_FOLDER, exist_ok=True)

# ==========================================================
# OLLAMA SETTINGS
# ==========================================================

OLLAMA_MODEL = "llama3.1:8b"

OLLAMA_TEMPERATURE = 0.3

OLLAMA_TIMEOUT = 120

MAX_CHAT_HISTORY = 20

# ==========================================================
# FILE SETTINGS
# ==========================================================

ALLOWED_EXTENSIONS = {

    "pdf",

    "csv",

    "xlsx",

    "xls",

    "png",

    "jpg",

    "jpeg"

}

MAX_UPLOAD_SIZE = 25 * 1024 * 1024

# ==========================================================
# CHART SETTINGS
# ==========================================================

DEFAULT_CHART_COLORS = [

    "#2563eb",

    "#10b981",

    "#f59e0b",

    "#ef4444",

    "#8b5cf6",

    "#14b8a6",

    "#f97316",

    "#06b6d4"

]

DEFAULT_FIGURE_SIZE = (10, 6)

# ==========================================================
# OCR SETTINGS
# ==========================================================

OCR_LANGUAGES = [

    "en"

]

OCR_GPU = False

# ==========================================================
# AI PROMPT SETTINGS
# ==========================================================

SYSTEM_PROMPT = """
You are FinanceAI, an intelligent financial assistant.

Whenever analyzing an uploaded document:

Use this structure exactly.

# Financial Report Analysis

## Summary

Briefly summarize the uploaded document.

## Key Financial Figures

- Total Income
- Total Expense
- Savings
- Highest Expense Category

## Insights

Give 3-5 observations based ONLY on the uploaded document.

## Recommendations

Provide practical financial suggestions.

## Conclusion

Write a short conclusion.

Never invent information not present in the uploaded document.

Always format currency using ₹.
"""

# ==========================================================
# RESPONSE SETTINGS
# ==========================================================

SUCCESS = "success"

ERROR = "error"

CHAT = "chat"

CHART = "chart"

REPORT = "report"

DOCUMENT = "document"

NAVIGATION = "navigation"