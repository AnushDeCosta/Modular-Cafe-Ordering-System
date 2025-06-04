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

@pytest.fixture
def sample_tea():
    return Tea(Size.SMALL, False, [TeaFlavour.CHAI], sugar=1, milk=True)

@pytest.fixture
def sample_coffee():
    return Coffee(Size.MEDIUM, True, [Bean.ROBUSTA], sugar=0)

@pytest.fixture
def sample_other():
    return Other(Size.SMALL, True, [Flavour.LEMONADE], soda=True)

@pytest.fixture
def sample_sweet():
    return Sweet(Size.SMALL, Type.MUFFIN)

@pytest.fixture
def sample_savoury():
    return Savoury(Size.MEDIUM, Type.SLICE, Flour.WHOLE)

# Code inspired by: Verma, M. (2021, June 5). *How to use conftest.py in PyTest | Python Pytest Tutorial*. [Video].
# YouTube. https://www.youtube.com/watch?v=PIwyrzCLTCI


