class Supplier:
    def __init__(self, company, specialty, my_reputation, reliability):
        self.company = company
        self.specialty = specialty
        self.my_reputation = my_reputation
        self.reliability = reliability


    def __str__(self):
        return (f"{self.company}: {self.specialty} supplier.\n"
                f"My Reputation: {self.my_reputation}, Reliability: {self.reliability}\n")

    def __repr__(self):
        return self.__str__()