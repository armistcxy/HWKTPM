import pytest
from calc import calculate_eat_cost


@pytest.mark.parametrize("t, v, expected", [
    (20, 14, 40000),                   
    (10, 14, 35000),
    (20, 15, 40000),
    (20, 14, 40000),
    (10, 15, 35000),                
])
def test_calculate_eat_cost(t, v, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calculate_eat_cost(t, v)
    else:
        assert calculate_eat_cost(t, v) == expected