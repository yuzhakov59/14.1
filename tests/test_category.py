def test_category_init(frukt_category, ovo_category):
    assert frukt_category.name == 'фрукты'
    assert frukt_category.description == 'сезонные фрукты'
    assert len(frukt_category.products) == 61

    assert frukt_category.categories_count == 2
    assert ovo_category.categories_count == 2

    assert frukt_category.product_count == 4
    assert ovo_category.product_count == 4

def test_category_str(ovo_category):
    assert str(ovo_category) == "овощи, количество продуктов: 6 шт."
