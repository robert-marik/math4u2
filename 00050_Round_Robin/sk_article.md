---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- kombinatorika, pravdepodobnosť a štatistika
- kombinatorika
is_finished: true
difficulty: 3
time: 40

---
# Round robin

Predstavte si, že usporadúvate školský turnaj v stolnom 
tenise, šachu, e-športe alebo napríklad futsale. Chcete, 
aby bol čo najspravodlivejší – aby každý hráč mal 
možnosť stretnúť sa so všetkými ostatnými. Práve na to 
slúži systém každý s každým, známy tiež ako round 
robin.

Jeho hlavnou výhodou je férovosť: výsledné poradie závisí 
len na výkonoch hráčov alebo tímov, nie na náhodnom 
losovaní súperov. Na druhú stranu, počet zápasov rýchlo 
rastie s počtom účastníkov – naplánovať taký turnaj 
môže byť celkom výzva. A práve tu prichádza ku slovu 
kombinatorika – matematika počítania možností.

## Futsalový turnaj

> **Úloha 1.** Na turnaj vo futsale sa prihlásilo 9 
> tímov. Je vedený systémom round robin, t. j. každý tím 
> hrá s každým jeden zápas. Tím za každé víťazstvo v 
> zápase dostáva 2 body, za remízu 1 bod a za prehru 0 
> bodov. O celkovom umiestnení tímu rozhodne záverečný 
> súčet bodov za všetky zápasy.
>
> Koľko zápasov je nutné na turnaji odohrať? Koľkými 
> spôsobmi je možné zostaviť rozvrh turnaja, ak je k 
> dispozícii jediné ihrisko, na ktorom sa zápasy postupne 
> odohrávajú?

\iffalse

*Riešenie.* Celkový počet odohraných zápasov zodpovedá 
počtu všetkých neusporiadaných dvojíc vytvorených z deviatich 
tímov. Inými slovami zodpovedá počtu všetkých dvojčlenných 
kombinácií bez opakovania vytvorených z deviatich prvkov. 
Tých je celkom
$$
\binom{9}{2} = 36.
$$
Pre určenie počtu spôsobov zostavenia turnaja hľadáme 
vlastne počet všetkých zoradení 36 zápasov, 
preto je všetkých možných rozvrhov turnaja celkom
$$
36! =371\,993\,326\,789\,901\,217\,467\,999\,448\,150\,835\,200\,000\,000 \doteq 3{,}72\cdot 10^{41}.
$$
Poznamenajme, že keby sme zhromaždili porovnateľný 
počet zrniek piesku, z ktorých každé bude mať objem 
rádovo $10^{-13}\,\text{m}^3$, celá kôpka by mala 
objem v radoch $10^{28}\,\text{m}^3$, čo je 
približne desaťnásobok objemu Slnka. Skôr než o 
kôpku by sa preto jednalo o relatívne hmotné 
vesmírne teleso.

\fi

> **Úloha 2.** Ukážte, že ak niektorý tím v 
> turnaji z predchádzajúcej úlohy získal celkom 13 bodov, potom 
> nutne patrí medzi štyri najlepšie tímy turnaja.

\iffalse

*Riešenie.* Úlohu budeme riešiť sporom. Pripusťme, že by 5 
tímov získalo 13 alebo viac bodov. Pretože sú v každom 
zápase medzi dva tímy rozdelené 2 body, je v celom 
turnaji rozdelených celkom $2\cdot 36 = 72$ bodov. Pritom 
je medzi 5 tímov rozdelených aspoň 65 bodov, medzi 
zostávajúce štyri tímy tak musí byť rozdelených nanajvýš 7 
zostávajúcich bodov. 

Ale tieto štyri tímy navzájom medzi sebou odohrajú celkom 
$\binom{4}{2}=6$ zápasov a musia si preto rozdeliť celkom 
12 bodov, dokopy by sa teda muselo rozdeliť aspoň 
77 bodov, čo nie je možné, dostávame teda spor. 

Tímov s 13 alebo viac bodmi tak môže byť najviac štyri.

\fi

## Férovejšia súťaž

Na ďalší ročník futsalového turnaja z predchádzajúcich úloh 
sa tentoraz prihlásilo 7 tímov. Pri zostavovaní rozvrhu 
turnaja si však organizátor dal novú podmienku, že 
žiadny tím nesmie hrať v dvoch zápasoch tesne za sebou, 
aby hráči nemuseli hrať unavení a turnaj bol férovejší. 

Libor vymyslel algoritmus, ako požadovanú postupnosť 
zápasov zostaviť. Vychádza z nasledujúcej tabuľky.  

