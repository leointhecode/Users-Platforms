class Strategy:
    def execute(self, num):
        pass

class StrategySpotify(Strategy):
    def execute(self, num):
        if num == "free":
            return 0
        elif num == "base":
            return 80

class StrategyDisney(Strategy):
    def execute(self, num):
        if num == "trial":
            return 130
        if num == "base":
            return 160

class StrategyNetflix(Strategy):
    def execute(self, num):
        if num == "oneDevice":
            return 120
        elif num == "twoDevice":
            return 170
        elif num == "fourDevice":
            return 200

class StrategyHBO(Strategy):
    def execute(self, num):
        if num == "trial":
            return 0
        elif num == "base":
            return 140

class StrategyAmazon(Strategy):
    def execute(self, num):
        if num == "base":
            return 110
        elif num == "premium":
            return 150


class Subject:
    def __init__(self):
        self.observers = []
        self.exObserver = []

    def attach(self, observer):

        self.observers.append(observer)
        
        if observer in self.exObserver:

            print(f"Bienvenido de vuelta {observer.name}")

        else:

            print(f"Hello {self.observers[-1].name}")     

    def detach(self, observer):

        self.observers.remove(observer)
        self.exObserver.append(observer)
        print(f"Lamentamos que nos dejes {observer.name}")

    def notify(self, message):
        for observer in self.observers:
            observer.update(self, observer.name     , message)





class Platform(Subject):
    def __init__(self, strategy):
        super().__init__()
        self.name = ""
        self.recomendaciones = []
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def level(self, num):
        return self.strategy.execute(num)
