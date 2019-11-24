import re

def generate_hashtag(s):
    lst = []
    container = re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
    lambda mo: mo.group(0)[0].upper() +
    mo.group(0)[1:].lower(),s)
    
    for i in container:
        lst.append(i)
    lst.insert(0, '#')
    txt = ''.join(lst)
    if len(txt) > 140:
        return False
    elif len(txt) <= 1:
        return False
    else:
        return txt.replace(' ', '')