"""
File: test_other.py
Description: Pytest unit tests for Other drink class in the café system.
             Covers price calculation, soda check, and flavour input validation.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import pytest
from enums import Size, Flavour
from other import Other

def test_price_with_soda_and_cold(sample_other):
    """
    Check correct price when soda is added and drink is cold.
    Expected: Base + soda + cold + flavour
    """
    assert sample_other.calculate_price() == 8.5

def test_invalid_flavour_type():
    """
    Raise error when invalid non-enum flavour is provided.
    """
    with pytest.raises(ValueError):
        Other(Size.SMALL, True, [123], soda=False)

def test_has_soda(sample_other):
    """
    Confirm the soda attribute reflects correct state.
    """
    assert sample_other.has_soda() is True

def test_price_without_soda_and_cold():
    """
    Check price without soda and cold options. Only base + flavour.
    """
    drink = Other(Size.SMALL, False, [Flavour.LEMONADE], soda=False)
    assert drink.calculate_price() == 7.0  # 5.0 base + 2.0 lemonade

def test_multiple_flavours_raises_error():
    """
    Raise error if more than one flavour is passed.
    """
    with pytest.raises(ValueError):
        Other(Size.SMALL, True, [Flavour.COLA, Flavour.WATER], soda=True)

def test_empty_flavour_list():
    """
    Raise error if flavour list is empty.
    """
    with pytest.raises(ValueError):
        Other(Size.MEDIUM, False, [], soda=False)
