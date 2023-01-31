"""Test Suite for Compute Quantity Test"""

import pytest
from hypothesis import assume, given
from hypothesis import strategies as st

from exercises.exercise1 import compute_quantity


@pytest.mark.parametrize(
    "price, available_budget, expected",
    [
        (10, 105, 10),
        (105, 10, 0),
        (10, 10, 1),
        (10, 0, 0),
    ],
    ids=[
        "price>0, available_budget > 0, available_budget > price",
        "price>0, available_budget > 0, available_budget < price",
        "price>0, available_budget > 0, available_budget = price",
        "price>0, available_budget = 0",
    ],
)
def test_compute_quantity_concrete_examples(
    price: float, available_budget: float, expected: int
):
    assert compute_quantity(price, available_budget) == expected


@given(st.floats())
def test_compute_quantity_zero_price(available_budget: float):
    with pytest.raises(ValueError):
        compute_quantity(0, available_budget)


@given(st.floats(max_value=0), st.floats())
def test_compute_quantity_negative_price(price: float, available_budget: float):
    assume(price != 0)
    with pytest.raises(ValueError):
        compute_quantity(price, available_budget)


@given(st.floats(), st.floats(max_value=0))
def test_compute_quantity_negative_budget(price: float, available_budget: float):
    assume(available_budget != 0)
    with pytest.raises(ValueError):
        compute_quantity(price, available_budget)


positive_floats = st.floats(min_value=0, allow_infinity=False, allow_nan=False)


@given(positive_floats, positive_floats)
def test_compute_quantity_deterministic(price: float, available_budget: float):
    assume(price != 0)

    result = compute_quantity(price, available_budget)
    replicated_result = compute_quantity(price, available_budget)

    assert result == replicated_result
