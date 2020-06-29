def is_palidrome(word):
    if word.lower() == word.lower()[::-1]:
        return True
    else:
        return False

print(is_palidrome('Ala'))
print(is_palidrome('test'))

#inna wersja to

def is_palidrome2(word):
    for i, j in zip(word, word[::-1]):
        if i != j:
            return False
    return True

print(is_palidrome2('ala'))
print(is_palidrome2('test'))

#inna jeszcze wersja

def is_palidrome3(word):
    return all([a == b for a, b  in zip(word, word[::-1])])

print(is_palidrome3('tattarrattat'))
print(is_palidrome3('test'))