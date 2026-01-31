
def test_category_init(frukt_category, ovo_category):
    assert frukt_category.name == 'фрукты'
    assert frukt_category.description == 'сезонные фрукты'
    assert len(frukt_category.prod_in_list) == 2

    assert frukt_category.categories_count == 2
    assert ovo_category.categories_count == 2

    assert frukt_category.product_count == 4
    assert ovo_category.product_count == 4


def test_cat_prod_properti(frukt_category):
    assert frukt_category.products == ('яблоко, 55 руб. Остаток: 5 шт.\nгруши, 70 руб. Остаток: 6 шт.\n')


def test_cat_prod_setter(frukt_category, ovo_product):
    assert len(frukt_category.prod_in_list) == 2
    frukt_category.products = ovo_product
    assert len(frukt_category.prod_in_list) == 3
