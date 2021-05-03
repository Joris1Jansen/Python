def fibonacco(n):
    assert n >=0 and int(n) == n, 'The number must be positive and integer only'
    if n in [0,1]:
        return n
    else:
        return fibonacco(n-1) + fibonacco(n-2)

print(fibonacco(9))