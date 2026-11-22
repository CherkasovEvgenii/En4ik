# variant.py
# Индивидуальный вариант 5: id не больше порога

def select_tasks(todos, user_id, parameter=None):
    """
    Возвращает список ID задач указанного пользователя, 
    у которых id <= parameter (порог).
    """
    if parameter is None:
        raise ValueError("Для варианта 5 требуется параметр (числовой порог)")

    result = []
    for item in todos:
        if item["userId"] == user_id and item["id"] <= parameter:
            result.append(item["id"])
    return result