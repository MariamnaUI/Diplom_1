from praktikum.bun import Bun


class TestBun:
    def test_get_name(self):
        bun = Bun(name="Флюоресцентная булка R2-D3", price=988)
        assert bun.get_name() == "Флюоресцентная булка R2-D3"

    def test_get_price(self):
        bun = Bun(name="Флюоресцентная булка R2-D3", price=988)
        assert bun.get_price() == 988
