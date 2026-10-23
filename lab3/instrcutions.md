Napisane programy zapisz na wydziałowym Gitlabie i daj dostęp do repozytorium prowadzącym. 
https://gitlab-stud.elka.pw.edu.pl
 

Zadanie 1 (2p) 
Napisz program, który:
1. (0.5p) za pomocą pętli While wczyta liczby a, b, c. 
2. (1.5p) przy pomocy instrukcji warunkowej wskazać rozwiązania (w zbiorze liczb rzeczywistych) równania 
ax2+bx+c=0
Przykład zastosowania elif: 
if x > y:
print(„x jest większe od y")
elif x == y:
print(„x i y są sobie równe")
else: print(„y jest większe od x")
Dodaj komentarze w programie poprzedzone „#” oraz wyświetlane na ekranie aby użytkownik był informowany co 
wykonuje program.


Zadanie 2 (3p) 
Mając do dyspozycji listę [7, 5.5, 2, 4, 3, 3.5, 5, 6, 1, 1, 1.1, 10, 8, 9, 8.5] napisz program, który ją:
1. – (0.5p) posortuje rosnąco, 
2. – (0.5p) posortuje malejąco, 
3. – (1.5p) wskaże element będący ostatnią cyfrą numeru Twojego albumu, 
4. – (0.5p) wskaże ile jest liczb w tej liście. 
Dodaj komentarze w programie poprzedzone „#” oraz wyświetlane na ekranie aby użytkownik był informowany co 
wykonuje program.


Źródła
1. https://gitlab-stud.elka.pw.edu.pl/prm1t-26z/prm1t-26z
2. https://docs.python.org/pl/3.12/tutorial/datastructures.html
3. https://docs.python.org/pl/3.12/tutorial/introduction.html
4. https://docs.python.org/pl/3.12/tutorial/datastructures.html#looping-techniques
Komendy Git 
$ git init # Inicjalizuje nową bazę danych Gita 
$ git clone # Kopiuje istniejące pliki projektu z Gita 
$ git status # Sprawdza status lokalnego projektu 
$ git diff # Pokazuje zmiany wprowadzone do projektu 
$ git add # Poleca Gitowi, aby dodał plik(i) 
$ git commit # Zapisuje bieżący stan projektu 
$ git push # Kopiuje lokalne pliki na zdalny serwer Gita
$ git log # Sprawdza historię projektu
$ git branch # Wyświetla listę gałęzi, tworzy je albo usuwa
$ git merge # Scala historię dwóch gałęzi
$ git stash # Składuje bieżące zmiany do wykorzystania późnie