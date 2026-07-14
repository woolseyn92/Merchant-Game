from product import Product
from supplier import Supplier
from customer import Customer

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

store = Store("Buy Mart", 1, 5000, 5000, 0, [], [], [])
welcome_string = (f"Welcome to {store.name}!\n"
                  f"You have {store.employees} employees.\n"
                  f"You have ${store.liquid_cash} in liquid cash.\n"
                  f"You have {store.all_inventory} total inventory.\n"
                  f"Buy products from suppliers and sell them to customers.\n"
                  f"Make money.\n")

print(welcome_string)