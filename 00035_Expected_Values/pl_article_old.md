---
keywords:
- ciągi i szeregi
- prawdopodobieństwo
- wartość oczekiwana
- ciąg geometryczny
is_finished: true
---

# Który los na loterię jest bardziej opłacalny?

W życiu bardzo często spotykamy się z sytuacjami, które wiążą się z przypadkiem i prawdopodobieństwem. Wyobraźmy sobie, że stajemy przed wyborem pomiędzy kilkoma opcjami - na przykład wybierając los na loterię lub inwestując w projekt. Każdy wybór wiąże się z ryzykiem i potencjalnymi korzyściami, ale jak możemy określić, który z nich jest najkorzystniejszy? 
W tym miejscu do gry wkracza tak zwana *wartość oczekiwana*.

Wartość oczekiwana informuje nas o średnim wyniku, jakiego możemy się spodziewać, wybierając konkretną opcję. Pomaga nam lepiej oszacować, która opcja prawdopodobnie opłaci się w dłuższej perspektywie. Nie jest to dokładna prognoza, ale narzędzie, które pozwala nam lepiej zrozumieć ryzyko i zysk, zarówno w prostych grach, jak i w rzeczywistych decyzjach.

Rozważmy na przykład dwa losy na loterię:

* Los A: Kosztuje 10 zł i ma prawdopodobieństwo $0{.}1$ wygrania 100 zł; w przeciwnym razie nie wygrywa nic.
* Los B: Kosztuje 10 zł i ma $0{.}2$ prawdopodobieństwa wygrania 60 zł; w przeciwnym razie nie wygrywa nic.

W przypadku losu A oczekujemy, że jeśli kupimy 10 losów, jeden z nich wygra 100 zł, podczas gdy pozostałe dziewięć nie wygra nic.
W związku z tym możemy oczekiwać, że każdy los na loterię przyniesie średni zwrot w wysokości 10 zł.

Podobnie, w przypadku losu na loterię B, spodziewamy się, że jeśli kupimy 10 losów, dwa z nich wygrają 60 zł, a osiem nie wygra nic.
Możemy zatem oczekiwać, że każdy los na loterię przyniesie średni zwrot w wysokości 12 zł.

To pokazuje, że los B jest lepszą opcją.

## Wartość oczekiwana

Średnia wygrana, którą właśnie obliczyliśmy, nazywana jest *wartością oczekiwaną*.

Ogólnie można powiedzieć, że dla zmiennej losowej $X$, która przyjmuje skończenie wiele wartości $x_1,\,\dots,\,x_k$ z prawdopodobieństwami $p_1,\,\dots,\,p_k$,
obliczamy jego wartość oczekiwaną za pomocą tego wzoru:

$$
EV=\sum_{i=1}^k x_ip_i.
$$

## Który los na loterię jest najlepszy?

Przyjrzyjmy się trzem kuponom loteryjnym.
Kupon Black Pearl o wartości 50 zł, kupon Black Pearl o wartości 100 zł oraz kupon loterii Rental King o wartości 50 zł.

Struktura nagród dla kuponów loterii Black Pearl o wartości 50 zł, których jest łącznie 13 000 000, przedstawia się następująco.

|Kwota nagrody (w zł) | Liczba zwycięskich kuponów | 
| ------------- | ------------- |  
| $50$  | $1{\,}820{\,}000$  |
| $100$  | $1\,040{\,}000$  |
| $150$  | $260{\,}000$  |
| $200$  | $130{\,}000$  |
| $300$  | $130{\,}000$  |
| $500$  | $104{\,}000$  |
| $1{\,}000$  | $5{\,}550$  |
| $2{\,}000$  | $2{\,}300$  |
| $4{\,}000$  | $480$  |
| $10{\,}000$  | $185$  |
| $20{\,}000$  | $84$  |
| $100{\,}000$  | $14$  |
| $1{\,}500{\,}000$  | $6$  |
| Total | $3{\,}492{\,}619$  |

Struktura nagród dla kuponu loterii 100 zł Black Pearl wygląda podobnie, z łączną kwotą 15{,}000{,}000$ wyemitowanych kuponów.

| Kwota nagrody (w zł) | Liczba zwycięskich kuponów | 
| ------------- | ------------- |  
| $100$  | $2{\,}400{\,}000$  |
| $200$  | $900{\,}000$  |
| $300$  | $450{\,}000$  |
| $500$  | $150{\,}000$  |
| $600$  | $150{\,}000$  |
| $900$  | $75{\,}000$  |
| $1{\,}000$  | $75{\,}000$  |
| $1{\,}500$  | $20{\,}000$  |
| $6{\,}000$  | $4{\,}000$  |
| $20{\,}000$  | $185$  |
| $50{\,}000$  | $84$  |
| $100{\,}000$  | $30$  |
| $200{\,}000$  | $13$  |
| $5{\,}000{\,}000$  | $6$  |
| Total | $4{\,}224{\,}318$  |

