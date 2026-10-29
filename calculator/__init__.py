"""
calculator package initialization.

Exports core arithmetic functions for direct import:
    from calculator import add, subtract, multiply, divide, power
"""

from .operations import add, subtract, multiply, divide, power

__all__ = ["add", "subtract", "multiply", "divide", "power"]
