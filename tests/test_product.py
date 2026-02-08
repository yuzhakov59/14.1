def test_product_init(ovo_product):
    assert ovo_product.name == 'картошка'
    assert ovo_product.description == 'статус картошка'
    assert ovo_product.price == 35
    assert ovo_product.quantity == 5

def test_product_str(ovo_product):
    assert str(ovo_product) == "картошка, 35 руб. Остаток: 5 шт."

def test_product_add(ovo_product, app_product):
    assert ovo_product + app_product == 35 * 5 + 55 * 5
