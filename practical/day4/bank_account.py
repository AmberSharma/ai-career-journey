class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def __str__(self):
        return f"Name: {self.name}, Balance: {self.__balance}"

obj = BankAccount("Amber", 10000)
print(obj)
obj.deposit(500)
print(obj)
obj.withdraw(200)
print(obj)