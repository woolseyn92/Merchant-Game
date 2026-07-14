class Product:
    def __init__(self, wholesale_price, retail_price, name, description, demand, supply, inventory):
        self.wholesale_price = wholesale_price
        self.retail_price = retail_price
        self.name = name
        self.description = description
        self.demand = demand
        self.supply = supply
        self.inventory = inventory

    def __str__(self):
        return (f"{self.name}: {self.description}.\n"
                f"Wholesale Price: {self.wholesale_price}\n"
                f"Retail Price: {self.retail_price}\n"
                f"Demand: {self.demand}, Supply: {self.supply}, Inventory: {self.inventory}\n")

    def __repr__(self):
        return self.__str__()

    def buy(self, amount):
        self.inventory += amount
        self.supply -= amount
        return amount * self.wholesale_price


class Grocery(Product):
    def __init__(self, wholesale_price, retail_price, name, description, demand, supply, inventory):
        super().__init__(wholesale_price, retail_price, name, description, demand, supply, inventory)
