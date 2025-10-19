"""
File: test_tea.py
Description: Pytest unit tests for the Tea class in the café system.
             Verifies flavour handling, brew logic, sugar/milk settings, and input validation.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import pytest
from enums import Size, TeaFlavour
from tea import Tea


def test_price_with_multiple_flavours():
    """Check price calculation with multiple tea flavours, sugar, and milk."""
    tea = Tea(Size.MEDIUM, False, [TeaFlavour.CHAI, TeaFlavour.GREEN], sugar=2, milk=True)
    assert tea.calculate_price() > 0


def test_brewing(sample_tea):
    """Verify that brew() sets readiness to True and does not start brewed."""
    assert not sample_tea.is_ready()
    sample_tea.brew()
    assert sample_tea.is_ready()


def test_add_remove_flavour(sample_tea):
    """Test that flavours can be added and removed correctly."""
    sample_tea.add_flavour(TeaFlavour.PEPPERMINT)
    assert TeaFlavour.PEPPERMINT in sample_tea.get_flavours()

    sample_tea.remove_flavour(TeaFlavour.CHAI)
    assert TeaFlavour.CHAI not in sample_tea.get_flavours()


def test_invalid_flavour_type():
    """Ensure ValueError is raised when non-enum is passed as a flavour."""
    with pytest.raises(ValueError):
        Tea(Size.SMALL, False, ["string not enum"], sugar=1)


def test_get_sugar_and_milk(sample_tea):
    """Check getter methods for sugar and milk return expected values."""
    assert sample_tea.get_sugar() == 1
    assert sample_tea.has_milk() is True


def test_empty_flavour_list():
    """Edge case: test Tea with no flavours added."""
    tea = Tea(Size.SMALL, False, [], sugar=0)
    assert tea.get_flavours() == []
    assert tea.calculate_price() == 2.00  # Only base price should apply
