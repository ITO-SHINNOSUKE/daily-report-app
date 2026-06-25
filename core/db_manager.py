# SupabaseやSQLiteの接続管理。ここではSQLiteでの実装例
import sqlite3

def save_report(content):
    conn = sqlite3.connect('reports.db')
    conn.execute('CREATE TABLE IF NOT EXISTS reports (id INTEGER PRIMARY KEY, content TEXT)')
    conn.execute('INSERT INTO reports (content) VALUES (?)', (content,))
    conn.commit()
    conn.close()