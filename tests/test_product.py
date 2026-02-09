import pytest
from src.product import Product

def test_product_init(ovo_product):
    assert ovo_product.name == 'картошка'
    assert ovo_product.description == 'статус картошка'
    assert ovo_product.price == 35
    assert ovo_product.quantity == 5

def test_product_str(ovo_product):
    assert str(ovo_product) == "картошка, 35 руб. Остаток: 5 шт."

def test_product_add(ovo_product, app_product):
    sum_prod = ovo_product + app_product
    assert sum_prod == 450

def test_typeerror(smartphone1, smartphone2, grass1):

    expected_total_cost = (smartphone1.price * smartphone1.quantity) + (smartphone2.price * smartphone2.quantity)
    assert expected_total_cost == 2580000.0


    # Проверяем, что сложение с другим типом объекта вызывает TypeError
    with pytest.raises(TypeError):
        smartphone1 + grass1

def test_dict_new_product():
    new_prod = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    assert new_prod.name == "Samsung Galaxy S23 Ultra"
    assert new_prod.description == "256GB, Серый цвет, 200MP камера"
    assert new_prod.price == 180000.0
    assert new_prod.quantity == 5
