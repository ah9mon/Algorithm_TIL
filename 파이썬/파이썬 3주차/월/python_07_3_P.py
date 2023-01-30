# 1 + 2
# 2 – 1
# 3 * 4
# 4 / 0

class Calculator:

    def add(n1, n2):
        return n1 + n2

    def substract(n1, n2):
        return n1 - n2

    def multiply(n1, n2):
        return n1 * n2

    def divide(n1, n2):
        if n2 == 0:
            return f'0으로 나눌 수 없습니다.'
        else:
            return n1 / n2

print(Calculator.add(1,2))
print(Calculator.substract(1,2))
print(Calculator.multiply(1,2))
print(Calculator.divide(1,2))