def is_square(n):    
    if n < 0:
        return False
    sqrt = n ** (1 / 2)
    number_dec = str(sqrt-int(sqrt))[1:]
    if len(number_dec) > 2:
        return False
    else:
        return True