# variant.py
# Вариант 5: Положительные числа
text = input("Введите целые числа через пробел: ")

numbers = [int(x) for x in text.split()]

# Отбираем только положительные числа (> 0)
positive_nums = [x for x in numbers if x > 0]

# Считаем статистику
count = len(positive_nums)
total_sum = sum(positive_nums)

# Создаем новую отсортированную копию
sorted_copy = sorted(positive_nums)

print(f"Выборка: {positive_nums}")
print(f"Количество: {count}")
print(f"Сумма: {total_sum}")
print(f"Сортированная копия: {sorted_copy}")