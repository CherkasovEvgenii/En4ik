# variant.py
# Индивидуальный вариант 5: Видеокурсы (amount = Кол-во уроков)

# Набор данных (5 записей)
records = [
    {"title": "Python Basics", "category": "Программирование", "amount": 15},
    {"title": "SQL для начинающих", "category": "Базы данных", "amount": 10},
    {"title": "SQL Advanced", "category": "Базы данных", "amount": 12},
    {"title": "Web Design", "category": "Дизайн", "amount": 8},
    {"title": "Data Science", "category": "Программирование", "amount": 20},
]

# Функция для подсчета суммы уроков по категориям
def totals_by_category(recs):
    totals = {}
    for r in recs:
        cat = r["category"]
        # Суммируем amount для каждой категории
        totals[cat] = totals.get(cat, 0) + r["amount"]
    return totals

# Функция для поиска названий курсов по категории
def titles_in_category(recs, cat):
    titles = []
    for r in recs:
        if r["category"] == cat:
            titles.append(r["title"])
    return titles

# Вывод сводки по категориям в алфавитном порядке
totals = totals_by_category(records)
print("Сводка по категориям:")
for cat in sorted(totals):
    print(f"{cat}: {totals[cat]}")

# Поиск по категории, введенной пользователем
user_cat = input("\nВведите категорию для поиска: ")
result = titles_in_category(records, user_cat)

if result:
    print(f"Названия: {result}")
else:
    print(f"Неизвестная категория. Результат: {result}")