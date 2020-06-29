lst = [1, 0, 0, 1, 1, 1, 0, 1]

def is_chain(n):
    gen = list(lst[i:i + 3] for i in range(len(lst)))
    for i in gen:
        if sum(i) == n:
            return True
    return False


print(is_chain(3))
print(is_chain(1))
print(is_chain(2))
print(is_chain(4))