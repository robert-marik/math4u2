---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- kombinatoryka, prawdopodobieństwo, statystyka
- statystyki
- matematyka finansowa
is_finished: true
---



# Odczytywanie danych z wykresu


Czeski Urząd Statystyczny (CSO) został założony w 1969 roku i pełni funkcję głównej instytucji odpowiedzialnej za oficjalne statystyki w kraju.
Jego rolą jest gromadzenie, przetwarzanie i publikowanie danych statystycznych dotyczących różnych aspektów życia w Czechach i ich regionach.
Na oficjalnej stronie internetowej <https://www.czso.cz/> można uzyskać swobodny dostęp do wykresów i tabel podsumowujących np.
trendy demograficzne, wyniki wyborów, wypadki drogowe, ceny nieruchomości i stopy bezrobocia. W poniższych ćwiczeniach przeanalizujemy jeden
z tych wykresów. Odczytywanie danych z wykresu


![Headquarters of the Czech Statistical Office in Prague (2017)](03_graf_csu.jpg)

Wśród zasobów udostępnionych przez Czeski Urząd Statystyczny znajduje się wykres przedstawiający zmiany średniego miesięcznego wynagrodzenia brutto, 
przedstawiony na rysunku 2. Oś pozioma przedstawia kwartały obserwowanych lat. Niebieskie słupki przedstawiają średnie wynagrodzenie brutto w ujęciu nominalnym w danym 
czasie, a czerwona linia wskazuje trend wynagrodzenia nominalnego skorygowanego o efekty sezonowe. Obie te wartości odczytuje się z lewej osi pionowej 
w koronach czeskich. Jasnoniebieska linia przedstawia stopę wzrostu wynagrodzenia nominalnego (odczytuje się ją z prawej osi pionowej w procentach), a ciemnoniebieska 
linia przedstawia stopę wzrostu wynagrodzenia realnego (odczytuje się ją również z prawej osi pionowej).

![Average Monthly Wage and Wage Growth](03_graf_1.jpg)

**Słownik**

Od *wynagrodzenia brutto* wypłacanego przez pracodawcę potrącane są składki na ubezpieczenie zdrowotne i społeczne oraz podatek dochodowy. Pracownik otrzymuje wówczas wynagrodzenie netto, które jest niższe o kwotę tych potrąceń.

*Wynagrodzenie nominalne* to miesięczne wynagrodzenie brutto wyrażone w koronach czeskich. Wynagrodzenie nominalne skorygowane o czynniki sezonowe to wynagrodzenie nominalne zmodyfikowane statystycznie w celu wyeliminowania wpływu sezonowych zmian w zatrudnieniu i wynagrodzeniach.

**Słownik**

Od *wynagrodzenia brutto* wypłacanego przez pracodawcę potrącane są składki na ubezpieczenie zdrowotne i społeczne oraz podatek dochodowy. Pracownik otrzymuje wówczas wynagrodzenie netto, które jest niższe o kwotę tych potrąceń.

*Wynagrodzenie nominalne* to miesięczne wynagrodzenie brutto wyrażone w koronach czeskich. Wynagrodzenie nominalne skorygowane o czynniki sezonowe to wynagrodzenie nominalne zmodyfikowane statystycznie w celu wyeliminowania wpływu sezonowych zmian w zatrudnieniu i wynagrodzeniach.

> **Ćwiczenie 1.** Zdecyduj, czy każde z poniższych stwierdzeń wynika z wykresu, czy nie.
> 
> 1. Od 2018 r. średnia nominalna płaca brutto nigdy nie spadła poniżej 30 000 CZK.
> 
> 2. Jeśli średnia nominalna płaca brutto wzrasta, wzrasta również nominalny wskaźnik płac.
> 
> 3. Wzrost płac realnych był najniższy w 2020 r. w porównaniu z poprzednimi pięcioma latami.


*Rozwiązanie.* 

