def sumDigits(number):
    a = [int(i) for i in str(abs(number))]
    return sum(a)