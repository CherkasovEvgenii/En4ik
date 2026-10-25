# variant.py
# Индивидуальный вариант 5: слова которые заканчиваются на а

text = input("Введите текст: ")

count = 0

for word in text.split():
    # убираем знаки препинания по краям и делаем маленькие буквы
    clean_word = word.strip(".,!?;:").lower()

    # пустые слова пропускаем
    if clean_word == "":
        continue

    # условие варианта 5: заканчивается на а
    if clean_word.endswith("а"):
        print(clean_word)
        count = count + 1

if count == 0:
    print("Нет совпадений")

print("Количество:", count)
