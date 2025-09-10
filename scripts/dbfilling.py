import sqlite3

# подключение к базе
conn = sqlite3.connect("../sql_training/base.db")
cursor = conn.cursor()

# создаём таблицу
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT,
    salary INTEGER
)
""")

# вставляем данные
cursor.executemany("""
INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)
""", [
    ("Ali", "IT", 3000),
    ("Sara", "Finance", 3500),
    ("Murat", "HR", 2500),
    ("Dana", "IT", 4000),
])

conn.commit()
conn.close()
print("База заполнена!")