total = int(input("Количество участников: "))
capacity = int(input("участники в группе: "))

print("Заполненных групп:", total // capacity)
print("Остаток участников:", total % capacity)
print("Минимум групп:", (total + capacity - 1) // capacity)