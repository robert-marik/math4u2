---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- analytická geometria
- optimalizácia
- všeobecná rovnica priamky
- všeobecná rovnica roviny
is_finished: true
---

# Optimalizácia 

## Lineárne programovanie

Lineárne programovanie je matematická metóda používaná na nájdenie najlepšieho riešenia určitého problému. Jedná sa o techniku, ktorá sa zameriava na maximalizáciu alebo minimalizáciu lineárnej funkcie pri určitých obmedzeniach, ktoré sú takisto vyjadrené ako lineárne rovnice alebo nerovnice.

Táto oblasť začala priťahovať pozornosť matematikov až po prvej svetovej vojne. Prvým z nich bol Leonid Kantorovič, ktorý však v dôsledku vtedajších vládnych represálií (a následne obáv o svoj život) musel túto prácu zanechať. V tehdajšom Sovietskom zväze s centrálne riadenou ekonomikou totiž optimalizovať výrobné procesy nebol práve dobrý nápad (v jednej továrni sa mu napríklad podarilo zefektívniť výrobu na 94 %, ale potom prišlo nariadenie, že všetky závody musia navýšiť svoju efektívnosť rovnakým způsobom).

Skutočným prelomovým bodom v rozvoji lineárneho programovania bolo zverejnenie tzv. simplexového algoritmu na riešenie týchto úloh v roku 1947. Jeho autorom je americký matematik George Dantzig, ktorý sa tejto oblasti začal venovať počas druhej svetovej vojny v snahe optimalizovať niektoré procesy v americkej armáde. Volali to
*metódy programovacieho plánovania pomocou stolných kalkulátorov*. Vo svojej prvej odbornej prednáške na túto tému hovoril o *programovaní v lineárnej štruktúre*, čo sa následne skrátilo iba na *lineárne programovanie*.
Slovo *programovanie* je pozostatkom vojensky motivovanej terminológie, ktorá odkazuje na plánovanie či rozvrhovanie tréningov, logistiky či rozmiestnenia mužstva.
Princípy si ukážeme na nasledujúcich jednoduchých príkladoch.

## Optimalizácia výroby v pražiarni 

> **Úloha 1.**   Berenika a Peter si otvorili novú kaviareň s pražiarňou, kde okrem iného začali vyrábať dve zmesi kávy: letnú a exotickú. Letná zmes je zložená zo $40\,\%$ zŕn sladkej etiópskej kávy a zo $60\,\%$ zŕn šťavnatej kávy z Peru. Exotická zmes je vyrobená z tých istých kávových zŕn, ale v pomere 3:1 (tentokrát je viac etiópskej kávy). K dispozícii je 
> $90\,\text{kg}$ etiópskej kávy a $70\,\text{kg}$ peruánskej kávy. Kilogram letnej zmesi sa predáva za 650 Kč a kilogram exotickej zmesi za 800 Kč. Koľko ktorej zmesi by mali Berenika a Peter z dostupných kávových zŕn namiešať, aby maximalizovali svoj zisk?

\iffalse

*Riešenie* Najprv potrebujeme celý tento problém matematicky modelovať. Začneme tým, že množstvo namiešanej letnej zmesi označíme ako $x$, množstvo exotickej zmesi ako $y$ a zisk z ich predaja označíme ako $z$. Bez ohľadu na množstvo vyrábaných zmesí môžeme zisk vyjadriť pomocou výrazu
$$
z=650x+800y.
$$
Je zrejmé, že množstvá vyrábaných zmesí nemôžu nadobúdať záporné hodnoty, preto musí platiť
$$
  x\geq0\quad \text{a zároveň}\quad y\geq0. \tag{1}
$$
Teraz musíme zohľadniť obmedzené množstvo dostupných kávových zŕn. Celkovú spotrebu etiópskej kávy môžeme vzhľadom na pomery miešania vyjadriť ako
$$
  0{,}4x+0{,}75y 
$$
a v prípade peruánskej kávy to je
$$
  0{,}6x+0{,}25y.
$$
Spolu s dostupným množstvom získavame dvojicu podmienok
$$
  0{,}4x+0{,}75y\leq90 \quad\text{a zároveň}\quad\quad 0{,}6x+0{,}25y\leq70. \tag{2}
