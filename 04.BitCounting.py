def countBits(n):
    """
    the func returns the number of bits that are equal to one in the binary representation of that number.
    """
    binary = bin(n)[2:]
    counter = 0
    
    for i in binary:
        if i == '1':
            counter += 1
    
    return counter
