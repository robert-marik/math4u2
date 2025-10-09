---
keywords:
- wykładniki i logaritmy
- logarytmy
- równanie logarytmiczne
- równanie wykładnicze
is_finished: true
---

# Dźwięk

Dźwięk jest falą mechaniczną, którą odbieramy za pomocą słuchu.
Wszyscy ludzie postrzegają wysokość i czas trwania tonu w przybliżeniu w ten sam sposób,
ale percepcja głośności jest bardzo subiektywna.
Głośność jest określana przez amplitudę oscylacji w medium, przez które rozchodzi się fala dźwiękowa.
Ponieważ amplituda fal dźwiękowych nie jest łatwa do zmierzenia,
wielkości natężenia dźwięku $I$ i poziomu natężenia dźwięku $L$
są używane do obiektywnego porównywania głośności.

*Natężenie dźwięku* wyraża ilość energii przenoszonej przez fale dźwiękowe na jednostkę powierzchni prostopadłą do kierunku propagacji dźwięku w jednostce czasu.
Zdrowe ucho może wykryć najmniejsze natężenie dźwięku $I_0=10^{-12}\,\text{W}/\text{m}^2$ przy częstotliwości $1000\,\text{Hz}$, co odpowiada progowi słyszenia.
Z drugiej strony, natężenie dźwięku $10\,\text{W}/\text{m}^2$ jest wystarczająco głośne, aby odpowiadać progowi bólu.
Jednak dziesięciokrotne zwiększenie natężenia dźwięku $I$ nie odpowiada postrzeganiu dźwięku dziesięć razy głośniej.
Dlatego poziom natężenia dźwięku $L$ jest raczej używany do wyrażania głośności dźwięku,
który wykorzystuje skalę logarytmiczną w decybelach (dB).

*Poziom natężenia dźwięku* $L$ w decybelach jest zdefiniowany przez równanie $$L=10\log{\frac{I}{I_0}},$$
gdzie $I$ to natężenie dźwięku w danej lokalizacji
a $I_0=10^{-12}\,\text{W}/\text{m}^2$, co odpowiada progowi słyszenia.
Poziom natężenia dźwięku $60\,\text{dB}$ odpowiada głośności normalnej rozmowy, $90\,\text{dB}$ to głośność kosiarki do trawy, a $110\,\text{dB}$ to głośność dyskoteki.

Istnieje ryzyko uszkodzenia słuchu w przypadku długotrwałego słuchania
(nawet jeśli nie odczuwamy bólu) przy głośności wyższej niż $85\,\text{dB}$.
Od poziomu głośności wyższego niż $100\,\text{dB}$ istnieje ryzyko uszkodzenia słuchu w ciągu kilku minut.
Zbadajmy związek między natężeniem dźwięku a poziomem natężenia dźwięku, tj. głośnością odbieraną przez słuch.

>**Zadanie 1.** Natężenie dźwięku wynosi $1{,}27\cdot10^{-3}\,\text{W}/\text{m}^2$ 
>podczas słuchania głośnika o mocy akustycznej $20\,\text{W}$
>w odległości $50\,\text{m}$ od niego
>(zakładają równomierną transmisję fali dźwiękowej do wolnej półprzestrzeni).
>Ile decybeli zmierzymy w tym miejscu?

\iffalse

*Rozwiązanie* Do obliczeń używamy definicji poziomu natężenia dźwięku $L=10\log{\frac{I}{I_0}},$ gdzie $I=1{,}27\cdot10^{-3}\,\text{W}/\text{m}^2$ to natężenie dźwięku w danej lokalizacji i $I_0=10^{-12}\,\text{W}/\text{m}^2$.
$$L=10\log{\frac{I}{I_0}}=10\log{\left(\frac{1{,}27\cdot10^{-3}}{10^{-12}}\right)}=10\log{\left(1{,}27\cdot10^{9}\right)}=91\;\text{dB}\,.$$

Poziom natężenia dźwięku wynosi 91 dB w odległości 50 m od głośnika,
co odpowiada poziomowi hałasu motocykla lub kosiarki.

\iffalse

>**Zadanie 2.** Jak zmieni się poziom natężenia dźwięku, jeśli w lokalizacji z poprzedniego przykładu natężenie dźwięku będzie dwukrotnie większe, tj,
>,$2\cdot1{,}27\cdot10^{-3}\,\text{W}/\text{m}^2$ ?

\iffalse

*Rozwiązanie.* Używamy tego samego wzoru, co w poprzednim ćwiczeniu:
$$L=10\log{\frac{I}{I_0}}=10\log{\left(\frac{2\cdot1{,}27\cdot10^{-3}}{10^{-12}}\right)}=10\log{\left(2{,}54\cdot10^{9}\right)}=94\;\text{dB}\,.$$
Obliczenia pokazują, że dwukrotność natężenia dźwięku nie odpowiada dwukrotności liczby decybeli.
 Poziom natężenia dźwięku wzrośnie z
