import client


class Fan:
    def __init__(self, price, brand, power, voltage, size, maximum_rotation):
        self._price = price
        self._brand = brand
        self._power = power
        self._voltage = voltage
        self._size = size
        self._maximum_rotation = maximum_rotation

    def buy_fan(self, clients):
        if clients._account_value < self._price:
            raise ValueError("desculpe mais sua conta não tem recurso suficiente")
        clients.has_a_fan = True
        return clients

    def __str__(self):
        return f"""
            price: {self._price}
            brand: {self._brand}
            power: {self._power}
            voltage: {self._voltage}
            size: {self._size}
            maximum_rotation: {self._maximum_rotation}
        """


first_fan = Fan(250.98, 'toshiba', 1200, 110, 'pequeno', 300)
second_fan = Fan(354.98, 'max wind', 1500, 110, 'médio', 430)
thirth_fan = Fan(550.90, 'max wind', 1800, 110, 'grande',  650)

first_buy = first_fan.buy_fan(client.first_client)
print(first_buy)
