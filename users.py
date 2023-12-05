from shop import*
class User:
    def __init__(self, name) -> None:
        self.name = name
    
class Customer(User):
    def __init__(self, name, email, password) -> None:
        self.wallet = 0
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

    def add_to_cart():
        # for product in store.products:
            # print(product.name)
            pass

    def buy_product(self, product):
        pass
    
    def pay_bill(self, amount):
        pass

    def show_cart(self):
        pass

    def return_products(self):
        pass

class Seller(User):
    def __init__(self, name, email, password) -> None:
        self.email = email
        self.password = password
        self.balance = 0
        self.profit = 0
        self.sell_list = []
        self.email = None
        self.password = None
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
        pass

# Customer.add_to_cart()