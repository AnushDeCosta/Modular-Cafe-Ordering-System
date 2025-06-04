"""
File: test_coffee.py
Description: Pytest unit tests for Coffee class in the café system.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import pytest
from enums import Size, Bean
from coffee import Coffee

def test_price_for_excelsa():
    coffee = Coffee(Size.LARGE, True, [Bean.EXCELSA], sugar=1)
    assert coffee.calculate_price() > 0

def test_invalid_bean():
    with pytest.raises(ValueError):
        Coffee(Size.SMALL, False, ["invalid_bean"], sugar=0)

def test_brew_state(sample_coffee):
    assert not sample_coffee.get_ready()
    sample_coffee.brew()
    assert sample_coffee.get_ready()

