---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- ciągi i szeregi
- ciąg geometryczny
- geometria fraktalna
- płatek śniegu Kocha
is_finished: true
---

# Geometria fraktalna

Fraktal to obiekt, którego struktura geometryczna się powtarza. 
Charakterystyczną cechą fraktali jest ich samopodobieństwo. Przykłady
fraktali w przyrodzie to chmury, drzewa lub główka kalafioru. Słowo "fraktal" pochodzi od łacińskiego słowa "fractus", które oznacza
 złamany lub rozbity. Termin ten został stworzony przez Benoita B. Mandelbrota,
uważany za ojca geometrii fraktalnej, znany ze
swojej książki The Fractal Geometry of Nature (1982).

W badaniu fraktali ważną rolę odgrywa ich wymiar. Wymiar topologiczny, znany z klasycznej geometrii euklidesowej, okazał się
niewystarczający do opisu fraktali. Dlatego potrzebny był inny rodzaj wymiaru.
Został on wprowadzony przez Felixa Hausdorffa, znany jako wymiar Hausdorffa. Dla prostych obiektów możemy go rozumieć jako liczba:
$$d=\frac{\ln N}{\ln\frac{1}{r}}, $$
gdzie $N$ to liczba części, z których składa się obiekt, utworzona przez
samopodobieństwo ze współczynnikiem $r$ z oryginalnego objektu. Na przykład, dla kwadratu prawdą jest, że może on 
składać się z czterech mniejszych kwadratów, które powstają z niego przez
samopodobieństwo ze współczynnikiem $r=\frac{1}{2}$, tj.,
$$d=\frac{\ln 4}{\ln2}=2.$$
Zatem dla kwadratu jego wymiar fraktalny (wymiar Hausdorffa) jest równy jego normalnemu wymiarowi intuicyjnemu (wymiar topologiczny).

## Płatek śniegu Kocha

*Płatek śniegu Kocha* jest krzywą na płaszczyźnie utworzoną w iteracyjnym procesie
z trójkąta równobocznego.

Na początku dany jest trójkąt równoboczny o bokach długości 1.
W każdym kolejnym kroku wykonywane są następujące czynności:


1. Każdy odcinek linii jest podzielony na trzy części.
2. Trójkąt równoboczny jest skonstruowany nad środkową trzecią częścią odcinka.
3. Podstawa skonstruowanego trójkąta (wcześniej środkowa jedna trzecia
   odcinka linii) jest usuwana.

![Pierwsza iteracja płatka śniegu Kocha](math4you_00007.svg)

Z rysunku widać, że aby wyznaczyć długość jednego boku
płatka śniegu po pierwszej iteracji, potrzebujemy 4 boków
trójkąta, który został utworzony przez zmniejszenie boku oryginalnego trójkąta
od kroku zerowego ze współczynnikiem samopodobieństwa $r=\frac{1}{3}$,
tj.
$$
d=\frac{\ln4}{\ln3}\approx 1{,}26.
$$
Ponieważ płatek śniegu Kocha jest krzywą, jego wymiar powinien wynosić
$1$. Ta rozbieżność wynika z faktu, że płatek śniegu Kocha jest ostatecznie tak
pofragmentowany, że wynikowy fraktal ma nieskończoną
długość, ale ogranicza strukturę płaszczyzny o skończonej powierzchni.

> **Zadanie 1.** Oblicz obwód płatka śniegu Kocha po
> pierwszej, drugiej i trzeciej iteracja.

\iffalse

*Rozwiązanie.* Początkowo mamy trójkąt równoboczny o
obwodzie $o_0=3$. W pierwszej iteracji każdy z trzech odcinków 
segmentów jest podzielony na trzy części, a środkowa trzecia część jest zastąpiona przez
dwa odcinki o długości $\frac{1}{3}$. Każdy bok oryginalnego
trójkąta jest przedłużony o $\frac{1}{3}$, co daje obwód po
pierwszej iteracji
$$o_1=3+3\cdot\frac{1}{3}=4.$$


W drugiej iteracji każdy bok oryginalnego trójkąta jest dzielony
na cztery odcinki o długości jednej trzeciej pierwotnej długości, które są
dalej dzielone na trzy części i przedłużone o $\frac{1}{9}$. Prowadzi to do obwodu
$$
o_2=3+3\cdot\frac{1}{3}+3\cdot\frac{4}{9}=\frac{16}{3}.
$$ 
W trzeciej iteracji rozszerzamy 16 segmentów linii z każdej strony
o $\frac{1}{27}$, co daje obwód
$$
o_3=3+3\cdot\frac{1}{3}+3\cdot\frac{4}{9}+3\cdot\frac{16}{27}=3+1+\frac{4}{3}+\frac{16}{9}=\frac{64}{9}.
$$

\fi

> **Zadanie 2.** Jaki jest obwód płatka śniegu Kocha po
> $n$-tej iterakcji? Udowodnij, że obwód płatka śniegu Kocha
> jest nieskończony.

\iffalse

