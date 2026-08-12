"""
==========================================================
FINANCE ANALYTICS PLATFORM
FinanceAI v2.0
Prompt Builder
==========================================================
"""

from .utils import Utils


class PromptBuilder:

    # ======================================================
    # INITIALIZATION
    # ======================================================

    def __init__(

            self,

            database,

            memory

    ):

        self.db = database

        self.memory = memory

    # ======================================================
    # SYSTEM PROMPT
    # ======================================================

    def system_prompt(self):

        return """
You are Finance AI Assistant.

You are a professional AI Financial Advisor.

Behave like ChatGPT.

You help users with:

• Budget Planning

• Expense Analysis

• Income Analysis

• Savings Tracking

• Investment Guidance

• Financial Goal Planning

• Document Analysis

• Receipt OCR

• PDF Analysis

• Excel Analysis

• Financial Reports

Rules:

1. Always be polite.

2. Always answer in Markdown.

3. Use bullet points whenever possible.

4. Never invent user financial data.

5. Use ₹ for all currency values.

6. If data is unavailable, clearly say so.

7. Keep answers concise unless the user asks for detailed explanations.

8. Suggest practical financial improvements whenever appropriate.

9. Never expose database queries or internal implementation details.

10. If the user asks about uploaded documents, base your answer only on the extracted document content.

You are a smart financial assistant, not a generic chatbot.
"""

    # ======================================================
    # CHAT STYLE
    # ======================================================

    def assistant_style(self):

        return """
Response Style

• Friendly
• Professional
• Helpful
• Clear
• Structured
• Easy to understand

Preferred Format

## Summary

## Analysis

## Recommendation

## Conclusion
"""

    # ======================================================
    # GREETING PROMPT
    # ======================================================

    def greeting_prompt(self):

        return """
Introduce yourself briefly.

Tell the user you can help with:

• Income

• Expenses

• Budget

• Investments

• Goals

• Reports

• Charts

• PDF Analysis

• Receipt OCR

Keep the greeting short and welcoming.
"""

    # ======================================================
    # USER FINANCIAL CONTEXT
    # ======================================================

    def financial_context(self, user_id):

        data = self.db.get_complete_user_data(user_id)

        income = data["income"]

        expenses = data["expenses"]

        budget = data["budget"]

        investments = data["investments"]

        goals = data["financial_goals"]

        notifications = data["notifications"]

        # ------------------------------------------
        # TOTAL INCOME
        # ------------------------------------------

        total_income = sum(

            Utils.safe_float(

                row["amount"]

            )

            for row in income

        )

        # ------------------------------------------
        # TOTAL EXPENSE
        # ------------------------------------------

        total_expense = sum(

            Utils.safe_float(

                row["amount"]

            )

            for row in expenses

        )

        savings = total_income - total_expense

        # ------------------------------------------
        # BUDGET
        # ------------------------------------------

        monthly_budget = 0

        if budget:

            try:

                monthly_budget = Utils.safe_float(

                    budget["monthly_budget"]

                )

            except:

                monthly_budget = 0

        budget_used = Utils.percentage(

            total_expense,

            monthly_budget

        )

        # ------------------------------------------
        # HEALTH SCORE
        # ------------------------------------------

        health_score = 100

        if savings < 0:

            health_score -= 40

        elif savings == 0:

            health_score -= 20

        if budget_used > 100:

            health_score -= 30

        elif budget_used > 80:

            health_score -= 10

        health_score = max(

            health_score,

            0

        )

        # ------------------------------------------
        # CONTEXT
        # ------------------------------------------

        context = f"""
==================================================
USER FINANCIAL PROFILE
==================================================

Total Income:
{Utils.format_currency(total_income)}

Total Expense:
{Utils.format_currency(total_expense)}

Savings:
{Utils.format_currency(savings)}

Monthly Budget:
{Utils.format_currency(monthly_budget)}

Budget Used:
{Utils.format_percentage(budget_used)}

Financial Health Score:
{health_score}/100

Investments:
{len(investments)}

Financial Goals:
{len(goals)}

Notifications:
{len(notifications)}
"""

        return context

    # ======================================================
    # CONVERSATION CONTEXT
    # ======================================================

    def conversation_context(

            self,

            user_id,

            limit=10

    ):

        history = self.memory.get_history(

            user_id

        )

        if not history:

            return """

==================================================
CONVERSATION HISTORY
==================================================

No previous conversation available.

"""

        recent_messages = history[-limit:]

        context = """

==================================================
CONVERSATION HISTORY
==================================================

"""

        for message in recent_messages:

            role = message.get(

                "role",

                "user"

            ).capitalize()

            content = Utils.clean_text(

                message.get(

                    "content",

                    ""

                )

            )

            timestamp = message.get(

                "timestamp",

                ""

            )

            context += f"""

[{timestamp}]

{role}

{content}

"""

        return context


    # ======================================================
    # LAST USER MESSAGE
    # ======================================================

    def last_user_message(

            self,

            user_id

    ):

        message = self.memory.last_user_message(

            user_id

        )

        if message:

            return message["content"]

        return ""


    # ======================================================
    # LAST AI MESSAGE
    # ======================================================

    def last_ai_message(

            self,

            user_id

    ):

        message = self.memory.last_ai_message(

            user_id

        )

        if message:

            return message["content"]

        return ""


    # ======================================================
    # MEMORY SUMMARY
    # ======================================================

    def memory_summary(

            self,

            user_id

    ):

        history = self.memory.get_history(

            user_id

        )

        if not history:

            return "No previous conversation."

        total_messages = len(history)

        user_messages = len(

            [

                m

                for m in history

                if m["role"] == "user"

            ]

        )

        ai_messages = len(

            [

                m

                for m in history

                if m["role"] == "assistant"

            ]

        )

        return f"""

Conversation Summary

Total Messages : {total_messages}

User Messages : {user_messages}

AI Messages : {ai_messages}

"""


    # ======================================================
    # MEMORY PROMPT
    # ======================================================

    def memory_prompt(

            self,

            user_id

    ):

        summary = self.memory_summary(

            user_id

        )

        history = self.conversation_context(

            user_id,

            limit=10

        )

        return f"""

==================================================
CHAT MEMORY
==================================================

{summary}

{history}

"""

    # ======================================================
    # DOCUMENT CONTEXT
    # ======================================================

    def document_context(

            self,

            document_data=None

    ):

        if not document_data:

            return """

==================================================
DOCUMENT CONTEXT
==================================================

No document has been uploaded.

"""

        filename = document_data.get(

            "filename",

            "Unknown"

        )

        filetype = document_data.get(

            "type",

            "Unknown"

        )

        filesize = document_data.get(

            "size",

            "Unknown"

        )

        summary = document_data.get(

            "summary",

            ""

        )

        keywords = document_data.get(

            "keywords",

            []

        )

        extracted_text = document_data.get(

            "text",

            ""

        )

        if len(extracted_text) > 3000:

            extracted_text = extracted_text[:3000]

        keyword_text = ", ".join(keywords)

        return f"""

==================================================
UPLOADED DOCUMENT
==================================================

Filename:
{filename}

Document Type:
{filetype}

File Size:
{filesize}

Keywords:
{keyword_text}

==================================================
DOCUMENT SUMMARY
==================================================

{summary}

==================================================
EXTRACTED CONTENT
==================================================

{extracted_text}

"""

    # ======================================================
    # DOCUMENT QUESTION
    # ======================================================

    def document_question(

            self,

            question,

            document_data=None

    ):

        if not document_data:

            return ""

        return f"""

==================================================
USER QUESTION ABOUT DOCUMENT
==================================================

{question}

Answer ONLY using the uploaded document
whenever possible.

If the document does not contain the
requested information, clearly mention it.

"""

    # ======================================================
    # DOCUMENT STATISTICS
    # ======================================================

    def document_statistics(

            self,

            document_data=None

    ):

        if not document_data:

            return ""

        return f"""

Document Statistics

Characters :
{len(document_data.get("text",""))}

Keywords :
{len(document_data.get("keywords",[]))}

Type :
{document_data.get("type","Unknown")}

"""

    # ======================================================
    # COMPLETE DOCUMENT PROMPT
    # ======================================================

    def build_document_prompt(

            self,

            question,

            document_data=None

    ):

        return (

            self.document_context(

                document_data

            )

            +

            self.document_statistics(

                document_data

            )

            +

            self.document_question(

                question,

                document_data

            )

        )

    # ======================================================
    # FINAL PROMPT
    # ======================================================

    def build_prompt(

            self,

            user_id,

            question,

            document_data=None

    ):

        prompt = f"""
{self.system_prompt()}

{self.assistant_style()}

{self.financial_context(user_id)}

{self.memory_prompt(user_id)}

{self.build_document_prompt(question, document_data)}

==================================================
CURRENT USER QUESTION
==================================================

{question}

==================================================
IMPORTANT INSTRUCTIONS
==================================================

1. Answer the user's question directly.

2. Use the financial profile whenever relevant.

3. Use uploaded document information whenever relevant.

4. If information is unavailable, clearly say so.

5. Never invent values.

6. Use Markdown formatting.

7. Use bullet points whenever appropriate.

8. Keep the answer concise unless detailed information is requested.

9. End with a practical recommendation whenever possible.

"""

        return Utils.clean_text(prompt)


    # ======================================================
    # BUILD CHAT MESSAGES
    # ======================================================

    def build_messages(

            self,

            user_id,

            question,

            document_data=None

    ):

        return [

            {

                "role": "system",

                "content": self.system_prompt()

            },

            {

                "role": "user",

                "content": self.build_prompt(

                    user_id,

                    question,

                    document_data

                )

            }

        ]


    # ======================================================
    # QUICK PROMPT
    # ======================================================

    def quick_prompt(

            self,

            question

    ):

        return [

            {

                "role": "system",

                "content": self.system_prompt()

            },

            {

                "role": "user",

                "content": question

            }

        ]


    # ======================================================
    # DEBUG PROMPT
    # ======================================================

    def debug_prompt(

            self,

            user_id,

            question,

            document_data=None

    ):

        return {

            "system_prompt": self.system_prompt(),

            "assistant_style": self.assistant_style(),

            "financial_context": self.financial_context(user_id),

            "memory_context": self.memory_prompt(user_id),

            "document_context": self.build_document_prompt(

                question,

                document_data

            ),

            "question": question,

            "final_prompt": self.build_prompt(

                user_id,

                question,

                document_data

            )

        }


    # ======================================================
    # PROMPT INFORMATION
    # ======================================================

    def prompt_info(

            self,

            user_id,

            question,

            document_data=None

    ):

        prompt = self.build_prompt(

            user_id,

            question,

            document_data

        )

        return {

            "characters": len(prompt),

            "words": len(prompt.split()),

            "question": question

        }

    