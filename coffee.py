"""
File: coffee.py
Description: Defines the Coffee class, a hot or iced drink made with a single bean type.
             Supports optional milk and sugar, and includes logic for brewing and price calculation.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from drink import Drink
from enums import Bean

# --- Constants for pricing ---
MILK_COST = 0.75
SUGAR_UNIT_COST = 0.25
BEAN_PRICE_ADJUSTMENTS = {
    Bean.ARABICA: -3.00,
    Bean.ROBUSTA: 2.00,
    Bean.LIBERICA: 2.00,
    Bean.EXCELSA: 3.00
}


class Coffee(Drink):
    """
    Represents a coffee drink sold in the café.
    Inherits from the Drink class and includes sugar, milk, and readiness.
    """

    BASE_PRICE = 3.00

    def __init__(self, size, cold, beans, sugar, milk=False, ready=False):
        """
        Initialise a Coffee drink object.

        :param size: Size enum (SMALL / MEDIUM / LARGE)
        :param cold: True for iced coffee
        :param beans: list of Bean enums
        :param sugar: number of sugar units (≥ 0)
        :param milk: add milk (default False)
        :param ready: already brewed? (default False)
        :raises ValueError: for invalid bean list, milk type, sugar value, or readiness flag
        """
        super().__init__("Coffee", 0.00, size, cold)

        if not isinstance(beans, list) or len(beans) != 1 or not isinstance(beans[0], Bean):
            raise ValueError("beans must be a list containing exactly one Bean enum")
        if not isinstance(milk, bool):
            raise ValueError("milk must be a boolean")
        if not isinstance(sugar, int) or sugar < 0:
            raise ValueError("sugar must be a non-negative integer")
        if not isinstance(ready, bool):
            raise ValueError("ready must be a boolean")

        self.__beans = beans
        self.__milk = milk
        self.__sugar = sugar
        self.__ready = ready

    def brew(self):
        """
        Brew the coffee and mark it as ready.
        If already brewed, prints a message and does nothing.
        """
        # Flavour validity was checked during init, assumed safe here

        if self.__ready:
            print("Coffee is already brewed!")
            return

        print(f"Brewing your {self}… Done!")
        self.__ready = True

    def calculate_price(self):
        """
        Calculates the total price of the coffee based on ingredients.

        :return: Float – final price (clamped to 0 if negative)
        """
        milk_price = MILK_COST if self.__milk else 0.00
        sugar_price = SUGAR_UNIT_COST * self.__sugar
        bean = self.__beans[0]
        bean_price = BEAN_PRICE_ADJUSTMENTS.get(bean, 0.00)

        price = self.BASE_PRICE + milk_price + sugar_price + bean_price
        return max(price, 0.00)

    def get_bean(self):
        """
        Returns the selected Bean enum used in this coffee.

        :return: Bean
        """
        return self.__beans[0]

    def get_ready(self):
        """
        Returns the readiness state of the coffee (i.e., whether it has been brewed).

        :return: True if brewed, False otherwise
        :rtype: bool
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
        Returns a readable string describing the coffee, including size, temperature,
        bean type, milk/sugar preferences, and final price.

        :return: str
        """
        size_text = self.get_size().value
        temp_text = "iced" if self.is_cold() else "hot"
        bean_text = self.__beans[0].value
        extras = [bean_text]

        extras.append("milk" if self.__milk else "no milk")

        if self.__sugar > 0:
            sugar_text = f"{self.__sugar} sugar" if self.__sugar == 1 else f"{self.__sugar} sugars"
            extras.append(sugar_text)

        return f"{size_text} {temp_text} coffee with {', '.join(extras)} at price - ${self.calculate_price():.2f}"


