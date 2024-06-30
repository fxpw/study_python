from sqlite3 import connect
from pickle import load


# загрузка в новую базу данных из бинарного файла
with open('area.pkl', mode='rb') as f:
    data = load(f)
con = connect('base.db')
cur = con.cursor()

cur.executemany('insert into area values (null, ?, ?)', [(name, ind) for name, ind in data.items()])
con.commit()

con.close()
