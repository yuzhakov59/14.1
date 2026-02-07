def test_product_init(ovo_product):
    assert ovo_product.name == 'картошка'
    assert ovo_product.description == 'статус картошка'
    assert ovo_product.price == 35
    assert ovo_product.quantity == 5
