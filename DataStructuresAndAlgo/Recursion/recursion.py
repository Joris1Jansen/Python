def factorial(n):
    assert n >=0 and int(n) == n, 'The number must be positive and integer only'
    if n < 0:
        return n
    else:
        return n * factorial(n - 1)

print(factorial(4))