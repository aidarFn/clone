class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        try:
            return self.value / other.value
        except ZeroDivisionError:
            print('на 0 нельзя')

a = Calculator(15)
b = Calculator(0)

print(a+b)
print(a-b)
print(a*b)
print(a/b)