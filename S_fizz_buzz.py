"""
Napisz program, który wyświetla liczby od 1 do N.
Dla liczb podzielnych przez 3 niech program wyświetli „Fizz”;
dla liczb podzielnych przez 5 niech wyświetli ‚Buzz’;
a dla liczb podzielnych przez 15 niech wyświetli ‚FizzBuzz’.
"""

def fizzbuzz(n):
    for i in range(1, n+1):
        if  i% 15 == 0:
            print('FizzBuzz')
        elif i% 5 == 0:
            print('Buzz')
        elif  i% 3 == 0:
            print('Fizz')
        else:
            print(i)


def main():
    n = int(input("Provide number: "))
    fizzbuzz(n)

main()
