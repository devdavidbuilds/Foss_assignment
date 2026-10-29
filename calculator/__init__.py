"""
calculator package initialization.

Exports core arithmetic functions for direct import:
    from calculator import add, subtract, multiply, divide
"""

from .operations import add, subtract, multiply, divide

__all__ = ["add", "subtract", "multiply", "divide"]
