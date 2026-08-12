"""
==========================================================
FINANCE ANALYTICS PLATFORM
FinanceAI v2.0
Main AI Controller
==========================================================
"""

from .database_manager import DatabaseManager
from .memory_manager import MemoryManager
from .chat_engine import ChatEngine
from .chart_engine import ChartEngine
from .report_engine import ReportEngine
from .document_processor import DocumentProcessor
from .tool_router import ToolRouter


class FinanceAI:

    # ======================================================
    # INITIALIZATION
    # ======================================================

    def __init__(self):

        # Core Components
        self.database = DatabaseManager()
        self.memory = MemoryManager()

        # AI Engines
        self.chat_engine = ChatEngine()
        self.chat_engine.memory = self.memory
        self.chart_engine = ChartEngine()
        self.report_engine = ReportEngine()
        self.document_processor = DocumentProcessor()

        # Router
        self.router = ToolRouter()

    # ======================================================
    # SYSTEM INFORMATION
    # ======================================================

    def info(self):

        return {

            "name": "FinanceAI",

            "version": "2.0",

            "engines": {

                "chat": True,

                "documents": True,

                "charts": True,

                "reports": True,

                "router": True

            }

        }

    # ======================================================
    # HEALTH CHECK
    # ======================================================

    def health(self):

        return {

            "database": True,

            "memory": True,

            "chat_engine": True,

            "chart_engine": True,

            "report_engine": True,

            "document_processor": True,

            "tool_router": True

        }

    # ======================================================
    # AVAILABLE FEATURES
    # ======================================================

    def features(self):

        return [

            "AI Chat",

            "Financial Analysis",

            "Budget Analysis",

            "Expense Tracking",

            "Investment Analysis",

            "Charts",

            "Reports",

            "Document OCR",

            "PDF Analysis",

            "Excel Analysis"

        ]

        # ======================================================
    # SMART CHAT
    # ======================================================

    def smart_chat(

            self,

            user_id,

            message,

            document_data=None

    ):

        return self.router.route(

            user_id=user_id,

            message=message,

            chat_engine=self.chat_engine,

            chart_engine=self.chart_engine,

            report_engine=self.report_engine,

            document_processor=self.document_processor,

            document_data=document_data

        )

    # ======================================================
    # PROCESS DOCUMENT
    # ======================================================

    def process_document(

            self,

            uploaded_file

    ):

        return self.document_processor.save_document(

            uploaded_file

        )

    # ======================================================
    # ANALYZE DOCUMENT
    # ======================================================

    def analyze_document(

            self,

            filepath,

            question=None

    ):

        return self.document_processor.process(

            user_id=None,

            question=question,

            document=filepath

        )

    # ======================================================
    # GENERATE CHART
    # ======================================================

    def generate_chart(

            self,

            user_id,

            entity,

            chart_type="pie",

            period="all"

    ):

        return self.chart_engine.generate_chart(

            user_id=user_id,

            entity=entity,

            chart_type=chart_type,

            period=period

        )

    # ======================================================
    # GENERATE REPORT
    # ======================================================

    def generate_report(

            self,

            user_id,

            report_type="financial",

            ai_summary=None

    ):

        return self.report_engine.generate_report(

            user_id=user_id,

            report_type=report_type,

            ai_summary=ai_summary

        )

    # ======================================================
    # CLEAR CHAT
    # ======================================================

    def clear_chat(

            self,

            user_id

    ):

        return self.chat_engine.clear_chat(

            user_id

        )

    # ======================================================
    # CHAT HISTORY
    # ======================================================

    def chat_history(

            self,

            user_id

    ):

        return self.chat_engine.history(

            user_id

        )

    # ======================================================
    # RESET SESSION
    # ======================================================

    def reset_session(

            self,

            user_id

    ):

        return self.chat_engine.reset(

            user_id

        )

        # ======================================================
    # DASHBOARD SUMMARY
    # ======================================================

    def dashboard_summary(self, user_id):

        try:

            summary = self.report_engine.financial_summary(user_id)

            return {

                "success": True,

                "type": "dashboard",

                "data": summary

            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }


    # ======================================================
    # SYSTEM STATUS
    # ======================================================

    def system_status(self):

        return {

            "success": True,

            "database": self.database is not None,

            "memory": self.memory is not None,

            "chat_engine": self.chat_engine is not None,

            "chart_engine": self.chart_engine is not None,

            "report_engine": self.report_engine is not None,

            "document_processor": self.document_processor is not None,

            "tool_router": self.router is not None

        }


    # ======================================================
    # ENGINE INFORMATION
    # ======================================================

    def engine_information(self):

        return {

            "chat": self.chat_engine.info(),

            "charts": self.chart_engine.info(),

            "reports": self.report_engine.info(),

            "documents": self.document_processor.status()

        }


    # ======================================================
    # COMPLETE DIAGNOSTICS
    # ======================================================

    def diagnostics(self):

        return {

            "finance_ai": self.info(),

            "health": self.health(),

            "system": self.system_status(),

            "engines": self.engine_information()

        }


    # ======================================================
    # EXECUTE
    # ======================================================

    def execute(

            self,

            user_id,

            message,

            document_data=None

    ):

        return self.smart_chat(

            user_id=user_id,

            message=message,

            document_data=document_data

        )


    # ======================================================
    # VERSION
    # ======================================================

    def version(self):

        return {

            "name": "FinanceAI",

            "version": "2.0",

            "author": "Finance Analytics Platform"

        }

    