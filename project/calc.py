def fact(n):
    if n < 0:
        raise ValueError("Negative input not allowed")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def gcd(a, b):
 
    a, b = abs(a), abs(b)
    
    if a == 0 and b == 0:
        return 0
    elif a == 0:
        return b
    elif b == 0:
        return a
    
    while b != 0:
        a, b = b, a % b
    return a
