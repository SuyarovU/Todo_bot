import sqlite3

conn = sqlite3.connect('todos.db')

cursor = conn.cursor()

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    todo TEXT,
    status BOOLEAN DEFAULT False
)
    '''
)