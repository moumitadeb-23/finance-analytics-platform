"""
==========================================================
FINANCE ANALYTICS PLATFORM
FinanceAI v2.0
Report Engine
==========================================================
"""

import os

from datetime import datetime

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.platypus import (

    SimpleDocTemplate,

    Paragraph,

    Spacer,

    Table,

    TableStyle

)

from reportlab.lib import colors

from reportlab.lib.units import inch

from .database_manager import DatabaseManager

from .config import REPORT_FOLDER

from .utils import Utils


class ReportEngine:

    # ======================================================
    # INITIALIZATION
    # ======================================================

    def __init__(self):

        self.db = DatabaseManager()

        self.report_folder = REPORT_FOLDER

        os.makedirs(

            self.report_folder,

            exist_ok=True

        )

        self.styles = getSampleStyleSheet()

    # ======================================================
    # REPORT NAME
    # ======================================================

    def report_filename(

            self,

            prefix

    ):

        timestamp = datetime.now().strftime(

            "%Y%m%d_%H%M%S"

        )

        return f"{prefix}_{timestamp}.pdf"

    # ======================================================
    # REPORT PATH
    # ======================================================

    def report_path(

            self,

            filename

    ):

        return os.path.join(

            self.report_folder,

            filename

        )

    # ======================================================
    # CREATE DOCUMENT
    # ======================================================

    def create_document(

            self,

            filename

    ):

        filepath = self.report_path(

            filename

        )

        document = SimpleDocTemplate(

            filepath,

            rightMargin=30,

            leftMargin=30,

            topMargin=30,

            bottomMargin=30

        )

        return document, filepath

    # ======================================================
    # TITLE
    # ======================================================

    def title(

            self,

            text

    ):

        return Paragraph(

            f"<b><font size=18>{text}</font></b>",

            self.styles["Title"]

        )

    # ======================================================
    # HEADING
    # ======================================================

    def heading(

            self,

            text

    ):

        return Paragraph(

            f"<b>{text}</b>",

            self.styles["Heading2"]

        )

    # ======================================================
    # PARAGRAPH
    # ======================================================

    def paragraph(

            self,

            text

    ):

        return Paragraph(

            text,

            self.styles["BodyText"]

        )

    # ======================================================
    # SPACER
    # ======================================================

    def space(self):

        return Spacer(

            1,

            0.20 * inch

        )

    # ======================================================
    # RESPONSE
    # ======================================================

    def report_response(

            self,

            filepath,

            title

    ):

        return Utils.success(

            {

                "title": title,

                "path": filepath,

                "filename": Utils.filename(

                    filepath

                )

            },

            "report"

        )

    # ======================================================
    # STATUS
    # ======================================================

    def status(self):

        return Utils.success(

            {

                "folder": self.report_folder,

                "engine": "FinanceAI Report Engine",

                "version": "2.0"

            },

            "status"

        )

        # ======================================================
    # FINANCIAL SUMMARY
    # ======================================================

    def financial_summary(self, user_id):

        income = self.db.get_income(user_id)

        expenses = self.db.get_expenses(user_id)

        investments = self.db.get_investments(user_id)

        goals = self.db.get_financial_goals(user_id)

        budget = self.db.get_budget(user_id)

        total_income = sum(
            Utils.safe_float(row["amount"])
            for row in income
        )

        total_expense = sum(
            Utils.safe_float(row["amount"])
            for row in expenses
        )

        total_savings = total_income - total_expense

        investment_value = sum(
            Utils.safe_float(
                row["current_value"]
            )
            for row in investments
        )

        goal_count = len(goals)

        budget_amount = 0

        if budget:

            try:

                budget_amount = Utils.safe_float(
                    budget["monthly_budget"]
                )

            except:

                budget_amount = 0

        return {

            "income": total_income,

            "expense": total_expense,

            "savings": total_savings,

            "budget": budget_amount,

            "investments": investment_value,

            "goals": goal_count

        }


    # ======================================================
    # SUMMARY TABLE
    # ======================================================

    def summary_table(self, summary):

        data = [

            ["Metric", "Value"],

            [

                "Total Income",

                Utils.format_currency(
                    summary["income"]
                )

            ],

            [

                "Total Expense",

                Utils.format_currency(
                    summary["expense"]
                )

            ],

            [

                "Savings",

                Utils.format_currency(
                    summary["savings"]
                )

            ],

            [

                "Monthly Budget",

                Utils.format_currency(
                    summary["budget"]
                )

            ],

            [

                "Investment Value",

                Utils.format_currency(
                    summary["investments"]
                )

            ],

            [

                "Financial Goals",

                str(summary["goals"])

            ]

        ]

        table = Table(data)

        table.setStyle(

            TableStyle([

                (

                    "BACKGROUND",

                    (0,0),

                    (-1,0),

                    colors.darkblue

                ),

                (

                    "TEXTCOLOR",

                    (0,0),

                    (-1,0),

                    colors.white

                ),

                (

                    "GRID",

                    (0,0),

                    (-1,-1),

                    1,

                    colors.black

                ),

                (

                    "BACKGROUND",

                    (0,1),

                    (-1,-1),

                    colors.beige

                ),

                (

                    "ALIGN",

                    (0,0),

                    (-1,-1),

                    "CENTER"

                ),

                (

                    "BOTTOMPADDING",

                    (0,0),

                    (-1,0),

                    10

                )

            ])

        )

        return table


    # ======================================================
    # REPORT HEADER
    # ======================================================

    def report_header(self, user_id):

        return [

            self.title(

                "Finance Analytics Platform Report"

            ),

            self.space(),

            self.paragraph(

                f"<b>User ID :</b> {user_id}"

            ),

            self.paragraph(

                f"<b>Date :</b> {datetime.now().strftime('%d-%m-%Y %H:%M')}"

            ),

            self.space()

        ]


    # ======================================================
    # REPORT FOOTER
    # ======================================================

    def report_footer(self):

        return [

            self.space(),

            self.paragraph(

                "<b>Generated by Finance AI Assistant v2.0</b>"

            ),

            self.paragraph(

                "This report is automatically generated using your financial records."

            )

        ]


    # ======================================================
    # BUILD SUMMARY SECTION
    # ======================================================

    def build_summary_section(self, user_id):

        summary = self.financial_summary(

            user_id

        )

        return [

            self.heading(

                "Financial Summary"

            ),

            self.space(),

            self.summary_table(

                summary

            ),

            self.space()

        ]

        # ======================================================
    # INCOME SECTION
    # ======================================================

    def income_section(self, user_id):

        income = self.db.get_income(user_id)

        elements = [

            self.heading("Income Details"),

            self.space()

        ]

        if not income:

            elements.append(

                self.paragraph(

                    "No income records available."

                )

            )

            elements.append(self.space())

            return elements

        data = [

            ["Source", "Amount", "Date"]

        ]

        for row in income:

            data.append([

                str(row["source"]),

                Utils.format_currency(

                    row["amount"]

                ),

                str(row["date"])

            ])

        table = Table(data)

        table.setStyle(TableStyle([

            ("BACKGROUND",(0,0),(-1,0),colors.green),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("GRID",(0,0),(-1,-1),1,colors.black),

            ("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),

            ("ALIGN",(0,0),(-1,-1),"CENTER")

        ]))

        elements.append(table)

        elements.append(self.space())

        return elements


    # ======================================================
    # EXPENSE SECTION
    # ======================================================

    def expense_section(self, user_id):

        expenses = self.db.get_expenses(user_id)

        elements = [

            self.heading("Expense Details"),

            self.space()

        ]

        if not expenses:

            elements.append(

                self.paragraph(

                    "No expense records available."

                )

            )

            elements.append(self.space())

            return elements

        data = [

            ["Category","Amount","Date"]

        ]

        for row in expenses:

            data.append([

                str(row["category"]),

                Utils.format_currency(

                    row["amount"]

                ),

                str(row["date"])

            ])

        table = Table(data)

        table.setStyle(TableStyle([

            ("BACKGROUND",(0,0),(-1,0),colors.red),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("GRID",(0,0),(-1,-1),1,colors.black),

            ("BACKGROUND",(0,1),(-1,-1),colors.beige),

            ("ALIGN",(0,0),(-1,-1),"CENTER")

        ]))

        elements.append(table)

        elements.append(self.space())

        return elements


    # ======================================================
    # INVESTMENT SECTION
    # ======================================================

    def investment_section(self, user_id):

        investments = self.db.get_investments(user_id)

        elements = [

            self.heading("Investment Portfolio"),

            self.space()

        ]

        if not investments:

            elements.append(

                self.paragraph(

                    "No investment records available."

                )

            )

            elements.append(self.space())

            return elements

        data = [

            [

                "Investment",

                "Invested",

                "Current Value"

            ]

        ]

        for row in investments:

            data.append([

                str(row["investment_name"]),

                Utils.format_currency(

                    row["invested_amount"]

                ),

                Utils.format_currency(

                    row["current_value"]

                )

            ])

        table = Table(data)

        table.setStyle(TableStyle([

            ("BACKGROUND",(0,0),(-1,0),colors.darkblue),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("GRID",(0,0),(-1,-1),1,colors.black),

            ("BACKGROUND",(0,1),(-1,-1),colors.lightgrey),

            ("ALIGN",(0,0),(-1,-1),"CENTER")

        ]))

        elements.append(table)

        elements.append(self.space())

        return elements


    # ======================================================
    # GOAL SECTION
    # ======================================================

    def goal_section(self, user_id):

        goals = self.db.get_financial_goals(user_id)

        elements = [

            self.heading("Financial Goals"),

            self.space()

        ]

        if not goals:

            elements.append(

                self.paragraph(

                    "No financial goals found."

                )

            )

            elements.append(self.space())

            return elements

        data = [

            [

                "Goal",

                "Current",

                "Target",

                "Progress"

            ]

        ]

        for row in goals:

            current = Utils.safe_float(

                row["current_amount"]

            )

            target = Utils.safe_float(

                row["target_amount"]

            )

            progress = 0

            if target > 0:

                progress = round(

                    (current / target) * 100,

                    2

                )

            data.append([

                str(row["goal_name"]),

                Utils.format_currency(current),

                Utils.format_currency(target),

                f"{progress}%"

            ])

        table = Table(data)

        table.setStyle(TableStyle([

            ("BACKGROUND",(0,0),(-1,0),colors.purple),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("GRID",(0,0),(-1,-1),1,colors.black),

            ("BACKGROUND",(0,1),(-1,-1),colors.lavender),

            ("ALIGN",(0,0),(-1,-1),"CENTER")

        ]))

        elements.append(table)

        elements.append(self.space())

        return elements

        # ======================================================
    # FINANCIAL HEALTH SCORE
    # ======================================================

    def financial_health_score(self, user_id):

        summary = self.financial_summary(user_id)

        score = 100

        if summary["income"] <= 0:

            score -= 40

        if summary["expense"] > summary["income"]:

            score -= 30

        if summary["savings"] <= 0:

            score -= 20

        if summary["budget"] > 0:

            used = (
                summary["expense"] /
                summary["budget"]
            ) * 100

            if used > 100:

                score -= 20

            elif used > 80:

                score -= 10

        return max(score, 0)


    # ======================================================
    # HEALTH STATUS
    # ======================================================

    def health_status(self, score):

        if score >= 90:

            return "Excellent"

        elif score >= 75:

            return "Good"

        elif score >= 60:

            return "Average"

        elif score >= 40:

            return "Needs Improvement"

        return "Critical"


    # ======================================================
    # EXECUTIVE SUMMARY
    # ======================================================

    def executive_summary(self, user_id):

        summary = self.financial_summary(user_id)

        score = self.financial_health_score(user_id)

        status = self.health_status(score)

        text = f"""

Financial Overview

• Total Income:
{Utils.format_currency(summary['income'])}

• Total Expense:
{Utils.format_currency(summary['expense'])}

• Total Savings:
{Utils.format_currency(summary['savings'])}

• Investment Value:
{Utils.format_currency(summary['investments'])}

• Financial Goals:
{summary['goals']}

Financial Health Score:
{score}/100

Status:
{status}

"""

        return [

            self.heading(

                "Executive Summary"

            ),

            self.space(),

            self.paragraph(text),

            self.space()

        ]


    # ======================================================
    # AI INSIGHTS
    # ======================================================

    def ai_insights(

            self,

            ai_summary=None

    ):

        if not ai_summary:

            ai_summary = """

No AI-generated insights available.

"""

        return [

            self.heading(

                "AI Financial Insights"

            ),

            self.space(),

            self.paragraph(

                ai_summary

            ),

            self.space()

        ]


    # ======================================================
    # RECOMMENDATIONS
    # ======================================================

    def recommendations(self, user_id):

        score = self.financial_health_score(user_id)

        recommendations = []

        if score >= 90:

            recommendations.append(
                "Maintain your current financial habits."
            )

        elif score >= 70:

            recommendations.append(
                "Increase savings wherever possible."
            )

        else:

            recommendations.append(
                "Reduce unnecessary expenses."
            )

            recommendations.append(
                "Create a stricter monthly budget."
            )

            recommendations.append(
                "Track spending more frequently."
            )

        elements = [

            self.heading(

                "Recommendations"

            ),

            self.space()

        ]

        for recommendation in recommendations:

            elements.append(

                self.paragraph(

                    f"• {recommendation}"

                )

            )

        elements.append(self.space())

        return elements

        # ======================================================
    # BUILD REPORT
    # ======================================================

    def build_report(

            self,

            user_id,

            ai_summary=None

    ):

        elements = []

        elements.extend(

            self.report_header(user_id)

        )

        elements.extend(

            self.executive_summary(user_id)

        )

        elements.extend(

            self.build_summary_section(user_id)

        )

        elements.extend(

            self.income_section(user_id)

        )

        elements.extend(

            self.expense_section(user_id)

        )

        elements.extend(

            self.investment_section(user_id)

        )

        elements.extend(

            self.goal_section(user_id)

        )

        elements.extend(

            self.ai_insights(

                ai_summary

            )

        )

        elements.extend(

            self.recommendations(

                user_id

            )

        )

        elements.extend(

            self.report_footer()

        )

        return elements


    # ======================================================
    # GENERATE REPORT
    # ======================================================

    def generate_report(

            self,

            user_id,

            report_type="financial",

            ai_summary=None

    ):

        filename = self.report_filename(

            report_type

        )

        document, filepath = self.create_document(

            filename

        )

        story = self.build_report(

            user_id,

            ai_summary

        )

        document.build(

            story

        )

        return self.report_response(

            filepath,

            report_type.title()

        )


    # ======================================================
    # DELETE REPORT
    # ======================================================

    def delete_report(

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

                    "Report deleted.",

                    "report"

                )

            return Utils.error(

                "Report not found."

            )

        except Exception as e:

            return Utils.error(

                str(e)

            )


    # ======================================================
    # CLEAR REPORTS
    # ======================================================

    def clear_reports(self):

        deleted = 0

        for file in os.listdir(

                self.report_folder

        ):

            if file.endswith(".pdf"):

                os.remove(

                    os.path.join(

                        self.report_folder,

                        file

                    )

                )

                deleted += 1

        return Utils.success(

            {

                "deleted": deleted

            },

            "report"

        )


    # ======================================================
    # AVAILABLE REPORTS
    # ======================================================

    def available_reports(self):

        return Utils.success(

            [

                "financial",

                "expense",

                "investment",

                "budget",

                "goal"

            ],

            "report"

        )


    # ======================================================
    # ENGINE INFO
    # ======================================================

    def info(self):

        return Utils.success(

            {

                "engine":

                "FinanceAI Report Engine",

                "version":"2.0",

                "formats":[

                    "PDF"

                ],

                "reports":[

                    "Financial",

                    "Expense",

                    "Investment",

                    "Budget",

                    "Goal"

                ]

            },

            "report"

        )

    