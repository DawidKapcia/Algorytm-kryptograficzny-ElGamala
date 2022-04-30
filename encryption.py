def encryption(m, p, alpha, a_alpha):
 
    k = random.randint(1, p-2)
    
    gamma = mod_power(alpha, k, p)
    delta = m * mod_power(a_alpha, k, p)
 
    return gamma, delta
