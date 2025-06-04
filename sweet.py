"""
File: sweet.py
Description: Sweet food subclass with type only.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from food import Food
from enums import Type


class Sweet(Food):
    """
        Represents a sweet food item sold in the café.
        Inherits from the Food class and includes only types.
        """
    BASE_PRICE = 2.00

    def __init__(self, size, type):
        """
        Initialise a Sweet food object.

        :param size: Size enum (SMALL / MEDIUM / LARGE)
        :param type: Type enum (LOAF / MUFFIN / SLICE)
        """
        super().__init__("Sweet", 0.00, size)

        if not isinstance(type, Type):
            raise ValueError("food_type must be a member of the Type enum")

        self.__type = type

    def calculate_price(self):
        """
        Calculates the total price of the sweet food item based on type.

        :return: Float – final price
        """
        if self.__type == Type.LOAF:
            type_multiplier = 3
        elif self.__type == Type.MUFFIN:
            type_multiplier = 1
        elif self.__type == Type.SLICE:
            type_multiplier = 0.5
        else:
            type_multiplier = 1

        price = self.BASE_PRICE * type_multiplier
        return round(price, 2)

    def get_type(self):
        """
        Returns the selected Type enum used in this sweet food item.

        :return: Type
        """
        return self.__type

    def __str__(self):
        """
        Returns a readable string describing the Sweet item, including type,
        size and calculated price.

        :return: str
        """
        size_text = self.get_size().value
        type_text = self.__type.value
        price = self.calculate_price()

        return f"Sweet {size_text} {type_text} at price - ${price:.2f}"
