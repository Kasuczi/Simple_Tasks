def openOrSenior(data):
    """
    the func returns the sum of the absolute value of each of the number's decimal digits
    """
    lst = ''
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            lst += 'Senior' + ','
        else:
            lst += 'Open' + ','
    result = lst.split(',')
    return result[:-1]
