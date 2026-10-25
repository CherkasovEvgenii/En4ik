# positions.py
text = input("Введите целые числа через пробел: ")

if not text.strip():
    print("Нет данных")
else:
    numbers = [int(x) for x in text.split()]
    max_val = max(numbers)
    
    # Находим все индексы, где число равно максимуму
    indices = []
    for i, num in enumerate(numbers):
        if num == max_val:
            indices.append(i)
            
    print(f"Индексы максимума: {indices}")