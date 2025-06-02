"""
File: item.py
Description: Abstract class for all items. Defines name, price, and calculate_price().
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""


from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def calculate_price(self):
        pass
