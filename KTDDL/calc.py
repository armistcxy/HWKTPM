def calculate_eat_cost(t: int, v: int) -> int:
    if t < 1 or t > 150 or v < 0 or v > 30:
        raise Exception("invalid input")
    
    cost = 40000
    if t < 16 or t > 55:
        cost -= 5000

    if v >= 15:
        cost -= 5000

    return cost