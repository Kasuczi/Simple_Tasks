def remove_smallest(numbers):
    """
    the func returns array of integers, with removed the smallest value
    """
    x = numbers[:]
    if x:
        x.remove(min(x))
    return x
