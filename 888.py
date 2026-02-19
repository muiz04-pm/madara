import sqlite3
from tabulate import tabulate  # Библиотека для красивого вывода таблиц

# Подключаемся к базе данных
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 1. СОЗДАНИЕ ТАБЛИЦЫ С ДВУМЯ СТОЛБЦАМИ
print("=" * 60)
print("ТАБЛИЦА 1: Students (id, name)")
print("=" * 60)

cursor.execute('DROP TABLE IF EXISTS Students')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
''')

# Добавляем данные
students_names = [
    ('Иван',),
    ('Ольга',),
    ('Сергей',),
    ('Мария',),
    ('Анна',)
]
cursor.executemany('INSERT INTO Students (name) VALUES (?)', students_names)
conn.commit()

# Выводим в виде таблицы
cursor.execute('SELECT * FROM Students')
all_students = cursor.fetchall()
headers = [description[0] for description in cursor.description]  # Получаем названия колонок
print(tabulate(all_students, headers=headers, tablefmt="grid"))
print()

# 2. СОЗДАНИЕ РАСШИРЕННОЙ ТАБЛИЦЫ (5 КОЛОНОК, 10 СТРОК)
print("=" * 60)
print("ТАБЛИЦА 2: Students (id, name, age, grade, city)")
print("=" * 60)

cursor.execute('DROP TABLE IF EXISTS Students')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        grade INTEGER,
        city TEXT
    )
''')

# Добавляем 10 студентов
students_data = [
    ('Иван', 18, 5, 'Москва'),
    ('Ольга', 19, 4, 'Казань'),
    ('Сергей', 20, 5, 'Самара'),
    ('Мария', 18, 3, 'Омск'),
    ('Анна', 21, 4, 'Тула'),
    ('Павел', 22, 5, 'Пермь'),
    ('Юлия', 20, 3, 'Томск'),
    ('Андрей', 19, 4, 'Сочи'),
    ('Виктор', 18, 5, 'Уфа'),
    ('Светлана', 21, 4, 'Воронеж')
]
cursor.executemany('INSERT INTO Students (name, age, grade, city) VALUES (?, ?, ?, ?)', students_data)
conn.commit()

# Выводим всю таблицу
cursor.execute('SELECT * FROM Students')
all_students = cursor.fetchall()
headers = [description[0] for description in cursor.description]
print(tabulate(all_students, headers=headers, tablefmt="grid"))
print()

# 3. ВЫБОРКА ПО ОЦЕНКАМ (в виде таблиц)
print("=" * 60)
print("ВЫБОРКА СТУДЕНТОВ ПО ОЦЕНКАМ")
print("=" * 60)

# Студенты с оценкой 5
cursor.execute('SELECT id, name, age, grade, city FROM Students WHERE grade = 5')
grade_5 = cursor.fetchall()
print("📌 Студенты с оценкой 5:")
print(tabulate(grade_5, headers=headers, tablefmt="rounded_outline"))
print()

# Студенты с оценкой 4
cursor.execute('SELECT id, name, age, grade, city FROM Students WHERE grade = 4')
grade_4 = cursor.fetchall()
print("📌 Студенты с оценкой 4:")
print(tabulate(grade_4, headers=headers, tablefmt="rounded_outline"))
print()

# Студенты с оценкой 3
cursor.execute('SELECT id, name, age, grade, city FROM Students WHERE grade = 3')
grade_3 = cursor.fetchall()
print("📌 Студенты с оценкой 3:")
print(tabulate(grade_3, headers=headers, tablefmt="rounded_outline"))
print()

# 4. ДОПОЛНИТЕЛЬНО: СТАТИСТИКА ПО ГОРОДАМ
print("=" * 60)
print("СТАТИСТИКА: Количество студентов по городам")
print("=" * 60)

cursor.execute('''
    SELECT city, COUNT(*) as count, AVG(grade) as avg_grade 
    FROM Students 
    GROUP BY city
''')
city_stats = cursor.fetchall()
stats_headers = ['Город', 'Количество', 'Средний балл']
print(tabulate(city_stats, headers=stats_headers, tablefmt="double_outline"))
print()

# 5. ДОПОЛНИТЕЛЬНО: СОРТИРОВКА ПО ВОЗРАСТУ
print("=" * 60)
print("Студенты, отсортированные по возрасту (от младших к старшим)")
print("=" * 60)

cursor.execute('SELECT name, age, grade, city FROM Students ORDER BY age')
sorted_by_age = cursor.fetchall()
age_headers = ['Имя', 'Возраст', 'Оценка', 'Город']
print(tabulate(sorted_by_age, headers=age_headers, tablefmt="fancy_grid"))

# Закрываем соединение
conn.commit()
conn.close()
print("\n✅ Работа с базой данных завершена!")