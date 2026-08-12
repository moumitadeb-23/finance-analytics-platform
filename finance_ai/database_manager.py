"""
==========================================================
FINANCE ANALYTICS PLATFORM
FinanceAI v2.0
Database Manager
==========================================================
"""

import sqlite3

from .config import DATABASE_PATH


class DatabaseManager:

    # ======================================================
    # INITIALIZATION
    # ======================================================

    def __init__(self):

        self.database = DATABASE_PATH

    # ======================================================
    # CONNECTION
    # ======================================================

    def connect(self):

        conn = sqlite3.connect(self.database)

        conn.row_factory = sqlite3.Row

        return conn

    # ======================================================
    # EXECUTE QUERY
    # ======================================================

    def execute(self, query, params=()):

        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute(query, params)

        conn.commit()

        last_id = cursor.lastrowid

        conn.close()

        return last_id

    # ======================================================
    # FETCH ONE
    # ======================================================

    def fetch_one(

            self,

            query,

            params=()

    ):

        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute(

            query,

            params

        )

        row = cursor.fetchone()

        conn.close()

        return row

    # ======================================================
    # FETCH ALL
    # ======================================================

    def fetch_all(

            self,

            query,

            params=()

    ):

        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute(

            query,

            params

        )

        rows = cursor.fetchall()

        conn.close()

        return rows

    # ======================================================
    # USER PROFILE
    # ======================================================

    def get_user(

            self,

            user_id

    ):

        return self.fetch_one(

            """

            SELECT *

            FROM users

            WHERE id=?

            """,

            (

                user_id,

            )

        )

    # ======================================================
    # INCOME
    # ======================================================

    def get_income(

            self,

            user_id

    ):

        return self.fetch_all(

            """

            SELECT *

            FROM income

            WHERE user_id=?

            ORDER BY id DESC

            """,

            (

                user_id,

            )

        )

    # ======================================================
    # EXPENSE
    # ======================================================

    def get_expenses(

            self,

            user_id

    ):

        return self.fetch_all(

            """

            SELECT *

            FROM expense

            WHERE user_id=?

            ORDER BY id DESC

            """,

            (

                user_id,

            )

        )

    # ======================================================
    # BUDGET
    # ======================================================

    def get_budget(

            self,

            user_id

    ):

        return self.fetch_one(

            """

            SELECT *

            FROM budget

            WHERE user_id=?

            """,

            (

                user_id,

            )

        )

        # ======================================================
    # INVESTMENTS
    # ======================================================

    def get_investments(self, user_id):

        return self.fetch_all(
            """
            SELECT *
            FROM investments
            WHERE user_id=?
            ORDER BY id DESC
            """,
            (user_id,)
        )

    # ======================================================
    # FINANCIAL GOALS
    # ======================================================

    def get_financial_goals(self, user_id):

        try:

            return self.fetch_all(
                """
                SELECT *
                FROM financial_goal
                WHERE user_id=?
                ORDER BY id DESC
                """,
                (user_id,)
            )

        except:

            return []

    # ======================================================
    # GOALS (Alternative Table)
    # ======================================================

    def get_goals(self, user_id):

        try:

            return self.fetch_all(
                """
                SELECT *
                FROM goals
                WHERE user_id=?
                ORDER BY id DESC
                """,
                (user_id,)
            )

        except:

            return []

    # ======================================================
    # NOTIFICATIONS
    # ======================================================

    def get_notifications(self, user_id):

        try:

            return self.fetch_all(
                """
                SELECT *
                FROM notifications
                WHERE user_id=?
                ORDER BY created_at DESC
                """,
                (user_id,)
            )

        except:

            return []

    # ======================================================
    # CATEGORY BUDGETS
    # ======================================================

    def get_category_budgets(self, user_id):

        try:

            return self.fetch_all(
                """
                SELECT *
                FROM category_budget
                WHERE user_id=?
                """,
                (user_id,)
            )

        except:

            return []

    # ======================================================
    # USER SETTINGS
    # ======================================================

    def get_user_settings(self, user_id):

        try:

            return self.fetch_one(
                """
                SELECT *
                FROM user_settings
                WHERE user_id=?
                """,
                (user_id,)
            )

        except:

            return None

    # ======================================================
    # PREDICTION HISTORY
    # ======================================================

    def get_prediction_history(self, user_id):

        try:

            return self.fetch_all(
                """
                SELECT *
                FROM prediction_history
                WHERE user_id=?
                ORDER BY id DESC
                """,
                (user_id,)
            )

        except:

            return []

    # ======================================================
    # COMPLETE USER DATA
    # ======================================================

    def get_complete_user_data(self, user_id):

        return {

            "user": self.get_user(user_id),

            "income": self.get_income(user_id),

            "expenses": self.get_expenses(user_id),

            "budget": self.get_budget(user_id),

            "investments": self.get_investments(user_id),

            "financial_goals": self.get_financial_goals(user_id),

            "goals": self.get_goals(user_id),

            "notifications": self.get_notifications(user_id),

            "category_budgets": self.get_category_budgets(user_id),

            "settings": self.get_user_settings(user_id),

            "prediction_history": self.get_prediction_history(user_id)

        }

    # ======================================================
    # DATABASE STATUS
    # ======================================================

    def database_status(self):

        try:

            conn = self.connect()

            cursor = conn.cursor()

            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            )

            tables = [

                row["name"]

                for row in cursor.fetchall()

            ]

            conn.close()

            return {

                "connected": True,

                "tables": tables,

                "database": self.database

            }

        except Exception as e:

            return {

                "connected": False,

                "error": str(e)

            }
    # ======================================================
    # CREATE CHAT SESSION
    # ======================================================

    def create_chat_session(self, user_id, title):

        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO chat_sessions
            (
                user_id,
                title
            )
            VALUES
            (?, ?)
        """, (user_id, title))

        conn.commit()

        session_id = cursor.lastrowid

        conn.close()

        return session_id

    # ======================================================
    # SAVE CHAT MESSAGE
    # ======================================================

    def save_chat_message(
            self,
            session_id,
            role,
            message
    ):

        conn = sqlite3.connect(self.database)

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO chat_messages
            (
                session_id,
                role,
                message
            )
            VALUES
            (?, ?, ?)
        """, (
            session_id,
            role,
            message
        ))

        conn.commit()

        conn.close()


    # ======================================================
    # GET CHAT SESSIONS
    # ======================================================

    def get_chat_sessions(self, user_id):

        conn = sqlite3.connect(self.database)

        conn.row_factory = sqlite3.Row

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                title,
                created_at
            FROM chat_sessions
            WHERE user_id=?
            ORDER BY updated_at DESC
        """, (user_id,))

        rows = cursor.fetchall()

        conn.close()

        return [dict(row) for row in rows]

    # ======================================================
    # GET CHAT MESSAGES
    # ======================================================

    def get_chat_messages(self, session_id):

        conn = sqlite3.connect(self.database)

        conn.row_factory = sqlite3.Row

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                role,
                message,
                created_at
            FROM chat_messages
            WHERE session_id=?
            ORDER BY id ASC
        """, (session_id,))

        rows = cursor.fetchall()

        conn.close()

        return [dict(row) for row in rows]

    # ======================================================
    # UPDATE CHAT SESSION
    # ======================================================

    def update_chat_session(self, session_id):

        conn = sqlite3.connect(self.database)

        cursor = conn.cursor()

        cursor.execute("""
            UPDATE chat_sessions
            SET updated_at=CURRENT_TIMESTAMP
            WHERE id=?
        """, (session_id,))

        conn.commit()

        conn.close()