from datetime import datetime


def get_days_from_today(date):
    try:
        set_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("You have specified an incorrect date format.")
        return None
    current_date = datetime.today()     
    days_difference = current_date - set_date
    return days_difference.days
print(get_days_from_today("2025-10-10")) #correct
print(get_days_from_today("10-10-2025")) #incorrect