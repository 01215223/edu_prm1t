# Laboratorium3 Zadanie2
# Lista wejściowa podana w treści zadania
liczby = [7, 5.5, 2, 4, 3, 3.5, 5, 6, 1, 1, 1.1, 10, 8, 9, 8.5]

# STAŁA: TUTAJ WPISZ SWÓJ NUMER ALBUMU
NR_ALBUMU = "12345"  

print("Rozpoczynam działanie programu...")
print(f"Lista początkowa: {liczby}\n")

# 1. Sortowanie rosnąco (0.5p)
# Używamy metody sort(), która modyfikuje listę na miejscu w porządku rosnącym
liczby.sort()
print("1. Wynik sortowania rosnąco:")
print(liczby, "\n")

# 2. Sortowanie malejąco (0.5p)
# Używamy argumentu reverse=True, aby odwrócić kolejność na malejącą
liczby.sort(reverse=True)
print("2. Wynik sortowania malejąco:")
print(liczby, "\n")

# 3. Wskazanie elementu będącego ostatnią cyfrą numeru albumu oraz jego indeksu (1.5p)
# Pobieramy ostatni znak ze stałej NR_ALBUMU i zamieniamy go na liczbę (int)
ostatnia_cyfra = int(NR_ALBUMU[-1])
print(f"3. Szukanie elementu na podstawie numeru albumu ({NR_ALBUMU}):")
print(f"Ostatnia cyfra Twojego albumu to: {ostatnia_cyfra}")

# Sprawdzamy, czy ta cyfra znajduje się w naszej liście i wskazujemy jej pozycję
if ostatnia_cyfra in liczby:
    # Metoda .index() zwraca pozycję pierwszego wystąpienia elementu (indeksowanie od 0)
    indeks = liczby.index(ostatnia_cyfra)
    print(f"Sukces! Liczba {ostatnia_cyfra} znajduje się na liście pod indeksem: {indeks}")
else:
    print(f"Informacja: Liczby {ostatnia_cyfra} nie ma na liście.")
print()

# 4. Wskazanie ile jest liczb w tej liście (0.5p)
# Używamy wbudowanej funkcji len(), która zwraca liczbę elementów w kolekcji
ilosc_elementow = len(liczby)
print("4. Liczenie elementów w liście:")
print(f"W liście znajduje się dokładnie {ilosc_elementow} liczb.")
