> **Acknowledgement**: This debugging journal’s structure was inspired by a format shared by Alexandra Berdashkevich, with permission from the teaching team.

# Issue #1: Creating scaffold for all classes based on UML

**Status: Resolved**

**File(s) Affected:** item.py, drink.py, tea.py, coffee.py, other.py, food.py, savoury.py, sweet.py, order.py, store.py, enums.py, test_items.py  
**Commit (Noticed):** _N/A – Initial setup phase_  
**Commit (Resolved):** Update #1 - Created class file structure based on UML (`c20d1a1`)

### Error code and Description

There wasn’t an actual error thrown, but this step was essential to prevent future confusion. The entire café system’s class structure needed to reflect the UML and assessment brief from the beginning. This included ensuring:
- File naming matched class roles
- Relationships (like inheritance) were scaffolded correctly
- `Cafe` (not in UML) was added to `store.py` as per brief and forum guidance

Expected:
- One `.py` file per class and enum shown in the UML
- COMP1048-compliant headers in all files
- Classes defined with correct names and placeholder bodies
- Structure ready for testing, logic, and Pytest setup

Actual (if not fixed):
- Without this structure, logic could end up misplaced
- Missing files or inconsistent naming would make the system harder to scale or test later
- UML deviations (like Cafe) would go undocumented

### Resolution Log

- Created 12 total `.py` files based on UML and brief:
  - Abstract/base classes: `item.py`, `drink.py`, `food.py`
  - Subclasses: `tea.py`, `coffee.py`, `other.py`, `savoury.py`, `sweet.py`
  - Management: `order.py`, `store.py`
  - Supporting enums: `enums.py`
  - Test starter: `test_items.py`
- Inserted COMP1048-standard headers into each file
- Declared class names and parent relationships (e.g. `Drink(Item)`)
- Used `pass` or placeholder methods where needed
- Added `Cafe` to `store.py` to handle order history and total earnings (brief requirement)
- Confirmed structure with clean commit: `c20d1a1`

# Issue #2: Implemented Item constructor with validation

**Status:** Resolved  
**File(s) Affected:** item.py  
**Commit (Noticed):** Update #1 - Created class file structure based on UML (`c20d1a1`)  
**Commit (Resolved):** Update #2 - Implemented Item class logic (`c29bcb1`)

### Error code and Description

No error occurred during testing, but I identified a potential risk: future bugs could arise if item names or prices were invalid. 
Since all menu items inherit from Item, I decided to add validation up front in the constructor.

Expected:
- Name should be a non-empty string
- Price should be a non-negative float

Actual (if not fixed):
- Code could crash later or show incorrect prices if invalid data slipped through

### Resolution Log

- Added `__init__()` to `Item` with checks for valid name and price
- Raised `ValueError` on invalid inputs
- Added getter methods for `__name` and `__price`
- Confirmed class builds successfully and will enforce checks for all subclasses

# Issue #3: Implemented Drink class with validation and base preparation logic

**Status:** Resolved

**File(s) Affected:** drink.py  
**Commit (Noticed):** Update #2 - Implemented Item class logic (`c29bcb1`)
**Commit (Resolved):** Update #3 - Updated drink.py (`9c93fc9`)

### Error code and Description

There was no specific error during implementation, but I needed to ensure that `Drink` correctly handled two key attributes: `size` and `cold`. 
These are unique to drinks and required validation based on the UML and course requirements.

Expected:
- Ensure only valid `Size` enum values are accepted
- Prevent invalid `cold` inputs (like strings or integers)
- Make sure the `prepare()` method gives a clear, override-friendly message

Actual (if not handled):
- Invalid enum or boolean values could slip in and cause subtle bugs in subclasses
- `prepare()` wouldn’t produce helpful output or be easily overridden

### Resolution Log

- Created the `Drink` class inheriting from `Item`
- Added `__size` and `__cold` with validation in `__init__()`
- Used `isinstance()` to enforce clean enum and bool types
- Implemented `prepare()` with dynamic size and name formatting
- Added getters `get_size()` and `is_cold()` to support subclass logic

