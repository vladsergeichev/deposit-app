import pytest

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


@pytest.mark.parametrize(
    "content, expected_code, expected_json",
    [
        (
            {"date": "31.01.2021", "periods": 3, "amount": 10000, "rate": 6},
            200,
            {"31.01.2021": 10050, "28.02.2021": 10100.25, "31.03.2021": 10150.75},
        ),
        (
            {"date": "31.01.21", "periods": 3, "amount": 10000, "rate": 6},
            400,
            {"error": "Value error, Invalid date format"},
        ),
        ({"periods": 3, "amount": 10000, "rate": 6}, 400, {"error": "Field required"}),
    ],
)
def test_deposit(content, expected_code, expected_json):
    response = client.post("/deposit", json=content)
    assert response.status_code == expected_code
    assert response.json() == expected_json
