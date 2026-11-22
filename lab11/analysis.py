# analysis.py

def validate_todos(data):
    """
    Проверяет структуру данных. 
    Выбрасывает ValueError при нарушении.
    """
    if not isinstance(data, list):
        raise ValueError("Корень JSON должен быть списком")

    seen_ids = set()

    for i, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(f"Элемент {i} должен быть словарем")

        # Проверка id (строго int, положительный, уникальный)
        if "id" not in item or type(item["id"]) is not int or item["id"] <= 0:
            raise ValueError(f"Элемент {i}: неверный или отсутствующий id")
        
        if item["id"] in seen_ids:
            raise ValueError(f"Элемент {i}: дублирующийся id {item['id']}")
        seen_ids.add(item["id"])

        # Проверка userId (строго int, положительный)
        if "userId" not in item or type(item["userId"]) is not int or item["userId"] <= 0:
            raise ValueError(f"Элемент {i}: неверный или отсутствующий userId")

        # Проверка title (строго str, не пустой)
        if "title" not in item or not isinstance(item["title"], str) or not item["title"].strip():
            raise ValueError(f"Элемент {i}: title должен быть непустой строкой")

        # Проверка completed (строго bool, а не int)
        if "completed" not in item or type(item["completed"]) is not bool:
            raise ValueError(f"Элемент {i}: completed должен быть логическим значением (bool)")


def completion_counts(todos):
    """Возвращает словарь количества выполненных задач для каждого пользователя."""
    counts = {}
    for item in todos:
        user = item["userId"]
        if user not in counts:
            counts[user] = 0
        if item["completed"]:
            counts[user] += 1
    return counts


def top_users(counts):
    """Возвращает отсортированный список ID пользователей с максимальным количеством задач."""
    if not counts:
        return []
    
    max_completed = max(counts.values())
    if max_completed == 0:
        return []
        
    leaders = [user for user, count in counts.items() if count == max_completed]
    return sorted(leaders)