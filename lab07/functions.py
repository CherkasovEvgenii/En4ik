# functions.py

def sum_digits(number):
    """Возвращает сумму цифр модуля числа."""
    number = abs(number)
    total = 0
    while number > 0:
        total += number % 10
        number = number // 10
    return total

def average(numbers):
    """Возвращает среднее арифметическое или None, если список пуст."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def normalize_text(text):
    """Возвращает текст в нижнем регистре без лишних пробелов."""
    return " ".join(text.lower().split())

def select_numbers(numbers, threshold):
    """Вариант 5: возвращает числа не больше порога (<= threshold)."""
    result = []
    for num in numbers:
        if num <= threshold:
            result.append(num)
    return result