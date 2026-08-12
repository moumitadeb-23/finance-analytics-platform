"""
==========================================================
FINANCE ANALYTICS PLATFORM
FinanceAI v2.0
Memory Manager
==========================================================
"""

from datetime import datetime

from .config import MAX_CHAT_HISTORY


class MemoryManager:

    # ======================================================
    # INITIALIZATION
    # ======================================================

    def __init__(self):

        self.chat_memory = {}

    # ======================================================
    # CREATE USER MEMORY
    # ======================================================

    def initialize_user(self, user_id):

        if user_id not in self.chat_memory:

            self.chat_memory[user_id] = []

    # ======================================================
    # GET CHAT HISTORY
    # ======================================================

    def get_history(self, user_id):

        self.initialize_user(user_id)

        return self.chat_memory[user_id]

    # ======================================================
    # SAVE MESSAGE
    # ======================================================

    def add_message(

            self,

            user_id,

            role,

            content

    ):

        self.initialize_user(user_id)

        self.chat_memory[user_id].append(

            {

                "role": role,

                "content": content,

                "timestamp": datetime.now().strftime(

                    "%Y-%m-%d %H:%M:%S"

                )

            }

        )

        self.cleanup(user_id)

    # ======================================================
    # CLEANUP MEMORY
    # ======================================================

    def cleanup(self, user_id):

        self.initialize_user(user_id)

        history = self.chat_memory[user_id]

        max_messages = MAX_CHAT_HISTORY * 2

        if len(history) > max_messages:

            self.chat_memory[user_id] = history[-max_messages:]

    # ======================================================
    # LAST USER MESSAGE
    # ======================================================

    def last_user_message(self, user_id):

        history = self.get_history(user_id)

        for message in reversed(history):

            if message["role"] == "user":

                return message

        return None

    # ======================================================
    # LAST AI MESSAGE
    # ======================================================

    def last_ai_message(self, user_id):

        history = self.get_history(user_id)

        for message in reversed(history):

            if message["role"] == "assistant":

                return message

        return None

    # ======================================================
    # CLEAR CHAT
    # ======================================================

    def clear_history(self, user_id):

        self.chat_memory[user_id] = []

        return True

    # ======================================================
    # EXPORT CHAT
    # ======================================================

    def export_history(self, user_id):

        return self.get_history(user_id)

    # ======================================================
    # CONVERSATION CONTEXT
    # ======================================================

    def build_context(

            self,

            user_id,

            limit=10

    ):

        history = self.get_history(user_id)

        recent = history[-limit:]

        context = ""

        for item in recent:

            role = item["role"].capitalize()

            context += f"{role}: {item['content']}\n"

        return context

    # ======================================================
    # MEMORY STATUS
    # ======================================================

    def status(self):

        return {

            "users": len(self.chat_memory),

            "total_messages": sum(

                len(history)

                for history in self.chat_memory.values()

            )

        }