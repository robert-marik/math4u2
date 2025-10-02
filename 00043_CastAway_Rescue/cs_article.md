---
keywords:
- geometrie
- pythagorova věta
- osa úsečky
is_finished: True
difficulty: 2
time: 30
---

# Záchrana trosečníka

Letadlo hledá na otevřeném moři pozici trosečníka, který 
má na svém voru zařízení vysílající tísňový signál. 
Zařízení má pouze omezený dosah. Při letu nad mořem 
posádka letadla signál zachytí, ale po chvíli jej ztratí. 
Pilot proto letadlo stočí a podaří se mu signál na kratší 
dobu opět zachytit. 

Trajektorie celého letu je i s naznačeným směrem a místy 
zachycení (body $A_1$ a $A_2$) a ztrát (body $B_1$ a 
$B_2$) signálu znázorněn na mapě.

![Trajektorie letu letadla](math4you_00043_01.svg)

Během obou dob, kdy posádka přijímala signál, letadlo 
neměnilo svou výšku, mezi body $B_1$ a $A_2$ snížilo svou 
výšku o $500\,\text{m}$.

> **Úloha 1.** Konstrukčně určete v mapě pozici $X$ 
> trosečníka.

\iffalse

*Řešení.* Omezený dosah trosečníkova tísňového signálu určuje v 
prostoru nad hladinou polokouli, jejíž střed je polohou 
trosečníka. Vodorovné řezy této polokoule jsou kruhy, které se 
na mapě jeví jako soustředné se středem v bodě $X$. 

Protože letadlo mezi body $A_1$ a $B_1$ nemění svou výšku, je 
$A_1B_1$ tětivou jisté kružnice $k_1$ se středem v bodě $X$. 
Ten tak musí ležet na ose úsečky $A_1B_1$. Ze stejného důvodu 
musí bod $X$ ležet i na ose úsečky $A_2B_2$; je totiž středem 
jisté kružnice $k_2$, jíž je tato úsečka tětivou. 

![Řešení Úlohy 1](math4you_00043_02.svg)

\fi

> **Úloha 2.** V lokalitě se nachází dopravní loď (pozice $L$). 
> Může také zaznamenat trosečníkův tísňový signál, nebo je 
> příliš daleko?
>
> a) Velikosti úseček $LX$ a $A_1X$, $A_2X$ z řešení Úlohy 1 
> přeneste na měřítko. Užitím takto určených vzdáleností 
> (zaokrouhlených na celý nejmenší dílek stupnice) vyřešte 
> úlohu početně.
> 
> b) Vyjděte z řešení Úlohy 1 a úlohu vyřešte znovu, tentokrát 
> pouze užitím geometrických konstrukcí.


\iffalse

*Řešení.*

a) K vyřešení úlohy potřebujeme znát dosah trosečníkova 
zařízení, což je poloměr $r$ polokoule zmíněné v řešení 
předešlé úlohy. Přenesením úseček $A_1X$ a $A_2X$ na měřítko a 
zaokrouhlením jejich délek na desetiny kilometru dostáváme 
$\lvert A_1X \rvert \doteq 2{,}9\,\text{km}$ 
a $\lvert A_2X \rvert \doteq 3{,}4\,\text{km}$. Tyto délky jsou 
zřejmě poloměry $r_1$ a $r_2$ kružnic $k_1$ a $k_2$.

Uvažme takový průmět polokoule, ve kterém se kružnice $k_1$ a 
$k_2$ zobrazí po řadě jako rovnoběžné úsečky $K_1L_1$ a 
$K_2L_2$ takové, že mají stejnou osu $o$, jejich délky jsou po 
řadě $2r_1$ a $2r_2$ a jejich vzdálenost je $0{,}5\,\text{km}$. 
Označme dále střed polokoule $S$, střed úsečky $K_1L_1$ jako 
$S_1$ a střed úsečky $K_2L_2$ jako $S_2$. Viz obrázek, ve 
kterém je pro názornost vyznačena také mořská hladina přímkou $h$.

![Pomocný průmět polokoule při řešení Úlohy 2a)](math4you_00043_03.svg)

Z Pythagorovy věty aplikované na trojúhelníky $SS_1K_1$ a 
$SS_2L_2$ vyplývají rovnosti
$$
\begin{align*}
r^2 &= r_1 ^2 + \lvert SS_1 \rvert ^2 \\
r^2 &= r_2 ^2 + \lvert SS_2 \rvert ^2.
\end{align*}
$$

Platí však $\lvert SS_1 \rvert = \lvert SS_2 \rvert + 0{,}5$. 
Dosazením do první rovnice a porovnáním obou stran dostáváme 
lineární rovnici s jedinou neznámou $\lvert SS_2 \rvert$, 
kterou vyřešíme:
$$
\begin{align*}
r_2 ^2 + \lvert SS_2 \rvert ^2 &= r_1 ^2 + \left( \left\lvert SS_2 \right\rvert + 0{,}5 \right) ^2 \\[1mm]
\left\lvert SS_2 \right\rvert &=  r_2^2 - r_1^2 - 0{,}25
\end{align*}
$$

Vyjádřením $r$ z druhé rovnice a následným dosazením dostáváme
$$
r = \sqrt{r_2 ^2 + \left(r_2^2 - r_1^2 - 0{,}25 \right)^2 } \doteq 4{,}5\,\text{km}.
$$

Vzdálenost lodi od trosečníka je délkou úsečky $LX$. Přenesením 
této úsečky na měřítko vyčteme $\lvert LX \rvert \doteq 4{,}
0\,\text{km}$, úsečka je tedy kratší než dosah $r$ trosečníkova 
signálu. Loď proto může tento signál zaznamenat.

b) K odvození konstrukčního řešení úlohy (tj. sestrojení 
poloměru $r$ polokoule) využijeme stejný pomocný průmět 
polokoule jako v Úloze 2a. Střed polokoule $S$ je průsečíkem 
společné osy $o$ úseček $K_1L_1$ a $K_2L_2$ a osy úsečky 
$L_1L_2$, neboť ta je tětivou obrysové půlkružnice $k$. Hledaný 
poloměr $r$ je pak např. velikostí úsečky $SK_1$,  viz obrázek.

![Pomocný průmět polokoule při řešení Úlohy 2b)](math4you_00043_04.svg)

Při samotném provedení konstrukce přenášíme vzdálenosti $r_1$ a 
$r_2$ z řešení Úlohy 1 (kde připomínáme, že platí 
$r_1=\lvert A_1X\rvert$ a $r_2=\lvert A_2X\rvert$), vzdálenost 
středů kružnic $|S_1S_2|=d_{0{,}5}$, kde $d_{0{,}5}$ označuje 
vzdálenost na mapě odpovídající $0{,}5\,\text{km}$, kterou 
nanášíme z měřítka.

Průmět polokoule na mapě ohraničuje kružnice $l$ se středem v 
bodě $X$ a poloměrem $r$, který přeneseme z pomocného průmětu. 
Po sestrojení této kružnice je vidět, že se loď nachází v 
dosahu nouzového signálu.

![Řešení Úlohy 2b)](math4you_00043_05.svg)

\fi
