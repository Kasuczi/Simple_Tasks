#ZAJECIA NR1
#Dive into python -- ksiazka na ktora warto zwrocic uwage !
#ID - zintergoiwane srodowisko programistyczne
#

#program ma przyjac dwie dane wzrost i wage.
#pass - funkcja pusta
# """""" automatycznie dodaje info o tym czym zajmie sie funkcja
#kazda funkcja przyjmuje argumenty ale nie kazda zwraca
#Listy moga przechowywyac dane roznych typow, string, intiger itp.
# += powowduje inkrementacje
# range to funkcja, ktora tworzy liste wartosci

def compute_bmi(weight, height):              #funkcja przyjmuje dwie zmienne, dwa parametry, w momencie gdy jest wykonywana dwa argumenty
    """
    Calculate BMI and return category
    :param weight:
    :param height:
    :return:
    """
    bmi = weight/height **2                           # bmi - zmienna rozumiana jako nazwa wartosci wynikajacej z dzialania w tym wypadku**2 do potegi,

    if bmi < 18.5:                                     #sprawdza czy wynik miesci sie w przedzialach
        result = "To less"                             #jesli tak zwraca  wartosc result
    elif bmi > 25:                                     #jesli nie sprawdza kolejny
        result = "overweight"                           # zwraca wartosc result
    else:
        result = "normal"
    print(bmi)                                          #zwraca wartosc bmi
    return result                                       #zwraca przedzial w ktorym bmi sie znajduje
returned_bmi = compute_bmi(81,1.89)                     #przypisuje argumenty funkcji do kolejnej zmienne pozwalajac obliczyc wynik
print(returned_bmi)                                     #zwraca obliczony wynik

if __name__ == '__main__':                               #jezeli jest uruchomiony ten plik pythona to wykonaj to w tym bloku !
    weight = float(input("Your weight is [kg]: "))       #input to funkcja umozliwajaca wczytywanie danych od uzytkownika
    height = float(input("Your height is [m]: "))        #float konwertuje string do liczby w formacie zmiennoprzecinkowej
    user_result = compute_bmi(weight, height)
    print(f'You are {user_result}')                       #f'{a} zwraca wartosc a, podobnie jak print tzw f-string


###############################################################################
#petla for

def sheldon_knock(name):
    for i in range(3):                    # range(3) -> [0,1,2] Stanowi ile razy wykona sie petla, 3 jest iloscia pozycji na liscie, i jest stala
        print(f'{name} - {i}')            #

sheldon_knock('Penny')                    #Penny jest przypisywane do name

###############################################################################
#petla for w listach
some_list = ['a', 'b', 'c']
for i, item in enumerate(some_list):            # enumerata pozwala wyswietlic numery a nie wartosci z listy, czyli ktora pozycja na liscie
    print(i, item)                              # i = pozycja, item = wartosc pozycji
###############################################################################
#petla while

def count_down(number):

    while number > 0:                         #uruchamia sie petla, wykonuje sie dopoki number > 0
        print(number)                         #wywoluje argument funkcji
        number -= 3                           #dekrementacja

    print('Lift of!')                         #komunikat po udanej dekrementacji do 0

count_down(10)                                #funkcja(argument)

################################################################################3

def even_count_down(number):
    while number:
        number -= 1                           # dekrementacja
        if number % 2:                        # jezeli parzysta
            continue                          #jezeli warunek spelniony to continue
        print(number)

    print('Lift of!')

even_count_down(10)

###############################################################################
def permature_lift_off(number):
    while number > 0:                                         # petla uruchamia sie gdy warunek jest spelniony
        print(number)
        if number == 5:                                       # jezeli number =5
            break                                             # to zatrzymaj wykonywanie pentli
        number -= 1                                           # dekrementacja

    print("lift off")

permature_lift_off(10)
###############################################################################

##Listy
#append - pozwala dodac element do listy
#pop - usuwa element i zwraca tak aby mozna bylo na przyklad przypisac go do zmiennej

my_list = [1, 1.5, "abc", None, True]
print(my_list)

my_list.append({1,2,2})                            #dodaje do listy wartosci {1,2,2} ale bez duplikatów
print(my_list)

removed_element = my_list.pop(1)                   #usuwa z listy wartosc o indexie 1 czyli 1.5
print(my_list)

my_list[-1].remove(1)                              #usowa drugi pod konca index
print(my_list)


################################################################################
#SETY
# add - dodaje
# remove - usowa, chodz pop tez dziala
my_set = ['a','b','c']
removed = my_set.pop(1)                           #usuwa z setu wartosc o indeksie 1
print(my_set)


my_set = ['a','b','c']
removed = my_set.remove('a')                           #usuwa z setu wartosc a
print(my_set)
print(len(my_set))                                     #dlugosc listy

