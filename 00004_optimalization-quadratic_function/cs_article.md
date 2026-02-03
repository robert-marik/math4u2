---
workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- funkce
- kvadratická funkce
- optimalizace
is_finished: true
difficulty: 1
time: 20
---

# Nákup vozů pro taxislužbu

V České Republice majitel pražské taxislužby zvažuje, zda pořídit další vozy a kolik jich pořídit 
tak, aby jeho zisk byl co největší. Momentálně má $3$ vozy a z každého vozu (bez započítání nákladů na údržbu a řidiče) má průměrný měsíční výdělek $60\,000$ Kč. Dle letitých zkušeností v oboru však 
očekává, že s každým nakoupeným vozem průměrný výdělek každého vozu klesne 
o $5\,000$ Kč, neboť dojde k částečnému přelivu zákazníků do nového vozu. Naopak, s každým prodaným vozem tento výdělek o $5\,000$ Kč vzroste. Ještě dodejme, že dříve zmíněné náklady na řidiče a vůz za jeden měsíc činí $40\,000$ Kč.

>**Úloha 1.** Jaký je (po odečtení nákladů na údržbu a řidiče) měsíční zisk  majitele taxislužby nyní? 

\iffalse

*Řešení.* Každý ze tří vozů majiteli taxislužby přináší čistý zisk (po odečtení nákladů)
$20\,000$ Kč.  Dohromady tak současný čistý zisk ze tří vozů činí $60\,000$ Kč.

\fi

>**Úloha 2.** Určete předpis funkce, která vyjadřuje čistý zisk majitele taxislužby v závislosti na počtu nově dokoupených (případně vyřazených) vozů. O jakou funkci se jedná a jak vypadá její graf?

\iffalse

*Řešení.* Označme $n \in \mathbb{N} \cup \{-3,-2,-1,0\}$ počet nově pořízených vozů. Záporný počet přitom znamená, že se majitel příslušného počtu vozů zbavuje. Označme dále $f(n)$ čistý zisk majitele za jeden měsíc. 
Víme, že čistý zisk jednoho ze stávajících tří vozů je $20\,000$ Kč. Od této částky je třeba odečíst 
částku $5\,000n$ Kč, protože podle zadání víme, že s nákupem každého dalšího vozu klesne zisk z každého vozu o $5\,000$ Kč. Celkem tedy jeden vůz přinese 
majiteli čistý zisk $20\ 000-5\ 000n$ Kč. Celkový zisk při dokoupení $n$ vozů dostaneme vynásobením této částky aktuálním počtem vozů (a ten je roven $3+n$):  

$$
f(n)=(20\ 000-5\ 000n)(3+n)
$$

Po roznásobení a úpravě pravé strany dostaneme předpis  

$$
 f(n)= -5\ 000n^2 + 5\ 000n + 60\ 000. 
$$

Protože definičním oborem této funkce je množina $\mathbb{N} \cup \{-3,-2,-1,0\}$, je grafem naší funkce množina izolovaných bodů ležících na parabole
$p(x)=-5\ 000x^2 + 5\ 000x + 60\ 000$. Můžeme si všimnout, že koeficient u kvadratického členu je záporný, což znamená, že se jedná o konkávní parabolu. 

![Graf funkce $f$](parabola.png)

\fi

>**Úloha 3.** Určete jaký je maximální možný zisk majitele. O kolik se tento zisk liší od současného? Kolik vozů musí majitel koupit (nebo eventuálně prodat)?

\iffalse

*Řešení.* 
Naším úkolem je nyní určit maximum funkce $f$. Jedním ze způsobů, jak toto maximum najít, je provést tzv. úpravu na čtverec: 

$$
\begin{align*}
 f(n) &= -5\ 000n^2 + 5\ 000n + 60\ 000 = 
 -5000 \left( n^2 - n - 12 \right) = \\
 &= -5000 \left[ \left( n-\frac{1}{2} \right)^2 -\frac{1}{4}-12\right]
 = -5000 \left( n-\frac{1}{2} \right)^2 + 61\,250
\end{align*}
$$

Nyní je hezky vidět, že maximalitu $f(n)$ zajistíme, pokud bude výraz $\left( n-\frac{1}{2} \right)^2$ co nejmenší. To je jasné, protože je tento výraz nezáporný a v předpisu $f(n)$ se objevuje jeho záporný násobek. 
Vzhledem k tomu, že nás zajímají pouze hodnoty $n \in \mathbb{N} \cup \{-3,-2,-1,0\}$, je zřejmé, že výraz $\left( n-\frac{1}{2} \right)^2$ je nejmenší (a $f(n)$ tedy největší) pro $n=0$ a pro $n=1$. 

Zjistili jsme, že současný stav (ten odpovídá hodnotě $n=0$) je optimální a maximální možný čistý zisk majitele je $60\,000$ Kč. Pokud by majitel ještě jeden vůz dokoupil (to odpovídá hodnotě $n=1$), docílil by stejného zisku. Jakýkoliv jiný počet vozů by vedl ke snížení čistého zisku. 

*Poznámka.*
Pokud by definičním oborem funkce $f$ byla množina všech reálných čísel, maximum by se realizovalo pro $n=\frac{1}{2}$.  

\fi





<!-- STARÁ VERZE 

To se nachází v bodě, který je 
aritmetickým průměrem reálných kořenů kvadratického polynomu (za předpokladu, 
že existují). Tyto kořeny nyní určíme:

$$
\begin{aligned}
-5\ 000x^2 + 5\ 000x + 60\ 000 &= 0 \\
x^2  - x - 12 &= 0\\
(x-4)(x+3)&=0
\end{aligned}
$$


Kořeny kvadratické rovnice jsou $x_1=4$ a $x_2=-3$, tedy maximum funkce $f$ je 
v bodě $$x_{max}=\frac{-3+4}{2}=\frac{1}{2}.$$ 

![Graf funkce](04_graph_smaller.jpg)

Toto maximum je však nedosažitelné (nelze 
koupit půl auta). Nejvyšší funkční hodnota, kterou má smysl uvažovat, se v 
tomto případě nachází v nejbližších celočíselných bodech, tj. $x=0$ nebo $x=1$ 
(v obou bodech je stejná, jak plyne ze symetrie paraboly). To však znamená, 
že pro majitele není výhodné pořizovat další auta, protože jeho aktuální zisk 
je rovněž maximálním.
-->

