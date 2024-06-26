# deposit-app

### Описание
REST API сервис для расчета депозита.

Пример входных данных
```json
{
  "date": "31.01.2021",
  "periods": 3,
  "amount": 10000,
  "rate": 6
}
```

Пример ответа сервиса
```json
{
  "31.01.2021": 10050,
  "28.02.2021": 10100.25,
  "31.03.2021": 10150.75
}
```
___
### Запуск
Локальный запуск
```commandline
uvicorn main:app --reload
```

Запуск в Docker
```commandline
docker build . -t deposit_app:latest
docker run -d -p 7777:8000 deposit_app
```
___
### Тестирование
Проверка покрытия кода тестами
```commandline
coverage run -m pytest
coverage report
```