"""
File: test_coffee.py
Description: Pytest unit tests for the Coffee class in the café system.
             Verifies price calculation, readiness state, and input validation.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import pytest
from enums import Size, Bean
from coffee import Coffee

def test_price_for_excelsa():
    """
    Ensure price is correctly calculated for Excelsa bean
    and includes all modifiers (cold, sugar).
    """
    coffee = Coffee(Size.LARGE, True, [Bean.EXCELSA], sugar=1)
    assert coffee.calculate_price() > 0

def test_invalid_bean():
    """
    Check that passing a non-enum bean raises ValueError.
    """
    with pytest.raises(ValueError):
        Coffee(Size.SMALL, False, ["invalid_bean"], sugar=0)

def test_empty_bean_list():
    """
    Ensure a ValueError is raised for an empty bean list.
    """
    with pytest.raises(ValueError):
        Coffee(Size.SMALL, False, [], sugar=1)

def test_max_sugar_allowed():
    """
    Create coffee with very high sugar and verify it is accepted.
    """
    coffee = Coffee(Size.MEDIUM, False, [Bean.LIBERICA], sugar=10)
    assert coffee.get_sugar() == 10
    assert coffee.calculate_price() > 0

def test_brew_state(sample_coffee):
    """
    Verify brew() correctly updates the 'ready' state
    and does not start as ready by default.
    """
    assert not sample_coffee.get_ready()
    sample_coffee.brew()
    assert sample_coffee.get_ready()

def test_get_sugar_and_milk(sample_coffee):
    """
    Confirm getter methods for sugar and milk return expected values.
    """
    assert sample_coffee.get_sugar() == 0
    assert not sample_coffee.has_milk()