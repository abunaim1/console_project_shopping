from users import*
from shop import*

def main():
    #create shop
    store = Shop('Sazid Garments')

    #create product
    product_1 = Product('Pant', 2850, 40)
    product_2 = Product('Shirt', 1790, 30)
    product_3 = Product('Under Wear', 350, 10)

    #add product to the store
    store.add_product(product_1)
    store.add_product(product_2)
    store.add_product(product_3)

    #creating customer
    customer_1 = Customer('Naim', 'a', 'a', 3000)
    seller_1 = Seller('Fahad', 'a', 'a')

    while True:
        #seller or customer login
        print('1.Customer Registration')
        print('2.Customer login')
        print('3.Seller Registration')
        print('4.Seller login')
        print('5.Exit')
        press_1 = input()
        if press_1 == '1':
            customer_1.customer_registration()
        if press_1 == '2':
            customer_1.customer_login(store)
        if press_1 == '3':
            seller_1.seller_registration()
        if press_1 == '4':
            seller_1.seller_login(store)
        if press_1 == '5':
            break
        
if __name__ == '__main__':
    main()