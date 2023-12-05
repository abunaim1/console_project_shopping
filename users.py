from shop import*
class User:
    def __init__(self, name) -> None:
        self.name = name
    
class Customer(User):
    def __init__(self, name, email, password, amount) -> None:
        self.wallet = amount
        self.cart = []
        self.wishlist = []
        self.email = email
        self.password = password
        super().__init__(name)
    
    def customer_login(self, store):
        email = input('ENTER YOUR EMAIL: ')
        password = input('ENTER YOUR PASSWORD: ')
        if self.email == email and self.password == password:
            print('--------Welcome to our shop,sir ---------')
            print('--------Here is our product lsit:--------')
            store.show_shop()
            self.buy_product(store.products)
        else:
            print('Incorrect password or email, Please registration first!')
            self.customer_registration()

    def customer_registration(self):
        name = input('ENTER YOUR NAME: ')
        email = input('ENTER YOUR EMAIL: ')
        password = input('SET A NEW PASSWORD: ')
        self.name = name
        self.email = email
        self.password = password
        print('Your registration completed, Login Now!')

    def wishlist(self, product):
        pass

    def add_to_cart(self, product):
        print(f'Product Pric: {product.price} + vat 5%')
        total_bill = product.price + product.price * 5/100
        self.pay_bill(total_bill)
        
    def buy_product(self, products):
        print('Select a product: ')
        buy = input()
        match = False
        for product in products:
            if product.quantity > 0:
                if buy == product.name:
                    self.add_to_cart(product)
                    match = True
        if match == False:
            print('Not available!')

    def pay_bill(self, amount):
        print(f'Have to pay: {amount}')
        Seller.seller_wallet(amount)
        self.wallet - amount

    def show_cart(self):
        pass

    def return_products(self):
        pass

class Seller(User):
    def __init__(self, name, email, password) -> None:
        self.email = email
        self.password = password
        self.wallet = 0
        self.profit = 0
        self.sell_list = []
        super().__init__(name)
    
    def seller_login(self, store):
        email = input('ENTER YOUR EMAIL: ')
        password = input('ENTER YOUR PASSWORD: ')
        if self.email == email and self.password == password:
            print('Do you want to show the product list press 1: ')
            take = input()
            if take == '1':
                store.show_shop()
            else:
                print('Your Store')                
                store.show_shop()
        else:
            print('Incorrect password or email, Please registration first!')
            self.seller_registration()

    def seller_registration(self):
        name = input('ENTER YOUR NAME: ')
        email = input('ENTER YOUR EMAIL: ')
        password = input('SET A NEW PASSWORD: ')
        self.name = name
        self.email = email
        self.password = password
        print('Your registration completed, Login Now!')

    def delivery_product(self, date_time):
        print(f'Your estimate delivery date {date_time}')

    @classmethod
    def seller_wallet(self,amount):
        wallet = 0
        wallet += amount
        self.balance(Seller, wallet)

    def balance(self, cash):
        self.wallet = cash
        self.delivery_product('31 Dec, 2023')
    
        
