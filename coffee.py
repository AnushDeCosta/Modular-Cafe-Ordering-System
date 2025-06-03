"""
File: coffee.py
Description: Coffee subclass with extra shots and milk options.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from drink import Drink
from enums import Bean


class Coffee(Drink):
    """
    Represents a coffee drink sold in the café.
    Inherits from the Drink class and includes sugar, extra shots, milk, and readiness.
    """

    BASE_PRICE = 3

    def __init__(self, size, cold, beans, sugar, milk=False, ready=False):
        """
        Initialise a Coffee drink object.

        :param size: Size enum (SMALL / MEDIUM / LARGE)
        :param cold: True for iced coffee
        :param beans: list of Bean enums
        :param sugar: number of sugar units (≥ 0)
        :param milk: add milk (default False)
        :param ready: already brewed? (default False)
        """
        super().__init__("Coffee", 0.0, size, cold)

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
        milk_price = 0.75 if self.__milk else 0.00
        sugar_price = 0.25 * self.__sugar

        bean_price = 0.00
        bean = self.__beans[0]
        if bean == Bean.ARABICA:
            bean_price -= 3
        elif bean == Bean.ROBUSTA:
            bean_price += 2
        elif bean == Bean.LIBERICA:
            bean_price += 2
        elif bean == Bean.EXCELSA:
            bean_price += 3

        price = (self.BASE_PRICE + milk_price + sugar_price + bean_price)
        return max(price, 0.00)

    def get_bean(self):
        """
        Returns the selected Bean enum used in this coffee.

        :return: Bean
        """
        return self.__beans[0]

    def __str__(self):
        """
        Returns a readable string representing the coffee's description.

        :return: str
        """
        size_text = self.get_size().value
        temp_text = "iced" if self.is_cold() else "hot"
        bean_text = self.__beans[0].value
        extras = [bean_text]

        if self.__milk:
            extras.append("milk")
        else:
            extras.append("no milk")

        if self.__sugar > 0:
            sugar_text = f"{self.__sugar} sugar" if self.__sugar == 1 else f"{self.__sugar} sugars"
            extras.append(sugar_text)

        return f"{size_text} {temp_text} coffee with {', '.join(extras)}"


"""
File: coffee.py
Description: Coffee subclass with extra shots and milk options.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from drink import Drink
from enums import Bean


class Coffee(Drink):
    """
    Represents a coffee drink sold in the café.
    Inherits from the Drink class and includes sugar, extra shots, milk, and readiness.
    """

    BASE_PRICE = 3

    def __init__(self, size, cold, beans, sugar, milk=False, ready=False):
        """
        Initialise a Coffee drink object.

        :param size: Size enum (SMALL / MEDIUM / LARGE)
        :param cold: True for iced coffee
        :param beans: list of Bean enums
        :param sugar: number of sugar units (≥ 0)
        :param milk: add milk (default False)
        :param ready: already brewed? (default False)
        """
        super().__init__("Coffee", 0.0, size, cold)

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
        milk_price = 0.75 if self.__milk else 0.00
        sugar_price = 0.25 * self.__sugar

        bean_price = 0.00
        bean = self.__beans[0]
        if bean == Bean.ARABICA:
            bean_price -= 3
        elif bean == Bean.ROBUSTA:
            bean_price += 2
        elif bean == Bean.LIBERICA:
            bean_price += 2
        elif bean == Bean.EXCELSA:
            bean_price += 3

        price = (self.BASE_PRICE + milk_price + sugar_price + bean_price)
        return max(price, 0.00)

    def get_bean(self):
        """
        Returns the selected Bean enum used in this coffee.

        :return: Bean
        """
        return self.__beans[0]

    def __str__(self):
        """
        Returns a readable string representing the coffee's description.

        :return: str
        """
        size_text = self.get_size().value
        temp_text = "iced" if self.is_cold() else "hot"
        bean_text = self.__beans[0].value
        extras = [bean_text]

        if self.__milk:
            extras.append("milk")
        else:
            extras.append("no milk")

        if self.__sugar > 0:
            sugar_text = f"{self.__sugar} sugar" if self.__sugar == 1 else f"{self.__sugar} sugars"
            extras.append(sugar_text)

        return f"{size_text} {temp_text} coffee with {', '.join(extras)}"

