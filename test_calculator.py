"""
Test script for the calculator package.
Verifies all arithmetic functions and error handling.
"""

from calculator import add, subtract, multiply, divide

def run_tests():
    print("Running calculator package tests...")
    
    # 1. Test addition
    assert add(10, 5) == 15, f"Expected 15, got {add(10, 5)}"
    assert add(-2, 3) == 1, f"Expected 1, got {add(-2, 3)}"
    print("[PASS] add() tests passed.")

    # 2. Test subtraction
    assert subtract(10, 5) == 5, f"Expected 5, got {subtract(10, 5)}"
    assert subtract(3, 7) == -4, f"Expected -4, got {subtract(3, 7)}"
    print("[PASS] subtract() tests passed.")

    # 3. Test multiplication
    assert multiply(10, 5) == 50, f"Expected 50, got {multiply(10, 5)}"
    assert multiply(4, 0) == 0, f"Expected 0, got {multiply(4, 0)}"
    print("[PASS] multiply() tests passed.")

    # 4. Test division
    assert divide(10, 5) == 2.0, f"Expected 2.0, got {divide(10, 5)}"
    assert divide(7, 2) == 3.5, f"Expected 3.5, got {divide(7, 2)}"
    print("[PASS] divide() normal tests passed.")

    # 5. Test division by zero
    division_by_zero_caught = False
    try:
        divide(10, 0)
    except ValueError as e:
        division_by_zero_caught = True
        assert str(e) == "Cannot divide by zero.", f"Unexpected error message: {e}"
    assert division_by_zero_caught, "Expected ValueError when dividing by zero, but none was raised."
    print("[PASS] divide() by zero test passed (ValueError raised correctly).")

    print("\nAll initial tests passed successfully!")

if __name__ == "__main__":
    run_tests()