Na koniec przyjrzyjmy się losowi na loterię Rental King,
z łączną liczbą wyemitowanych losów w wysokości $8{\,}000{\,}000$. Nagrody zostały przedstawione w poniższej tabeli.

| Kwota nagrody (w zł) | Liczba zwycięskich kuponów | 
| ------------- | ------------- |  
| $50$  | $960{\,}000$  |
| $100$  | $720{\,}000$  |
| $150$  | $160{\,}000$  |
| $250$  | $160{\,}000$  |
| $500$  | $70{\,}000$  |
| $1{\,}000$  | $1{\,}300$  |
| $2{\,}000$  | $500$  |
| $5{\,}000$  | $160$  |
| $10{\,}000$  | $80$  |
| $100{\,}000$  | $6$  |
| $3{\,}500{\,}000$  | $3$  |
| Total | $2{\,}072{\,}049$  |

Nagroda główna w wysokości $3{\,}500{\,}000\,\text{zł}$ nie jest wypłacana od razu, ale składa się z nagrody natychmiastowej w wysokości $500{\,}000\,\text{zł}$
oraz renty w wysokości $50{\,}000\,\text{zł}$ przez 5 lat.

> **Zadanie 1.** Który kupon ma największą szansę na wygraną?

\iffalse

*Rozwiązanie.* W przypadku losu o wartości 50 zł Black Pearl, istnieje $3{\,}492{\,}619$ wygrywających losów z całkowitej liczby $13{\,}000{\,}000$ (patrz ostatni wiersz tabeli). Prawdopodobieństwo, że losowo wybrany kupon jest wygrywający można obliczyć jako

$$
P(V_1)=\frac{3{\,}492{\,}619}{13{\,}000{\,}000}=0{,}268633.
$$

Możemy powiedzieć, że jeśli kupimy jeden los na loterię, mamy szansę na wygranie około $26{,}86\%$.
Manipulując ułamkiem, możemy również zobaczyć, że szansa na zdobycie zwycięskiego losu na loterię wynosi $1\colon 3{,}72$.

Podobnie, w przypadku losu na loterię Black Pearl o wartości 100 zł otrzymujemy
$$
P(V_2)=\frac{4{\,}224{\,}318}{15{\,}000{\,}000}=0{,}2816212.
$$
Oznacza to, że szansa na wygraną wynosi $28{,}16\%$ lub $1\colon 3{,}55$.

W przypadku biletu Rental King otrzymujemy
$$
P(V_3)=\frac{2{\,}072{\,}049}{8{\,}000{\,}000}=0{,}259,
$$
więc szansa na wygraną wynosi $25{,}9\%$ lub $1\colon 3{,}86$.

Porównując poszczególne prawdopodobieństwa wygranej, okazuje się, że największą szansę na wygraną daje kupon Black Pearl o wartości 100 zł.

W tym kontekście możemy również rozważyć, co rozumiemy przez zwycięski kupon.
Kupon jest zwykle uznawany za wygrywający, jeśli przynosi jakąkolwiek kwotę pieniędzy.
Ale jeśli zapłaciliśmy 100 zł za bilet, to wygrana w wysokości 100 zł zwróci nam pieniądze, ale tak naprawdę nic nie wygraliśmy.
Aby uzyskać prawdopodobieństwo wygrania więcej niż zapłaciliśmy, nie będziemy brać pod uwagę pierwszego rzędu w naszych tabelach wygranych.
W ten sposób otrzymujemy skorygowane prawdopodobieństwo wygranej
$$
\begin{aligned}
P(V_1)&=\frac{1{\,}672{\,}619}{13{\,}000{\,}000}=0{,}128633,\\
P(V_2)&=\frac{1{\,}824{\,}318}{15{\,}000{\,}000}=0{,}1216212,\\
P(V_3)&=\frac{1{\,}112{\,}049}{8{\,}000{\,}000}=0{,}139.
\end{aligned}
$$
Widzimy, że gdy weźmiemy pod uwagę tylko losy loterii, które zwracają więcej niż koszt ich zakupu,
najlepszą opcją jest los na loterię Rental King, który ma $13{,}9\%$ szansy na taką wygraną.

\fi

> **Zadanie 2.** Jaka jest oczekiwana wartość każdego losu?

\iffalse

