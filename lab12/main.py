# main.py
from pathlib import Path
from storage import load_records, save_records
from logic import add_record, find_records, set_completed, delete_record, statistics

FILE_PATH = Path(__file__).parent / "data.json"

def input_int(prompt, min_val=0):
    while True:
        try:
            val = int(input(prompt))
            if val < min_val:
                print(f"Значение должно быть не меньше {min_val}")
                continue
            return val
        except ValueError:
            print("Ошибка: введите целое число.")

def main():
    print(f"Загрузка данных из {FILE_PATH.name}...")
    try:
        records = load_records(FILE_PATH)
        print(f"Успешно загружено {len(records)} записей.")
    except Exception as e:
        print(f"Ошибка загрузки: {e}")
        print("Запуск прерван.")
        return

    while True:
        print("\n--- МЕНЮ (Вариант 5: Видеокурсы) ---")
        print("1. Показать записи")
        print("2. Добавить запись")
        print("3. Найти записи")
        print("4. Изменить статус")
        print("5. Удалить запись")
        print("6. Показать статистику")
        print("7. Сохранить данные")
        print("8. Выйти")

        choice = input("Выберите пункт (1-8): ").strip()

        if choice == "1":
            if not records:
                print("Нет записей.")
            else:
                for r in sorted(records, key=lambda x: x["id"]):
                    status = "Пройден" if r["completed"] else "Не пройден"
                    print(f"[{r['id']}] {r['title']} | {r['category']} | {r['amount']} уроков | {status}")
        
        elif choice == "2":
            title = input("Название курса: ").strip()
            if not title:
                print("Название не может быть пустым.")
                continue
            category = input("Категория: ").strip()
            if not category:
                print("Категория не может быть пустой.")
                continue
            amount = input_int("Количество уроков: ", 0)
            
            new_id = add_record(records, title, category, amount)
            print(f"Запись добавлена. ID: {new_id}")

        elif choice == "3":
            query = input("Поиск по названию: ").strip()
            if not query:
                print("Поисковый запрос пуст.")
                continue
            results = find_records(records, query)
            if not results:
                print("Ничего не найдено.")
            else:
                for r in results:
                    print(f"[{r['id']}] {r['title']}")
                    
        elif choice == "4":
            rec_id = input_int("Введите ID записи: ", 1)
            new_status = input("Установить статус (1 - пройден, 0 - не пройден): ").strip()
            if new_status not in ("0", "1"):
                print("Неверный статус.")
                continue
            if set_completed(records, rec_id, bool(int(new_status))):
                print("Статус изменен.")
            else:
                print("ID не найден.")

        elif choice == "5":
            rec_id = input_int("Введите ID для удаления: ", 1)
            confirm = input(f"Удалить запись {rec_id}? (да/нет): ").strip().lower()
            if confirm == "да":
                if delete_record(records, rec_id):
                    print("Запись удалена.")
                else:
                    print("ID не найден.")
            else:
                print("Удаление отменено.")

        elif choice == "6":
            stats = statistics(records)
            print("\n--- СТАТИСТИКА ---")
            print(f"Всего записей: {stats['total']}")
            print(f"Пройдено: {stats['completed']}")
            print(f"Не пройдено: {stats['not_completed']}")
            print(f"Общее количество уроков: {stats['total_amount']}")
            print("По категориям:")
            for cat in sorted(stats["by_category"]):
                print(f"  {cat}: {stats['by_category'][cat]}")

        elif choice == "7":
            try:
                save_records(FILE_PATH, records)
                print("Данные успешно сохранены.")
            except Exception as e:
                print(f"Ошибка сохранения: {e}")

        elif choice == "8":
            ans = input("Сохранить изменения перед выходом? (да/нет): ").strip().lower()
            if ans == "да":
                try:
                    save_records(FILE_PATH, records)
                    print("Сохранено. Выход.")
                except Exception as e:
                    print(f"Ошибка сохранения: {e}. Выход без сохранения.")
            else:
                print("Выход без сохранения.")
            break

        else:
            print("Неверная команда. Повторите ввод.")

if __name__ == "__main__":
    main()