![Tabuľka pre tvorbu programu férového turnaja](math4you_00050.svg)

Jej každé pole v $i$-tom riadku a $j$-tom stĺpci 
zodpovedá zápasu $(i+1)$-tého a $j$-tého tímu. Hľadaná 
postupnosť zápasov bude zodpovedať poradiu polí, ktoré 
Libor postupne vyberá. Pre prehľadnosť budeme tieto polia 
označovať podľa tímov, ktorých zápas reprezentuje, t. j. $[1;2]$, 
$[3;5]$ atď. Ďalej označíme najdlhšiu diagonálu 
začínajúcu poľom $[1;2]$ a končiacu poľom $[6;7]$ ako 
$D_1$, kratšiu diagonálu začínajúcu poľom $[1;3]$ a 
končiacu poľom $[5;7]$ ako $D_2$ atď.

Liborov algoritmus vyzerá nasledovne:
- ako prvé vyberieme pole v prvom stĺpci a poslednom riadku, t. j. $[1;7]$;
- ďalej vyberáme po rade pole diagonály $D_1$ v párnych stĺpcoch zľava doprava;
- ďalej vyberáme po rade zostávajúce polia diagonály $D_1$ v nepárnych stĺpcoch zľava doprava;
- ďalej vyberáme zľava doprava všetky polia diagonály $D_2$;
- ďalej vyberáme zľava doprava všetky polia diagonály $D_3$, následne $D_4$ atď.

Pre turnaj o siedmych tímoch tak dostaneme nasledujúce 
poradie zápasov

$$
[1;7],\quad[2;3],\quad[4;5],\quad[6;7],\quad[1;2],\quad[3;4],\quad[5;6],
$$
$$
[1;3],\quad[2;4],\quad[3;5],\quad[4;6],\quad[5;7],\quad[1;4],\quad[2;5],
$$
$$
[3;6],\quad[4;7],\quad[1;5],\quad[2;6],\quad[3;7],\quad[1;6],\quad[2;7].
$$

> **Úloha 3.** Vypíšte využitím Liborovho algoritmu 
> postupnosť zápasov pre turnaj, ktorého sa zúčastní 9 
> tímov a overte, že v nej nedôjde k výskytu rovnakého 
> tímu v dvoch po sebe idúcich zápasoch.

\iffalse

*Riešenie.* Využitím algoritmu dostávame nasledujúcu postupnosť 36 polí a je zrejmé, že každé dve po sebe idúce polia majú všetky zložky rôzne.
$$
[1;9],\quad [2;3],\quad [4;5],\quad [6;7],\quad [8;9],\quad [1;2],\quad [3;4],\quad [5;6],\quad [7;8],\quad [1;3],\quad [2;4],\quad [3;5],
$$
$$
[4;6],\quad [5;7],\quad [6;8],\quad [7;9],\quad [1;4],\quad [2;5],\quad [3;6],\quad [4;7],\quad [5;8],\quad [6;9],\quad [1;5],\quad [2;6],
$$
$$
[3;7],\quad [4;8],\quad [5;9],\quad [1;6],\quad [2;7],\quad [3;8],\quad [4;9],\quad [1;7],\quad [2;8],\quad [3;9],\quad [1;8],\quad [2;9].
$$

\fi

> **Úloha 4.** Platí Liborov algoritmus všeobecne pre 
> ľubovoľný počet prihlásených tímov? Ak nie, tak pre 
> ktoré? A dokážete zostaviť pre tieto prípady 
> požadovanú postupnosť sami?

\iffalse

*Riešenie.* Označme $n$ počet prihlásených tímov (z 
kontextu úlohy je pritom zrejmé, že $n>1$). Z Liborovho 
algoritmu odvodíme nasledujúcu postupnosť polí, ktorú 
rozdelíme do niekoľkých nadväzujúcich sekcií podľa ich 
výskytu v tabuľke (pri diagonále $D_1$ pritom musíme 
rozlišovať medzi paritou $n$):
$$
\begin{alignat*}{2}
&[1;n], &&\quad\text{(1. pole)}\\[3mm]
&[2;3],[4;5],\ldots , [n-1;n], &&\quad\text{(1. časť diagonály } D_1\text{, nepárne } n) \\
&[1;2],[3;4],\ldots , [n-2;n-1], &&\quad\text{(2. časť diagonály } D_1\text{, nepárne } n)\\[3mm]
&[2;3],[4;5],\ldots , [n-2;n-1], &&\quad\text{(1. časť diagonály } D_1\text{, párne } n) \\
&[1;2],[3;4],\ldots , [n-1;n], &&\quad\text{(2. časť diagonály } D_1\text{, párne } n)\\[3mm]
&[1;3],[2;4],\ldots , [n-2;n], &&\quad\text{(diagonála } D_2)\\
&[1;4],[2;5],\ldots , [n-3;n], &&\quad\text{(diagonála } D_3)\\
&\vdots &&\\
&[1;i+1],[2;i+2],\ldots , [n-i;n], &&\quad\text{(diagonála } D_i, \text{ kde } i\leq n-2)\\
&[1;i+2],[2;i+3],\ldots , [n-(i+1);n], &&\quad\text{(diagonála } D_{i+1})\\
&\vdots &&\\
&[1;n-1],[2;n]. &&\quad\text{(diagonála } D_{n-2})
\end{alignat*}
$$

