import sqlite3

class DBManager:
    def __init__(self, db_path="db/cards.db"):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        """дєлает табліцу якщо іі нема"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS words (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    french TEXT UNIQUE NOT NULL,
                    ukrainian TEXT NOT NULL,
                    learned INTEGER DEFAULT 0
                )
            """)
            conn.commit()

    def add_word(self, french, ukrainian):
        """добавить слово в бд"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO words (french, ukrainian) VALUES (?, ?)", (french, ukrainian))
                conn.commit()
            except sqlite3.IntegrityError:
                print(f"Слово '{french}' вже є в базі.")

    def get_random_word(self):
        """рандом слово для вивчення"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT french, ukrainian FROM words WHERE learned = 0 ORDER BY RANDOM() LIMIT 1")
            return cursor.fetchone()

    def mark_as_learned(self, french):
        """позначить слово як вивчене"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE words SET learned = 1 WHERE french = ?", (french,))
            conn.commit()

