def calculate_fuel(mass):
    if type(mass) != int:
        return False
    if mass <= 0:
        return False

    fuel = mass // 3 - 2
    if mass > 0 and fuel <= 0:
        return 1
    return fuel
