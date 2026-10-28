import pytest
from app import app, calculate_total, bills

@pytest.fixture(autouse=True)
def clear_bills():
    bills.clear()
    yield
    bills.clear()

def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Shopping Bill Calculator" in response.data

def test_calculate_total_valid():
    assert calculate_total(10.50, 2) == 21.00
    assert calculate_total(0, 5) == 0.0

def test_calculate_total_negative_values():
    with pytest.raises(ValueError):
        calculate_total(-10, 2)
