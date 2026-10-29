# Calculator Package

A simple Python arithmetic package developed for **19CSP01 – Free Open Source Software, Assignment 2: Package Development & Version Control using Git and GitHub**.

## 1. Purpose

The `calculator` package provides fundamental arithmetic operations as an easy-to-use Python library. It demonstrates Python packaging using `setuptools` and version control management using Git and GitHub.

## 2. Directory Structure

```text
mypackage/
├── calculator/
│   ├── __init__.py
│   └── operations.py
├── setup.py
├── README.md
└── .gitignore
```

## 3. Installation

You can install this package locally in editable/development mode using `pip`:

```bash
cd mypackage
pip install -e .
```

Or install it as a standard package:

```bash
pip install .
```

## 4. Available Arithmetic Operations

| Function | Description | Example |
| :--- | :--- | :--- |
| `add(a, b)` | Returns the sum of `a` and `b` | `add(10, 5) -> 15` |
| `subtract(a, b)` | Returns the difference of `a - b` | `subtract(10, 5) -> 5` |
| `multiply(a, b)` | Returns the product of `a * b` | `multiply(10, 5) -> 50` |
| `divide(a, b)` | Returns the quotient `a / b` (raises `ValueError` on division by zero) | `divide(10, 5) -> 2.0` |

## 5. Usage Examples

```python
from calculator import add, subtract, multiply, divide

# Basic arithmetic operations
print("10 + 5 =", add(10, 5))          # Output: 15
print("10 - 5 =", subtract(10, 5))     # Output: 5
print("10 * 5 =", multiply(10, 5))     # Output: 50
print("10 / 5 =", divide(10, 5))       # Output: 2.0

# Division by zero handling
try:
    divide(10, 0)
except ValueError as e:
    print("Error:", e)                  # Output: Error: Cannot divide by zero.
```

## 6. Running Tests

To verify package functionality, you can run the test script included in the repository:

```bash
python test_calculator.py
```
