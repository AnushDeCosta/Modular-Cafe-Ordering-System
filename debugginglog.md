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

