import sqlite3


connection = sqlite3.connect('example.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS student ('
    id INTEGER PRIMARY KEY AUTOINCERMRNT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')
print('Таблица "students" создана')

cursor.execute("INSERT INTO students (name, age) VALUES ('Alice', 21)")
cursor.execute("INSERT INTO students (name, age) VALUES ('Bob', 22)")
print("Данные вставлены")

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("Данные из таблицы 'students': ")
for row in rows:
    print(row)

cursor.execute("UPDATE student SET age = 23 WHERE name = 'Alice")
connection.commit()
print('Данные обновлены')

cursor.execute("SELECT * FROM 'students': ")
rows = cursor.fetchall()
print("Данные из таблицы 'students': ")
for row in rows:
    print(row)

cursor.execute("DELITED FROM students WHERE name = 'Bob'")
connection.commit()
print('Данные удалены')

cursor.execute("SELECT * FROM 'students': ")
rows = cursor.fetchall()
print("Данные из таблицы 'students': ")
for row in rows:
    print(row)

cursor.execute("ALTER TABLE students ADD COLUMN grate TEXT")
