"""
==========================================================
FINANCE ANALYTICS PLATFORM
FinanceAI v2.0
Chart Engine
==========================================================
"""

import os

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

from datetime import datetime

from .database_manager import DatabaseManager

from .config import (

    CHART_FOLDER,

    DEFAULT_CHART_COLORS,

    DEFAULT_FIGURE_SIZE

)

from .utils import Utils


class ChartEngine:

    # ======================================================
    # INITIALIZATION
    # ======================================================

    def __init__(self):

        self.db = DatabaseManager()

        self.chart_folder = CHART_FOLDER

        self.colors = DEFAULT_CHART_COLORS

        self.figure_size = DEFAULT_FIGURE_SIZE

        os.makedirs(

            self.chart_folder,

            exist_ok=True

        )

    # ======================================================
    # CREATE FIGURE
    # ======================================================

    def create_figure(self):

        plt.figure(

            figsize=self.figure_size

        )

    # ======================================================
    # SAVE CHART
    # ======================================================

    def save_chart(

            self,

            filename

    ):

        filepath = os.path.join(

            self.chart_folder,

            filename

        )

        plt.tight_layout()

        plt.savefig(

            filepath,

            dpi=300,

            bbox_inches="tight"

        )

        plt.close()

        print("=" * 60)
        print("Chart saved to:")
        print(filepath)
        print("File exists:", os.path.exists(filepath))
        print("=" * 60)


        return filepath

    # ======================================================
    # CHART NAME
    # ======================================================

    def chart_filename(

            self,

            prefix

    ):

        timestamp = datetime.now().strftime(

            "%Y%m%d_%H%M%S"

        )

        return f"{prefix}_{timestamp}.png"

    # ======================================================
    # CHART RESPONSE
    # ======================================================

    def chart_response(self, filepath, title):

        filename = Utils.filename(filepath)

        return Utils.success(

            {

                "title": title,

                "path": f"/static/charts/{filename}",

                "filename": filename

            },

            "chart"

        )

    # ======================================================
    # CHART STATUS
    # ======================================================

    def status(self):

        return Utils.success(

            {

                "folder": self.chart_folder,

                "figure_size": self.figure_size,

                "colors": len(

                    self.colors

                )

            },

            "status"

        )

        # ======================================================
    # EXPENSE CATEGORY DATA
    # ======================================================

    def expense_category_data(self, user_id):

        expenses = self.db.get_expenses(user_id)

        categories = {}

        for expense in expenses:

            category = expense["category"] or "Other"

            amount = Utils.safe_float(

                expense["amount"] if expense["amount"] is not None else 0

            )

            categories[category] = (

                categories.get(

                    category,

                    0

                )

                + amount

            )

        return categories


    # ======================================================
    # EXPENSE PIE CHART
    # ======================================================

    def expense_pie_chart(self, user_id):

        data = self.expense_category_data(user_id)

        if not data:

            return Utils.error(

                "No expense data available."

            )

        self.create_figure()

        plt.pie(

            list(data.values()),

            labels=list(data.keys()),

            autopct="%1.1f%%",

            startangle=90

        )

        plt.title(

            "Expense Distribution"

        )

        filename = self.chart_filename(

            "expense_pie"

        )

        filepath = self.save_chart(

            filename

        )

        return self.chart_response(

            filepath,

            "Expense Pie Chart"

        )


    # ======================================================
    # EXPENSE BAR CHART
    # ======================================================

    def expense_bar_chart(self, user_id):

        data = self.expense_category_data(user_id)

        if not data:

            return Utils.error(

                "No expense data available."

            )

        self.create_figure()

        plt.bar(

            list(data.keys()),

            list(data.values())

        )

        plt.xticks(

            rotation=45,

            ha="right"

        )

        plt.ylabel(

            "Amount (₹)"

        )

        plt.title(

            "Expenses by Category"

        )

        filename = self.chart_filename(

            "expense_bar"

        )

        filepath = self.save_chart(

            filename

        )

        return self.chart_response(

            filepath,

            "Expense Bar Chart"

        )


    # ======================================================
    # INCOME VS EXPENSE
    # ======================================================

    def income_vs_expense(self, user_id):

        income = self.db.get_income(user_id)

        expenses = self.db.get_expenses(user_id)

        total_income = sum(

            Utils.safe_float(

                row["amount"] if row["amount"] is not None else 0

            )

            for row in income

        )

        total_expense = sum(

            Utils.safe_float(

                row["amount"] if row["amount"] is not None else 0

            )

            for row in expenses

        )

        self.create_figure()

        plt.bar(

            [

                "Income",

                "Expense"

            ],

            [

                total_income,

                total_expense

            ]

        )

        plt.ylabel(

            "Amount (₹)"

        )

        plt.title(

            "Income vs Expense"

        )

        filename = self.chart_filename(

            "income_expense"

        )

        filepath = self.save_chart(

            filename

        )

        return self.chart_response(

            filepath,

            "Income vs Expense"

        )

        # ======================================================
    # MONTHLY EXPENSE TREND
    # ======================================================

    def monthly_expense_trend(self, user_id):

        expenses = self.db.get_expenses(user_id)

        monthly = {}

        for row in expenses:

            try:

                date = row["date"][:7]

            except:

                date = "Unknown"

            amount = Utils.safe_float(row["amount"])

            monthly[date] = monthly.get(date, 0) + amount

        if not monthly:

            return Utils.error(

                "No expense data available."

            )

        months = sorted(monthly.keys())

        values = [monthly[m] for m in months]

        self.create_figure()

        plt.plot(

            months,

            values,

            marker="o",

            linewidth=2

        )

        plt.xticks(rotation=45)

        plt.ylabel("Amount (₹)")

        plt.title("Monthly Expense Trend")

        filename = self.chart_filename(

            "monthly_expense"

        )

        filepath = self.save_chart(filename)

        return self.chart_response(

            filepath,

            "Monthly Expense Trend"

        )


    # ======================================================
    # BUDGET UTILIZATION
    # ======================================================

    def budget_chart(self, user_id):

        budget = self.db.get_budget(user_id)

        expenses = self.db.get_expenses(user_id)

        if not budget:

            return Utils.error(

                "Budget not available."

            )

        budget_amount = Utils.safe_float(

            budget["monthly_budget"]

        )

        spent = sum(

            Utils.safe_float(

                row["amount"]

            )

            for row in expenses

        )

        remaining = max(

            budget_amount - spent,

            0

        )

        self.create_figure()

        plt.pie(

            [

                spent,

                remaining

            ],

            labels=[

                "Spent",

                "Remaining"

            ],

            autopct="%1.1f%%",

            startangle=90

        )

        plt.title(

            "Budget Utilization"

        )

        filename = self.chart_filename(

            "budget"

        )

        filepath = self.save_chart(

            filename

        )

        return self.chart_response(

            filepath,

            "Budget Utilization"

        )


    # ======================================================
    # INVESTMENT PORTFOLIO
    # ======================================================

    def investment_chart(self, user_id):

        investments = self.db.get_investments(user_id)

        if not investments:

            return Utils.error(

                "No investment data."

            )

        labels = []

        values = []

        for row in investments:

            labels.append(

                row["investment_name"]

            )

            values.append(

                Utils.safe_float(

                    row["current_value"]

                )

            )

        self.create_figure()

        plt.bar(

            labels,

            values

        )

        plt.xticks(

            rotation=45,

            ha="right"

        )

        plt.ylabel("Current Value (₹)")

        plt.title(

            "Investment Portfolio"

        )

        filename = self.chart_filename(

            "portfolio"

        )

        filepath = self.save_chart(

            filename

        )

        return self.chart_response(

            filepath,

            "Investment Portfolio"

        )


    # ======================================================
    # GOAL PROGRESS
    # ======================================================

    def goal_progress_chart(self, user_id):

        goals = self.db.get_financial_goals(user_id)

        if not goals:

            return Utils.error(

                "No goals found."

            )

        labels = []

        progress = []

        for goal in goals:

            labels.append(

                goal["goal_name"]

            )

            target = Utils.safe_float(

                goal["target_amount"]

            )

            current = Utils.safe_float(

                goal["current_amount"]

            )

            if target == 0:

                percent = 0

            else:

                percent = round(

                    (current / target) * 100,

                    2

                )

            progress.append(percent)

        self.create_figure()

        plt.bar(

            labels,

            progress

        )

        plt.ylabel("Completion (%)")

        plt.title("Financial Goal Progress")

        plt.ylim(0, 100)

        plt.xticks(

            rotation=45,

            ha="right"

        )

        filename = self.chart_filename(

            "goal_progress"

        )

        filepath = self.save_chart(

            filename

        )

        return self.chart_response(

            filepath,

            "Goal Progress"

        )

        # ======================================================
    # GENERATE CHART (MAIN DISPATCHER)
    # ======================================================

    def generate_chart(

            self,

            user_id,

            entity=None,

            chart_type="pie",

            period="all"

    ):

        entity = (entity or "").lower()

        chart_type = (chart_type or "pie").lower()

        # ==========================================
        # EXPENSE CHARTS
        # ==========================================

        if entity == "expense":

            if chart_type == "bar":

                return self.expense_bar_chart(

                    user_id

                )

            return self.expense_pie_chart(

                user_id

            )

        # ==========================================
        # INCOME
        # ==========================================

        elif entity == "income":

            return self.income_vs_expense(

                user_id

            )

        # ==========================================
        # BUDGET
        # ==========================================

        elif entity == "budget":

            return self.budget_chart(

                user_id

            )

        # ==========================================
        # INVESTMENTS
        # ==========================================

        elif entity == "investment":

            return self.investment_chart(

                user_id

            )

        # ==========================================
        # GOALS
        # ==========================================

        elif entity == "goal":

            return self.goal_progress_chart(

                user_id

            )

        # ==========================================
        # MONTHLY TREND
        # ==========================================

        elif entity in [

            "trend",

            "analytics",

            "monthly"

        ]:

            return self.monthly_expense_trend(

                user_id

            )

        # ==========================================
        # DEFAULT
        # ==========================================

        return self.expense_pie_chart(

            user_id

        )


    # ======================================================
    # AVAILABLE CHARTS
    # ======================================================

    def available_charts(self):

        return Utils.success(

            {

                "expense": [

                    "pie",

                    "bar"

                ],

                "income": [

                    "comparison"

                ],

                "budget": [

                    "utilization"

                ],

                "investment": [

                    "portfolio"

                ],

                "goal": [

                    "progress"

                ],

                "analytics": [

                    "monthly trend"

                ]

            },

            "chart"

        )


    # ======================================================
    # DELETE CHART
    # ======================================================

    def delete_chart(

            self,

            filepath

    ):

        try:

            if os.path.exists(

                    filepath

            ):

                os.remove(

                    filepath

                )

                return Utils.success(

                    "Chart deleted.",

                    "chart"

                )

            return Utils.error(

                "Chart not found."

            )

        except Exception as e:

            return Utils.error(

                str(e)

            )


    # ======================================================
    # CLEAR GENERATED CHARTS
    # ======================================================

    def clear_generated_charts(self):

        deleted = 0

        for file in os.listdir(

                self.chart_folder

        ):

            if file.endswith(".png"):

                os.remove(

                    os.path.join(

                        self.chart_folder,

                        file

                    )

                )

                deleted += 1

        return Utils.success(

            {

                "deleted": deleted

            },

            "chart"

        )


    # ======================================================
    # ENGINE INFORMATION
    # ======================================================

    def info(self):

        return Utils.success(

            {

                "engine": "FinanceAI Chart Engine",

                "version": "2.0",

                "supported_entities": [

                    "expense",

                    "income",

                    "budget",

                    "investment",

                    "goal",

                    "analytics"

                ],

                "supported_chart_types": [

                    "pie",

                    "bar",

                    "line"

                ]

            },

            "chart"

        )

    