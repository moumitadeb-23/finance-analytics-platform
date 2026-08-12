"""
==========================================================
FINANCE ANALYTICS PLATFORM
FinanceAI v2.0
Tool Router
==========================================================
"""

import re

from finance_ai import document_processor


class ToolRouter:

    # ======================================================
    # INITIALIZATION
    # ======================================================

    def __init__(self):

        self.intent_keywords = {

            "chart": [

                "chart",

                "graph",

                "plot",

                "visualize",

                "pie chart",

                "bar chart",

                "line chart",

                "analytics"

            ],

            "report": [

                "report",

                "summary",

                "pdf report",

                "financial report",

                "export report",

                "download report"

            ],

            "document": [

                "pdf",

                "receipt",

                "invoice",

                "document",

                "excel",

                "csv",

                "image",

                "upload",

                "ocr"

            ],

            "navigation": [

                "dashboard",

                "expense",

                "income",

                "budget",

                "goal",

                "investment",

                "analytics",

                "settings",

                "profile"

            ],

            "finance": [

                "income",

                "expense",

                "saving",

                "budget",

                "investment",

                "goal",

                "money",

                "financial",

                "health"

            ]

        }

    # ======================================================
    # CLEAN MESSAGE
    # ======================================================

    def clean_message(

            self,

            message

    ):

        message = message.lower()

        message = re.sub(

            r"\s+",

            " ",

            message

        )

        return message.strip()

    # ======================================================
    # FIND INTENT
    # ======================================================

    def detect_intent(

            self,

            message

    ):

        message = self.clean_message(

            message

        )

        scores = {}

        for intent, words in self.intent_keywords.items():

            score = 0

            for word in words:

                if word in message:

                    score += 1

            scores[intent] = score

        best = max(

            scores,

            key=scores.get

        )

        if scores[best] == 0:

            return "chat"

        return best

    # ======================================================
    # GREETING
    # ======================================================

    def is_greeting(

            self,

            message

    ):

        greetings = [

            "hi",

            "hello",

            "hey",

            "good morning",

            "good evening",

            "good afternoon"

        ]

        message = self.clean_message(

            message

        )

        return any(

            greeting in message

            for greeting in greetings

        )

    # ======================================================
    # HELP
    # ======================================================

    def is_help(

            self,

            message

    ):

        message = self.clean_message(

            message

        )

        return (

            "help" in message

            or

            "what can you do" in message

            or

            "commands" in message

        )

    # ======================================================
    # RESET CHAT
    # ======================================================

    def is_reset(

            self,

            message

    ):

        message = self.clean_message(

            message

        )

        return (

            "clear chat" in message

            or

            "reset chat" in message

            or

            "new chat" in message

        )

    # ======================================================
    # GET REQUEST TYPE
    # ======================================================

    def request_type(

            self,

            message

    ):

        if self.is_greeting(message):

            return "greeting"

        if self.is_help(message):

            return "help"

        if self.is_reset(message):

            return "reset"

        return self.detect_intent(message)

        # ======================================================
    # EXTRACT ENTITY
    # ======================================================

    def extract_entity(self, message):

        message = self.clean_message(message)

        entities = {

            "expense": [

                "expense",

                "expenses",

                "spending",

                "cost"

            ],

            "income": [

                "income",

                "salary",

                "earning",

                "earnings"

            ],

            "budget": [

                "budget",

                "monthly budget"

            ],

            "saving": [

                "saving",

                "savings"

            ],

            "investment": [

                "investment",

                "investments",

                "portfolio",

                "stocks",

                "mutual fund",

                "sip"

            ],

            "goal": [

                "goal",

                "goals",

                "target"

            ],

            "notification": [

                "notification",

                "notifications",

                "alert",

                "alerts"

            ],

            "health": [

                "health",

                "financial health",

                "score"

            ]

        }

        for entity, keywords in entities.items():

            for keyword in keywords:

                if keyword in message:

                    return entity

        return None


    # ======================================================
    # EXTRACT CHART TYPE
    # ======================================================

    def extract_chart_type(self, message):

        message = self.clean_message(message)

        chart_types = {

            "pie": [

                "pie",

                "pie chart"

            ],

            "bar": [

                "bar",

                "bar chart"

            ],

            "line": [

                "line",

                "line chart"

            ],

            "doughnut": [

                "doughnut",

                "donut"

            ]

        }

        for chart, keywords in chart_types.items():

            for keyword in keywords:

                if keyword in message:

                    return chart

        return "pie"


    # ======================================================
    # EXTRACT TIME PERIOD
    # ======================================================

    def extract_period(self, message):

        message = self.clean_message(message)

        periods = [

            "today",

            "yesterday",

            "week",

            "month",

            "year",

            "last month",

            "last year",

            "this month",

            "this year"

        ]

        for period in periods:

            if period in message:

                return period

        return "all"


    # ======================================================
    # PARSE USER REQUEST
    # ======================================================

    def parse_request(self, message):

        return {

            "intent": self.request_type(message),

            "entity": self.extract_entity(message),

            "chart_type": self.extract_chart_type(message),

            "period": self.extract_period(message),

            "original_message": message

        }


    # ======================================================
    # DEBUG REQUEST
    # ======================================================

    def debug_request(self, message):

        parsed = self.parse_request(message)

        return {

            "success": True,

            "parsed_request": parsed

        }

        # ======================================================
    # ROUTE REQUEST
    # ======================================================

    def route(

            self,

            user_id,

            message,

            chat_engine,

            chart_engine=None,

            report_engine=None,

            document_processor=None,

            document_data=None

    ):

        request = self.parse_request(

            message

        )

        intent = request["intent"]

        # ============================================
        # GREETING
        # ============================================

        if intent == "greeting":

            return chat_engine.welcome_message()

        # ============================================
        # HELP
        # ============================================

        if intent == "help":

            return {

                "success": True,

                "type": "help",

                "data": {

                    "title": "Finance AI Assistant Help",

                    "commands": [

                        "Show my expenses",

                        "Generate expense chart",

                        "Generate financial report",

                        "Analyze uploaded PDF",

                        "Analyze receipt",

                        "Investment summary",

                        "Budget analysis",

                        "Financial health"

                    ]

                }

            }

        # ============================================
        # RESET CHAT
        # ============================================

        if intent == "reset":

            return chat_engine.reset(

                user_id

            )

        # ============================================
        # CHART REQUEST
        # ============================================

        if intent == "chart":

            if chart_engine is None:

                return {

                    "success": False,

                    "type": "error",

                    "message": "Chart Engine not available."

                }

            return chart_engine.generate_chart(

                user_id=user_id,

                entity=request["entity"],

                chart_type=request["chart_type"],

                period=request["period"]

            )

        # ============================================
        # REPORT REQUEST
        # ============================================

        if intent == "report":

            if report_engine is None:

                return {

                    "success": False,

                    "type": "error",

                    "message": "Report Engine not available."

                }

            return report_engine.generate_report(

                user_id=user_id,

                report_type=request["entity"]

            )

        # ============================================
        # DOCUMENT REQUEST
        # ============================================

        if intent == "document":

            if document_data:

                return chat_engine.smart_chat(

                    user_id=user_id,

                    question=message,

                    document_data=document_data

                )

            return {

                "success": False,

                "type": "error",

                "message": "Please upload a document first."

            }

    
        # ============================================
        # DEFAULT → CHAT ENGINE
        # ============================================

        return chat_engine.smart_chat(

            user_id=user_id,

            question=message,

            document_data=document_data

        )

    