Dve po sebe idúce polia, ktoré patria do rovnakej sekcie, rovnaké číslo 
obsahovať nemôžu. V oboch častiach diagonály $D_1$ môžeme totiž ľubovoľné 
dve po sebe idúce polia zapísať v tvare $[j,j+1]$ a $[j+2,j+3]$ a v 
ľubovoľnej diagonále $D_i$ pre $i>1$ majú zase ľubovoľné dve po sebe 
idúce polia tvar $[j,j+i]$ a $[j+1,j+i+1]$. Stačí preto overiť, za 
akých podmienok môže posledný člen jednej sekcie obsahovať rovnaké číslo 
ako prvý člen nasledujúcej sekcie. Tieto špeciálne prípady potom posúdime 
zvlášť.

**1. pole – 1. časť diagonály $D_1$.** Pole $[2;3]$ nadväzuje nezávisle na parite $n$ na pole $[1;n]$. Požadovaná podmienka rôznosti všetkých štyroch zložiek tak nie je splnená pre $n=2$ a $n=3$. 

**1. časť – 2. časť diagonály $D_1$.** Pre nepárne $n$ nadväzuje pole $[1;2]$ na pole $[n-1;n]$, odkiaľ dostávame už spomenuté prípady $n=2$ a~$n=3$. Pre párne $n$ na seba nadväzujú polia $[n-2;n-1]$ a $[1;2]$, tu musíme navyše vylúčiť prípad $n=4$.  

**2. časť diagonály $D_1$ – diagonála $D_2$.** Pre nepárne $n$ na seba nadväzujú polia $[n-2;n-1]$ a $[1;3]$. Podmienka rôznosti zložiek tak nie je splnená pre $n\in\{2;3;4;5\}$. Ak je $n$ párne, nadväzuje na seba pole $[n-1;n]$ a pole $[1;3]$. Všetky doteraz nevylúčené čísla $n$ skúmanej podmienke vyhovujú.

**Diagonála $D_i$ – diagonála $D_{i+1}$.** Pole $[1;i+2]$ nadväzuje na pole $[n-i;n]$. Dostávame tak štyri možné rovnosti, pri ktorých nebude daná podmienka splnená: 
$$
n-i = 1, \qquad n-i = i + 2, \qquad n = 1, \qquad n = i+2.
$$ 
Tretia z rovností isto platiť nemôže. Prvá rovnosť by znamenala, že 
$i=n-1$, ale $i$ môže nadobúdať nanajvýš hodnotu $n-2$. Ak by platila 
štvrtá rovnosť, $i$ nadobúda hodnotu práve $n-2$; diagonála $D_{n-2}$ je 
však poslednou sekciou, ktorou je postupnosť ukončená, keďže žiadna ďalšia
diagonála nenadväzuje. Konečne druhú rovnosť možno prepísať do tvaru 
$i = \frac{n-2}{2}$. Ak je $n$ nepárne, nemôže platiť; pre ľubovoľné 
párne $n$ však existuje dokonca jednoznačné $i$ také, že platiť bude. 
Algoritmus preto zlyhá pre ľubovoľné párne $n$; napr. pre $n=14$ je 
$i=6$, posledný člen diagonály $D_6$ je $[8;14]$ a prvý člen diagonály 
$D_7$ je $[1;8]$.

Liborov algoritmus tak bez výhrad funguje pre nepárne $n$ s výnimkou 3 a 
5. Dodajme však, že zrejme triviálne funguje tiež pre $n=2$ (dva tímy 
odohrajú jediný zápas celého turnaja). Pre zostávajúce párne $n$, $n=3$ a $n=5$ 
by sme sa teraz mali pokúsiť nájsť požadované postupnosti inak. 
Konštatujme však najprv, že pre $n=3$ a $n=4$ je to nemožné, pretože

