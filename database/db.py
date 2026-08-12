import sqlite3


def get_connection():
    return sqlite3.connect("finance.db")


# ------------------------------
# Create Budget Table
# ------------------------------

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS budget(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE,
    monthly_budget REAL NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

conn.commit()
conn.close()



# ------------------------------
# Investment Functions
# ------------------------------

def add_investment(
    asset_type,
    investment_name,
    invested_amount,
    current_value,
    purchase_date,
    notes
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO investments
        (
            asset_type,
            investment_name,
            invested_amount,
            current_value,
            purchase_date,
            notes
        )
        VALUES (?,?,?,?,?,?)
    """, (
        asset_type,
        investment_name,
        invested_amount,
        current_value,
        purchase_date,
        notes
    ))

    conn.commit()
    conn.close()


def get_all_investments():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM investments
        ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def delete_investment(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM investments WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

def get_portfolio_analytics():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            asset_type,
            SUM(invested_amount) AS total_invested,
            SUM(current_value) AS total_current
        FROM investments
        GROUP BY asset_type
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def update_investment(
    investment_id,
    asset_type,
    investment_name,
    invested_amount,
    current_value,
    purchase_date,
    notes
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE investments

        SET
            asset_type = ?,
            investment_name = ?,
            invested_amount = ?,
            current_value = ?,
            purchase_date = ?,
            notes = ?

        WHERE id = ?
    """, (
        asset_type,
        investment_name,
        invested_amount,
        current_value,
        purchase_date,
        notes,
        investment_id
    ))

    conn.commit()
    conn.close()


# ============================================================
# MODULE 3 - FINANCIAL GOAL DATABASE FUNCTIONS
# ============================================================


def add_financial_goal(
        user_id,
        goal_type,
        goal_name,
        target_amount,
        saved_amount,
        target_date
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO financial_goals
        (
            user_id,
            goal_type,
            goal_name,
            target_amount,
            saved_amount,
            target_date
        )

        VALUES (?, ?, ?, ?, ?, ?)

    """, (

        user_id,
        goal_type,
        goal_name,
        target_amount,
        saved_amount,
        target_date

    ))

    conn.commit()

    conn.close()


# ============================================================
# GET ALL GOALS OF LOGGED-IN USER
# ============================================================


def get_all_financial_goals(user_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM financial_goals

        WHERE user_id=?

        ORDER BY id DESC

    """, (

        user_id,

    ))

    financial_goals = cursor.fetchall()

    conn.close()

    return financial_goals


# ============================================================
# UPDATE FINANCIAL GOAL
# ============================================================


def update_financial_goal(
        id,
        user_id,
        goal_type,
        goal_name,
        target_amount,
        saved_amount,
        target_date
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        UPDATE financial_goals

        SET
            goal_type=?,
            goal_name=?,
            target_amount=?,
            saved_amount=?,
            target_date=?

        WHERE id=?

        AND user_id=?

    """, (

        goal_type,
        goal_name,
        target_amount,
        saved_amount,
        target_date,
        id,
        user_id

    ))

    conn.commit()

    conn.close()


# ============================================================
# ADD SAVINGS TO GOAL
# ============================================================


def add_goal_savings(
        id,
        user_id,
        savings_amount
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        UPDATE financial_goals

        SET saved_amount = saved_amount + ?

        WHERE id=?

        AND user_id=?

    """, (

        savings_amount,
        id,
        user_id

    ))

    goal = cursor.fetchone()

    if goal and goal[2] >= goal[1]:
        add_notification(
            user_id,
            "Goal Achieved",
            f"🎉 Congratulations! You achieved your goal '{goal[0]}'.",
            "success"
        )

    conn.commit()

    conn.close()


# ============================================================
# DELETE FINANCIAL GOAL
# ============================================================


def delete_financial_goal(
        id,
        user_id
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        DELETE FROM financial_goals

        WHERE id=?

        AND user_id=?

    """, (

        id,
        user_id

    ))

    conn.commit()

    conn.close()


# ============================================================
# ADD NOTIFICATION 
# ============================================================

def add_notification(user_id, title, message, notification_type):

    print("Notification Called:", title)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO notifications
        (user_id, title, message, type)
        VALUES (?, ?, ?, ?)
    """, (
        user_id,
        title,
        message,
        notification_type
    ))

    conn.commit()

    print("Rows inserted:", cursor.rowcount)

    conn.close()

# ==========================================================
# DATASET MANAGEMENT
# ==========================================================

from datetime import datetime


def get_dataset_info(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM dataset_info
        WHERE user_id=?
    """, (user_id,))

    data = cursor.fetchone()

    conn.close()

    return data


def get_dataset_history(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM dataset_history

        WHERE user_id=?

        ORDER BY id DESC

    """, (user_id,))

    history = cursor.fetchall()

    conn.close()

    return history

