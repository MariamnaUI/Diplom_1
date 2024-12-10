from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.burger import Burger


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        bun = Bun('Флюоресцентная булка R2-D3', 988)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient_mock = Mock()
        burger.add_ingredient(ingredient_mock)
        assert burger.ingredients == [ingredient_mock]

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.remove_ingredient(0)
        assert burger.ingredients == [ingredient_2]

    def test_move_ingredient(self):
        burger = Burger()
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        ingredient_3 = Mock()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.add_ingredient(ingredient_3)
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [ingredient_2, ingredient_3, ingredient_1]

    def test_get_price(self):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_price.return_value = 988
        ingredient_1 = Mock()
        ingredient_1.get_price.return_value = 1337
        ingredient_2 = Mock()
        ingredient_2.get_price.return_value = 15
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        total_price = burger.get_price()
        expected_price = bun_mock.get_price() * 2 + ingredient_1.get_price() + ingredient_2.get_price()
        assert total_price == expected_price

    def test_get_receipt(self):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_name.return_value = "Флюоресцентная булка R2-D3"
        bun_mock.get_price.return_value = 988
        ingredient_mock = Mock()
        ingredient_mock.get_name.return_value = "Соус Spicy-X"
        ingredient_mock.get_type.return_value = "SAUCE"
        ingredient_mock.get_price.return_value = 90
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        receipt = burger.get_receipt()
        expected_receipt = (
            "(==== Флюоресцентная булка R2-D3 ====)\n"
            "= sauce Соус Spicy-X =\n"
            "(==== Флюоресцентная булка R2-D3 ====)\n\n"
            "Price: 2066"
        )
        assert receipt == expected_receipt
        assert bun_mock.get_name.call_count == 2
