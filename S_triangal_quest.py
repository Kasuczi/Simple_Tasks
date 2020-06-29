"""
Dane wejściowe
Dana jest liczba całkowita dodatnia N taka, że 1<=N<=9

Zadanie
Wyświetl trójkąt liczb w wierszach N-1, czyli dla N=6
"""

def number_triangle(n):
    for i in range(n):
        print(str(i)*i)

number_triangle(10)
