import heapq


def min_cost_to_connect_cables(cables):
    # Створюємо купу з усіх кабелів
    heapq.heapify(cables)
    total_cost = 0

    # Поки у купі є більше одного кабелю
    while len(cables) > 1:
        # Видаляємо два найменші кабелі
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)

        # Об'єднуємо їх та обчислюємо витрати
        combined_cost = cable1 + cable2
        total_cost += combined_cost

        # Додаємо отримані витрати назад у купу
        heapq.heappush(cables, combined_cost)

    return total_cost


# Приклад використання
cable_lengths = [4, 3, 2, 6]
min_total_cost = min_cost_to_connect_cables(cable_lengths)

print("Мінімальні витрати на з'єднання кабелів:", min_total_cost)
