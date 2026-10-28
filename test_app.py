import pytest
from app import app, calculate_total, bills

@pytest.fixture(autouse=True)
def clear_bills():
    bills.clear()
    yield
    bills.clear()

def test_calculate_total_with_discount():
    # Test valid discount calculations
    assert calculate_total(100.0, 1, 10) == 90.00
    # Backward compatibility checking for zero discount
    assert calculate_total(10.50, 2, 0) == 21.00

def test_invalid_discount_boundaries():
    with pytest.raises(ValueError):
        calculate_total(100, 1, 120)
    with pytest.raises(ValueError):
        calculate_total(100, 1, -5)
