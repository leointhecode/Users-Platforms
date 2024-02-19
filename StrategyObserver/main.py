from User import User
from Plataform import Platform, StrategyAmazon, StrategyDisney, StrategyHBO, StrategyNetflix, StrategySpotify

spotify = Platform(StrategySpotify())

Alicia = User("ALicia", 50)
Leo = User("Leo", 2000)

spotify.attach(Alicia)
spotify.attach(Leo)

print(Alicia.get_money())

Alicia.pay(spotify.level("base"), spotify)

print(f"The account has: {Alicia.get_money()}")

print(spotify.observers)

spotify.attach(Alicia)

print(spotify.observers)

spotify.notify("TESSSSTTTT")


#TODO Revisar notify
#TODO Cambiar sistema de pago para tomar en cuenta la cuenta de los meses
#TODO Implementar response en .txt
