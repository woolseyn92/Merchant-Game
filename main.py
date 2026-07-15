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

store.supplier_list.append(Supplier("General Goods", "Miscellaneous Items", 1, 5))
print("Available Products:")
for item in store.product_list:
    print(f"{item.name} - Wholesale Price: ${item.wholesale_price:.2f} - Retail Price: ${item.retail_price:.2f}")
print("")
print("Available Suppliers:")
for supplier in store.supplier_list:
    print(f"{supplier.company} - {supplier.specialty}")