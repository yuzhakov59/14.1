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
        product_count = 0
        for product in self.__products:
            product_count += product.quantity
        return f'{self.name}, количество продуктов: {product_count} шт.'

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
        Category.product_count += products.price * products.quantity


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))
