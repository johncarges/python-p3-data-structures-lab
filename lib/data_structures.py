spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [item["name"] for item in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]
    pass

def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        print(f"{item['name']} ({item['cuisine']}) | Heat Level: {'🌶' * item['heat_level']}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return [item for item in spicy_foods if item["cuisine"]==cuisine][0]
    pass

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))
    pass

def get_average_heat_level(spicy_foods):
    total = 0
    count = 0
    for item in spicy_foods:
        total += item["heat_level"]
        count += 1
    return total / count
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass

# print(spicy_foods)
# print(create_spicy_food(spicy_foods, {
#                 "name": "Griot",
#                 "cuisine": "Haitian",
#                 "heat_level": 10,
#             }))