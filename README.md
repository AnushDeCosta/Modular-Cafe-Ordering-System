# Advanced Programming OOP Assessment

![Image](https://github.com/user-attachments/assets/883b6998-3a1a-4a7c-8771-5dc8f95aa995)

## Summary
**Advanced Programming OOP Assessment** is a Python project demonstrating the use of advanced object-oriented programming concepts to simulate a modular café ordering system. It incorporates abstract classes, inheritance, encapsulation, and test-driven development with Pytest, as well as a focus on clean design and modularity.

## Introduction
This assessment models a café environment that supports customisable drink and food orders:

- **Abstraction & Inheritance**: Base classes like `Item`, `Drink`, and `Food` are extended by specialised classes such as `Tea`, `Coffee`, `Sweet`, and `Savoury`.
- **Composition & Aggregation**: The `Cafe` class handles orders and manages internal state, delegating behaviour to items.
- **Encapsulation**: Private attributes and setter/getter methods enforce data integrity.
- **Test-Driven Development**: Pytest is used to validate core logic, edge cases, helper methods, and price calculations.
- **UML Compliance**: All classes and methods implemented according to the provided UML diagram.

> **Note:** The implementation adheres closely to the provided UML and programming standards.

## Project Features
- **Customisable Orders**: Customers can build drinks (e.g. `Tea`, `Coffee`, `Other`) and food items with dynamic components.
- **Cafe Management**: The `Cafe` class handles multiple orders and tracks total revenue.
- **Item Pricing**: All price logic follows the assignment's guidelines, with multipliers based on attributes.
- **Error Handling**: Input validation ensures users cannot create invalid or contradictory orders.
- **Debugging Log**: All issues, resolutions, and test cases are documented in `debugginglog.md`.
- **Helper Methods**: Added methods like `has_milk()`, `get_sugar()`, `get_total_price()`, and `get_earnings()` to support output formatting and testing.

## Core Mechanics
- **Item**: Abstract class for all products, with enforced implementation of `get_price()` and `__str__()`.
- **Drink**: Adds shared drink attributes like size and milk. Subclasses define specific logic (e.g., bean vs. flavour).
- **Food**: Handles base food logic. Subclasses like `Sweet` and `Savoury` apply flour and type multipliers.
- **Order**: Collects `Item` objects and calculates total cost.
- **Cafe**: Manages all orders, tracks cumulative profits, and summarises completed orders.

## Output Formatting
- **Console Messages**: Clear and descriptive outputs from `__str__()` methods.
- **Pytest Output**: Structured test feedback with edge case coverage.
- **Summary Reports**: Orders and revenue are presented in clean, readable summaries.

## Testing
- Full unit testing using `pytest`
- 33 test cases, including edge cases (e.g. invalid enums, empty lists, boundary sugar values)
- Fixtures defined in `conftest.py` for reuse and consistency

## Tools
- **Language**: Python 3.13+  
- **IDE**: PyCharm  
- **Testing**: Pytest  
- **Version Control**: Git & GitHub

## File Overview
- **item.py**: Abstract base class for all products
- **drink.py**, **tea.py**, **coffee.py**, **other.py**: Drink types
- **food.py**, **savoury.py**, **sweet.py**: Food categories
- **order.py**: Collects items and calculates totals
- **store.py**: Implements `Cafe` class for order handling
- **enums.py**: Contains constants like `Size`, `Flavour`, `Type`, and `Flour`
- **main.py**: Demo script for running sample orders (optional)
- **debugginglog.md**: Issue tracking and resolution documentation
- **README.md**: Project overview

## Usage
To run the sample script (if implemented), use the following steps:

1. Open a terminal.
2. Navigate to the project root directory.
3. Run the main demo:
```bash
python main.py
```

To run tests:
```bash
pytest
```

## Future Enhancements
- Implement persistence using CSV or SQLite for order history.
- Add a user interface (GUI or CLI) for live ordering.
- Extend logic to include promotional discounts and allergy flags.

## Acknowledgements
Thank you to the UniSA teaching team for feedback and structure. This assessment was built using the guidelines, UML, and example formats provided throughout the course.

- The debugging journal format was inspired by Alexandra Berdashkevich, used with permission from the teaching team.
- Banner image generated using OpenAI’s image tool.

This code is submitted for the UniSA Bachelor of Data Analytics course as part of Assignment 2.  
© 2025 Anush De Costa
