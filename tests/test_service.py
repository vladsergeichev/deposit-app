import pytest

from schemas import SDepositParams
from service import calculate_deposit, date_add_months


@pytest.mark.parametrize('date, num_month, expected', [
    ("31.01.2021", 1, "28.02.2021"),
    ("31.01.2021", 2, "31.03.2021"),
    ("30.11.2021", 3, "28.02.2022"),
    ("30.11.2021", 15, "28.02.2023"),
    ("31.12.2021", 26, "29.02.2024"),
])
def test_date_add_months(date, num_month, expected):
    assert date_add_months(date, num_month) == expected


@pytest.mark.parametrize('data, expected', [
    (SDepositParams(
        date="31.01.2021",
        periods=3,
        amount=10000,
        rate=6
    ),
     {
         "31.01.2021": 10050,
         "28.02.2021": 10100.25,
         "31.03.2021": 10150.75
     }),
    (SDepositParams(
        date="31.10.2021",
        periods=5,
        amount=10000,
        rate=3
    ),
     {
         "31.10.2021": 10025,
         "30.11.2021": 10050.06,
         "31.12.2021": 10075.19,
         "31.01.2022": 10100.38,
         "28.02.2022": 10125.63
     }),
])
def test_calculate_deposit(data, expected):
    assert calculate_deposit(data) == expected
