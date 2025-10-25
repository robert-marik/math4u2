---
keywords:
- analytická geometria
- kvadratická rovnica
- sústava rovníc
- rovnica kružnice
is_finished: true
difficulty: 2
time: 20

---

# Optimalizácia výnosov

Pri rozhodovaní o investíciách nestačí spoliehať sa na jednoduché lineárne modely – trh je 
totiž dynamický a plný neistôt. Zostavenie optimálneho investičného portfólia si tak 
vyžaduje prístup, ktorý zohľadní nielen očakávaný výnos, ale aj riziko a ďalšie obmedzenia, 
ako sú dostupné finančné prostriedky alebo požiadavky na diverzifikáciu. Výnosy jednotlivých 
aktív nie je možné vopred presne určiť – ich správanie je ovplyvnené mnohými faktormi, a preto je potrebné 
využiť modely založené na kvadratických funkciách. Práve tento prístup – dnes známy ako moderná 
teória portfólia – položil základy pre nový pohľad na investovanie. Za zásadný prínos v tejto oblasti 
boli v roku 1990 ocenení Nobelovou cenou Harry Markowitz, William Sharpe a Merton Miller.

Tieto problémy tak vedú na úlohy tzv. *kvadratického programovania*, čo je oblasť matematickej optimalizácie, 
ktorá sa zaoberá hľadaním extrémov (zvyčajne minima alebo maxima) kvadratickej funkcie na množine bodov vymedzenej 
lineárnymi rovnicami a nerovnicami.

## Influencer túži po úspechu

Neznámy influencer by rád pomocou propagácie príspevkov a platenej reklamy zvýšil počet svojich sledujúcich 
na Instagrame a TikToku. Podľa dostupných informácií predpokladá, že investovaných 10 000 Kč do propagácie
na Instagrame mu prinesie 1000 sledujúcich a rovnaká suma investovaná do reklamy na TikToku mu prinesie tiež
1000 sledujúcich na tejto sociálnej sieti. Vďaka výhodnej ponuke môže minúť maximálne 20 000 Kč za propagáciu 
na Instagrame a 10 000 Kč za reklamu na TikToku.

> **Úloha 1.** Koľko peňazí má influencer minúť za reklamu a propagáciu na jednotlivých sociálnych sieťach, 
> ak sa chce čo najviac priblížiť tomu, aby mal 3 000 sledujúcich na Instagrame a 2 000 sledujúcich 
> na TikToku?

\iffalse

*Riešenie.* Označme $x$ veľkosť investície do propagácie na Instagrame v desiatkach tisíc a podobne $y$ 
veľkosť investície do reklamy na TikToku, tak optimálna hodnota celkových nákladov musí spĺňať podmienky 
$$
0\leq x \leq 2 \qquad\text{a}\qquad 0\leq y\leq 1,
$$
t. j. leží v obdĺžniku. Do tej istej sústavy súradníc môžeme tiež vyznačiť aj bod, ktorý označuje
cieľovú hodnotu počtu sledujúcich. Ak je $x$ počet sledujúcich na Instagrame v tisícoch a $y$
počet sledujúcich v tisícoch na TikToku, tak sa jedná o bod so súradnicami $[3,2]$.

Hľadáme teda bod, ktorý leží vnútri daného obdĺžnika a má najmenšiu vzdialenosť od bodu $[3,2]$.

Vzdialenosť ľubovoľného bodu $[x,y]$ od bodu $[3,2]$ je daná vzťahom 
$$
v(x,y)=\sqrt{(x-3)^2+(y-2)^2}.
$$
Keďže odmocnina je rastúca funkcia, tak ak $0\leq a<b$, potom nutne platí aj $\sqrt{a}<\sqrt{b}$.
Aby sme teda minimalizovali hodnotu $\sqrt{(x-3)^2+(y-2)^2}$, stačí minimalizovať hodnotu $(x-3)^2+(y-2)^2$.

Pre ľubovoľné $c>0$ rovnosť 
$$
  (x-3)^2+(y-2)^2=c
