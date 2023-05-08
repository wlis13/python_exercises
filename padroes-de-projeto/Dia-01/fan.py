class Fan:
    def __init__(self, price, brand, power, voltage, size, maximum_rotation):
        self._price = price
        self._brand = brand
        self._power = power
        self._voltage = voltage
        self._size = size
        self._maximum_rotation = maximum_rotation


first_fan = Fan(250.98, 'toshiba', 1200, 110, 'pequeno', 300)
second_fan = Fan(354.98, 'max wind', 1500, 110, 'médio', 430)
thirth_fan = Fan(550.90, 'max wind', 1800, 110, 'grande',  650)
