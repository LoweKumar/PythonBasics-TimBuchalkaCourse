def fibonacci(number: int) -> int:
    """Return the `n` th fibonacci number , for the positive 'n'."""

    if 0<= number <=1:
        return number

    n_minus1, n_minus2 = 1, 0

    result = None
    for i in range(number-1):
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result

    return result

for i in range(10):
    print(i,fibonacci(i))
