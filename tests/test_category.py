from src.product import Product
from src.category import Category


def test_category_init(frukt_category, ovo_category):
    assert frukt_category.name == 'фрукты'
    assert frukt_category.description == 'сезонные фрукты'
    assert len(frukt_category.products) == 61

    assert frukt_category.category_count == 2
    assert ovo_category.category_count == 2

    assert frukt_category.product_count == 4
    assert ovo_category.product_count == 4

def test_category_str(ovo_category):
    assert str(ovo_category) == "овощи, количество продуктов: 6 шт."

def test_middle_price(ovo_category):
    category1 =  ovo_category
    assert category1.middle_price() == 37.5

def test_middle_price(category_empty):
    category1 =  category_empty
    assert category1.middle_price() == 0
