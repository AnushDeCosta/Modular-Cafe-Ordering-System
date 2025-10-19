"""
File: test_savoury.py
Description: Pytest unit tests for Savoury class in the café system.
             Tests price calculation, enum validation, and price consistency.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import pytest
from enums import Size, Type, Flour
from savoury import Savoury

def test_price_logic(sample_savoury):
    """
    Ensure calculated price is greater than zero for valid input.
    """
    assert sample_savoury.calculate_price() > 0

def test_invalid_flour_type():
    """
    Raise error when flour is not a valid enum.
    """
    with pytest.raises(ValueError):
        Savoury(Size.SMALL, Type.MUFFIN, "Coconut")

def test_get_price_matches_calculate_price(sample_savoury):
    """
    Confirm get_price delegates to calculate_price correctly.
    """
    assert sample_savoury.get_price() == sample_savoury.calculate_price()

def test_invalid_type_enum():
    """
    Raise error when type is not from the Type enum.
    """
    with pytest.raises(ValueError):
        Savoury(Size.LARGE, "Roll", Flour.WHOLE)

def test_flour_edge_case_unexpected_enum():
    """
    Accept default multiplier if flour is an unused enum value.
    """
    savoury = Savoury(Size.SMALL, Type.SLICE, Flour.WHITE)
    assert savoury.calculate_price() == 1.0  # 2.0 base × 0.5 × 1.0

def test_zero_price_with_missing_multipliers():
    """
    Validate fallback logic with unlisted multipliers still results in valid price.
    """
    savoury = Savoury(Size.SMALL, Type.SLICE, Flour.WHITE)
    assert savoury.calculate_price() >= 0.0