* pre $n=3$ musíme zoradiť tri polia $[1;2]$, $[1;3]$, $[2;3]$, ale každé 
takéto zoradenie nespĺňa zadanú podmienku;
* pre $n=4$ zvolíme bez ujmy na všeobecnosti prvé pole $[1;2]$, nasledovať 
nutne musí pole $[3;4]$ a ďalej potom opäť $[1;2]$, čo nie je možné.

Pre ostatné $n$ už nájsť postupnosti požadovaných vlastností vieme. 
Pretože ich je (a algoritmov, ktorými ich môžeme nájsť) viac, uveďme 
aspoň niektoré príklady, ktoré dostaneme úpravou pôvodného Liborovho 
algoritmu. Pre $n=5$ ho modifikujeme nasledovne:

* ako prvé vyberieme pole v prvom stĺpci a poslednom riadku, t. j. $[1;5]$;
* ďalej vyberáme po rade pole diagonály $D_1$ v párnych stĺpcoch zľava doprava;
* ďalej vyberáme po rade zostávajúce polia diagonály $D_1$ v nepárnych stĺpcoch zľava doprava;
* ďalej vyberáme sprava doľava všetky polia diagonály $D_3$;
* ďalej vyberáme sprava doľava všetky polia diagonály $D_2$.

Výsledná postupnosť je tvaru
$$
[1;5],\quad [2;3],\quad [4;5],\quad [1;2],\quad [3;4],\quad [2;5],\quad [1;4],\quad [3;5],\quad [2;4],\quad [1,3].
$$

Pre párne $n$ rôzne od 2 a 4 spočítame číslo $k=\frac{n-2}{2}$. (Práve 
toto číslo totiž bolo v diskusii všeobecného prípadu "problematické".) 
Následne aplikujeme Liborov algoritmus s tým rozdielom, že pri výbere 
polí zameníme poradie diagonál $D_{k+1}$ a $D_{k+2}$. S ohľadom na to, že 
je zvyšok algoritmu rovnaký, skontrolujme len rozdielne napojenia 
dotknutých sekcií.

**Diagonála $D_k$ – diagonála $D_{k+2}$.** Na pole $[n-k;n]$ nadväzuje 
pole $[1;k+3]$. Dosadením za $k$, úpravou a porovnaním možných zhodných 
zložiek dostávame štyri rovnosti
$$
\frac{n+2}{2} = 1, \qquad \frac{n+2}{2} = \frac{n+4}{2}, \qquad n = 1, \qquad n = \frac{n+4}{2}.
$$
Druhá a tretia z rovností platiť nemôže a prvá (resp. štvrtá) rovnosť je 
splnená práve vtedy, keď $n=0$ (resp. $n=4$), čo tiež neplatí.

**Diagonála $D_{k+2}$ – diagonála $D_{k+1}$.** Na pole $[n-(k+2);n]$ 
nadväzuje pole $[1;k+2]$. Dosadením a úpravou odvodíme opäť štyri 
rovnosti, ktorých platnosť by porušila zadanú podmienku:
$$
\frac{n-2}{2} = 1, \qquad \frac{n-2}{2} = \frac{n+2}{2}, \qquad n = 1, \qquad n = \frac{n+2}{2}.
$$
Žiadna z uvedených rovností však platiť nemôže, pretože $n$ nemôže byť 4, 
1 ani 2.

**Diagonála $D_{k+1}$ – diagonála $D_{k+3}$.** Na pole $[n-(k+1);n]$ 
nadväzuje pole $[1;k+4]$. Obdobne ako v predchádzajúcich dvoch prípadoch 
môžeme odvodiť štvoricu rovností
$$
\frac{n}{2} = 1, \qquad \frac{n}{2} = \frac{n+6}{2}, \qquad n = 1, \qquad n = \frac{n+6}{2}.
$$
Prvé tri z uvedených rovností platiť nemôžu už z predtým uvedených 
dôvodov. Štvrtá rovnosť platí pre $n=6$; pre toto číslo však neexistuje 
diagonála $D_{k+3}$, pretože $k+3 = \frac{6-2}{2} + 3 = 5$. (Pripomeňme, 
že pre $n=6$ sú definované len diagonály $D_1$–$D_4$.) Algoritmus 
pre $n=6$ tak končí výberom členov diagonály $D_{k+1}=D_3$.

Upravený algoritmus tak pre párne $n$ rôzne od 2 a 4 skonštruuje požadovanú 
postupnosť polí. Jediné prirodzené $n>1$, pre ktoré žiadna postupnosť 
zadaných vlastností neexistuje, sú preto 3 a 4.

\fi
---
