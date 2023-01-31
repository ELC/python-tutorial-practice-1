"""Test Suite for Square Area - Different Implementations"""

import math
from typing import Callable

import pytest
from hypothesis import assume, given
from hypothesis import strategies as st

from exercises.exercise1 import square_area, square_area_pow, square_area_power

parametrized_functions = pytest.mark.parametrize(
    "function",
    [square_area, square_area_pow, square_area_power],
    ids=["multiplication", "power", "pow"],
)


@pytest.mark.parametrize(
    "side, expected",
    [
        (10, 100),
        (0, 0),
    ],
    ids=["side>0", "side=0"],
)
@parametrized_functions
def test_square_area_concrete_examples(
    side: float, expected: float, function: Callable[[float], float]
):
    assert function(side) == expected


@parametrized_functions
@given(st.floats(max_value=0))
def test_square_area_negative(function: Callable[[float], float], side: float):
    assume(side != 0)
    with pytest.raises(ValueError):
        function(side)


@parametrized_functions
@given(st.floats(min_value=0, max_value=2**32))
def test_square_area_deterministic(function: Callable[[float], float], side: float):
    result = function(side)
    replicated_result = function(side)

    assume(math.isfinite(result))

    assert math.isclose(result, replicated_result, abs_tol=1e-5)


@parametrized_functions
@given(st.floats(min_value=1, max_value=2**32))
def test_square_area_greater_area_for_side_greater_than_one(
    function: Callable[[float], float], side: float
):
    assert function(side) >= side


@parametrized_functions
@given(st.floats(min_value=0, max_value=1))
def test_square_area_smaller_area_for_side_less_than_one(
    function: Callable[[float], float], side: float
):
    assert function(side) <= side


# Avoid Floating point errors
safe_floats = st.floats(min_value=2**-32, max_value=2**32)


@parametrized_functions
@given(safe_floats, safe_floats)
def test_square_area_injective(
    function: Callable[[float], float], side1: float, side2: float
):
    assume(not math.isclose(side1, side2))

    side1_squared = function(side1)
    side2_squared = function(side2)

    assert not math.isclose(side1_squared, side2_squared)
