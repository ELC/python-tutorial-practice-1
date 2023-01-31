"""Basic Arithmetic"""


def square_area(side: float) -> float:
    """
    Calculate the area of the square giving its side.
    Constraint: Use the multiplication operator.
    """
    ...


# DO NOT MODIFY - START
assert square_area(5) == 25
# DO NOT MODIFY - END


def square_area_power(side: float) -> float:
    """
    Re-Write using the power operator.
    """
    ...


# DO NOT MODIFY - START
assert square_area_power(5) == 25
# DO NOT MODIFY - END


def square_area_pow(side: float) -> float:
    """
    Re-Write using the pow function.
    """
    ...


# DO NOT MODIFY - START
assert square_area_pow(5) == 25
assert square_area_pow(0) == 0
# DO NOT MODIFY - END


def compute_quantity(price: float, available_budget: float) -> int:
    """
    Calculate the number of units to buy.
    Constraint: Use the integer division operator.
    """
    ...


# DO NOT MODIFY - START
assert compute_quantity(3.74, 10) == 2
# DO NOT MODIFY - END


def is_divisible_by_seven(number: int) -> bool:
    """
    Determine if a number is divisible by 7.
    Constraint: Use the modulus operator.
    """
    ...


# DO NOT MODIFY - START
assert is_divisible_by_seven(7)
assert is_divisible_by_seven(0)
# DO NOT MODIFY - END
