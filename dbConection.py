import sqlite3

class DbConection:
    def __init__(self, db_name='infinite-craft.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    # returns user as a player object by username
    def get(self, id):
        self.cursor.execute('SELECT * FROM combination WHERE id = ?', (id,))

        row = self.cursor.fetchone()
        it1 = row[1]
        it2 = row[2]
        res = row[3]
        return it1, it2, res
    
