import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self._load_menu_data(source_path)

    def _load_menu_data(self, source_path: str) -> list:
        menu = set()

        with open(source_path) as csv_file:
            csv_lines = csv.reader(csv_file)
            next(csv_lines)

            for line in csv_lines:
                dish_name, price_str, ingredient_name, quantity_str = line

                price = float(price_str)
                quantity = int(quantity_str)

                dish = next((d for d in menu if d.name == dish_name), None)

                if not dish:
                    dish = Dish(dish_name, price)
                    menu.add(dish)

                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, quantity)

        return menu
