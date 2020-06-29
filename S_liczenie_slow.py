""""
policz wystąpienia poszczególnych słów w tekście. Wyświetl słownik złożony z par {'słowo': liczba_wystąpień, }

Przykład
Na wejściu otrzymujemy tekst.

the quick brown fox jumps over the lazy dog.
Dane wyjściowe:

{'the': 2, 'jumps': 1, 'brown': 1, 'lazy': 1, 'fox': 1, 'over': 1, 'quick': 1, 'dog.': 1}
"""


def word_count(text):
    dict_word = {}
    text_words = text.split()    #tworzy liste z tekstu, poprzez pociecie go na elementy
    for word in text_words:
        if dict_word.get(word):
            dict_word[word] += 1     #odwolujemy sie bezposrednio do word i inkrementujemy o 1
        else:
            dict_word[word] = 1      # sipledict {'key':value} gdzie [word] to key
    return dict_word


def main():
    text = input('Type something:  ')
    print(word_count(text))

main()
