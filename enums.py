"""
File: enums.py
Description: Enumerations for size, flavour, bean, type, and flour based on UML.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from enum import Enum


class Size(Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"


class Flavour(Enum):
    LEMONADE = "Lemonade"
    WATER = "Water"
    COLA = "Cola"


class TeaFlavour(Enum):
    EARL_GREY = "Earl Grey"
    GREEN = "Green"
    CHAMOMILE = "Chamomile"
    PEPPERMINT = "Peppermint"
    CHAI = "Chai"


class Bean(Enum):
    ARABICA = "Arabica"
    ROBUSTA = "Robusta"
    LIBERICA = "Liberica"
    EXCELSA = "Excelsa"


class Flour(Enum):
    WHOLE = "Whole"
    WHITE = "White"


class Type(Enum):
    LOAF = "Loaf"
    MUFFIN = "Muffin"
    SLICE = "Slice"
