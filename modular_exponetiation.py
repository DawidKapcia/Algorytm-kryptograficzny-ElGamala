def mod_power(a, b, c):
    
    x = 1
    y = a
 
    while b > 0:
        
        if b % 2 != 0:
            x = (x * y) % c
            
        y = (y * y) % c
        b = b // 2
 
    return x % c
