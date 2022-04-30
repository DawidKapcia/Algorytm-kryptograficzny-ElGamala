def decryption(gamma, delta, p, a):
    
    pom = mod_power(gamma, p-1-a, p)
    m = (pom * delta) % p
    
    return m
