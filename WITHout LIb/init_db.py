import sqlite3

def init_db():
    conn = sqlite3.connect('url_shortener.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS urls
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  long_url TEXT NOT NULL,
                  short_url TEXT UNIQUE NOT NULL)''')
    conn.commit()
    conn.close()

init_db()
