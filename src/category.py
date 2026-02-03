from src.product import Product

class Category:
    name: str
    description: str
    __products: list
    categories_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.categories_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        return f'{self.name}, количество продуктов: {Category.product_count} шт.'  #Название категории, количество продуктов: 200 шт.

    def add_product(self, product):
        """Добавляет продукт в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise ValueError("Можно добавлять только объекты класса Product")

    @property
    def products(self):
        str_product = ""
        for product in self.__products:
            str_product += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return str_product

    @products.setter
    def products(self, products: Product):
        self.__products.append(products)
        Category.product_count += 1
