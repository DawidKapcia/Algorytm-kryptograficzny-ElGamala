def mod_power(a, b, c):
    
    x = 1
    y = a
 
    while b > 0:
        
        if b % 2 != 0:
            x = (x * y) % c
            
        y = (y * y) % c
        b = b // 2
 
    return x % c


def prime(a, b):
    
    p = random.randint(a, b)
    
    while not sympy.isprime(p):
        p = random.randint(a, b)
    
    return p
  

def alpha_generator(p):
    
    while True:
        alpha = random.randint(2, p-1)
        
        if (p-1) % alpha != 1:
            return alpha
