class Customer:
    def __init__(self, name, age, cash, looking_for, rates_us):
        self.name = name
        self.age = age
        self.cash = cash
        self.looking_for = looking_for
        self.rates_us = rates_us

    def __str__(self):
        return (f"{self.name} is {self.age} years old.\n"
                f"They have ${self.cash} to spend and are looking for {self.looking_for}.\n"
                f"They rate us {self.rates_us} stars.\n")

    def __repr__(self):
        return self.__str__()
