def factorial(number: int) -> int:
    if number <= 1:
        return 1

    result = 2
    for x in range(3, number+1):
        result *= x

    return result


for i in range(10):
    print(i, factorial(i))