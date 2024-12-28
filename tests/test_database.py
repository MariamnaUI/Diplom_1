from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_available_buns_count(self):
        """Тест на получение количества доступных булочек"""
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3

    def test_available_buns_content(self):
        """Тест на содержимое доступных булочек"""
        database = Database()
        buns = database.available_buns()

        expected_buns = [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300),
        ]
        for i in range(len(buns)):
            bun = buns[i]
            name, price = expected_buns[i]
            assert bun.get_name() == name and bun.get_price() == price

    def test_available_ingredients_count(self):
        """Тест на получение количества доступных ингридиентов"""
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6

    def test_available_ingredients_content(self):
        """Тест на содержимое доступных ингредиентов"""
        database = Database()
        ingredients = database.available_ingredients()

        expected_ingredients = [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (INGREDIENT_TYPE_FILLING, "sausage", 300),
        ]

        for i in range(len(ingredients)):
            ingredient = ingredients[i]
            ingredient_type, name, price = expected_ingredients[i]
            assert ingredient.get_type() == ingredient_type and ingredient.get_name() == name and ingredient.get_price() == price
