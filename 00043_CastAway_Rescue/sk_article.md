---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- geometria v rovine
- Pytagorova veta
- os úsečky
is_finished: true
---

# Záchrana stroskotanca

Lietadlo hľadá na otvorenom mori pozíciu stroskotanca, ktorý 
má na svojom člne zariadenie vysielajúce tiesňový signál. 
Zariadenie má len obmedzený dosah. Pri lete nad morom 
posádka lietadla signál zachytí, ale po chvíli ho stratí. 
Pilot preto lietadlo stočí a podarí sa mu signál na kratší 
dobu opäť zachytiť. 

Trajektória celého letu je aj s naznačeným smerom a miestami 
zachytenia (body $A_1$ a $A_2$) a strát (body $B_1$ a 
$B_2$) signálu znázornená na mape.

![Trajektória letu lietadla](math4you_00043_01.svg)

Počas oboch dôb, keď posádka prijímala signál, lietadlo 
nemalo svoju výšku, medzi bodmi $B_1$ a $A_2$ znížilo svoju 
výšku o $500\,\text{m}$.

> **Úloha 1.** Konštrukčne určte v mape pozíciu $X$ 
> stroskotanca.

\iffalse

*Riešenie.* Obmedzený dosah stroskotancovho tiesňového signálu určuje v 
priestore nad hladinou pologuľu, ktorej stred je polohou 
stroskotanca. Vodorovné rezy tejto pologule sú kruhy, ktoré sa 
na mape javia ako sústredné so stredom v bode $X$. 

Pretože lietadlo medzi bodmi $A_1$ a $B_1$ nemení svoju výšku, je 
$A_1B_1$ tetivou istej kružnice $k_1$ so stredom v bode $X$. 
Ten tak musí ležať na osi úsečky $A_1B_1$. Z rovnakého dôvodu 
musí bod $X$ ležať aj na osi úsečky $A_2B_2$; je totiž stredom 
istej kružnice $k_2$, ktorej je táto úsečka tetivou. 

![Riešenie Úlohy 1](math4you_00043_02.svg)

\fi

> **Úloha 2.** V lokalite sa nachádza dopravná loď (pozícia $L$). 
> Môže tiež zaznamenať stroskotancov tiesňový signál, alebo je 
> príliš ďaleko?
>
> a) Veľkosti úsečiek $LX$ a $A_1X$, $A_2X$ z riešenia Úlohy 1 
> preneste na mierku. Užitím takto určených vzdialeností 
> (zaokrúhlených na celý najmenší dielok stupnice) vyriešte 
> úlohu početne.
> 
> b) Vychádzajte z riešenia Úlohy 1 a úlohu vyriešte znovu, tentoraz 
> len užitím geometrických konštrukcií.


\iffalse

*Riešenie.*

a) Na vyriešenie úlohy potrebujeme poznať dosah stroskotancovho 
zariadenia, čo je polomer $r$ pologule zmienený v riešení 
predošlej úlohy. Prenesením úsečiek $A_1X$ a $A_2X$ na mierku a 
zaokrúhlením ich dĺžok na desatiny kilometra dostávame 
$\lvert A_1X \rvert \doteq 2{,}9\,\text{km}$ 
a $\lvert A_2X \rvert \doteq 3{,}4\,\text{km}$. Tieto dĺžky sú 
zrejme polomery $r_1$ a $r_2$ kružníc $k_1$ a $k_2$.

Uvažujme taký priemet pologule, v ktorom sa kružnice $k_1$ a 
$k_2$ zobrazia po rade ako rovnobežné úsečky $K_1L_1$ a 
$K_2L_2$ také, že majú rovnakú os $o$, ich dĺžky sú po 
rade $2r_1$ a $2r_2$ a ich vzdialenosť je $0{,}5\,\text{km}$. 
Označme ďalej stred pologule $S$, stred úsečky $K_1L_1$ ako 
$S_1$ a stred úsečky $K_2L_2$ ako $S_2$. Pozri obrázok, v 
ktorom je pre názornosť vyznačená aj morská hladina priamkou $h$.

![Pomocný priemet pologule pri riešení Úlohy 2a)](math4you_00043_03.svg)

Z Pytagorovej vety aplikovanej na trojuholníky $SS_1K_1$ a 
$SS_2L_2$ plynú rovnosti
$$
\begin{align*}
r^2 &= r_1 ^2 + \lvert SS_1 \rvert ^2 \\
r^2 &= r_2 ^2 + \lvert SS_2 \rvert ^2.
\end{align*}
$$

Platí však $\lvert SS_1 \rvert = \lvert SS_2 \rvert + 0{,}5$. 
Dosadením do prvej rovnice a porovnaním oboch strán dostávame 
lineárnu rovnicu s jedinou neznámou $\lvert SS_2 \rvert$, 
ktorú vyriešime:
$$
\begin{align*}
r_2 ^2 + \lvert SS_2 \rvert ^2 &= r_1 ^2 + \left( \left\lvert SS_2 \right\rvert + 0{,}5 \right) ^2 \\[1mm]
\left\lvert SS_2 \right\rvert &=  r_2^2 - r_1^2 - 0{,}25
\end{align*}
$$

Vyjadrením $r$ z druhej rovnice a následným dosadením dostávame
$$
r = \sqrt{r_2 ^2 + \left(r_2^2 - r_1^2 - 0{,}25 \right)^2 } \doteq 4{,}5\,\text{km}.
$$

Vzdialenosť lode od stroskotanca je dĺžkou úsečky $LX$. Prenesením 
tejto úsečky na mierku vyčítame $\lvert LX \rvert \doteq 4{,}
0\,\text{km}$, úsečka je teda kratšia než dosah $r$ stroskotancovho 
signálu. Loď preto môže tento signál zaznamenať.

b) Na odvodenie konštrukčného riešenia úlohy (t. j. skonštruovanie 
polomeru $r$ pologule) využijeme rovnaký pomocný priemet 
pologule ako v Úlohe 2a. Stred pologule $S$ je priesečníkom 
spoločnej osi $o$ úsečiek $K_1L_1$ a $K_2L_2$ a osi úsečky 
$L_1L_2$, pretože tá je tetivou obrysu polkružnice $k$. Hľadaný 
polomer $r$ je potom napr. veľkosťou úsečky $SK_1$, pozri obrázok.

![Pomocný priemet pologule pri riešení Úlohy 2b)](math4you_00043_04.svg)

Pri samotnom vykonaní konštrukcie prenášame vzdialenosti $r_1$ a 
$r_2$ z riešenia Úlohy 1 (kde pripomíname, že platí 
$r_1=\lvert A_1X\rvert$ a $r_2=\lvert A_2X\rvert$), vzdialenosť 
stredov kružníc $|S_1S_2|=d_{0{,}5}$, kde $d_{0{,}5}$ označuje 
vzdialenosť na mape zodpovedajúcu $0{,}5\,\text{km}$, ktorú 
nanášame z mierky.

Priemet pologule na mape ohraničuje kružnica $l$ so stredom v 
bode $X$ a polomerom $r$, ktorý prenesieme z pomocného priemetu. 
Po skonštruovaní tejto kružnice je vidieť, že sa loď nachádza v 
dosahu núdzového signálu.

![Riešenie Úlohy 2b)](math4you_00043_05.svg)

\fi
