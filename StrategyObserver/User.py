class Observer:
    def update(self, subject):
        pass

class User(Observer):
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.suscriptions = []

    # def update(self, subject):
    #    return super().update(subject)
    
    def update(self, subject):
        print(f"Welcome to {subject.name}, {self.name}")

    def get_money(self):
        return self.money
    
    def pay(self, price, platform):
        if self.money - price < 0:
            platform.detach(self)
        else:
            self.money = self.money - price

        