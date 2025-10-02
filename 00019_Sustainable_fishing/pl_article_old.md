---
keywords:
- funkcja kwadratowa
- równanie kwadratowe
is_finished: True
---

# Upadek połowów dorsza

Państwa nadbrzeżne mają w zasięgu ręki ogromne bogactwo ryb w oceanach.
To bogactwo jest pozornie nieskończone i stabilne. Jednak ludzie
nauczyli się kilku gorzkich lekcji, że tak nie jest. Jedna z najważniejszych lekcji sięga roku 1992. Zatoka u wybrzeży Nowej Fundlandii zawsze była
bogata w dorsze(*Gadus morhua*, dorsz atlantycki). Łódź, która przybyła tam na ryby, nigdy nie odpłynęła
bez obfitego połowu. Z czasem jednak sytuacja zaczęła się zmieniać. Pod koniec lat 80 biolodzy wezwali do ograniczenia połowów o 50%, aby uniknąć plądrowania łowisk. Jednakże, ponieważ ograniczenie połowów doprowadziłoby obszar do recesji, rząd nie zdecydował się na nałożenie limitów. Niestety, natura rządzi się swoimi
prawami. Stopniowo sytuacja osiągnęła punkt, w którym wstrzymanie połowów było nieuniknione. Populacja dorsza spadła do zaledwie jednego procenta pierwotnego poziomu. W związku z tym ogłoszono moratorium na połowy. Początkowo moratorium miało trwać dwa lata. Jednak
mała populacja dorsza nie odbudowała się znacząco. Dlatego ograniczenia trwały znacznie dłużej niż pierwotnie
przewidywano. Pomimo pewnej nadziei na złagodzenie ograniczeń w 2015 r., dopuszczalny wskaźnik
został ponownie zmniejszony w 2018 r. po ponownym załamaniu się populacji. Moratorium na połowy spowodowało utratę pracy przez 35 tys.
rybaków i pracowników przetwórni ryb. Miało to ogromny wpływ ekonomiczny i
socjologiczny wpływ na cały region.

![Wykres przedstawia ewolucję połowów dorsza na Nowej Fundlandii w tonach ryb. Źródło: Milenijna ocena ekosystemów](cod.svg)

Należy dodać, że opisany powyżej przypadek nie jest wyjątkowy. Równolegle z załamaniem się rybołówstwa na Nowej Fundlandii, podobna sytuacja miała miejsce na pięciu innych kanadyjskich łowiskach, na których w 1993 r. wydano moratorium na połowy (Southern Grand Bank, St. Pierre Bank, Northern Gulf of St. Lawrence, Southern Gulf of St.
Wawrzyńca, Szelf Szkocji Wschodniej). A czy czytałeś powieść Steinbecka z 1945 roku *Cannery Row*? Opisuje ona życie w fabryce sardynek w Kalifornii. Wkrótce po opublikowaniu powieści rybołówstwo zaczęło się załamywać z powodu niezrównoważonych połowów, a połowy komercyjne musiały zostać zakazane w 1967 roku.

## Modelowanie wzrostu populacji

Aby zapobiegać załamaniom rybołówstwa i być w stanie realistycznie i skutecznie modelować wzrost populacji w przyrodzie, opracowano skuteczne i sprawdzone modele matematyczne. Jeden prosty, ale dość dokładny model opisuje tempo wzrostu populacji za pomocą funkcji kwadratowej:

$$ f(N) = r N \left(1-\frac NK\right), $$

