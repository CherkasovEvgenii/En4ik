# main.py
from functions import sum_digits, average, normalize_text, select_numbers

def main():
    # Запрос данных у пользователя
    num_str = input("Введите целое число: ")
    list_str = input("Введите строку чисел через пробел: ")
    text_str = input("Введите произвольный текст: ")
    threshold_str = input("Введите порог (целое число): ")
    
    # Преобразование данных
    number = int(num_str)
    numbers = [int(x) for x in list_str.split()] if list_str.strip() else []
    threshold = int(threshold_str)

    # Демонстрация работы функций
    print(f"Сумма цифр числа {number}: {sum_digits(number)}")
    
    avg = average(numbers)
    if avg is None:
        print("Среднее: Нет данных")
    else:
        print(f"Среднее: {avg}")
        
    print(f"Нормализованный текст: '{normalize_text(text_str)}'")
    
    selected = select_numbers(numbers, threshold)
    print(f"Числа не больше {threshold}: {selected}")

if __name__ == "__main__":
    main()