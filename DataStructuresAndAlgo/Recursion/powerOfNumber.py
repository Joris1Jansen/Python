def powerOfNumber(base, exponent):
    assert exponent >= 0 and int(exponent) == exponent, 'The must be a positive interger'
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    else:
        return base * powerOfNumber(base, exponent - 1)

print(powerOfNumber(2, 2))