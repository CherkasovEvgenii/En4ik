# topics.py

# Ввод двух списков тем (разделенных пробелом)
first = input("Введите темы первого списка: ").split()
second = input("Введите темы второго списка: ").split()

# Преобразуем списки во множества для математических операций
set_first = set(first)
set_second = set(second)

# Пересечение (&) - общие темы
common = set_first & set_second

# Объединение (|) - все уникальные темы
all_unique = set_first | set_second

# Вывод (обязательно с sorted, т.к. множества неупорядочены)
print(f"Общие темы: {sorted(common)}")
print(f"Все темы: {sorted(all_unique)}")