$$
Množina bodov, ktoré vyhovujú podmienkam $(1)$ a $(2)$ je
vyšrafovaná na obrázku nižšie, pričom zelenou farbou je zakreslená
hraničná priamka $0{,}4x+0{,}75y=90$ a modrou farbou priamka $0{,}6x+0{,}25y=70$.

![Oblasť vyhovujúca daným podmienkam](00032_obr_1.svg)

Vo vyšrafovanej oblasti sú tak všetky body, ktorých súradnice $x$ 
a $y$ odpovedajú možným riešeniam našej úlohy. Ako ale nájdeme bod s
maximálnym ziskom, t. j. bod, v ktorom je hodnota výrazu $z=650x+800y$ maximálna?

Môžeme si uvedomiť, že tento výraz je rovnicou roviny v trojrozmernom priestore.
Ak z tejto roviny uvažujeme iba tú časť, ktorá je nad vyšrafovanou oblasťou, dostávame v priestore
štvoruholník.
Namiesto toho, aby sme kreslili priestorový obrázok, dokreslíme si do obrázka ešte tzv. *vrstevnice*. Sú to priamky s rovnicami
$$
650x+800y=c
$$
pre vhodné $c$. Význam týchto vrstevníc je podobný ako význam vrstevníc
na mape. Iba namiesto bodov s rovnakou nadmorskou výškou spájajú naše
vrstevnice body, v ktorých dosiahneme rovnaký zisk.

Týmto postupom dostaneme obrázok s vrstevnicami zakreslenými hnedou farbou.

![Oblasť vyhovujúca daným podmienkam](00032_obr_2.svg)

Ako určíme vhodnú hodnotu ? Nemusíme ju zložito počítať, pretože ju môžeme odčítať priamo z obrázka. Pri hodnote $c=0$ získame priamku prechádzajúcu počiatkom súradnicovej sústavy. Keďže všetky vrstevnice sa líšia len hodnotou $c$, sú všetky hnedé priamky rovnobežné. Z obrázka je zrejmé, že maximum (pričom sa vrstevnice s rastúcou hodnotou $c$ posúvajú v severovýchodnom smere) nastáva v bode, kde sa pretínajú modrá a zelená priamka.

Súradnice tohto bodu teda môžeme nájsť ako riešenie sústavy lineárnych rovníc o dvoch neznámych
$$
\begin{align*}
0{,}4x+0{,}75y&=90 \\
0{,}6x+0{,}25y&=70.
\end{align*}
$$
Výsledkom je bod so súradnicami $\left[\frac{600}{7},\frac{520}{7}\right]$. 
Dosadením týchto hodnôt do výrazu $z=650x+800y$ dostaneme hodnotu
maximálneho zisku približne $115\,143\,\text{Kč}$. Tento zisk dosiahnu Berenika s Petrom pri výrobe približne 
$
\frac{600}{7} \approx 85{,}71\,\text{kg}
$
letnej zmesi a 
$
\frac{520}{7} \approx 74{,}29\,\text{kg}
$
exotickej zmesi.

*Poznámka.* To, že riešenie leží v priesečníku dvoch hraničných priamok, nie je náhoda. Pri lineárnych úlohách platí, že ak existuje riešenie, nachádza sa vždy v niektorom z vrcholov mnohouholníka, ktorý ohraničuje všetky prípustné body. Tento fakt možno využiť aj pri úlohách s omnoho väčším počtom neznámych.
Stačí nájsť všetky vrcholy a porovnať funkčné hodnoty. Použitie tzv. hrubej sily však môže byť výpočtovo náročné a vyžaduje zaručenú existenciu riešenia. Napriek tomu táto myšlienka stála pri zrode prvého veľmi efektívneho a dodnes používaného algoritmu na riešenie takýchto úloh, ktorý systematicky prechádza vrcholy (nie však nutne všetkými).

\fi

## Najlepšie parkovisko

