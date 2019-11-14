def openOrSenior(data):
    lst = ''
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            lst += 'Senior' + ','
        else:
            lst += 'Open' + ','
    result = lst.split(',')
    return result[:-1]