destination = "Reykjavik"

destinations = {
    "Nicosia": 1980,
    "Reykjavik": 2900,
    "Chartum": False
}

distance = destinations[destination]

if distance:
    cost = 2 * distance
    if distance < 2000:
        cost += 100
    print(f"Cost to {destination} is {cost}")
else:
    print(f"No travel to {destination}")
