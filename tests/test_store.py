"""
File: test_store.py
Description: Pytest unit tests for Cafe class in the café system.
             Verifies order creation, profit reporting, and earnings tracking.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import pytest
from store import Cafe

def test_create_order():
    """
    Confirm create_order() appends a new order to the history list.
    """
    cafe = Cafe()
    order = cafe.create_order()
    assert order is not None
    assert len(cafe.get_order_history()) == 1

def test_report_profit_empty_order():
    """
    Ensure report_profit() returns zero when order contains no items.
    """
    cafe = Cafe()
    cafe.create_order()
    assert cafe.report_profit() == 0.00

def test_get_earnings_after_profit_report():
    """
    Validate get_earnings() reflects latest value after report_profit().
    """
    cafe = Cafe()
    cafe.create_order()
    cafe.report_profit()
    assert cafe.get_earnings() == 0.00
