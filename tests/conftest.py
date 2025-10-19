"""
File: conftest.py
Description: Shared fixtures for the café system tests.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import pytest
from enums import Size, TeaFlavour, Bean, Flavour, Type, Flour
from tea import Tea
from coffee import Coffee
from other import Other
from sweet import Sweet
from savoury import Savoury

# --- Tea Fixture ---
@pytest.fixture
def sample_tea():
    """
    Returns a sample Tea object with chai flavour, milk, and 1 sugar.
    """
    return Tea(Size.SMALL, False, [TeaFlavour.CHAI], sugar=1, milk=True)

# --- Coffee Fixture ---
@pytest.fixture
def sample_coffee():
    """
    Returns a sample Coffee object with Robusta beans, no milk, no sugar.
    """
    return Coffee(Size.MEDIUM, True, [Bean.ROBUSTA], sugar=0)

# --- Other Drink Fixture ---
@pytest.fixture
def sample_other():
    """
    Returns a sample Other drink with Lemonade flavour and soda.
    """
    return Other(Size.SMALL, True, [Flavour.LEMONADE], soda=True)

# --- Sweet Fixture ---
@pytest.fixture
def sample_sweet():
    """
    Returns a sample Sweet food item (Small Muffin).
    """
    return Sweet(Size.SMALL, Type.MUFFIN)

# --- Savoury Fixture ---
@pytest.fixture
def sample_savoury():
    """
    Returns a sample Savoury food item (Medium Slice with Whole flour).
    """
    return Savoury(Size.MEDIUM, Type.SLICE, Flour.WHOLE)


# Code inspired by: Verma, M. (2021, June 5). *How to use conftest.py in PyTest | Python Pytest Tutorial*. [Video].
# YouTube. https://www.youtube.com/watch?v=PIwyrzCLTCI


