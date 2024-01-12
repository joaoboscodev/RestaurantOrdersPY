import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    Recipe_A = Dish("lasanha berinjela", 27.00)
    Recipe_B = Dish("lasanha presunto", 25.90)

    assert Recipe_A.__repr__() == "Dish('lasanha berinjela', R$27.00)"

    with pytest.raises(AssertionError):
        assert Recipe_A.name == "lasanha bolonhesa"

    assert Recipe_A.name == "lasanha berinjela"
    assert Recipe_A.price == 27.00

    assert Recipe_A.__hash__() == hash(Recipe_A.__repr__())
    assert Recipe_B.__hash__() != hash(Recipe_A.__repr__())

    assert Recipe_A.__eq__(Recipe_A) is True
    assert Recipe_B.__eq__(Recipe_A) is False

    with pytest.raises(TypeError):
        Dish("Sushi", "20")

    with pytest.raises(ValueError):
        Dish("lasanha presunto", -20)

    bacon = Ingredient("bacon")
    Recipe_A.add_ingredient_dependency(bacon, 20)

    assert Recipe_A.get_ingredients() == {bacon}

    bacon_restriction = {Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED}
    assert Recipe_A.get_restrictions() == bacon_restriction
