import sympy

def isPrime(number):
    if not sympy.isprime(number):
        return False
    return True


def test_small_2():
    assert isPrime(2) == False

def test_small_3():
    assert isPrime(3) == True

def test_small_21():
    assert isPrime(21) == False