*Rozwiązanie.* Z powyższych obliczeń wynika, że każdy odcinek
jest jedną trzecią długości odcinka z poprzedniej iteracji, a jednocześnie każdy odcinek
iteracji jest w następnej iteracji
wydłużany o jedną trzecią, tj. odcinek jest wydłużany do $\frac{4}{3}$
swojej poprzedniej długości. Obwód płatka śniegu Kocha po
$n$-tej iteracji można wyrazić za pomocą sumy szeregu geometrycznego
ze wspólnym współczynnikiem $\frac{4}{3}$ for $n\in\mathbb{N}$:
$$
o_n=3+\left(\frac{4}{3}\right)^0+\left(\frac{4}{3}\right)^1+\left(\frac{4}{3}\right)^2+\cdots+\left(\frac{4}{3}\right)^{n-1}=3+\sum_{i=1}^n\left(\frac{4}{3}\right)^{i-1}.
$$   
Gdybyśmy kontynuowali w ten sposób w nieskończoność, otrzymalibyśmy nieskończony ciąg geometryczny w drugim członie powyższej sumy.
Ponieważ stosunek odpowiedniego ciągu geometrycznego jest większy niż jeden, ciąg jest rozbieżny, a obwód płatka śniegu Kocha jest nieskończony.

\fi

> **Zadanie 3.** Oblicz pole powierzchni płatka śniegu Kocha po
> pierwszej i drugej iteracja.

\iffalse

*Rozwiązanie.* Na początku przyjmijmy, że wysokość trójkąta
 równobocznego o boku długości  $a$ wynosi
$\frac{\sqrt{3}}{2}a$, a jego pole powierzchni wynosi
$$S=\frac{\sqrt{3}}{4}a^2.$$
Pole powierzchni początkowego trójkąta równobocznego wynosi
$S_0=\frac{\sqrt{3}}{4}$. W pierwszej iteracji dzielimy odcinki na
 tercje i umieszczamy mniejszy trójkąt równoboczny
o boku długości $\frac{1}{3}$ w środkowej trzeciej części. Pole powierzchni
po pierwszej iteracji wynosi
$$
S_1=\frac{\sqrt{3}}{4}+3\cdot\frac{\sqrt{3}}{4}\cdot\left(\frac{1}{3}\right)^2=\frac{\sqrt{3}}{4}\cdot\frac{4}{3}.
$$ 
W drugiej iteracji każdy bok oryginalnego trójkąta jest dzielony na cztery odcinki, a mniejszy trójkąt równoboczny o boku długości $\frac{1}{9}$ jest umieszczany na każdym odcinku.
Pole powierzchni po drugiej iteracji wzrośnie do
$$
S_2=\frac{\sqrt{3}}{4}+3\cdot\frac{\sqrt{3}}{4}\cdot\left(\frac{1}{3}\right)^2+3\cdot4\cdot\frac{\sqrt{3}}{4}\cdot\left(\frac{1}{9}\right)^2=\frac{\sqrt{3}}{4}\left(1+\frac{1}{3}+\frac{1}{3}\cdot\frac{4}{9}\right)=\frac{\sqrt{3}}{4}\cdot\frac{40}{27}.
$$

\fi

> **Zadanie 4.** Jakie jest pole powierzchni płatka śniegu Kocha po $n$-tej
> iteracji? Ile razy większe jest pole powierzchni płatka śniegu Kocha
> w stosunku do oryginalnego trójkąta równobocznego?

\iffalse

*Rozwiązanie.* Z poprzednich rozważań wynika, że liczba
 odcinków, w których dodajemy nowy trójkąt, jest czterokrotnie większa
w każdej iteracji. W tym samym czasie bok naszego nowego trójkąta
zmniejsza się do jednej trzeciej jego poprzedniego rozmiaru, więc jego pole powierzchni zmniejsza się do
jednej dziewiątej. Otrzymujemy wyrazy ciągu geometrycznego o współczynniku
$\frac{4}{9}$, a pole powierzchni płatka śniegu Kocha po $n$-tej
iteracji  jest tworzone przez pole pierwotnego trójkąta i sumę
pierwszych $n$ wyrazów tego ciągu geometrycznego:
$$S_n=\frac{\sqrt{3}}{4}\left[1+\frac{1}{3}+\frac{1}{3}\cdot\frac{4}{9}+\dots+\frac{1}{3}\left(\frac{4}{9}\right)^{n-1}\right]=\frac{\sqrt{3}}{4}\left[1+\frac{1}{3}\sum_{i=1}^n\left(\frac{4}{9}\right)^{i-1}\right].$$
Ponieważ stosunek ciągu geometrycznego jest mniejszy niż jeden, kontynuując do nieskończoności, otrzymujemy zbieżny ciąg geometryczny. Korzystając ze wzoru na jego sumę, otrzymujemy pole powierzchni płatka śniegu Kocha po nieskończonej liczbie iteracji.
$$S=\frac{\sqrt{3}}{4}\left(1+\frac{1}{3}\cdot\frac{1}{1-\frac{4}{9}}\right)=\frac{\sqrt{3}}{4}\left(1+\frac{1}{3}\cdot\frac{9}{5}\right)=\frac{8}{5}\cdot\frac{\sqrt{3}}{4}= 1{,}6 \cdot S_0.$$

Płatek śniegu Kocha ma nieskończony obwód otaczający skończone pole powierzchni, 
który jest około 1,6 razy większy niż pole powierzchni oryginalnego
trójkąta równobocznego.

\fi

## Literatura

* MathWorld. *Koch snowflake* [online]. Dostępny pod adresem <https://mathworld.wolfram.com/KochSnowflake.html> [cit. 13. 7. 2023].
* *Koch curve* [online]. Dostepny pod adresem <https://cs.wikipedia.org/wiki/Kochova_k%C5%99ivka> [cit. 13. 7. 2023].