*Rozwiązanie.* Aby obliczyć wartość oczekiwaną, z definicji musimy znać prawdopodobieństwa poszczególnych wygranych:

|Kwota nagrody (w zł) | Prawdopodobieństwo wygranej |
| ------------- | ------------- |  
| $50$  | $0{,}14$  |
| $100$  | $0{,}08$  |
| $150$  | $0{,}02$  |
| $200$  | $0{,}01$  |
| $300$  | $0{,}01$  |
| $500$  | $0{,}008$  |
| $1{\,}000$  | $0{,}0004269$  |
| $2{\,}000$  | $0{,}000176923$  |
| $4{\,}000$  | $0{,}000036923$  |
| $10{\,}000$  | $0{,}000014231$  |
| $20{\,}000$  | $0{,}000006461538$  |
| $100{\,}000$  | $0{,}000006461538$  |
| $1{\,}500{\,}000$  | $0{,}000000461538$  |

Niech wartości poszczególnych wygranych będą oznaczone od $n_1$ do $n_{13}$, a odpowiadające im prawdopodobieństwa od $p_1$ do $p_{13}$.
Wówczas wartość oczekiwana $EV(L_1)$ losu Czarnej Perły wynosi

$$
EV(L_1)=\sum_{k=1}^{13}n_kp_k=29\,\text{CZK}.
$$

Biorąc pod uwagę sposób obliczania poszczególnych prawdopodobieństw, możemy również obliczyć wartość oczekiwaną w następujący sposób:
$$
EV(L_1)=\frac{1}{13{\,}000{\,}000}\left(50\cdot 1{\,}820{\,}000+100\cdot1{\,}040{\,}000+ \cdots + 100{\,}000\cdot14+1{\,}500{\,}000\cdot6 \right).
$$

To podejście jest bardziej wygodne, ponieważ nie musimy obliczać prawdopodobieństwa każdej możliwej nagrody w tabeli.
Dla losu Black Pearl za 100 CZK otrzymujemy wartość oczekiwaną $EV(L_2)$:
$$
EV(L_2)=\frac{1}{15{\,}000{\,}000}\left(100\cdot 2{\,}400{\,}000+200\cdot 900{\,}000+ \cdots + 200{\,}000\cdot 13+5{\,}000{\,}000 \cdot 6 \right)=64\,\text{CZK}.
$$
W przypadku losu na loterię Rental King otrzymujemy wartość oczekiwaną $EV(L_3)$:
$$
EV(L_3)=\frac{1}{8{\,}000{\,}000}\left(50\cdot 960{\,}000+100\cdot 720{\,}000+ \cdots + 100{\,}000\cdot 6+3{\,}500{\,}000\cdot 3 \right)=29{,}25\,\text{CZK}.
$$

*Uwaga.* 

* Loterie zazwyczaj podają całkowitą pulę nagród i liczbę losów. Wartość oczekiwana to oczywiście stosunek tych dwóch liczb.
* Podane wartości są często jeszcze niższe w rzeczywistości, ponieważ nagrody loteryjne są zazwyczaj opodatkowane.
* To samo podejście można zastosować do obliczenia oczekiwanej wartości paczki różnych gier karcianych (Pokémon, Lorcana, Magic the Gathering lub kart sportowych).

\fi

> **Zadanie 3.** W poprzednich przykładach uznaliśmy, że główną nagrodą w loterii Rental King jest $3{\,}500{\,}000\,\text{zł}$.
>Ale czy jest to rzeczywista wartość nagrody, biorąc pod uwagę, że nie jest ona wypłacana od razu?
\iffalse

*Rozwiązanie.* Prosta odpowiedź brzmi: nie.

Ważne jest, aby pamiętać, że gdybyśmy otrzymali pieniądze natychmiast, moglibyśmy je zaoszczędzić lub w jakiś sposób zainwestować.
Aby określić wartość $50{\,}000\,\text{zł}$ otrzymanych za miesiąc, możemy użyć koncepcji znanej jako *wartość bieżąca*.
Korzystając z tej koncepcji, zadajemy sobie pytanie, ile pieniędzy musielibyśmy zainwestować dzisiaj, aby uzyskać pożądaną kwotę w ciągu jednego miesiąca (np. rozważane $50{\,}000 $).
Kwotę tę nazywamy wartością bieżącą.

Załóżmy, że możemy zaoszczędzić daną kwotę $P_0$ przez miesiąc z miesięczną stopą procentową w wysokości $0{.}5\%$.
Po miesiącu otrzymalibyśmy $P_1=1{,}005P_0$. Wartość bieżąca to zatem kwota $P_0$, którą musimy zdeponować, aby $P_1$ wyniosło $50{\,}000\,\text{zł}$, tj. 
$$
P_0=\frac{50\,000}{1{,}005}=49\,751{,}24\,\text{zł}.
$$

