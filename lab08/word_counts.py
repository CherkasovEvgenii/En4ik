# word_counts.py

text = input("Введите текст: ")

# Приводим текст к нижнему регистру и разбиваем по пробелам
words = text.lower().split()
counts = {}

for word in words:
    # Удаляем знаки препинания с краев (.,!?:;)
    clean_word = word.strip(".,!?:;")
    
    # Если после очистки слово не пустое, добавляем в словарь
    if clean_word:
        counts[clean_word] = counts.get(clean_word, 0) + 1

# Вывод результата по алфавиту
if not counts:
    print("{}")
else:
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")