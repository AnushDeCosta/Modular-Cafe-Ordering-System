"""
File: tea.py
Description: Tea subclass with flavours, milk, sugar, and brew().
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from drink import Drink
from enums import TeaFlavour

class Tea(Drink):
    """
    Represents a tea drink sold in the café.
    Inherits from the Drink class and includes flavours, milk, sugar, and readiness.
    """

    BASE_PRICE = 2

    def __init__(self, size, cold, flavours, sugar, milk=False, ready=False):
        """
        Initialise a Tea drink object.

        :param size: Size enum (SMALL / MEDIUM / LARGE)
        :param cold: True for iced tea
        :param flavours: list of TeaFlavour enums
        :param sugar: number of sugar units (≥ 0)
        :param milk: add milk (default False)
        :param ready: already brewed? (default False)
        """
        super().__init__("Tea", 0.0, size, cold)

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
        milk_price = 0.75 if self.__milk else 0.00
        sugar_price = 0.25 * self.__sugar

        flavour_price = 0.00
        for flavour in self.__flavours:
            if flavour == TeaFlavour.CHAI:
                flavour_price += 1
            elif flavour == TeaFlavour.EARL_GREY:
                flavour_price -= 3
            elif flavour == TeaFlavour.GREEN:
                flavour_price += 2
            elif flavour == TeaFlavour.CHAMOMILE:
                flavour_price += 2

        price = (self.BASE_PRICE + milk_price + sugar_price + flavour_price)
        return max(price, 0.0)

    def get_flavours(self):
        """
        Returns the list of TeaFlavour enums currently in the tea.

        :return: List[TeaFlavour]
        """
        return self.__flavours

    def is_ready(self):
        """
        Returns True if the tea has been brewed, False otherwise.

        :return: Boolean
        """
        return self.__ready

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

        return f"{size_text} {temp_text} tea with {', '.join(extras)}"
