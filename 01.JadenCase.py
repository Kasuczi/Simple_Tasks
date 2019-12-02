import re
def toJadenCase(string):
    """
    The func returns upper case for every word in the string
    """
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
     lambda mo: mo.group(0)[0].upper() +
     mo.group(0)[1:].lower(),string)
