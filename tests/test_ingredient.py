from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_get_price(self):
        ingredient = Ingredient('SAUCE', 'hot sauce', 50.0)
        assert ingredient.get_price() == 50.0

    def test_get_name(self):
        ingredient = Ingredient('SAUCE', 'sour cream', 75.0)
        assert ingredient.get_name() == 'sour cream'

    def test_get_type(self):
        ingredient = Ingredient('FILLING', 'sausage', 120.0)
        assert ingredient.get_type() == 'FILLING'
