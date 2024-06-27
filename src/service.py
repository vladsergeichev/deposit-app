from calendar import monthrange
from datetime import datetime
from typing import Dict, Union

from schemas import SDepositParams


def date_add_months(string_date: str, num: int) -> str:
    """
    Функция прибавляет N месяцев к дате
    """
    date = datetime.strptime(string_date, "%d.%m.%Y")
    year = date.year
    month = date.month

    # Прибавляем месяцы
    year += num // 12
    lost = num % 12
    if month + lost > 12:
        month += lost - 12
        year += 1
    else:
        month += lost

    # Получаем число дней в месяце
    days_in_month = monthrange(year, month)[1]

    return datetime(year, month, min(date.day, days_in_month)).strftime("%d.%m.%Y")


def calculate_deposit(data: SDepositParams) -> Dict[str, Union[float, int]]:
    """
    Функция рассчитывает депозит
    """
    dates = {}
    amount = data.amount
    print(amount, data.rate)
    for p in range(data.periods):
        amount = amount + amount * (data.rate / 1200)
        dates[date_add_months(data.date, p)] = float(format(amount, ".2f"))
    return dates