gdzie $N$ to wielkość populacji, $f(N)$ to tempo wzrostu populacji, a $r$ i $K$ to stałe. Stała $K$ nazywana jest nośnością środowiska. Stałe $r$ i $K$ określają zdolności reprodukcyjne populacji i wpływ środowiska na populację. Stałe te nadały również nazwy teorii selekcji *r*/*K*, która opisuje dwie podstawowe strategie życiowe, które pomagają populacjom w przyrodzie z powodzeniem się rozwijać. 
Populacje, które kwalifikują się jako *r*-strategowie, są w stanie szybko się rozmnażać. Nie troszczą się one zbytnio o swoje potomstwo i rekompensują troskę obfitością. Populacje te mają dużą wartość stałej $r$. W przeciwieństwie do tego, *K*-strategowie mają niewiele potomstwa, ale dbają o nie i lepiej radzą sobie ze zmianami środowiskowymi. Dlatego wielkość ich populacji jest bliższa pojemności środowiska niż w przypadku *r*-strategów.

![Tempo wzrostu populacji jako funkcja wielkości populacji.](rate.svg)

Tempo wzrostu wskazuje, o ile zwiększa się wielkość populacji w jednostce czasu. Jeśli wynosi zero, wielkość populacji nie zmienia się. Jeśli tempo wzrostu jest dodatnie i liczbowo duże, liczebność populacji szybko rośnie. Jeśli tempo wzrostu jest ujemne, liczebność populacji spada i populacja wymiera. Wykres funkcji modelującej tempo wzrostu przedstawiono na rysunku. Model ten odzwierciedla dobrze znane fakty, że populacja o niewielkich rozmiarach rozmnaża się powoli (mała populacja ma niewiele osobników, a zatem niewiele osobników zdolnych do reprodukcji). Model uwzględnia również fakt, że większa populacja rozmnaża się szybciej, ale tylko do pewnego stopnia, na jaki pozwala nośność środowiska.

## Zadania

Rozważmy hipotetyczną populację narażoną na zbiory. Zmierzymy wielkość populacji w odpowiednich jednostkach. Może to być liczba osobników, tysiące osobników, tony itd. Dla przykładu, rozważmy parametry $K=1000$ i $r=0{,}1$. Oznacza to, że wielkość populacji, która może przetrwać w środowisku, wynosi 1000, a mała populacja, która nie cierpi z powodu konkurencji wewnątrzgatunkowej, rośnie w tempie 10% jej obecnego rozmiaru na jednostkę czasu.

>**Zadanie 1.** Wyznacz wielkość populacji $N_*$, która gwarantuje maksymalne tempo wzrostu. Znajdź to maksymalne tempo wzrostu. Odtąd będziemy oznaczać tę wartość przez $h_*$, ponieważ jest to również maksymalny teoretyczny możliwy wskaźnik odłowu (zwany również intensywnością odłowu). Wartość $N_*$ to wielkość populacji przy tym maksymalnym wskaźniku.

\iffalse

*Rozwiązanie.* Funkcja
$$f(N) = r N \left(1-\frac NK\right),$$
opisująca wzrost jest funkcją kwadratową, a jej wykresem jest parabola. Wykres ten ma znaczenie tylko dla $N\geq0$.

![Tempo wzrostu populacji jako funkcja wielkości populacji, wskazujące maksymalną możliwą intensywność odłowu $h_*$ i odpowiadającą jej stabilną wielkość populacji $N_*$.](rate2.svg)

Ponieważ funkcja jest podana w postaci iloczynu pierwiastków, widzimy, że pierwiastki to $N=0$ i $N=K$. Funkcja osiąga maksimum w wierzchołku paraboli, tj, dla $N_*=\frac
{K}{2}=500$. Wartość funkcji to

$$
h_* = f(N_*) = r \frac{K}2 \left(1-\frac{\frac K2}{K}\right)=\frac{rK}4
$$ 

a dla podanych wartości stałych $K$ i $r$ otrzymujemy

$$h_* = \frac{0{,}1 \cdot 1000}{4} = 25.$$

Porównując to do pojemności środowiska ($K=1000$), widzimy, że wartość ta wynosi 2,5 procent pojemności środowiska. Ponieważ populacja stabilizuje się na poziomie połowy pojemności środowiska, oznacza to, że połowy odbywają się w takim tempie, że w jednostce czasu odławianych jest 5 procent obecnej populacji.

\fi

> **Zadanie 2.** Określ, ile razy zmniejszy się tempo wzrostu populacji, jeśli liczebność populacji spadnie z poziomu $N_*$, który pozwala na maksymalną możliwą intensywność zbiorów, do jednego procenta.
> Jest to wartość, do której należałoby zmniejszyć zbiory, aby zapobiec dalszemu spadkowi. (W praktyce jednak chcielibyśmy odbudować populację,
> i dlatego samo ograniczenie określone w tym kroku nie jest
> wystarczające).

\iffalse

*Rozwiązanie.* Niech $N_2$ będzie wielkością populacji po spadku.
Zatem 
$$
N_2=0{,}01N_*=0{,}01 \frac K2
$$ 
i otrzymujemy
$$f(N_2) = r \cdot 0{,}01 \frac K2 \left(1-\frac{0{,}01 \frac K2}{K}\right) = 0{,}004975\cdot \,r\,K$$
oraz 
$$\frac{f(N_2)}{f(N_*)} = \frac{0{,}004975 rK}{0{,}25 rK} \approx 0{,}02.$$
Jeśli wielkość populacji spadnie do jednego procenta, intensywność zbiorów musi zostać zmniejszona do dwóch procent pierwotnej intensywności, aby uniknąć dalszego spadku.

\fi

>**Zadanie 3.** Załóżmy ostrożne połowy na poziomie 80 procent maksymalnego zrównoważonego odłowu $h_*$. Nawet w tym przypadku należy zachować ostrożność. Jeśli populacja jest zbyt mała, nie poradzi sobie z połowami. Określ, jaka jest minimalna wielkość populacji, która jest w stanie poradzić sobie z połowami na poziomie równym $80\,\%$ $h_*$ bez załamania.

\iffalse

*Rozwiązanie.* Zgodnie z zadaniem, musimy rozwiązać równanie

$$ r N \left(1-\frac NK\right) = 0{,}8 \frac{rK}{4}.$$

Możemy rozwinąć nawiasy i przenieść wszystkie wyrażenia na jedną stronę, aby uzyskać postać

$$ -\frac{r}{K} N^2 + rN - 0{,}8 \frac{rK}{4} = 0.$$

Dla $r=0{,}1$ i $K=1000$ otrzymujemy

$$ -0{,}0001 N^2 +0{,}1 N - 20 = 0$$

co można zapisać jako

$$N^2 - 1000 N + 200000 = 0$$

Pierwiastkami tego równania kwadratowego są
$$N_{1,2}=\frac{1000\pm \sqrt{1000^2-4\cdot 200000}}{2}$$
i stąd $$N_1\approx 276$$ and $$N_2\approx 724.$$

![Tempo wzrostu populacji jako funkcja czasu, z ustaloną intensywnością odłowu i stanami, w których intensywność odłowu jest taka sama jak naturalne tempo wzrostu populacji..](rate3.svg)

Rysunek przedstawia parabolę definiującą tempo wzrostu, poziomą linię definiującą tempo zbiorów oraz punkty przecięcia $N_1$ i
$N_2$. W przypadku populacji mniejszych niż $N_1$ odławianie przewyższa wzrost. W takiej sytuacji wzrost populacji nie jest w stanie zrekompensować tempa odłowu. Populacja jest przełowiona, spada i załamuje się. Aby ustalić połowy na poziomie 80 procent maksymalnego zrównoważonego odłowu, należy poczekać, aż populacja
 wzrośnie do rozmiaru $N_1=276$. Wartość ta stanowi nieco ponad połowę $N_*$, tj. ponad połowę wartości, przy której populacja stabilizuje się przy maksymalnej zrównoważonej intensywności odłowu.

Ta ostatnia część pokazuje, że po załamaniu się populacji nie jest możliwe ustalenie wcześniejszej zrównoważonej intensywności odłowów i liczenie na spontaniczną odbudowę populacji. Populacja musi mieć wystarczającą dynamikę wzrostu, aby poradzić sobie z tym poziomem odłowu. Należy poczekać, aż populacja ryb powróci do wystarczająco dużych zasobów. Powrót do poprzedniego poziomu odłowu jest możliwy tylko wtedy, gdy zostanie osiągnięta wielkość populacji, która zapobiega wyginięciu.

\fi

## Referencje i literatura

### Literatura


* Wikipedie, *Collapse of the Atlantic northwest cod fishery*, <https://en.wikipedia.org/wiki/Collapse_of_the_Atlantic_northwest_cod_fishery>, October 1, 2023
* Ransom A. Myers; Jeffrey A. Hutchings; Nicholas J. Barrowman (1997). *Why do fish stocks collapse? The example of cod in Atlantic Canada* (PDF). Ecological Applications. 7 (1): 91–106. doi:10.1890/1051-0761(1997)007[0091:WDFSCT]2.0.CO;2. JSTOR 2269409. 
* *Collapse of the Pacific Sardine (Again)*, <https://fishbio.com/collapse-pacific-sardine/>, October 1, 2023
* *r/K selection theory*, Wikipedie, <https://en.wikipedia.org/wiki/R/K_selection_theory>, October 1, 2023

### Źródła obrazu

*  Millennium Ecosystem Assessment: Ecosystems and Human Well-being: Opportunities and Challenges
for Business and Industry Ecosystems, <https://www.millenniumassessment.org/documents/document.353.aspx.pdf>, October 1,2023



