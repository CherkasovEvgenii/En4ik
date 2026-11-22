# records.py

# Создаем словарь с начальными данными
record = {
    "title": "Python для начинающих",
    "hours": 10
}

# Изменяем значение по ключу "hours" и добавляем новый ключ "completed"
record["hours"] = 15
record["completed"] = False

# Создаем кортеж из значений title и hours
pair = (record["title"], record["hours"])

# Распаковываем кортеж в две переменные
title, hours = pair

print(f"Title: {title}, Hours: {hours}")