$91\,\text{dB}$ do $94\,\text{dB}\,$.

\fi

>**Zadanie 3.** Ze wzoru na poziom natężenia dźwięku,
>znajdź wartość $\Delta L$, przez którą poziom natężenia dźwięku $L$,
>zmienia się, jeśli natężenie dźwięku zostanie podwojone z $I$ do $2I$.

\iffalse

*Rozwiązanie.* Jest to uogólnienie poprzedniego zadania.$$\Delta L=10\log{\frac{2I}{I_0}}-10\log{\frac{I}{I_0}}=10\cdot\left(\log{\frac{2I}{I_0}}-\log{\frac{I}{I_0}}\right)=10\log\left(\frac{\frac{2I}{I_0}}{\frac{I}{I_0}}\right)=10\log2=3\;\text{dB}$$
Przy podwojeniu natężenia dźwięku, poziom natężenia dźwięku wzrasta o $3\,\text{dB}\,$.

Jest to uogólnienie poprzedniego zadania.$$\Delta L=10\log{\frac{2I}{I_0}}-10\log{\frac{I}{I_0}}=10\cdot\left(\log{ \frac{2I}{I_0}}-\log{\frac{I}{I_0}}\right)=10\log\left(\frac{\frac{2I}{I_0}}{\frac{I} {I_0}}\right)=10\log2\doteq3\;\text{dB}$$
Poziom natężenia dźwięku wzrasta o $3\,\text{dB}\,$, gdy natężenie dźwięku podwaja się.

\fi

>**Zadanie 4.** Natężenie dźwięku jest odwrotnie proporcjonalne do kwadratu odległości od źródła dźwięku. O ile zmieni się poziom natężenia dźwięku, jeśli odległość od źródła dźwięku zostanie podwojona?

\iffalse

*Rozwiązanie.* Ponieważ natężenie dźwięku $I$ jest odwrotnie proporcjonalne do kwadratu odległości, otrzymujemy $$I=\frac{k}{l^2},$$ gdzie $l$ to odległość od źródła dźwięku. Gdy odległość zostanie podwojona, natężenie dźwięku wyniesie 
$$
\tilde{I}=\frac{k}{(2l)^2}=\frac{1}{4}\cdot\frac{k}{l^2}=\frac{1}{4}I\,.
$$.
Natężenie dźwięku zostanie zredukowane do $\frac{1}{4}$ jego pierwotnej wartości.

$$\Delta L=10\log{\frac{\frac{1}{4}I}{I_0}}-10\log{\frac{I}{I_0}}=10\cdot\left(\log{\frac{\frac{1}{4}I}{I_0}}-\log{\frac{I}{I_0}}\right)=10\log\left(\frac{\frac{\frac{1}{4}I}{I_0}}{\frac{I}{I_0}}\right)=10\log\frac{1}{4}\doteq-6\;\text{dB}\,.$$
Poziom natężenia dźwięku zmniejsza się o $6\,\text{dB}$, jeśli
podwoimy odległość od źródła dźwięku.

\fi

>**Zadanie 5.** Ze wzoru na poziom natężenia dźwięku $L=10\log{\frac{I}{I_0}}$,
>wyraź natężenie dźwięku $I$.

\iffalse

*Rozwiązanie.* Najpierw wyodrębniamy funkcję logarytmiczną
$\frac{L}{10}=\log{\frac{I}{I_0}}$a następnie używamy
odwrotność funkcji logarytmicznej, tj. funkcja wykładnicza:
$$10^{\frac{L}{10}}=\frac{I}{I_0}.$$
Stąd wyrażamy natężenie dźwięku
$$I=I_0 \cdot 10^{\frac{L}{10}}.$$

\fi

>**Zadanie 6.** O ile razy wzrośnie natężenie dźwięku
>jeśli poziom natężenia dźwięku wzrośnie o $20\,\text{dB}$?

\iffalse

*Rozwiązanie.* Wartość poziomu natężenia dźwięku zmienia się z $L_1=L$ do $L_2=L+20\,\text{dB}$. Używamy wzoru $I=I_0 \cdot 10^{\frac{L}{10}}$
i wyrażamy iloraz $\frac{I_2}{I_1}$:
$$\frac{I_2}{I_1}=\frac{I_0 \cdot 10^{\frac{L_2}{10}}}{I_0 \cdot 10^{\frac{L_1}{10}}}=\frac{10^{\frac{L+20}{10}}}{10^{\frac{L}{10}}}=10^{\frac{L+20}{10}-\frac{L}{10}}=10^2=100.$$

Gdy poziom natężenia dźwięku wzrasta o $20\,\text{dB}$, natężenie dźwięku wzrasta stukrotnie.

\fi

## Literature 
1. Kubera, Miroslav; Nečas, Tomáš; Beneš, Vojtěch. *Online učebnice fyziky pro gymnázia - Zvuk.* Dostępne na <https://e-manuel.cz/kapitoly/mechanicke-vlneni/vyklad/zvuk/> [cit. 24.10.2023].




