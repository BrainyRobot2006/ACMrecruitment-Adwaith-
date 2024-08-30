import math
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)
def multipleNumbers(numbers):
    result = 1
    for number in numbers:
        result = lcm(result, number)
    return result

numbers = range(1, 20)
smallest_multiple = multipleNumbers(numbers)
print(smallest_multiple)
