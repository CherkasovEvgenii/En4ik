# logic.py

def validate_records(records):
    """Проверяет список записей на корректность."""
    if not isinstance(records, list):
        raise ValueError("Корень JSON должен быть списком")
    
    seen_ids = set()
    for i, item in enumerate(records):
        if not isinstance(item, dict):
            raise ValueError(f"Запись {i} должна быть словарем")
        
        # id
        if "id" not in item or type(item["id"]) is not int or item["id"] <= 0:
            raise ValueError(f"Запись {i}: неверный id")
        if item["id"] in seen_ids:
            raise ValueError(f"Повторяющийся id: {item['id']}")
        seen_ids.add(item["id"])
        
        # title, category
        for field in ["title", "category"]:
            if field not in item or not isinstance(item[field], str) or not item[field].strip():
                raise ValueError(f"Запись {i}: поле {field} должно быть непустой строкой")
                
        # amount
        if "amount" not in item or type(item["amount"]) is not int or item["amount"] < 0:
            raise ValueError(f"Запись {i}: поле amount должно быть целым неотрицательным числом")
            
        # completed
        if "completed" not in item or type(item["completed"]) is not bool:
            raise ValueError(f"Запись {i}: поле completed должно быть логическим (bool)")

def add_record(records, title, category, amount):
    """Добавляет новую запись, возвращает её ID."""
    new_id = 1 if not records else max(r["id"] for r in records) + 1
    new_record = {
        "id": new_id,
        "title": title.strip(),
        "category": category.strip(),
        "amount": amount,
        "completed": False
    }
    records.append(new_record)
    return new_id

def find_records(records, query):
    """Ищет записи по подстроке в названии (без учета регистра)."""
    if not query.strip():
        return []
    query = query.lower()
    return [r for r in records if query in r["title"].lower()]

def set_completed(records, record_id, completed):
    """Меняет статус выполнения. Возвращает True при успехе, False если ID не найден."""
    for r in records:
        if r["id"] == record_id:
            r["completed"] = completed
            return True
    return False

def delete_record(records, record_id):
    """Удаляет запись по ID. Возвращает True при успехе."""
    for i, r in enumerate(records):
        if r["id"] == record_id:
            del records[i]
            return True
    return False

def statistics(records):
    """Возвращает словарь со статистикой."""
    total = len(records)
    completed = sum(1 for r in records if r["completed"])
    not_completed = total - completed
    total_amount = sum(r["amount"] for r in records)
    
    # Сумма по категориям
    by_category = {}
    for r in records:
        cat = r["category"].strip()
        by_category[cat] = by_category.get(cat, 0) + r["amount"]
        
    return {
        "total": total,
        "completed": completed,
        "not_completed": not_completed,
        "total_amount": total_amount,
        "by_category": by_category
    }