Aby określić wartość bieżącą kwoty, którą otrzymamy za $n$ miesięcy,
zakładamy, że dana kwota będzie zdeponowana przez cały ten czas.
Korzystając z procentu składanego, otrzymujemy wartość bieżącą $P_0$ kwoty $P_n$ otrzymanej po $n$ miesiącach w następujący sposób:
$$
P_0=\frac{P_n}{1{,}005^n}.
$$
Przypomnijmy, że główna nagroda w loterii Rental King składa się z $500{,}000\,\text{zł}$ i trzydziestu miesięcznych płatności w wysokości $50{,}000\,\text{zł}$.
Biorąc pod uwagę miesięczną stopę procentową w wysokości $0{.}5\,\%$, wartość bieżąca $PV$ tych płatności wynosi
$$
PV=\frac{50{\,}000}{1{,}005}+\frac{50{\,}000}{1{,}005^2}+\cdots+\frac{50{\,}000}{1{,}005^{29}}+\frac{50{\,}000}{1{,}005^{30}}.
$$
Zauważmy, że jest to suma wyrazów ciągu geometrycznego, a zatem obliczenia można znacznie skrócić.
$$
PV=\frac{50{\,}000}{1{,}005}\cdot\frac{1-\left(\frac{1}{1{,}005}\right)^{30}}{1-\frac{1}{1{,}005}}=1{\,}389{\,}702{,}7\,\text{zł}.
$$
W związku z tym zakładamy, że wartość głównej nagrody wynosi tylko $1{\,}889{\,}702{,}7\,\text{zł}$.


Gdy użyjemy tej kwoty do obliczenia oczekiwanej wartości losu na loterię Rental King, otrzymamy
$$
EV(L_3)=28{,}65\,\text{zł}.
$$

*Uwaga.* Wcześniejsze rozważania były nadal bardzo uproszczone, ponieważ nie uwzględniały na przykład wpływu inflacji.

\fi

> **Zadanie 4.** Na podstawie wyników poprzednich zadań wybierz najlepszy los na loterię.

\iffalse

*Rozwiązanie.* W oparciu o poprzednie zadania, możemy porównać kupony loteryjne według różnych kryteriów:

1. Według prawdopodobieństwa wygranej.

Zgodnie z tym kryterium, najlepszym kuponem jest kupon 100 zł Black Pearl z szansą na wygraną w wysokości $28{,}16\,\%$,
następnie kupon 50 zł Black Pearl z szansą na wygraną w wysokości $26{,}86\,\%$, a najgorszy jest kupon Rental King z szansą na wygraną w wysokości $25{,}9\,\%$.

2. Według prawdopodobieństwa rzeczywistej wygranej.

Jeśli zamiast tego weźmiemy pod uwagę szansę na wygranie więcej niż zapłaciliśmy, otrzymamy inny ranking.
Najlepszy jest kupon Rental King z szansą na wygraną w wysokości $13{,}9\,\%$, następnie kupon 50 zł Black Pearl z szansą na wygraną w wysokości $12{,}86\,\%$
a ostatni jest kupon 100 zł Black Pearl z szansą na wygraną w wysokości $12{,}16\,\%$.

3. Według wartości oczekiwanej.

Oczekiwana wartość losu na Czarną Perłę o wartości 50 zł wynosi $29\,\text{zł}$. Średnio tracimy $21\,\text{zł}$ kupując jeden bilet.
Analogicznie, oczekiwana wartość losu na Czarną Perłę o wartości 100 zł wynosi 64 zł. Średnio tracimy $36\,\text{zł}$.
W przypadku kuponu Rental King o wartości 50 zł skorygowana wartość oczekiwana wynosi $28{,}65\,\text{zł}$, więc średnio tracimy $21{,}35\,\text{zł}$.

Możemy zatem powiedzieć, że zgodnie z oczekiwaniami, wszystkie losy przynoszą stratę. Jednak los Black Pearl o wartości 50 zł można uznać za najlepszy, ponieważ przynosi najmniejszą stratę.


\fi

## Literatura

* Novák, J., *Střední hodnota v úlohách na střední škole.* Učitel matematiky, 2, JČMF, 2024. 
* *Herní plán loterií SAZKA* [online] Dostępne na https://static.sazka.cz/kentico-media/sazka/media/content/herni-plany/hp-sazka-od-17-7-24-komplet-sazka.pdf, [cit. 1. 9. 2024]

