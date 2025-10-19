"""
File: other.py
Description: Defines the Other class for drinks like water, cola, or lemonade.
             Includes soda and cold drink surcharges, and flavour-based price adjustments.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from drink import Drink
from enums import Flavour

# --- Constants for pricing ---
SODA_COST = 0.50
COLD_DRINK_SURCHARGE = 1.00
FLAVOUR_PRICE_ADJUSTMENTS = {
    Flavour.WATER: -3.00,
    Flavour.LEMONADE: 2.00,
    Flavour.COLA: 2.00
}


class Other(Drink):
    """
    Represents any 'Other' drink sold in the café.
    Inherits from the Drink class and includes a soda option and flavour-based pricing.
    """

    BASE_PRICE = 5.00

    def __init__(self, size, cold, flavour, soda=False):
        """
        Initialise an 'Other' drink item with size, temperature, flavour, and soda option.

        :param size: Size enum (SMALL / MEDIUM / LARGE)
        :param cold: Boolean – True if the drink is cold (iced), False if hot
        :param flavour: List containing exactly one Flavour enum
        :param soda: Boolean – True if soda is included (default is False)
        :raises ValueError: for invalid flavour list or soda type
        """
        super().__init__("Other", 0.00, size, cold)

        if not isinstance(flavour, list) or len(flavour) != 1 or not isinstance(flavour[0], Flavour):
            raise ValueError("Flavour must be a list containing exactly one flavour enum")

        self.__flavour = flavour
        self.__soda = soda

    def calculate_price(self):
        """
        Calculates the total price of the drink based on flavor.

        :return: Float – final price (clamped to 0 if negative)
        """
        soda_price = SODA_COST if self.__soda else 0.00
        cold_price = COLD_DRINK_SURCHARGE if self.is_cold() else 0.00
        flavour = self.__flavour[0]
        flavour_price = FLAVOUR_PRICE_ADJUSTMENTS.get(flavour, 0.00)

        price = (self.BASE_PRICE + soda_price + cold_price + flavour_price)
        return max(price, 0.00)

    def get_flavour(self):
        """
        Returns the selected Flavour enum used in this drink.

        :return: Flavour
        """
        return self.__flavour[0]

    def has_soda(self):
        """
        Returns True if the drink includes soda.

        :return: bool – whether soda is added
        """
        return self.__soda

    def __str__(self):
        """
        Returns a readable string representing the drink's description.

        :return: str
        """
        size_text = self.get_size().value
        temp_text = "iced" if self.is_cold() else "hot"
        flavour_text = self.__flavour[0].value
        extras = []

        if self.__soda:
            extras.append("with soda")
        else:
            extras.append("no soda")

        return f"{size_text} {temp_text} {flavour_text} ({', '.join(extras)}) at price - ${self.calculate_price():.2f}"