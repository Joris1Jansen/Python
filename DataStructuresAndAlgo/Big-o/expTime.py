def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(8))

fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]