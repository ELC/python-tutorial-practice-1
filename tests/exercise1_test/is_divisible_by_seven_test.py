"""Test Suite for Divisibility by Seven"""

import math

import pytest
from hypothesis import given
from hypothesis import strategies as st

from exercises.exercise1 import is_divisible_by_seven


@pytest.mark.parametrize(
    "number, expected",
    [
        (7, True),
        (6, False),
        (0, True),
        (-7, True),
        (-6, False),
    ],
    ids=[
        "number>0, number is divisible",
        "number>0, number is not divisible",
        "number=0",
        "number<0, number is divisible",
        "number>0, number is not divisible",
    ],
)
def test_is_divisible_by_seven_concrete_examples(number: float, expected: int):
    assert is_divisible_by_seven(number) == expected


@pytest.mark.parametrize(
    "number",
    [
        (math.inf),
        (math.nan),
    ],
    ids=[
        "number is inf",
        "number is nan",
    ],
)
def test_is_divisible_by_seven_invalid(number: float):
    with pytest.raises(ValueError):
        is_divisible_by_seven(number)


@given(st.integers(), st.integers())
def test_is_divisible_by_seven_cyclic(number: float, remainder: int):
    result = is_divisible_by_seven(number)
    assert result == is_divisible_by_seven(number + remainder * 7)


@given(st.integers())
def test_is_divisible_by_seven_multiples(number: float):
    assert is_divisible_by_seven(number * 7)
