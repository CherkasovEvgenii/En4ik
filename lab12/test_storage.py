# test_storage.py
from pathlib import Path
from tempfile import TemporaryDirectory
from storage import load_records, save_records

def test_storage():
    with TemporaryDirectory() as tmp:
        path = Path(tmp) / "test.json"
        
        # Тест: если файла нет, возвращается []
        assert load_records(path) == []
        
        # Тест: сохранение и чтение
        data = [{"id": 1, "title": "A", "category": "B", "amount": 2, "completed": True}]
        save_records(path, data)
        
        loaded = load_records(path)
        assert loaded == data
        
        print("Все тесты в test_storage.py пройдены!")

if __name__ == "__main__":
    test_storage()