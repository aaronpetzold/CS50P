# --- test_project.py ---


import pytest
from datetime import date
from Week_9.Final_Project.projectFinal_Project.project import calculate_profit_loss, get_sell_price_api, get_price_from_csv


def test_calculate_profit_loss():
    # Profit
    profit, roi = calculate_profit_loss(50000, 75000, 1000)
    assert profit == 500
    assert roi == 50

    # Loss
    profit, roi = calculate_profit_loss(50000, 25000, 1000)
    assert profit == -500
    assert roi == -50


def test_get_price_from_csv():
    assert get_price_from_csv(date(2010,1,1), "nonexistent.csv") is None


def test_get_sell_price_api():
    price = get_sell_price_api()
    assert price is None or isinstance(price, float)