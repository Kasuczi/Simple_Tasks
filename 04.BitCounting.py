def countBits(n):
    binary = bin(n)[2:]
    counter = 0
    
    for i in binary:
        if i == '1':
            counter += 1
    
    return counter