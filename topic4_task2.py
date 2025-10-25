import random


def get_numbers_ticket(min, max, quantity):
   
    if not (1 <= min <=max <= 1_000 and quantity <= (max - min + 1)):
        return []

    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()
    return numbers

user_ticket = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", user_ticket)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Виграшні числа:", lottery_numbers)

matched = set(user_ticket).intersection(lottery_numbers)
print(f"Ви вгадали {len(matched)} чисел: {matched}")


