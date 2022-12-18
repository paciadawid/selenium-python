class Calculator:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            return False
        return a / b

    def inverse(self, a):
        if a == 0:
            return False
        return 1 / a


calculator = Calculator()
print(calculator.add(0, 1))
