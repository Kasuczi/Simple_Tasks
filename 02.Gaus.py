def f(n):
    lst = []
    if isinstance(n, int) and n > 0:
        for i in range(n + 1):
            lst.append(i)
    else:
        return None
    return sum(lst)