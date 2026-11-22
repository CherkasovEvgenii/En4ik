# main.py
import json
from pathlib import Path
from analysis import validate_todos, completion_counts, top_users
from variant import select_tasks

def main():
    file_path = Path(__file__).parent / "todos.json"

    # Чтение
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Ошибка: файл todos.json не найден.")
        return
    except json.JSONDecodeError as e:
        print(f"Ошибка формата JSON: {e}")
        return

    # Проверка структуры
    try:
        validate_todos(data)
    except ValueError as e:
        print(f"Ошибка структуры данных: {e}")
        return

    print("Данные успешно прочитаны и проверены.")

    # Лидеры
    counts = completion_counts(data)
    print(f"Количество завершенных задач: {counts}")
    
    leaders = top_users(counts)
    print(f"Лидеры: {leaders}")

    # Сохранение leaders.json
    leaders_path = Path(__file__).parent / "leaders.json"
    leader_ids = [t["id"] for t in data if t["userId"] in leaders and t["completed"]]
    with open(leaders_path, "w", encoding="utf-8") as f:
        json.dump(leader_ids, f, ensure_ascii=False, indent=2)
    print(f"Результат сохранен в {leaders_path.name}")

    # Индивидуальный вариант 5
    try:
        user_id_str = input("Введите ID пользователя (положительное целое): ")
        user_id = int(user_id_str)
        if user_id <= 0:
            raise ValueError
    except ValueError:
        print("Некорректный ID пользователя.")
        return

    try:
        selected_ids = select_tasks(data, user_id, parameter=2)
        print(f"Результат варианта (ID <= 2): {selected_ids}")
        
        selected_path = Path(__file__).parent / "selected.json"
        with open(selected_path, "w", encoding="utf-8") as f:
            json.dump(selected_ids, f, ensure_ascii=False, indent=2)
        print("Результат сохранен в selected.json")
        
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()