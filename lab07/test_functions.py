# test_functions.py
from functions import average, normalize_text, sum_digits, select_numbers

# Базовые проверки из задания
assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""
print("Базовые проверки пройдены")

# Дополнительные проверки для Варианта 5 (Не больше порога)
# Контрольный список: [-5, 0, 2, 5], порог 2. Ожидаем: [-5, 0, 2]
assert select_numbers([-5, 0, 2, 5], 2) == [-5, 0, 2]
assert select_numbers([], 5) == []

# Проверка на границе и рядом с ней (порог 2)
# Нам подходят числа <= 2, значит 2 подходит, а 3 - уже нет.
assert select_numbers([1, 2, 3], 2) == [1, 2]

# Проверка на сохранение повторов
assert select_numbers([1, 1, 5], 2) == [1, 1]

# Проверка, что исходный список не меняется
original = [3, 1, 2]
copy_original = original.copy()
select_numbers(original, 2)
assert original == copy_original

print("Проверки варианта пройдены")