$$
zodpovedá kružnici so stredom v bode $[3,2]$ a polomerom $\sqrt{c}$, t. j. našou úlohou je nájsť 
kružnicu s najmenším možným polomerom, ktorá má neprázdny prienik s daným obdĺžnikom. Situácia
je znázornená na obrázku, z ktorého môžeme riešenie uhádnuť. 

![K riešeniu Úlohy 1](math4you_00051_01.svg)

Odtiaľ vidíme, že riešením je bod $[2,1]$. Je to však skutočne pravda? Z obrázku vidíme, že výsledná kružnica 
sa dotkne daného obdĺžnika v pravom hornom vrchole. To znamená, že prienik tejto kružnice s priamkou určujúcou hornú stranu 
obdĺžnika a prienik kružnice s priamkou určujúcou pravú stranu obdĺžnika musia byť rovnaké. Inými slovami, sústavy
$$
\begin{align*}
(x-3)^2+(y-2)^2&=c\\  
y&=1
\end{align*}
$$
a 
$$
\begin{align*}
  (x-3)^2+(y-2)^2&=c\\ 
  x&=2
\end{align*}
$$
musia mať aspoň jedno spoločné riešenie. Vyriešiť každú sústavu osobitne nemôžeme, pretože by sme dostali kvadratickú 
rovnicu o 2 neznámych. Avšak dosadením $x=2$ a $y=1$ dostaneme dvojicu rovníc
$$
\begin{align*}
  (x-3)^2+1&=c\\ 
  1+(y-2)^2&=c,
\end{align*}
$$
z čoho vyplýva, že nutne 
$$
  (x-3)^2+1=1+(y-2)^2
$$
alebo
$$
  (x-3)^2=(y-2)^2,
$$
čo po odmocnení dáva
$$
|x-3|=|y-2|.
$$
Táto rovnosť je zjavne splnená pre bod $[2,1]$. Vidíme teda, že najbližšie sa svojmu cieľu dostane, ak investuje
maximálnu sumu 20 000 Kč za propagáciu na Instagrame a 10 000 Kč za reklamu na TikToku.

\fi

> **Úloha 2.** Ako sa zmení riešenie Úlohy 1, ak je cieľová hodnota 1 000 
> sledujúcich na Instagrame a 3 000 na TikToku?

\iffalse

*Riešenie.* V tomto prípade minimalizujeme vzdialenosť od bodu 
$[1,3]$. Situácia tak vyzerá nasledovne.

![K riešeniu Úlohy 2](math4you_00051_02.svg)

Riešením teda bude bod ležiaci na priamke $y=1$, čo nás privádza k sústave
$$
\begin{align*}
(x-1)^2+(y-3)^2&=c\\ 
y&=1.
\end{align*}
$$ 
Jedná sa o sústavu kvadratickej a lineárnej rovnice o 3 neznámych, z ktorej ľahko urobíme kvadratickú 
rovnicu o 2 neznámych
$$
(x-1)^2+4=c.
$$
Z obrázku vidíme, že hľadaná kružnica s najmenším polomerom sa daného obdĺžnika iba dotkne, 
t. j. číslo $c$ musí byť také, že kvadratická rovnica má iba 1 riešenie (ak nemá žiadne, je 
polomer malý a kružnica má prázdny prienik s obdĺžnikom, ak má dve rôzne riešenia, potom nutne existuje 
kružnica s o niečo menším polomerom, ktorá má opäť neprázdny prienik s obdĺžnikom). Riešenie kvadratickej 
rovnice je
$$
x_{1,2}=\pm\sqrt{c-4}+1.
$$
Riešenie bude jediné (resp. obe riešenia splynú), iba pre $c=4$. V takom prípade bude $x=1$, t. j. riešením je bod 
$[1,1]$. Tentoraz teda stačí minúť 10 000 Kč za propagáciu na Instagrame a 10 000 Kč za reklamu na TikToku.

\fi
