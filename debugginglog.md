# Issue #1: Setting up project and UML-based class structure

**Status:** Resolved

**File(s) Affected:** menu_item.py, drink.py, food.py, tea.py, coffee.py, other.py, savoury.py, sweet.py, order.py, store.py, enums.py

**Commit (Noticed):** None – initial project setup  
**Commit (Resolved):** 1. Created class file structure and abstract MenuItem base class

### Error code and Description

No errors occurred during this stage, but it was important to align the file layout and class naming with the UML diagram and Reid Honan's forum clarifications.

Expected:
- One `.py` file per class
- Abstract base class created
- Class names and responsibilities matching UML

Actual:
- Confirmed that `Store.py` (as `Cafe`) is needed to meet brief, even though not shown in UML

### Resolution Log

- Created one `.py` file for each class in the UML
- Added required docstring header to each file
- Declared abstract base class `MenuItem` using ABC module
- Logged deviation: implemented `Cafe` class in `Store.py` for managing total earnings and order history
- Committed structure setup as first Git commit
