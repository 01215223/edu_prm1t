# Laboratorium3 Zadanie1
# Program do rozwiązywania równania kwadratowego ax^2 + bx + c = 0

# Pętla while do poprawnego wczytania trzech liczb
while True:
    try:
        print("Podaj współczynniki równania kwadratowego.")
        a = float(input("Podaj a: "))
        b = float(input("Podaj b: "))
        c = float(input("Podaj c: "))
        break  # Wyjście z pętli, jeśli dane są poprawne
    except ValueError:
        print("To nie jest poprawna liczba! Spróbuj ponownie.\n")

# Informowanie użytkownika o rozpoczęciu obliczeń
print(f"\nRozwiązuję równanie: {a}x^2 + ({b})x + ({c}) = 0")

# Przypadek 1: Równanie liniowe (a == 0)
if a == 0:
    if b == 0:
        if c == 0:
            print("Równanie tożsamościowe (nieskończenie wiele rozwiązań).")
        else:
            print("Równanie sprzeczne (brak rozwiązań).")
    else:
        x = -c / b
        print(f"To jest równanie liniowe. Jedno rozwiązanie: x = {x}")

# Przypadek 2: Równanie kwadratowe (a != 0)
else:
    # Obliczanie wyróżnika równania (delty)
    dt = b**2 - 4 * a * c
    print(f"Delta wynosi: {delta}")

    # Instrukcja warunkowa sprawdzająca liczbę rozwiązań w zbiorze liczb rzeczywistych
    if dt > 0:
        # Dwa rozwiązania
        x1 = (-b - dt**0.5) / (2 * a)
        x2 = (-b + dt**0.5) / (2 * a)
        print(f"Delta > 0. Równanie ma dwa rozwiązania: x1 = {x1} oraz x2 = {x2}")
    elif dt == 0:
        # Jedno rozwiązanie
        x0 = -b / (2 * a)
        print(f"Delta = 0. Równanie ma jedno rozwiązanie: x0 = {x0}")
    else:
        # Brak rozwiązań rzeczywistych
        print("Delta < 0. Równanie nie ma rozwiązań w zbiorze liczb rzeczywistych.")
