"""
File: test_tea.py
Description: Pytest unit tests for Tea class in the café system.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import pytest
from enums import Size, TeaFlavour
from tea import Tea

def test_price_with_multiple_flavours():
    tea = Tea(Size.MEDIUM, False, [TeaFlavour.CHAI, TeaFlavour.GREEN], sugar=2, milk=True)
    assert tea.calculate_price() > 0

def test_brewing(sample_tea):
    assert not sample_tea.is_ready()
    sample_tea.brew()
    assert sample_tea.is_ready()

def test_add_remove_flavour(sample_tea):
    sample_tea.add_flavour(TeaFlavour.PEPPERMINT)
    assert TeaFlavour.PEPPERMINT in sample_tea.get_flavours()
    sample_tea.remove_flavour(TeaFlavour.CHAI)
    assert TeaFlavour.CHAI not in sample_tea.get_flavours()

def test_invalid_flavour_type():
    with pytest.raises(ValueError):
        Tea(Size.SMALL, False, ["string not enum"], sugar=1)
