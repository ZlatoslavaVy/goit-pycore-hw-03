from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users):
    today = date.today()
    result = []
    for user in users:
    
        born = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        candidate = born.replace(year=today.year)
        
        if candidate < today:
            candidate = born.replace(year=today.year + 1)

        delta = (candidate - today).days
        
        if 0 <= delta <= 7:
            
            if candidate.weekday() == 5:
                candidate += timedelta(days=2)
            elif candidate.weekday() == 6:
                candidate += timedelta(days=1)

            result.append({
                "name": user["name"],
                "congratulation_date": candidate.strftime("%Y.%m.%d")
            })

    result.sort(key=lambda x: x["congratulation_date"])

    return result

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

users.append({"name": "Kamelia Grossen", "birthday": "1995.10.27"})


upcoming_birthdays = get_upcoming_birthdays(users)

print("Список привітань на цьому тижні:")
for item in upcoming_birthdays:
    print(f"{item['name']} — {item['congratulation_date']}")



