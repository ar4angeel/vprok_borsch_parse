import sqlite3
con = sqlite3.connect('vprok_borsch_part.db')
cur = con.cursor()
with con:
    cur.execute("CREATE TABLE IF NOT EXISTS 'vprok_borsch_part' ('ID' INTEGER, 'AMOUNT' REAL, 'PRICE' REAL)")
    con.commit()
    cur.close()