# Issue #4: Implemented Tea class with full logic and pricing

**Status:** Resolved

**File(s) Affected:** tea.py, drink.py, item.py  
**Commit (Noticed):** N/A – New class implementation  
**Commit (Resolved):** Update #4 - Updated tea.py, item.py and drink.py (`7e40952`)

### Error code and Description

No specific error occurred, but the implementation involved interpreting a number of design decisions from the UML. In particular:
- The UML listed `flavours: teaFlavour[]`, which in real life wouldn't make sense to allow multiple, but had to be implemented as a list to follow the diagram.
- Care was needed to validate inputs (milk, sugar, ready, flavours) without breaking constructor logic.
- Price calculation involved both additive and subtractive adjustments and had to be clamped to $0.

Expected:
- Tea class should correctly inherit from Drink and match the UML attributes and methods
- All pricing logic for flavours (including Earl Grey's -$3) handled safely
- Methods like `brew()`, `add_flavour()` and `remove_flavour()` should handle edge cases (e.g., duplicates)

Actual (if not fixed):
- Multiple flavours could break display logic or cause pricing errors
- Users could add duplicates or remove non-existent flavours
- Price could drop below 0 without clamping

### Resolution Log

- Implemented `__init__()` with full validation for all attributes
- Wrote `brew()` method with size, temperature and joined flavour output
- Added `add_flavour()` and `remove_flavour()` with enum type checks and duplication handling
- Implemented `calculate_price()` with per-flavour adjustments and clamping at $0.00
- Created getters `get_flavours()` and `is_ready()` for private attribute access
- All docstrings were rewritten to match COMP1048 standards

### What I Learned

- How to work with enums in a list, and extract their `.value` strings for printing
- That UML design overrides real-world intuition in assignments
- How to structure price logic with edge case protections
- The importance of defensive programming and clean error messages

# Issue #5: Finalised Tea class with __str__, price logic, and full validation

**Status:** Resolved  
**File(s) Affected:** tea.py 
**Commit (Noticed):** Update #4 - Updated tea.py, item.py and drink.py (`7e40952`)
**Commit (Resolved):** Update #5 – Finalised tea.py (`858ae3b`)

### Problem

The Tea class needed a complete implementation:
- The UML required handling of multiple flavours, milk, sugar, and readiness.
- Printing was embedded across methods; needed to switch to __str__ for clean output.
- Pricing logic had to include both additive and negative values (e.g., Earl Grey -$3).
- Missing return in calculate_price() and improper constants usage (hardcoded `2`).

### Fix Summary

- Added class constant `BASE_PRICE = 2` for clarity and reusability
- Updated `calculate_price()` to include all pricing rules and use `max(..., 0.0)`
- Rewrote `__str__()` to return dynamic, realistic café-style descriptions
- Used `self` in `brew()` print output for consistency and clarity
- Kept user-relevant print statements for add/remove flavour methods
- Confirmed that `get_flavours()` and `is_ready()` work as expected for testing

### What I Learned

- How to use `__str__` to replace print-based outputs for cleaner testing
- The importance of clamping price and checking enums in lists
- That docstring consistency across methods improves readability and compliance

# Issue #6: Implemented Coffee class with bean validation, pricing, and __str__ output

**Status:** Resolved  
**File(s) Affected:** coffee.py  
**Commit (Noticed):** N/A – New class implementation 
**Commit (Resolved):** Update #6 – Updated coffee.py (`a25c292`)

### Description and Rationale

- Implemented `Coffee` class as a subclass of `Drink`, with attributes: `beans`, `milk`, `sugar`, and `ready`.
- Although the UML specifies `beans: bean[]`, no `add_bean()` or `remove_bean()` methods were included — unlike `Tea`, which allows customisation.
- Decided to enforce selection of **exactly one bean** during initialisation, as this:
  1. Keeps the coffee creation model simple and realistic (cafés typically use a single roast/blend per cup)
  2. Avoids unnecessary complexity around balancing multiple beans types (in reality).
- Used a list structure to comply with the UML, but validated it contains only one `Bean` enum.
- Implemented `brew()` to reflect preparation state and notify if already brewed.
- Used `calculate_price()` to apply per-bean price modifiers and clamp the final result to $0 minimum.
- Overrode `__str__()` to provide clear description output with size, temperature, bean, milk, and sugar.
- Added a `get_bean()` method to expose the bean for use in other classes (e.g. order summary or testing).

### What I Learned

- That UML design allows for interpretation based on structure and context — especially when dynamic methods are missing
- How to balance real-world customer logic (one bean per coffee) with assignment requirements (bean[])
- How to validate list content and structure clearly with defensive programming
- Reusing logic patterns across subclasses while tailoring design for specific item behaviour (e.g. Coffee ≠ Tea)

# Issue #7: Implemented Other class with soda, flavour, and cold modifiers

**Status:** Resolved  
**File(s) Affected:** other.py, tea.py, coffee.py  
**Commit (Noticed):** N/A – New class implementation  
**Commit (Resolved):** Update #7 – Implemented other.py and updated tea.py, coffee.py (`3b71670`)

### Description and Rationale

- Created the `Other` class based on UML and brief, representing fizzy/cold drinks like Water, Cola, and Lemonade.
- Added constructor validation to ensure the flavour is a list containing exactly one `Flavour` enum.
- Implemented `calculate_price()` using:
  - `BASE_PRICE = $5.00`
  - `+0.50` if soda is True
  - `+1.00` if cold
  - flavour modifiers: Water `-3`, Cola/Lemonade `+2`
- Used `max(price, 0.00)` to avoid negative prices.
- Overrode `__str__()` to match café-style output: `Medium iced Cola (with soda) at price - $8.50`
- Updated `__str__()` in `tea.py` and `coffee.py` to include the formatted price for consistency.

### What I Learned

- How to reuse design patterns from existing subclasses while adapting to new logic (e.g. Other ≠ Tea/Coffee)
- The importance of consistent user output across multiple classes
- The usefulness of testing flavour and soda combinations to confirm dynamic pricing
- Why test logic should be separated from implementation files to avoid duplicate output

# Issue #8: Implemented Food base class with size and order logic

**Status:** Resolved  
**File(s) Affected:** food.py  
**Commit (Noticed):** N/A – New class implementation  
**Commit (Resolved):** Update #9 – Implemented base Food class in food.py (`b954b06`)

### Description and Rationale

- Created `Food` as an abstract base class inheriting from `Item`, based on the UML design.
- Added a private `__size` attribute, validated against the `Size` enum.
- Implemented `get_size()` getter for use in subclasses (`Savoury`, `Sweet`).
- Defined `order()` method to be overridden in child classes, but provided default user-friendly output for testing.
- Declared `calculate_price()` as an `@abstractmethod`, ensuring that all subclasses implement their own pricing logic.

### What I Learned

- The role of base classes in simplifying shared logic across subclasses
- Why abstract methods are useful for enforcing consistent subclass responsibilities
- That even minimal classes should validate early (e.g. checking enum types)

# Issue #9: Implemented Savoury class with type/flour pricing logic

**Status:** Resolved  
**File(s) Affected:** savoury.py  
**Commit (Noticed):** N/A – New class implementation  
**Commit (Resolved):** Update #10 – Implemented Savoury class in savoury.py (`5a7632f`)

### Description and Rationale

- Implemented the `Savoury` subclass of `Food`, with `Type` and `Flour` enums as per UML.
- Validated that both inputs were single enum values and stored them as private attributes.
- Used `if/elif` logic in `calculate_price()` to apply multipliers:
  - Type: Loaf ×3, Muffin ×1, Slice ×0.5
  - Flour: Whole ×2, White ×1
- Ensured final price is calculated as `BASE_PRICE × type × flour`, with `round()` for currency precision.
- Added `__str__()` for realistic output like `"Savoury Small Loaf made with Whole flour at price - $12.00"`.

### What I Learned

- That enforcing enum validation early prevents bugs in price logic
- How to apply nested pricing models (multiplicative instead of additive)
- How to make output both machine-readable and user-friendly using `__str__`
- Importance of separating business logic (price) from display logic


