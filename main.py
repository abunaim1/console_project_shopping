from users import*
from shop import*

def main():
    #create shop
    store = Shop('Sazid Garments')

    #making some product
    product_1 = Product('Pant', 2850, 40)
    product_2 = Product('Shirt', 1790, 30)
    product_3 = Product('Under Wear', 350, 10)

    #add product to the store
    store.add_product(product_1)
    store.add_product(product_2)
    store.add_product(product_3)

    #showing store
    store.show_shop()

    #creating customer
    customer_1 = Customer('Naim', 'naim@gmail.com', '123', 'Barishal', 234)
    customer_1.customer_login(store)

if __name__ == '__main__':
    main()