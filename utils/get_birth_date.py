import random


def get_birth_date() -> tuple:
    month_map = {
        "January": 31, "February": 28, "March": 31,
        "April": 30, "May": 31, "June": 30,
        "July": 31, "August": 31, "September": 30,
        "October": 31, "November": 30, "December": 31
    }
    month: str = random.choice(list(month_map.keys()))
    year: str = str(random.randint(1900, 2100))
    day: str = str(random.randint(1, month_map[month] + (
        1 if month == "February" and (
                    (int(year) % 4 == 0 and int(year) % 100 != 0) or (int(year) % 400 == 0)) else 0))).rjust(2, "0")
    return day, month, year