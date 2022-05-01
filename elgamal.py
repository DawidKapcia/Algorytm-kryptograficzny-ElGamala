import random
import sympy

def key():
    
    p = prime(a, b)
    alpha = generator_alpha(p)
    a = random.randint(1, p-2)
    
    a_alpha = mod_power(alpha, a, p)
    
    return p, alpha, a_alpha, a


def encryption(m, p, alpha, a_alpha):
 
    k = random.randint(1, p-2)
    
    gamma = mod_power(alpha, k, p)
    delta = m * mod_power(a_alpha, k, p)
 
    return gamma, delta


def decryption(gamma, delta, p, a):
    
    pom = mod_power(gamma, p-1-a, p)
    m = (pom * delta) % p
    
    return m


def ElGamal(m, a, b):
    
    sep = 60 * "-"
    
    print("%s\nInput message:\t%s\n%s" % (sep, m, sep))
    
    p, alpha, a_alpha, a = key()
    print("\nPublic key:\n\np = %s\nalpha = %s\na_alpha = %s\n%s" % (p, alpha, a_alpha, sep))
    
    gamma, delta = encryption(m, p, alpha, a_alpha)
    print("\nEncrypted message:\n\n(%s, %s)\n\n%s" % (gamma, delta, sep))
    
    m = decryption(gamma, delta, p, a)
    print("\nDecrypted message:\n\n%s\n\n%s" % (m, sep))