> **Úloha 2.** Miestny developer sa rozhodol zakúpiť
> továreň na výrobu videokaziet a magnetofónových pások.
> Továreň už dnes nemá žiadne využitie, a  bude
> zbúraná, aby na jej mieste vyrástlo P+R parkovisko
> pre osobné automobily a zároveň odstavné parkovisko
> pre nákladné automobily. Developer však teraz rieši
> problém, akú nastaviť kapacitu pre jednotlivé druhy
> vozidiel. Celkový dostupný priestor bude $480\,\text{m}^2$. 
> Parkovacie miesto pre osobný automobil zaberie $12\,\text{m}^2$, 
> zatiaľ čo pre nákladný automobil to je $30\,\text{m}^2$. 
Stavebný úrad však zároveň požaduje, aby kapacita pre
osobné automobily bola aspoň dvakrát väčšia ako pre
nákladné, ale zároveň tam musí byť najmenej 6
parkovacích miest pre nákladné automobily.
Stanovte optimálny počet parkovacích miest pre osobné i
nákladné automobily, ktorý bude spĺňať všetky
uvedené podmienky a zároveň maximalizuje zisk z plného
parkoviska, ak za každé parkovacie miesto pre osobné
automobily bude platba 100 Kč a pre nákladné automobily 400 Kč.
\iffalse

*Riešenie.* Môžeme postupovať podobne ako v predchádzajúcom
príklade, avšak je potrebné mať na mysli, že tentokrát
musia byť počty parkovacích miest celočíselné.
Ak označíme $x$ ako počty parkovacích miest pre osobné automobily a $y$ ako počty parkovacích miest pre
nákladné automobily, potom naším cieľom je maximalizovať zisk 
$z$ daný vzťahom
$$
z=100x+400y.
$$
Navyše z uvedených podmienok vyplývajú nasledujúce obmedzenia.

| Podmienka  | Zdôvodnenie | 
| ------------- | ------------- | 
| $y\geq 6$  | požiadavka na minimálny počet pre nákladné automobily | 
| $2y\leq x$  | požiadavka na druh parkovacích miest  | 
| $12x+30y\leq480$ | kapacitné obmedzenie pozemku  | 
| $x,y\in\mathbb{N}\cup\{0\}$  | počty sú prirodzené čísla, resp. nula | 

Množina spĺňajúca všetky uvedené podmienky je znázornená na obrázku nižšie. Vyznačené sú priamky
$y=6$ (zelenou farbou), $2y=x$ (hnedou farbou), $12x+30y=480$ 
(modrou farbou) a vrstevnice $100x+400y=c$ pre rôzne hodnoty $c$ (červenou farbou). Čím väčšie je $c$, tým viac sú vrstevnice „hore vpravo“.

Ružovou farbou je vyznačený mnohouholník, ktorý spĺňa všetky uvedené podmienky okrem poslednej. Čierne body predstavujú všetky body, ktoré spĺňajú aj túto poslednú podmienku, teda súradnice sú prirodzené čísla, pričom nula v tejto oblasti neprichádza do úvahy.

![Oblasť vyhovujúca daným podmienkam](00032_obr_3.svg)

Z obrázka je zrejmé, že maximum bude v bode, ktorý je najviac vpravo hore. Aké sú však jeho súradnice?
Keďže ide o priesečník modrej a hnedej priamky, môžeme jeho súradnice určiť riešením sústavy rovníc
$$
\begin{align*}
2y&=x\\  
12x+30y&=480 
\end{align*}
$$
Jej riešením je usporiadaná dvojica $\left[\frac{160}{9},\frac{80}{9}\right]$, ktorá však nie je celočíselná.

Ak sa na obrázok pozrieme pozornejšie a zvážime smer vrstevníc, môžeme odhadnúť, že hľadané maximum dostaneme pre $y=8$. Súčasne vidíme, že čierny bod s touto hodnotou leží na modrej priamke. Teda po dosadení 
$y=8$ do rovnice tejto priamky dostaneme $x=20$. 

Maximálny zisk $5200$ Kč preto bude dosiahnutý v prípade, keď bude vybudovaných $20$ parkovacích miest pre osobné automobily a $8$ parkovacích miest pre nákladné vozidlá. 

Ako kontrolu môžeme samozrejme určiť všetky celočíselné body spĺňajúce dané obmedzenia a overiť, že v žiadnom z nich nie je hodnota výrazu $100x+400y$ väčšia alebo rovná $5200$.

\fi
