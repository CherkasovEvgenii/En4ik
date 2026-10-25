# statistics.py
text = input("Введите целые числа через пробел: ")

if not text.strip():
    print("Нет данных")
else:
    # Создаем список чисел из введенной строки
    numbers = [int(x) for x in text.split()]
    
    count = len(numbers)
    total_sum = sum(numbers)
    min_val = min(numbers)
    max_val = max(numbers)
    average = total_sum / count
    
    print(f"Количество: {count}")
    print(f"Сумма: {total_sum}")
    print(f"Минимум: {min_val}")
    print(f"Максимум: {max_val}")
    print(f"Среднее: {average:.2f}")