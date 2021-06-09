def fibMemo(n, memo={}):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    if not n in memo:
        memo[n] = fibMemo(n-1, memo) + fibMemo(n-2, memo)
    return memo[n]


print(fibMemo(6))