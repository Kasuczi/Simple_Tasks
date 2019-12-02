def sumDigits(number):
    """
    the func returns the sum of the absolute value of each of the number's decimal digits
    """
    a = [int(i) for i in str(abs(number))]
    return sum(a)
