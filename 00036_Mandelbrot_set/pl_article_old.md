---
keywords:
- liczby zespolone
- płaszczyzna Gaussa
- ciągi
- zbieżność
- wartość bezwzględna
is_finished: true
---

# Zbiór Mandelbrota

Zbiór Mandelbrota jest jednym z najbardziej znanych i najpiękniejszych fraktali, 
fascynującym matematyków, naukowców i artystów na całym świecie. 
Chociaż na pierwszy rzut oka wygląda jak skomplikowany wzór, 
opiera się on na prostej regule matematycznej polegającej na powtarzaniu potęgowania i dodawania. 
To, co czyni go tak interesującym, to jego nieskończona złożoność 
i piękne wzory ukryte w każdym szczególe.


![The Mandelbrot set; the color of points in its vicinity corresponds to the index of the first term in the sequence at which it is determined that the sequence goes to infinity.](Mandelbrot.png)

Zastosowanie zbioru Mandelbrota wykracza daleko poza matematykę. 
Wykorzystuje się go w grafice komputerowej do tworzenia złożonych i realistycznych obiektów 
podczas modelowania struktur naturalnych, takich jak linie brzegowe, góry lub formacje chmur. 
Można go nawet wykorzystać w ekonomii i fizyce do symulacji systemów chaotycznych.

Zbiór Mandelbrota jest dowodem na to, że nawet proste procedury matematyczne mogą prowadzić 
do niezwykle złożonych i pięknych wyników, które mają zastosowanie w świecie rzeczywistym.

## Tworzenie zbioru

Rozważmy stosunkowo prostą formułę rekurencyjną

$$z_{n+1}=z_{n}^2+c,$$ 

gdzie wartość początkowa wynosi $z_0=0$, a $c$ reprezentuje dowolną liczbę zespoloną. 
Francusko-amerykański matematyk Benoit Mandelbrot (1924–2010) 
był zainteresowany tym, kiedy sekwencja liczb utworzona w ten sposób jest ograniczona, 
tj. dla jakich wartości $c$ w płaszczyźnie zespolonej sekwencja ta zbiega się lub oscyluje. 
Jeśli w pewnym momencie ciąg rozbiega się, chciał wiedzieć, jak szybko. 
Można udowodnić, że jeśli wartość bezwzględna dowolnego wyrazu ciągu $z_{n}$ przekracza 2, 
to ciąg ten nie jest ograniczony.1029

*Zbiór Mandelbrota* jest zatem zbiorem punktów $c$ na płaszczyźnie zespolonej, dla których ciąg utworzony przez wzór rekurencyjny zbiega się lub oscyluje. Dzięki powyższemu faktowi wiemy, że dla każdego wyrazu $z$ tego ciągu jego wartość bezwzględna $|z|$ musi być mniejsza lub równa dwóm.

Weryfikacja, czy dana wartość $c$ należy do zbioru Mandelbrota, odbywa się poprzez obliczenie poszczególnych iteracji i obserwację wartości bezwzględnych tych iteracji. Do obliczenia iteracji używamy wzoru rekurencyjnego

$$
z_{n+1}=z_{n}^2+c,\qquad z_0=0.
$$

Na przykład dla $c=-i$ otrzymujemy:

$$z_{1}=z_{0}^2-i=0^2-i=-i, \quad |z_1|=1,$$
$$z_{2}=z_{1}^2-i=(-i)^2-i=-1-i, \quad |z_2|=\sqrt{2},$$
$$z_{3}=z_{2}^2-i=(-1-i)^2-i=i, \quad |z_3|=1,$$
$$z_{4}=z_{3}^2-i=(i)^2-i=-1-i, \quad |z_4|=\sqrt{2}.$$

Z obliczeń jasno wynika, że wyniki $-i$ i $-1-i$ będą się powtarzać w nieskończoność.
W związku z tym warunek $|z|\leq2$ będzie zawsze spełniony, a zatem liczba $-i$ należy do zbioru Mandelbrota.

## Ćwiczenia

> **Ćwiczenie 1.** Sprawdź, czy liczby zespolone $1$; $i$; $-1$; $1+i$ należą do zbioru Mandelbrota.


*Rozwiązanie.* Dla uproszczenia rozważymy tylko kilka pierwszych kroków iteracji. 
Obraz liczby $c$ na płaszczyźnie Gaussa należy do zbioru Mandelbrota, jeśli dla wszystkich wyników 
iteracyjnego obliczenia wartość bezwzględna wyniku jest mniejsza lub równa $2$.

