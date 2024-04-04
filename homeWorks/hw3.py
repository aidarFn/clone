class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        plusmoney = float(input('Введите сумму для добавления на ваш счет: '))
        self._balance += plusmoney
        print(f'Ваша сумма: {self._balance}')

    def _kill(self):
        self._balance = 0
        print('Ваш счет обнулен')

    def _jackpot(self):
        self._balance *= 10

    def getbalance(self):
        return self._balance

    def sum_money(self, other):
        mybalance = self._balance
        otherbalance = other.getbalance()


        self._balance += otherbalance
        other._balance = client2.getbalance()  # Устанавливаем баланс второго клиента равным 100
        print(f'Баланс после объединения: {self._balance}')

client1 = Bank('', 100)
client2 = Bank('Азамат', 1000)


print(f'Мой баланс {client1._name}: {client1.getbalance()}')
print(f'Баланс {client2._name}: {client2.getbalance()}')

client1.moneyX()


client1.sum_money(client2)


print(f'Мой баланс {client1._name}: {client1.getbalance()}')
print(f'Баланс {client2._name}: {client2.getbalance()}')
