import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    pasta_recipe = {
        Ingredient("spaghetti"): 200,
        Ingredient("tomato sauce"): 150,
        Ingredient("ground beef"): 250,
        Ingredient("onion"): 50,
        Ingredient("garlic"): 10,
    }
    pasta_dish = Dish("Spaghetti Bolognese", 15.99)
    for ingredient, amount in pasta_recipe.items():
        pasta_dish.add_ingredient_dependency(ingredient, amount)

    assert pasta_dish.name == "Spaghetti Bolognese"

    assert hash(pasta_dish) == hash(Dish("Spaghetti Bolognese", 15.99))

    assert hash(pasta_dish) != hash(Dish("Carbonara", 12.99))

    assert pasta_dish == pasta_dish

    assert pasta_dish != Dish("Carbonara", 12.99)

    assert repr(pasta_dish) == "Dish('Spaghetti Bolognese', R$15.99)"

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Invalid Dish", "not a float")

    with pytest.raises(ValueError, match="Price must be greater than zero."):
        Dish("Invalid Dish", 0)

    assert pasta_dish.recipe.get(Ingredient("spaghetti")) == 200

    assert pasta_dish.get_restrictions() == set()

    assert pasta_dish.get_ingredients() == set(pasta_recipe.keys())

    cheese = Ingredient("parmesan cheese")
    pasta_dish.add_ingredient_dependency(cheese, 50)

    assert pasta_dish.get_restrictions() == {Restriction.ANIMAL_DERIVED}

    expected_ingredients = set(pasta_recipe.keys()).union({cheese})
    assert pasta_dish.get_ingredients() == expected_ingredients