################################################################################
#Slowniki
# kluczem moze byc dowoly typ haszowalny a jest to typ niezmienny i prosty (liczba calkowita, zmiennoprzecinkowa, string, bool, tulpa ale juz nie lista poniewaz jest niezmienna)
my_phonebook = {
    'police': 997,
    'my_girlfriend': None,
    'home': 605,
    'pizza': 555,
}
print(my_phonebook)
my_phonebook['sda'] = 343                  #dodaje do slownika wartosc o wybranej w [nazwie]

print(my_phonebook)


my_old_phonebook = {
    'ex':111,
    'boss':1211
}
my_phonebook.update(my_old_phonebook)       #dodaje do slownika wartosci z innego
print(my_phonebook)

del my_phonebook['ex']                      #usuowa ze slownika [wartosc]
print(my_phonebook)
print(my_phonebook['boss'])                 #zwraca konkretna [wartosc] ze slownika
print(my_phonebook.get('emergency', 112))   #sprawdza czy jest taka wartosc i zwraca ja, lub domyslna 112

my_phonebook['boss'] ={                      #slownik zagniezdzony w slowniku
    'home': 666,
    'mobile': 444,
}
print(my_phonebook)
################################################################################
#ZADANIE - slack tresc
#sprawdza czy rok przestepny
#podzielny przez 4,
#nie jest podzielny przez 100, chyba że
#jest podzielny przez 400.

def is_leap(year):
    if not year %4:                    #podzielny przez 4,
        if year %100 or not year %400: #nie jest podzielny przez 100, chyba że jest podzielny przez 400.
            return True

    return False

print(is_leap(2016))
print(is_leap(2500))
print(is_leap(2015))

#inny zapis tego samego
def is_leap_2(year):
    if not year %4 == 0:
        if year %100 or  year %400 ==0 :
            return True

    return False
print(is_leap_2(2016))
print(is_leap_2(2500))
print(is_leap_2(2015))

# w jednej linicje

def is_leap_3(year):
    return year % 4==0 and (year % 100 or year % 400 ==0)

if __name__ == '__main__':
    user_year = int(input("please provide year: "))
    result = is_leap(user_year)
    print(f'{user_year} is leap?  {result}')
################################################################################
# DNA -> RNA

"""Transcribe RNA"""
TRANSCRIPTION = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
}

def transcribe_rna(dna):
    """
    Get DNA and return valid RNA
    :param dna:
    :return:
    """
    rna = ''                          #okresla ze bedzie rna mialo jakas wartosc
    for letter in dna:                #dla litery z dna
        rna += TRANSCRIPTION[letter] #wykonal rna += slownik[literka z lancucha znakow]
    return rna                        #zwraca jej wartosc

def validate_dna(dna):
    """
    Validate if DNA contains only valid letters
    :param dna:
    :return:
    """
    dna_set = set(dna)
    dna_keys = set(TRANSCRIPTION.keys())
    return dna_set.issubset(dna_keys)       #sprawdza czy dna_set jest w zbiorze dna_keys

if __name__ == '__main__':
    while True:
        user_dna = input('Please provide DNA: ')
        if validate_dna(user_dna):
            rna = transcribe_rna(user_dna)
            print(f'RNA is: {rna}')
        else:
            print('Provide correct data')



################################################################################
#ZADANIE 2
"""
Zwróć średnią wartość z listy liczb całkowitych,
która jest średnią arytmetyczną wszystkich wartości z wyjątkiem najmniejszej i największej.
Jeżeli wartość najmniejsza lub największa występuje wielokrotnie w liście.
Pomiń tylko pojedyncze wystąpienie każdej z nich. Załóż, że lista ma conajmniej 3 elementy.

"""

def avg_list(numbers):
    numbers.sort()                         #sortuje rosnaco argumenty funkcji
    print(numbers)
    sliced_numbers = numbers[1:-1]         #wycina pierwszy i ostatni wynik na liscie
    print(sliced_numbers)                   #wyswietla wycieta liste
    sum_of_sliced = sum(sliced_numbers)     #sumuje
    return sum_of_sliced/len(sliced_numbers)  #liczy srednia poprzez podzieleni przez odcieta liste


lista_test = [1,1,5,5,10,8,7]
avg_list(lista_test)

if __name__ == '__main__':
    list_lenght = int(input('Please input some data: '))   #okresla dlugosc listy
    user_list = []
    for i in range(list_lenght):                          #dla kazdego i przypisuje
        item = float(input('type a number: '))             #wartosc wybrana przez usera i powtarza pentel
        user_list.append(item)                              #poki nie zotsanie osiagnieta liczba wartosci z dlugosci listy

    print(f'List your provided: {user_list}')
    print(f'Centred avg', avg_list(user_list))
################################################################################
