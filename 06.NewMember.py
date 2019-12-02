def openOrSenior(data):
    """
    the func returns data depends on if a member is senior or regular
    """
    lst = ''
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            lst += 'Senior' + ','
        else:
            lst += 'Open' + ','
    result = lst.split(',')
    return result[:-1]
