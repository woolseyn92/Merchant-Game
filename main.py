from product import Product
from supplier import Supplier
from customer import Customer
import random



names = ["Adam", "Blake", "Chris", "David", "Earl", "Frank", "Gary", "Harold", "Isaac", "Josh", "Kent",
         "Larry", "Mike", "Nick", "Oscar", "Pete", "Quincy", "Robert", "Steve", "Tom", "Ulysses", "Vern"]

categories = ["Miscellaneous", "Grocery", "Electronics", "Clothing"]

def generate_customers(number):
    customer_list = []
    for i in range(0, number):
        customer_name = random.choice(names)
        customer_age = random.randint(18, 65)
        customer_cash = random.randint(100, 1000)
        looking_for = random.choice(categories)
        rates_us = 1
        customer = Customer(customer_name, customer_age, customer_cash, looking_for, rates_us)
        customer_list.append(customer)


    return customer_list


class Store:
    def __init__(self, name, employees, liquid_cash, gross_assets, all_inventory, supplier_list, customer_list, product_list):
        self.name = name
        self.employees = employees
        self.liquid_cash = liquid_cash
        self.gross_assets = gross_assets
        self.all_inventory = all_inventory
        self.supplier_list = supplier_list
        self.customer_list = customer_list
        self.product_list = product_list

    def buy_product(self, product, amount):
        cost = product.buy(amount)
        self.liquid_cash -= cost

    def sell_product(self, product, amount):
        income = product.sell(amount)
        self.liquid_cash += income


store = Store("Buy Mart", 1, 5000, 5000, 0, [], [], [])
welcome_string = (f"Welcome to {store.name}!\n"
                  f"You have {store.employees} employees.\n"
                  f"You have ${store.liquid_cash} in liquid cash.\n"
                  f"You have {store.all_inventory} total inventory.\n"
                  f"Buy products from suppliers and sell them to customers.\n"
                  f"Make money.\n")

print(welcome_string)
store.product_list.append(Product(1.00, 1.50, "Pencil",
                                  "A Basic Writing Tool",1, 1000, 0))
store.product_list.append(Product(2.00, 2.50, "Mug",
                                  "A Container For Liquids",1, 1000, 0))
store.product_list.append(Product(3.50, 5.00, "Alarm Clock",
                                  "An Analog Clock With An Alarm",1, 1000, 0))

store.supplier_list.append(Supplier("General Goods", "Wholesaler", "Miscellaneous Items", 1, 5))
print("Available Products:")
for item in store.product_list:
    print(f"{item.name} - Wholesale Price: ${item.wholesale_price:.2f} - Retail Price: ${item.retail_price:.2f}")
print("")
print("Available Suppliers:")
for supplier in store.supplier_list:
    print(f"{supplier.company} - {supplier.wholesaler} - {supplier.specialty}")
store.customer_list = generate_customers(10)
print("")
print("Available Customers:")
for customer in store.customer_list:
    print(f"{customer}")