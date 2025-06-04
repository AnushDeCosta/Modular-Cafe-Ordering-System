"""
File: test_savoury.py
Description: Pytest unit tests for Savoury class in the café system.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import pytest
from enums import Size, Type, Flour
from savoury import Savoury

def test_price_logic(sample_savoury):
    assert sample_savoury.calculate_price() > 0

def test_invalid_flour_type():
    with pytest.raises(ValueError):
        Savoury(Size.SMALL, Type.MUFFIN, "Coconut")
