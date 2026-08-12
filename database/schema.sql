CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    email TEXT UNIQUE NOT NULL,

    password TEXT NOT NULL,

    phone TEXT,

    occupation TEXT,

    monthly_income REAL DEFAULT 0,

    profile_photo TEXT DEFAULT 'default.png',

    date_of_birth TEXT,

    gender TEXT,

    address TEXT,

    city TEXT,

    state TEXT,

    country TEXT DEFAULT 'India',

    pincode TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);


-- ==============================
-- INCOME TABLE
-- ==============================

CREATE TABLE IF NOT EXISTS income (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER,

    source TEXT,

    amount REAL,

    date TEXT,

    FOREIGN KEY(user_id) REFERENCES users(id)

);


-- ==============================
-- EXPENSE TABLE
-- ==============================

CREATE TABLE IF NOT EXISTS expense (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER,

    category TEXT,

    amount REAL,

    description TEXT,

    date TEXT,

    FOREIGN KEY(user_id) REFERENCES users(id)

);


-- ==============================
-- BUDGET TABLE
-- ==============================

CREATE TABLE IF NOT EXISTS budget (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER UNIQUE,

    monthly_budget REAL NOT NULL,

    FOREIGN KEY(user_id) REFERENCES users(id)

);


-- ==============================
-- CATEGORY BUDGET TABLE
-- ==============================

CREATE TABLE IF NOT EXISTS category_budget (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER NOT NULL,

    category TEXT NOT NULL,

    budget REAL NOT NULL,

    FOREIGN KEY(user_id) REFERENCES users(id)

);


-- ==============================
-- USER SETTINGS TABLE
-- ==============================

CREATE TABLE IF NOT EXISTS user_settings (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER UNIQUE,

    theme TEXT DEFAULT 'light',

    currency TEXT DEFAULT 'INR',

    remember_login INTEGER DEFAULT 1,

    two_factor INTEGER DEFAULT 0,

    email_alert INTEGER DEFAULT 1,

    ai_level TEXT DEFAULT 'Balanced',

    notifications INTEGER DEFAULT 1,

    FOREIGN KEY(user_id) REFERENCES users(id)

);


-- ==============================
-- INVESTMENTS TABLE
-- ==============================

CREATE TABLE IF NOT EXISTS investments (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    asset_type TEXT NOT NULL,

    investment_name TEXT NOT NULL,

    invested_amount REAL NOT NULL,

    current_value REAL NOT NULL,

    purchase_date TEXT,

    notes TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);


-- ==============================
-- FINANCIAL GOAL TABLE
-- ==============================

CREATE TABLE IF NOT EXISTS financial_goals (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER NOT NULL,

    goal_type TEXT NOT NULL,

    goal_name TEXT NOT NULL,

    target_amount REAL NOT NULL,

    saved_amount REAL DEFAULT 0,

    target_date TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id) REFERENCES users(id)

);


-- ==============================
-- NOTIFICATIONS TABLE
-- ==============================

CREATE TABLE IF NOT EXISTS notifications (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER NOT NULL,

    title TEXT NOT NULL,

    message TEXT NOT NULL,

    type TEXT DEFAULT 'info',

    is_read INTEGER DEFAULT 0,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id) REFERENCES users(id)

);

-- ==============================
-- BILLS TABLE
-- ==============================

CREATE TABLE bills(

id INTEGER PRIMARY KEY AUTOINCREMENT,

user_id INTEGER NOT NULL,

bill_name TEXT NOT NULL,

category TEXT,

amount REAL NOT NULL,

due_date TEXT,

frequency TEXT,

status TEXT DEFAULT 'Pending',

reminder_days INTEGER DEFAULT 3,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);