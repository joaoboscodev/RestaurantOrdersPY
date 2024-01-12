from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    cheese = Ingredient("queijo mussarela")
    flour = Ingredient("farinha")

    assert cheese.name == "queijo mussarela"
    assert flour.name == "farinha"

    assert cheese.restrictions == {
        Restriction.LACTOSE, Restriction.ANIMAL_DERIVED
    }

    assert repr(cheese) == "Ingredient('queijo mussarela')"

    assert cheese == cheese
    assert cheese != flour

    assert hash(cheese) == hash(Ingredient("queijo mussarela"))

    assert hash(cheese) != hash(flour)