1. Stwierdzenie jest prawdziwe – wszystkie niebieskie słupki na wykresie od 2018 r. znajdują się powyżej 30 000 CZK, co widać na rysunku 3.

![Średnia miesięczna płaca i wzrost płac](03_graf_graf_2.jpg)

2. Stwierdzenie jest nieprawdziwe – na przykład między trzecim a czwartym kwartałem 2021 r. średnia płaca nominalna brutto wzrosła, ale nominalny wskaźnik płac spadł.

3. Stwierdzenie jest nieprawdziwe – wzrost płac realnych był niższy w 2022 i 2023 r.



> **Ćwiczenie 2.** Określ zakres wartości zmiennych w obserwowanym okresie.




*Rozwiązanie.* Średnia nominalna płaca brutto w obserwowanym okresie wynosi od 22 000 CZK do 50 000 CZK.
Wzrost płacy nominalnej wynosi od 0% do 13%, natomiast wzrost płacy realnej wynosi od -12% do 10%.



> **Ćwiczenie 2.** Spróbuj wyjaśnić różnice między wzrostem płac nominalnych i realnych od około trzeciego kwartału 2021 r. Co natomiast można powiedzieć o sytuacji w latach 2015–2016, kiedy obie wartości były porównywalne?



*Rozwiązanie.* Na wykresie widać, że od trzeciego kwartału 2021 r. indeks płac realnych gwałtownie spadł, podczas gdy pozostałe dwa wskaźniki pozostały na niezmienionym poziomie (płaca nominalna brutto nawet nieznacznie wzrosła, podobnie jak w poprzednich okresach). Wskazuje to na prawdopodobną przyczynę – wysoką inflację. Podejrzenie to można potwierdzić na stronie internetowej GUS <https://www.czso.cz/csu/czso/mira_inflace>, gdzie tabele śledzące stopę inflacji pokazują, że jej wzrost rozpoczął się w trzecim kwartale 2021 r.
|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| - | -: | -: | -: | -: | -: | -: | -: | -: | -: | -: | -: | -: |
| **2020** | 2.9 | 3.0 | 3.1 | 3.1 | 3.1 | 3.1 | 3.2 | 3.2 | 3.3 | 3.3 | 3.2 | 3,2 |
| **2021** | 3.0 | 2.9 | 2.8 | 2.8 | 2.8 | 2.8 | 2.8 | 2.8 | 3.0 | 3.2 | 3.5 | 3,8 |
| **2022** | 4.0 | 5.2 | 6.1 | 7.0 | 8.1 | 9.4 | 10.6 | 11.7 | 12.7 | 13.5 | 14.4 | 15.1 |
| **2023** | 15.7 | 16.2 | 16.4 | 16.2 | 15.8 | 15.1 | 14.3 | 13.6 | 12.7 | 12.1 | 11.4 | 10.7 |
| **2024** | 9.4 | 8.2 | 7.1 | 6.3 | 5.6 | 4.9 | 4.4 | 3.9 | 3.5 | 3.1 | 2.7 | 2.4 |

Można oczekiwać, że w latach 2015–2016 stopa inflacji była niska. Można to zweryfikować w tym samym źródle, o którym mowa w poprzednim akapicie.


|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| -- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| **2015** | 0.3 | 0.3 | 0.3 | 0.4 | 0.4 | 0.5 | 0.5 | 0.4 | 0.4 | 0.4 | 0.3 | 0.3 |
| **2016** | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 | 0.3 | 0.3 | 0.3 | 0.3 | 0.4 | 0.5 | 0.7 |
| **2017** | 0.8 | 1.0 | 1.2 | 1.3 | 1.5 | 1.7 | 1.8 | 2.0 | 2.2 | 2.3 | 2.4 | 2.5 |
| **2018** | 2.4 | 2.4 | 2.3 | 2.3 | 2.3 | 2.3 | 2.3 | 2.3 | 2.3 | 2.2 | 2.2 | 2.1 |

