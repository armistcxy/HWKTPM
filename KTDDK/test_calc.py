import pytest
from calc import calculate_eat_cost


@pytest.mark.parametrize("t, v", [
    (0, -1),  # Test case 1
])
def test_calculate_eat_cost_exception(t, v):
    with pytest.raises(Exception):
        calculate_eat_cost(t, v)


@pytest.mark.parametrize("t, v, expected", [
    (15, 15, 35000),                    # Test case 2 (bug case)
    (25, 12, 40000),                    # Test case 3
])
def test_calculate_eat_cost(t, v, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calculate_eat_cost(t, v)
    else:
        assert calculate_eat_cost(t, v) == expected



