"""
File: enums.py
Description: Enumerations used in the Campus Café system to define valid options for size, flavour, bean, flour, and item type.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from enum import Enum


# --- Drink Sizes ---
class Size(Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"


# --- Flavours for 'Other' drinks ---
class Flavour(Enum):
    LEMONADE = "Lemonade"
    WATER = "Water"
    COLA = "Cola"


# --- Flavours for Tea drinks ---
class TeaFlavour(Enum):
    EARL_GREY = "Earl Grey"
    GREEN = "Green"
    CHAMOMILE = "Chamomile"
    PEPPERMINT = "Peppermint"
    CHAI = "Chai"


# --- Coffee bean types ---
class Bean(Enum):
    ARABICA = "Arabica"
    ROBUSTA = "Robusta"
    LIBERICA = "Liberica"
    EXCELSA = "Excelsa"


# --- Flour types for Savoury items ---
class Flour(Enum):
    WHOLE = "Whole"
    WHITE = "White"


# --- Item types (used by Sweet and Savoury) ---
class Type(Enum):
    LOAF = "Loaf"
    MUFFIN = "Muffin"
    SLICE = "Slice"
