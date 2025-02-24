import re
from datetime import datetime, timedelta
from random import randint


# Task 1
def get_days_from_today(date: str) -> int:
    time_format = "%Y-%m-%d"
    try:
        current_date = datetime.today().date()
        user_date = datetime.strptime(date, time_format).date()
        result = current_date - user_date
        return result.days
    except ValueError:
        raise ValueError("Incorrect format of date. Use YYYY-MM-DD")


# Task 2
def validate_ticket_params(min: int, max: int, quantity: int):
    if min < 1 or max > 1000:
        raise ValueError("Choose numbers between 1 and 1000")
    if min > max:
        raise ValueError("Min value cannot be greater than max value")
    if quantity > (max - min + 1):
        raise ValueError("Quantity is too large for the given range")

    return True


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:

    random_numbers = set()

    validate_ticket_params(min, max, quantity)

    while len(random_numbers) < quantity:
        random_numbers.add(randint(min, max))

    return sorted(list(random_numbers))


# Task 3
def normalize_phone_number(phone_number: str) -> str:
    cleaned_number = re.sub(r"[^\d+]", "", phone_number).strip()

    if cleaned_number.startswith("380"):
        return f"+{cleaned_number}"

    if cleaned_number.startswith("+380"):
        return cleaned_number

    if cleaned_number.startswith("0"):
        return f"+38{cleaned_number}"

    return cleaned_number


def get_upcoming_birthdays(users: list):
    birthday_fellas = []
    today = datetime.today().date()
    end_of_week = today + timedelta(days=7)

    for user in users:
        name = user["name"]
        birthday_str = user["birthday"]
        birthday_date = datetime.strptime(birthday_str, "%Y.%m.%d").date()

        birthday_this_year = birthday_date.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if today <= birthday_this_year <= end_of_week:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() in (5, 6):
                congratulation_date += timedelta(days=(7 - congratulation_date.weekday()))

            birthday_fellas.append({
                "name": name,
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return birthday_fellas
