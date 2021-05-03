def sumdiggets(n):
    assert n >=0 and int(n) == n, 'The number must be positive and integer only'
    if n == 0:
        return 0
    else:
        return int(n%10) + sumdiggets(int(n/10))

print(sumdiggets(111))