import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    Recipe_A = Dish("lasanha berinjela", 27.00)
    Recipe_B = Dish("lasanha presunto", 25.90)

    assert Recipe_A.__repr__() == "Dish('lasanha berinjela', 27.00)"
    assert Recipe_B.__repr__() == "Dish('lasanha presunto', 25.90)"

    with pytest.raises(AssertionError):
        assert Recipe_A.name == "lasanha bolonhesa"

    assert Recipe_A.name == "lasanha berinjela"
    assert Recipe_A.price == 27.00

    assert Recipe_A.__hash__() == hash(Recipe_A.__repr__())
    assert Recipe_B.__hash__() != hash(Recipe_A.__repr__())

    assert Recipe_A.__eq__(Recipe_A) is True
    assert Recipe_B.__eq__(Recipe_B) is False

    with pytest.raises(TypeError):
        Dish("Sushi", "500")

    with pytest.raises(ValueError):
        Dish("lasanha presunto", -500)

    camarao = Ingredient('camarao')
    Recipe_A.add_ingredient_dependency(camarao, 200)
    assert Recipe_A.get_ingredients() == {camarao}

    camarao_restriction = {Restriction.SEAFOOD}
    assert Recipe_A.get_restrictions() == camarao_restriction
