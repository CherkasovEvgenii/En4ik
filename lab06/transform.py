# transform.py
text = input("Введите целые числа через пробел: ")

numbers = [int(x) for x in text.split()]
# Создаем новый список с модулями чисел (abs)
transformed = [abs(x) for x in numbers]

print(f"Исходный список: {numbers}")
print(f"Новый список: {transformed}")