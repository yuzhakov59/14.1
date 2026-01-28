def test_category_init(frukt_category, ovo_category):
    assert frukt_category.name == 'фрукты'
    assert frukt_category.description == 'сезонные фрукты'
    assert len(frukt_category.products) == 2

    assert frukt_category.categories_count == 2
    assert ovo_category.categories_count == 2

    assert frukt_category.products_count == 4
    assert ovo_category.products_count == 4
