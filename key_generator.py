def key_generator():
    
    p = prime(a, b)
    alpha = alpha_generator(p)
    a = random.randint(1, p-2)
    
    a_alpha = mod_power(alpha, a, p)
    
    return p, alpha, a_alpha, a
