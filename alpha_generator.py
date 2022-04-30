def alpha(p):
    
    while True:
        alpha = random.randint(2, p-1)
        
        if (p-1) % alpha != 1:
            return alpha
