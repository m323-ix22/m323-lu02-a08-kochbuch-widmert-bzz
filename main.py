"""
This function adjusts the ingredients of a recipe based on the number of servings.
"""
import json

def adjust_recipe(recipe, servings):
    for ingredient in recipe['ingredients']:
        recipe['ingredients'][ingredient] = recipe['ingredients'][ingredient] / recipe['servings'] * servings
    recipe['servings'] = servings
    return recipe


def load_recipe(my_json):
    return json.loads(my_json)


if __name__ == '__main__':
    recipe_json = ('{"title": "Spaghetti Bolognese", "ingredients": '
                   '{"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}')
    print(adjust_recipe(load_recipe(recipe_json), 2))
