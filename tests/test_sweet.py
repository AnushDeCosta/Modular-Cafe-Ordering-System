"""
File: test_sweet.py
Description: Pytest unit tests for Sweet class in the café system.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import pytest
from enums import Size, Type
from sweet import Sweet

def test_price_for_slice(sample_sweet):
    assert sample_sweet.calculate_price() == 2.0

def test_invalid_type():
    with pytest.raises(ValueError):
        Sweet(Size.SMALL, "cake")
