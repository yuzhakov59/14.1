

class Product:
    name: str
    description: str
    products: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


if __name__ == "__main__":
    product = Product('яблоко', 'статус яблока', 55)

    print(product.name)
    print(product.description)
    print(product.price)
