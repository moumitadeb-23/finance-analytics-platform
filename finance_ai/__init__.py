
"""
==========================================================
FINANCE ANALYTICS PLATFORM
FinanceAI v2.0
Package Initializer
==========================================================
"""

__version__ = "2.0.0"
__author__ = "Finance Analytics Platform"

# ==========================================================
# CORE MODULES
# ==========================================================

from .config import *

from .utils import Utils

from .database_manager import DatabaseManager

from .memory_manager import MemoryManager

# ==========================================================
# AI MODULES
# ==========================================================

from .prompt_builder import PromptBuilder

from .chat_engine import ChatEngine

from .tool_router import ToolRouter

from .document_processor import DocumentProcessor

from .chart_engine import ChartEngine

from .report_engine import ReportEngine

from .finance_ai import FinanceAI

# ==========================================================
# PUBLIC API
# ==========================================================

__all__ = [

    "FinanceAI",

    "ChatEngine",

    "PromptBuilder",

    "ToolRouter",

    "DocumentProcessor",

    "ChartEngine",

    "ReportEngine",

    "DatabaseManager",

    "MemoryManager",

    "Utils"

]