Proces iteracyjny dla $c=1$.
$$z_{1}=z_{0}^2+1=0^2+1=1, \quad |z_1|=1,$$
$$z_{2}=z_{1}^2+1=1^2+1=2, \quad |z_2|=2,$$
$$z_{3}=z_{2}^2+1=2^2+1=5, \quad |z_3|=5.$$
Obliczenia wyraźnie pokazują, że warunek $|z|\leq2$ nie został spełniony w trzecim kroku iteracji, 
co oznacza, że liczba $1$ nie należy do zbioru Mandelbrota.

Proces iteracyjny dla $c=i$.
$$z_{1}=z_{0}^2+i=0^2+i=i, \quad |z_1|=1,$$
$$z_{2}=z_{1}^2+i=i^2+i=-1+i, \quad |z_2|=\sqrt{2},$$
$$z_{3}=z_{2}^2+i=(-1+i)^2+i=-i, \quad |z_3|=1,$$
$$z_{4}=z_{3}^2+i=(-i)^2+i=-1+i, \quad |z_4|=\sqrt{2}.$$
Obliczenia pokazują, że wartości $-1+i$ i $i$ będą się powtarzać w nieskończoność. 
Warunek $|z|\leq2$ będzie zawsze spełniony, dlatego liczba $i$ należy do zbioru Mandelbrota.

Proces iteracyjny dla $c=-1$.
$$z_{1}=z_{0}^2-1=0^2-1=-1, \quad |z_1|=1,$$
$$z_{2}=z_{1}^2-1=(-1)^2-1=0, \quad |z_2|=0,$$
$$z_{3}=z_{2}^2-1=0^2-1=-1, \quad |z_3|=1.$$
Wartości będą się powtarzać, a warunek $|z|\leq2$ będzie zawsze spełniony, 
dlatego liczba $-1$ należy do zbioru Mandelbrota.

Proces iteracyjny dla $c=1+i$
$$z_{1}=z_{0}^2+1+i=0^2+1+i=1+i, \quad |z_1|=\sqrt{2},$$
$$z_{2}=z_{1}^2+1+i=(1+i)^2+1+i=1+2i+i^2+1+i=1+3i, \quad |z_2|=\sqrt{10}.$$
Z obliczeń jasno wynika, że warunek $|z|\leq2$ nie został spełniony w drugim kroku iteracji 
i liczba $1+i$ nie należy do zbioru Mandelbrota.


> **Ćwiczenie 2.** Udowodnij, że jeśli istnieje $k\in \mathbb{N}$ takie, że $|z_k|>2$, to ciąg $z_n$ jest rozbieżny.



*Rozwiązanie.* Stosując wzór rekurencyjny, otrzymujemy ułamek
$$
\frac{|z_{n+1}|}{|z_n|}=\frac{|z^2_n+c|}{|z_n|}. 
\tag{1}
$$

Wykorzystanie nierówności trójkąta
$$
|a+b|\leq|a|+|b|,
$$ 
where $a=z^2+c$ and $b=-c$, we get
$$
|z^2+c-c|\leq|z^2+c|+|-c|=|z^2+c|+|c|
$$
and hence $|z^2+c|\geq|z^2|-|c|=|z|^2-|c|$.

Podstawiając do $(1)$ i modyfikując, otrzymujemy
$$
\frac{|z^2_n+c|}{|z_n|}\geq \frac{|z_n|^2-|c|}{|z_n|}=|z_n|-\frac{|c|}{|z_n|}.
$$
Ponadto wiemy, że istnieje takie $n$, że zachodzi warunek $|z_n|>|c|$. Dla $|c|\leq2$ wynika to z założenia. Dla $c>2$, wówczas dla $n=2$ zachodzi następująca zależność:
$$
|z_2|=|c^2+c|\geq|c|^2-|c|=|c|(|c|-1)>|c|.
$$
Więc można zapisać
$$
\frac{|z^2_n+c|}{|z_n|}\geq \frac{|z_n|^2-|c|}{|z_n|}=|z_n|-\frac{|c|}{|z_n|}>|z_n|-1>1.
$$
A zatem
$$
\frac{|z_{n+1}|}{|z_n|}>1,
$$
lub $|z_{n+1}|>|z_n|$ i nasza sekwencja się rozbiega.

## Literatura

*  Čápka Hartinger, David. *Zbiór Mandelbrota – lekcja 3 [online]* https://www.itnetwork.cz/algoritmy/graficke/algoritmus-vykresleni-fraktalu-mandelbrotovy-mnoziny} [dostęp: 22.09.2023]

* Wikipedia. *Zbiór Mandelbrota [online]*. Dostępne na stronie https://en.wikipedia.org/wiki/Mandelbrot_set [dostęp: 22.09.2023].

* PantheraLeo1359531. *Zbiór Mandelbrota – rysunek [online]*. Dostępne na stronie https://commons.wikimedia.org/w/index.php?curid=103476207 [dostęp: 22.09.2023]
