"""
==========================================================
FINANCE ANALYTICS PLATFORM
FinanceAI v2.0
Chat Engine
==========================================================
"""

import ollama
from datetime import datetime

from .config import (
    OLLAMA_MODEL,
)

from .utils import Utils
from .prompt_builder import PromptBuilder
from .memory_manager import MemoryManager
from .database_manager import DatabaseManager


class ChatEngine:

    # ======================================================
    # INITIALIZATION
    # ======================================================

    def __init__(self):

        self.model = OLLAMA_MODEL

        self.database = DatabaseManager()

        self.memory = MemoryManager()

        self.prompt_builder = PromptBuilder(

            self.database,

            self.memory

        )

        self.started = datetime.now()

    # ======================================================
    # ENGINE INFORMATION
    # ======================================================

    def info(self):

        return {

            "engine": "FinanceAI v2.0",

            "model": self.model,

            "started": self.started.strftime(

                "%Y-%m-%d %H:%M:%S"

            )

        }

    # ======================================================
    # HEALTH CHECK
    # ======================================================

    def health(self):

        try:

            ollama.list()

            return {

                "success": True,

                "message": "Ollama is running."

            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }

    # ======================================================
    # CHECK MODEL
    # ======================================================

    def model_exists(self):

        try:

            models = ollama.list()

            installed = []

            for model in models.get(

                "models",

                []

            ):

                name = model.get(

                    "model",

                    ""

                )

                installed.append(name)

            return self.model in installed

        except:

            return False

    # ======================================================
    # LOAD MODEL
    # ======================================================

    def load_model(self):

        if self.model_exists():

            return {

                "success": True,

                "message":

                f"{self.model} is available."

            }

        return {

            "success": False,

            "message":

            f"{self.model} is not installed."

        }

    # ======================================================
    # AI STATUS
    # ======================================================

    def status(self):

        health = self.health()

        return {

            "engine": "FinanceAI",

            "model": self.model,

            "running": health["success"],

            "message": health["message"]

        }

        # ======================================================
    # SEND REQUEST TO OLLAMA
    # ======================================================

    def ask_ollama(

            self,

            messages

    ):

        try:

            response = ollama.chat(

                model=self.model,

                messages=messages,

                stream=False

            )

            if (

                "message" not in response

                or

                "content" not in response["message"]

            ):

                return Utils.error(

                    "Invalid response received from Ollama."

                )

            answer = response["message"]["content"]

            answer = Utils.clean_text(

                answer

            )

            if answer == "":

                answer = (

                    "Sorry, I couldn't generate a response."

                )

            return Utils.success(

                answer,

                "chat"

            )

        except Exception as e:

            return Utils.error(

                f"Ollama Error : {str(e)}"

            )


    # ======================================================
    # ASK QUICK QUESTION
    # ======================================================

    def ask(

            self,

            question

    ):

        messages = self.prompt_builder.quick_prompt(

            question

        )

        return self.ask_ollama(

            messages

        )


    # ======================================================
    # ASK WITH USER CONTEXT
    # ======================================================

    def ask_user(

            self,

            user_id,

            question,

            document_data=None

    ):

        messages = self.prompt_builder.build_messages(

            user_id,

            question,

            document_data

        )

        return self.ask_ollama(

            messages

        )


    # ======================================================
    # MODEL INFORMATION
    # ======================================================

    def model_information(self):

        try:

            models = ollama.list()

            return Utils.success(

                models,

                "model"

            )

        except Exception as e:

            return Utils.error(

                str(e)

            )


    # ======================================================
    # TEST MODEL
    # ======================================================

    def test(self):

        result = self.ask(

            "Say Hello."

        )

        return result

        # ======================================================
    # CHAT WITH MEMORY
    # ======================================================

    def chat(

            self,

            user_id,

            question,

            document_data=None

    ):

        # -----------------------------
        # Create Chat Session
        # -----------------------------

        session_id = self.database.create_chat_session(

            user_id,

            question[:50]

        )



        # -----------------------------
        # Save User Message
        # -----------------------------

        self.memory.add_message(

            user_id,

            "user",

            question

        )
        self.database.save_chat_message(

            session_id,

            "user",

            question

        )

        # -----------------------------
        # Generate AI Response
        # -----------------------------

        result = self.ask_user(

            user_id,

            question,

            document_data

        )

        # -----------------------------
        # Save AI Response
        # -----------------------------

        if result["success"]:

            self.memory.add_message(

                user_id,

                "assistant",

                result["data"]

            )

            self.database.save_chat_message(

                session_id,

                "assistant",

                result["data"]

            )


            self.database.update_chat_session(

                session_id

            )

        return result


    # ======================================================
    # CHAT HISTORY
    # ======================================================

    def history(

            self,

            user_id

    ):

        history = self.memory.get_history(

            user_id

        )

        return Utils.success(

            history,

            "history"

        )


    # ======================================================
    # CLEAR CHAT
    # ======================================================

    def clear_chat(

            self,

            user_id

    ):

        self.memory.clear_history(

            user_id

        )

        return Utils.success(

            "Conversation cleared successfully.",

            "chat"

        )


    # ======================================================
    # LAST RESPONSE
    # ======================================================

    def last_response(

            self,

            user_id

    ):

        response = self.memory.last_ai_message(

            user_id

        )

        if response:

            return Utils.success(

                response,

                "chat"

            )

        return Utils.error(

            "No previous AI response found."

        )


    # ======================================================
    # LAST USER MESSAGE
    # ======================================================

    def last_question(

            self,

            user_id

    ):

        message = self.memory.last_user_message(

            user_id

        )

        if message:

            return Utils.success(

                message,

                "chat"

            )

        return Utils.error(

            "No previous user message found."

        )


    # ======================================================
    # CHAT SUMMARY
    # ======================================================

    def chat_summary(

            self,

            user_id

    ):

        history = self.memory.get_history(

            user_id

        )

        return Utils.success(

            {

                "messages": len(history),

                "last_user": self.memory.last_user_message(

                    user_id

                ),

                "last_ai": self.memory.last_ai_message(

                    user_id

                )

            },

            "summary"

        )


    # ======================================================
    # RESET AI SESSION
    # ======================================================

    def reset(

            self,

            user_id

    ):

        self.memory.clear_history(

            user_id

        )

        return Utils.success(

            "AI session reset successfully.",

            "reset"

        )

        # ======================================================
    # CHAT WITH METADATA
    # ======================================================

    def chat_with_metadata(

            self,

            user_id,

            question,

            document_data=None

    ):

        start_time = datetime.now()

        result = self.chat(

            user_id,

            question,

            document_data

        )

        end_time = datetime.now()

        latency = (

            end_time - start_time

        ).total_seconds()

        if result["success"]:

            result["metadata"] = {

                "model": self.model,

                "latency": round(

                    latency,

                    2

                ),

                "timestamp": datetime.now().strftime(

                    "%Y-%m-%d %H:%M:%S"

                )

            }

        return result


    # ======================================================
    # FOLLOW-UP SUGGESTIONS
    # ======================================================

    def follow_up_questions(

            self,

            question

    ):

        question = question.lower()

        if "expense" in question:

            return [

                "Show my expense chart",

                "Which category has the highest expense?",

                "How can I reduce my expenses?"

            ]

        elif "income" in question:

            return [

                "Compare income and expenses",

                "Show my savings",

                "Generate income report"

            ]

        elif "budget" in question:

            return [

                "How much budget is remaining?",

                "Show budget chart",

                "Give budget advice"

            ]

        elif "investment" in question:

            return [

                "Show investment summary",

                "Investment performance",

                "Suggest investment ideas"

            ]

        return [

            "Show financial summary",

            "Generate report",

            "Analyze my spending"

        ]


    # ======================================================
    # CHAT WITH SUGGESTIONS
    # ======================================================

    def smart_chat(

            self,

            user_id,

            question,

            document_data=None

    ):

        result = self.chat_with_metadata(

            user_id,

            question,

            document_data

        )

        if result["success"]:

            result["suggestions"] = self.follow_up_questions(

                question

            )

        return result


    # ======================================================
    # RETRY CHAT
    # ======================================================

    def retry_chat(

            self,

            user_id,

            question,

            retries=2,

            document_data=None

    ):

        for _ in range(retries + 1):

            result = self.smart_chat(

                user_id,

                question,

                document_data

            )

            if result["success"]:

                return result

        return Utils.error(

            "Unable to generate a response after multiple attempts."

        )


    # ======================================================
    # AI GREETING
    # ======================================================

    def welcome_message(self):

        return Utils.success(

            """
            👋 Welcome to Finance AI Assistant!

            I can help you with:

            • Financial Analysis
            • Budget Planning
            • Expense Tracking
          
              • Investment Advice
            • Financial Goals
            • Reports
            • Charts
            • PDF Analysis
            • Receipt OCR
            • Excel & CSV Analysis

            How can I assist you today?
                        """,

                        "welcome"

                    )

    