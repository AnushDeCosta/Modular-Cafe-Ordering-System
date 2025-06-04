"""
File: test_order.py
Description: Pytest unit tests for Order class in the café system.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import pytest
from order import Order
from tea import Tea
from enums import Size, TeaFlavour

@pytest.fixture
def simple_order():
    order = Order()
    tea = Tea(Size.SMALL, False, [TeaFlavour.CHAI], sugar=1)
    order.add_item_to_order(tea)
    return order

def test_order_add_and_total(simple_order):
    assert simple_order.calculate_price() > 0

def test_order_remove_item(simple_order):
    item = simple_order.get_items()[0]
    simple_order.remove_item_from_order(item)
    assert simple_order.calculate_price() == 0.0

def test_get_total_price(simple_order):
    assert simple_order.get_total_price() == simple_order.calculate_price()
