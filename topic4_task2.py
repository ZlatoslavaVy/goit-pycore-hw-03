import random
def get_numbers_ticket(min, max, quantity):
    
    # вимоги до параметрів функції:
    if not (1 <= min <= 1000):
        print("Помилка: мінімальне число повинно бути не менше 1 і не більше 1000.")
        return []

    if not (1 <= max <= 1000):
        print("Помилка: максимальне число повинно бути не менше 1 і не більше 1000.")
        return []

    if min >= max:
        print("Помилка: мінімальне число має бути менше за максимальне.")
        return []

    max_quantity = max - min + 1
    if not (1 <= quantity <= max_quantity):
        print(f"Помилка: кількість чисел повинна бути від 1 до {max_quantity}.")
        return []

    # генеруємо список унікальних випадкових чисел:
    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()
    return numbers

if __name__ == "__main__":
    # приклад використання — визначаємо змінні ПЕРЕД викликом функції
    min, max, quantity = 1, 49, 6

    # генеруємо білет користувача:
    user_ticket = get_numbers_ticket(min, max, quantity)
    print("Ваші лотерейні числа:", user_ticket)

    # генеруємо виграшну комбінацію:
    winning_ticket = get_numbers_ticket(min, max, quantity)
    print("Виграшні числа:", winning_ticket)

    # перевіряємо скільки чисел вгадано:
    matched = set(user_ticket).intersection(winning_ticket)
    print(f"Ви вгадали {len(matched)} чисел: {matched}")

    # результат:
    if len(matched) == quantity:
        print("Вітаємо! Ви виграли головний приз!")
    elif len(matched) >= 3:
        print("Є частковий виграш!")
    else:
        print("Ви програли!")

    # кілька тестових викликів:
    print(get_numbers_ticket(1, 49, 6))
    print(get_numbers_ticket(1, 36, 5))
    print(get_numbers_ticket(5, 1, 4))