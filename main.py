from datetime import datetime
from get_birthdays_per_week import get_birthdays_per_week

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


get_birthdays_per_week(users)
