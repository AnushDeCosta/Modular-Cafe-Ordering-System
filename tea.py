"""
File: tea.py
Description: Defines the Tea class, a hot or iced drink that allows multiple flavours,
             optional milk and sugar, and supports brewing.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from drink import Drink
from enums import TeaFlavour

# --- Constants for pricing ---
MILK_COST = 0.75
SUGAR_UNIT_COST = 0.25
FLAVOUR_PRICE_ADJUSTMENTS = {
    TeaFlavour.CHAI: 1.00,
    TeaFlavour.EARL_GREY: -3.00,
    TeaFlavour.GREEN: 2.00,
    TeaFlavour.CHAMOMILE: 2.00
}


class Tea(Drink):
    """
    Represents a tea drink sold in the café.
    Inherits from the Drink class and includes flavours, milk, sugar, and readiness.
    """

    BASE_PRICE = 2.00

    def __init__(self, size, cold, flavours, sugar, milk=False, ready=False):
        """
        Initialise a Tea drink object.

        :param size: Size enum (SMALL / MEDIUM / LARGE)
        :param cold: True for iced tea
        :param flavours: list of TeaFlavour enums
        :param sugar: number of sugar units (≥ 0)
        :param milk: add milk (default False)
        :param ready: already brewed? (default False)
        :raises ValueError: for invalid flavour list, milk type, sugar value, or readiness flag
        """
        super().__init__("Tea", 0.00, size, cold)

        if not isinstance(flavours, list) or \
                not all(isinstance(flavour, TeaFlavour) for flavour in flavours):
            raise ValueError("flavours must be a list of TeaFlavour enums")
        if not isinstance(milk, bool):
            raise ValueError("milk must be a boolean")
        if not isinstance(sugar, int) or sugar < 0:
            raise ValueError("sugar must be a non-negative integer")
        if not isinstance(ready, bool):
            raise ValueError("ready must be a boolean")

        self.__flavours = flavours
        self.__milk = milk
        self.__sugar = sugar
        self.__ready = ready

    def brew(self):
        """
        Brew the tea and mark it as ready.
        If already brewed, prints a message and does nothing.
        """
        # Flavour validity was checked during init, assumed safe here

        if self.__ready:
            print("Tea is already brewed!")
            return

        print(f"Brewing your {self}… Done!")
        self.__ready = True

    def add_flavour(self, flavour):
        """
        Adds a TeaFlavour to the drink if not already present.

        :param flavour: A TeaFlavour enum
        :raises ValueError: if input is not a TeaFlavour enum
        """
        if not isinstance(flavour, TeaFlavour):
            raise ValueError("flavour must be a TeaFlavour enum")

        if flavour in self.__flavours:
            print("…already in this tea.")
            return

        self.__flavours.append(flavour)
        print(f"{flavour.value} added to your tea.")

    def remove_flavour(self, flavour):
        """
        Removes a TeaFlavour from the drink if present.

        :param flavour: A TeaFlavour enum
        :raises ValueError: if input is not a TeaFlavour enum
        """
        if not isinstance(flavour, TeaFlavour):
            raise ValueError("flavour must be a TeaFlavour enum")

        if flavour not in self.__flavours:
            print("flavour is not in this tea.")
            return

        self.__flavours.remove(flavour)
        print(f"{flavour.value} removed from your tea.")

    def calculate_price(self):
        """
        Calculates the total price of the tea based on ingredients.

        :return: Float – final price (clamped to 0 if negative)
        """
        milk_price = MILK_COST if self.__milk else 0.00
        sugar_price = SUGAR_UNIT_COST * self.__sugar

        flavour_price = sum(FLAVOUR_PRICE_ADJUSTMENTS.get(f, 0.00) for f in self.__flavours)

        price = (self.BASE_PRICE + milk_price + sugar_price + flavour_price)
        return max(price, 0.00)

    def get_flavours(self):
        """
        Returns the list of TeaFlavour enums currently in the tea.

        :return: List[TeaFlavour]
        """
        return self.__flavours

    def is_ready(self):
        """
        Returns True if the tea has been brewed, False otherwise.

        :return: bool – True if brewed, False otherwise
        """
        return self.__ready

    def has_milk(self):
        """
        Returns True if milk is included in the drink.

        :return: bool – whether the drink contains milk
        """
        return self.__milk

    def get_sugar(self):
        """
        Returns the number of sugar units in the drink.

        :return: int – sugar quantity (≥ 0)
        """
        return self.__sugar

    def __str__(self):
        """
        Returns a readable string representing the tea's description.

        :return: str
        """
        size_text = self.get_size().value
        temp_text = "iced" if self.is_cold() else "hot"
        flavour_names = [flavour.value for flavour in self.__flavours]
        flavour_text = " & ".join(flavour_names)
        extras = []

        if flavour_text:
            extras.append(flavour_text)

        if self.__milk:
            extras.append("milk")
        else:
            extras.append("no milk")

        if self.__sugar > 0:
            sugar_text = f"{self.__sugar} sugar" if self.__sugar == 1 else f"{self.__sugar} sugars"
            extras.append(sugar_text)

        return f"{size_text} {temp_text} tea with {', '.join(extras)} at price - ${self.calculate_price():.2f}"


