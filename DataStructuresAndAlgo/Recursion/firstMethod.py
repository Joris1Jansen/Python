def firstMethod():
    secondMethod()
    print("I am first")

def secondMethod():
    thirdMethod()
    print("I am second")

def thirdMethod():
    fourthMethod()
    print("I am third")

def fourthMethod():
    print('finish')
    
firstMethod()