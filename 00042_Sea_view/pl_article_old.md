---
keywords:
- geometria płaska
- trygonometria
is_finished: true
---

# Widok na morze

Czy kiedykolwiek spacerując latem wzdłuż brzegu morza, zatrzymałeś się, spojrzałeś na horyzont i zadałeś sobie pytanie: jak daleko sięga mój wzrok? A co, jeśli na drugim brzegu znajduje się coś – czy byłbym w stanie to dostrzec?

Aby uczynić to pytanie bardziej konkretnym, przenieśmy się na chwilę do jednego z najpopularniejszych miejsc wakacyjnych w Europie: Chorwacji, na wybrzeże Morza Adriatyckiego w pobliżu góry Sveti Jure. Oto, co możemy przeczytać o tej górze[^1]: 

[^1]: www.chorvatsko.cz

*Sveti Jure* (Święty Jerzy) to najwyższy szczyt (1762 m n.p.m.) wapiennego pasma Biokovo, które rozciąga się na długości 36 km wzdłuż wybrzeża i oddziela Riwierę Makarską od regionu śródlądowego znanego jako Dalmatyńskie Hinterland. Wznosi się nad wybrzeżem niczym potężny kamienny mur. Dzięki swojej wyjątkowej geologii i naturalnemu pięknu część tego obszaru została w 1981 r. uznana za park przyrodniczy (Park Przyrodniczy Biokovo o powierzchni 196 km²).

Charakterystyczną cechą szczytu Sveti Jure jest nadajnik telewizyjny, który można dostrzec z większości okolicznych terenów górskich. W pogodny dzień, przy dobrej widoczności, widok ze szczytu – zarówno w kierunku morza, jak i lądu – jest niezapomniany. Niestety, na szczycie nie ma możliwości zakupu posiłków ani napojów.

![Szczyt Sveti Jure.](sveti_jure.jpg)

> **Ćwiczenie 1.** Jeśli staniemy na szczycie Sveti Jure i spojrzymy w stronę morza, jak daleko znajduje się punkt na horyzoncie, w którym morze styka się z niebem?


*Rozwiązanie.* Dla uproszczenia załóżmy, że Ziemia jest kulą o promieniu $6371\,\text{km}$. Niech $S$ będzie środkiem Ziemi, $V$ naszą lokalizacją (szczytem góry Sveti Jure), a $H$ dowolnym punktem na powierzchni morza leżącym na horyzoncie. Przekrój Ziemi przez płaszczyznę $SVH$ jest okręgiem o promieniu Ziemi, a linia $VH$ jest styczną do tego okręgu. Oznacza to, że kąt $VHS$ jest kątem prostym (patrz rysunek poniżej).

![Solution to Exercise 1](math4you_00042_01.svg)

Wiemy, że $\lvert SH \rvert = 6371\,\text{km}$ oraz 
$\lvert SV \rvert  = 6372{.}762\,\text{km}$ (ponieważ dodajemy wysokość góry do promienia Ziemi). 
Wykorzystując twierdzenie Pitagorasa w trójkącie prostokątnym $VHS$, obliczamy długość odcinka $VH$:

$$
\lvert VH \rvert = \sqrt{\lvert SV \rvert ^2 - \lvert SH \rvert ^2} \doteq 150\,\text{km}.
$$

Ta długość to odległość do horyzontu, której szukaliśmy.

> **Ćwiczenie 2.** Czy ze szczytu Sveti Jure można zobaczyć szczyt Monte Calvo (1056 m n.p.m.) na włoskim półwyspie Gargano? Monte Calvo znajduje się w odległości około 210 km od Sveti Jure i między tymi dwoma miejscami nie ma żadnych przeszkód lądowych. Jedyną rzeczą, która mogłaby zasłaniać widok, jest krzywizna Ziemi.

\iffalse

*Rozwiązanie.* Rozwiążemy to zadanie, wyobrażając sobie hipotetyczną górę o tej samej wysokości co Monte Calvo, której szczyt znajduje się dokładnie na horyzoncie. W takim przypadku góra byłaby po prostu ukryta za horyzontem. Oznaczmy szczyt tej hipotetycznej góry jako $M$, jej pionową rzutnię na poziom morza jako $M_0$, a rzutnię punktu $V$ (Sveti Jure) jako $V_0$.

![Solution to Exercise 2](math4you_00042_02.svg)

Naszym celem jest określenie odległości między dwiema górami, tj. długości łuku $M_0V_0$. Jeśli długość ta jest mniejsza niż $210\,\text{km}$ 
(rzeczywista odległość), wówczas Monte Calvo będzie znajdować się powyżej horyzontu i będzie widoczne ze Sveti Jure.

Niech $\alpha$ będzie kątem $VSH$, a $\beta$ kątem $MSH$. Ze znanych długości przeciwprostokątnej i przyległego boku w trójkącie prostokątnym $VHS$ otrzymujemy:

$$
\cos\alpha = \frac{6371}{6372{.}762} \Longrightarrow \alpha \doteq 1^{\circ}\,20'\,51''.
$$

Podobnie, z trójkąta $MHS$:

$$
\cos\beta = \arccos \frac{6371}{6372{.}056} \Longrightarrow \beta \doteq 1^{\circ}\,3'\,35''.
$$

Długość łuku $M_0V_0$, odpowiadająca kątowi $\alpha + \beta$, może być następnie obliczona przy użyciu proporcji bezpośredniej i znanego obwodu koła:

$$
\frac{\alpha + \beta}{360^{\circ}}\cdot 2\pi\cdot 6371 \doteq 268\,\text{km}.
$$

Ponieważ prawdziwa góra Monte Calvo znajduje się bliżej, jej szczyt wznosi się ponad horyzont i przy dobrej widoczności można ją dostrzec ze szczytu Sveti Jure.



## Literatura i źródła

### Literatura

* Chorvatsko.cz. *Sveti Jure* (online). Dostępne pod adresem: https://www.chorvatsko.cz/stdal/svjure.html (dostęp 12 grudnia 2024 r.).

### Źródła danych liczbowych


* Sveti Jure, SKas – Praca własna, CC SA 4.0, dostępna pod adresem: https://upload.wikimedia.org/wikipedia/commons/7/70/The_highest_peak_Sv_Jure_\%281762_m\%29_in_Biokovo_Nature_Park.jpg (dostęp 12 grudnia 2024 r.). 



