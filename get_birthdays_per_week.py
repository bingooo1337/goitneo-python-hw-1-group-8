from collections import defaultdict
from datetime import datetime, timedelta

users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jeff Bezos", "birthday": datetime(1964, 1, 12)},
    {"name": "Tim Cook", "birthday": datetime(1960, 11, 1)},
    {"name": "Mark Zuckerberg", "birthday": datetime(1984, 5, 14)},
    {"name": "Volodymyr Kamyshanov", "birthday": datetime(1997, 3, 6)},
    {"name": "Birthday_user", "birthday": datetime(2024, 3, 1)},
    {"name": "Birthday_user_same_day", "birthday": datetime(2024, 3, 1)},
    {"name": "Birthday_user_another_day", "birthday": datetime(2024, 2, 28)},
    {"name": "Birthday_user_this_week_but_not_congratulate", "birthday": datetime(2024, 3, 2)},
]

def get_congratulation_day(today, birthday):
    birthday_this_year = birthday.replace(year=today.year)

    congratulation_day = birthday_this_year

    # birthday will be next year
    if (birthday_this_year < today):
        congratulation_day = birthday_this_year.replace(year=today.year + 1)

    weekday = congratulation_day.weekday()
    # 4 - Friday index
    if (weekday > 4):
        # birthday is on weekend, congratulation on next work day
        congratulation_day = congratulation_day + timedelta(days=7 - weekday)

    return congratulation_day


def get_users_to_congratulate(users):
    start = datetime.now().date()
    end = (start + timedelta(days=5))

    users_to_congratulate = defaultdict(list)
    for user in users:
        congratulation_day = get_congratulation_day(
            start,
            user['birthday'].date()
        )

        if (start <= congratulation_day and congratulation_day <= end):
            users_to_congratulate[congratulation_day].append(user['name'])

    return users_to_congratulate


def get_birthdays_per_week(users):
    users_to_congratulate_by_days = get_users_to_congratulate(users)

    for day in sorted(users_to_congratulate_by_days.items()):
        print(f'{day[0].strftime("%A")}: {", ".join(day[1])}')
