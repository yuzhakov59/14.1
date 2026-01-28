import pytest

from src.product import Product
from src.category import Category


@pytest.fixture
def frukt_category():
    return Category(
        name='фрукты',
        description='сезонные фрукты',
        products=[
            Product('яблоко', 'статус яблока', 55, 5),
            Product('груши', 'статус груши', 70, 6)
        ]
    )


@pytest.fixture
def ovo_category():
    return Category(
        name='овощи',
        description='сезонные овощи',
        products=[
            Product('картошка', 'статус картошка', 35, 5),
            Product('огурцы', 'статус огурцы', 40, 6)
        ]
    )


@pytest.fixture
def ovo_product():
    return Product('картошка', 'статус картошка', 35, 5)
