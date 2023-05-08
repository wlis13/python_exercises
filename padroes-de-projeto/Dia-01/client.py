class Client:
    def __init__(self, name, cpf, identity, phone, address, number_address):
        self._name = name
        self._cpf = cpf
        self._identity = identity
        self._phone = phone
        self._address = address
        self._number_address = number_address


first_client = Client(
    'Gustavo Santos',
    '145.362.158-98',
    'SC: 01.248.369',
    '(31) 94587-2514',
    'Rua: Delfino Duarte/Dom Bosco',
    1478)
second_client = Client(
    'Adriana Gonçalves',
    '147.288.369-12',
    'MG: 9.562.348',
    '(33) 98747-1256',
    'Rua: Reginal Amaral/Sintia',
    146)
thirth_client = Client(
    'Eliza Martins',
    '956.236.158-47',
    'MS: 14.123.321',
    '(25) 97845-2365',
    'Rua: Rezende Siqueira/Santo Antônio',
    958)
