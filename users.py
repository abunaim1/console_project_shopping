from shop import*
class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password

    # @property
    # def set_password(self):
    #     return self.__password
    
    # @set_password.setter
    # def set_password(self, new_password):
    #     self.__password = new_password
    
class Customer(User):
    def __init__(self, name, email, password, address, contact) -> None:
        self.address = address
        self.contact = contact
        self.wallet = 0
        self.cart = []
        self.wishlist = []
        super().__init__(name, email, password)
    
    def customer_login(self, store):
        email = input('ENTER YOUR EMAIL: ')
        password = input('ENTER YOUR PASSWORD: ')
        if self.email == email and self.password == password:
            print('--------Welcome to our shop,sir ---------')
            print('--------Here is our product lsit:--------')
            print()
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
        self.customer_login()


    def wishlist(self, product):
        pass

    def cart(self):
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
        self.balance = 0
        self.profit = 0
        self.sell_list = []
        super().__init__(name, email, password)
    
    def delivery_product(self, date_time):
        pass
