# storage.py
import json
from pathlib import Path
from logic import validate_records

def load_records(path):
    """Загружает записи из JSON. Возвращает пустой список, если файла нет."""
    p = Path(path)
    if not p.exists():
        return []
    
    try:
        with open(p, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Файл поврежден или содержит невалидный JSON")
        
    validate_records(data)
    return data

def save_records(path, records):
    """Сохраняет записи в JSON."""
    p = Path(path)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)