"""
File: test_sweet.py
Description: Pytest unit tests for Sweet class in the café system.
             Tests price calculation, validation of type input, and getter accuracy.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import pytest
from enums import Size, Type
from sweet import Sweet

def test_price_for_slice(sample_sweet):
    """
    Verify that price for a small sweet slice matches expected value.
    """
    assert sample_sweet.calculate_price() == 2.0

def test_invalid_type():
    """
    Ensure ValueError is raised if type is not a valid Type enum.
    """
    with pytest.raises(ValueError):
        Sweet(Size.SMALL, "cake")

def test_get_price_matches_calculate_price(sample_sweet):
    """
    Confirm get_price() returns the same value as calculate_price().
    """
    assert sample_sweet.get_price() == sample_sweet.calculate_price()
