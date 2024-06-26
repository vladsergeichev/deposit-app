from datetime import datetime

from pydantic import BaseModel, field_validator


class SDepositParams(BaseModel):
    date: str
    periods: int
    amount: int
    rate: float

    @field_validator("date")
    @classmethod
    def check_date(cls, value: str) -> str:
        # Проверка корректности формата даты
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except:
            raise ValueError("Invalid date format")
        return value
