def prime(a, b):
    
    p = random.randint(a, b)
    
    while not sympy.isprime(p):
        p = random.randint(a, b)
    
    return p
