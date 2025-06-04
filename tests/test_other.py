"""
File: test_other.py
Description: Pytest unit tests for Other drink class in the café system.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import pytest
from enums import Size, Flavour
from other import Other

def test_price_with_soda_and_cold(sample_other):
    assert sample_other.calculate_price() == 8.5

def test_invalid_flavour_type():
    with pytest.raises(ValueError):
        Other(Size.SMALL, True, [123], soda=False)

def test_has_soda(sample_other):
    assert sample_other.has_soda() is True
