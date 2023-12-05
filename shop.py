class Shop:
    def __init__(self, name) -> None:
        self.name = name
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)

    def remove_product(self):
        pass

    def show_shop(self):
        if len(self.products) > 0:
            for product in self.products:
                print(f'PRODUCT NAME: {product.name}, PRICE: {product.price}, QUANTITY: {product.quantity}')



class Product:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
    