# 5! = 1*2*3*4*5
# 3! = 1*2*3
# 1! = 1
# 0! = 1
# no negative value


def factorial(n):
    if type(n) != int:
        return False

    if n < 0:
        return False
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i  # result = result * i
    return result
