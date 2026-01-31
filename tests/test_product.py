from src.product import Product


def test_product_init(ovo_product):
    assert ovo_product.name == 'картошка'
    assert ovo_product.description == 'статус картошка'
    assert ovo_product.price == 35
    assert ovo_product.quantity == 5


def test_product_create():
    product1 = Product('картошка', 'статус картошка', 35, 5)
    product1.name = 'картошка'
    product1.description = 'статус картошка'
    product1.price = 35
    product1.quantity = 5


def test_product_update(capsys, ovo_product):
    ovo_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    ovo_product.price = 800
    assert ovo_product.price == 800
