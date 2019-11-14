def remove_smallest(numbers):
    x = numbers[:]
    if x:
        x.remove(min(x))
    return x