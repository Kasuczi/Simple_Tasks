# metody do list itp
# min - zwraca najmniejszy element
# max - zwraca najwiekszy element
# sum - zwraca sume elementow
# len - zwraca dlugosc listy
# reversed - odwraca liste
# sorted  - umozliwia sortowanie listy  z kopiowaniem
# sort - sortuje ale bez kopii
# ZADANIE
"""
Izogram jest słowem w którym żadna litera nie powtarza się.
Przykładem jest np. słowo “skrzynia”.
Należy napisać program który poprosi użytkownika o podanie słowa i napisze czy dane słowo jest izogramem czy nie.
"""

def is_iso(phrase):
    for letter in phrase:
        how_many = phrase.count(letter)
        if how_many > 1:
            return ('not iso')
        break

    return ('it is iso')

print(is_iso('skrzynia'))

########################### LUB ###########################

def is_isogram_set(word):
    word_set = set(word)                        #przypisuje do zmiennej zbior word jednoczesnie konwertuje stringa na zbior
    if len(word_set) == len(word):              # sprawdza dlugosc tym samym ilosc liter
        return 'isogram'                        #zwraca wartosc jesli warunek powyzej spelniony
    return 'not isogram'                        # zwraca wartosc jesli nie jest spelniony

print(is_isogram_set('skrzynia'))


########################### LUB ###########################

def is_isogram_sets(word):
    result = 'isogram'
    for i in  word:
        if word.count(i) > 1:
            result = 'not isogram'
    return result

def main():
    word = input('Please provide word')     #pozwala wprowadzic wlasne slowo
    result_fun = is_isogram_sets(word)
    print(f'Your word is {result_fun}')

main()
