class User:
    id_counter = 100
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password
        self.user_id = User.generate_id()

    @classmethod
    def generate_id(self):
        id = self.id_counter
        self.id_counter += 1
        return id

    def __repr__(self) -> str:
        return f'email: {self.email} user_id: {self.user_id}'

class Products:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        return f'name: {self.name} || price: {self.price} || quantity: {self.quantity}'

class Store:
    def __init__(self) -> None:
        self.total_products = {}

    def add_product(self, seller_id, product):

        product_dict = vars(product)
        if seller_id not in self.total_products:
            self.total_products[seller_id] = []

            seller_info = {}
            seller_info["total_sell_product"] = 0
            seller_info["total_sell_amount"] = 0
            seller_info["total_profit_amount"] = 0

            self.total_products[seller_id].append(seller_info)
        self.total_products[seller_id].append(product_dict)

class Owner(User):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)

class Seller(User):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)

    def add_product(self, store, name, price, quantity):
        product = Products(name, price, quantity)
        store.add_product(self.user_id, product)

class Customer(User): 
    def __init__(self, email, password) -> None:
        super().__init__(email, password)

    def show_products(self, store):
        seller_keys = store.total_products.keys()
        for seller_id in seller_keys:
            print('seller_id: ', seller_id)
            print('=================')
            for index in range(1, len(store.total_products[seller_id])):
                product = store.total_products[seller_id][index]
                print('name:', product['name'], 'price:', product['price'], 'quantity:', product['quantity'])
store = Store()

seller_1 = Seller('seller@gmail.com', 1234)
seller_2 = Seller('seller2@gmail.com', 4321)
seller_3 = Seller('seller3@gmail.com', 1243)

seller_1.add_product(store, 'Samsung S22', 150, 15)
seller_1.add_product(store, 'iphone 10', 100, 5)

seller_2.add_product(store, 'Oppo A8', 200, 20)
seller_2.add_product(store, 'Oppo A9', 110, 12)

seller_3.add_product(store, 'Samsung S11', 200, 20)
seller_3.add_product(store, 'Vivo B5', 160, 8)

customer_1 = Customer('customer1@gmail.com', 5593)

# print(store.total_products)

customer_1.show_products(store)