class Observer:
    def update(self, name, message):
        pass

class User(Observer):
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.suscriptions = []

    # def update(self, subject):
    #    return super().update(subject)
    
    def update(self, name , message):
        print(f"test {name}, {message}")

    def get_money(self):
        return self.money
    
    def pay(self, price, platform):
        if self.money - price < 0:
            platform.detach(self)
        else:
            self.money = self.money - price

        