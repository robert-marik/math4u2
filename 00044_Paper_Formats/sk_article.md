---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- postupnosti a rady
- pomer
- geometrická postupnosť
- aritmetická postupnosť
is_finished: true
---

# Matematika ukrytá v liste papiera

## Formáty papiera

Medzinárodný štandard formátov papiera je daný normou ISO 216 a zahŕňa dve základné rady. Rada A 
obsahuje formáty A0-A10 a rada B formáty B0-B10.
Táto norma je založená na pôvodnej norme DIN 476, ktorá sa používala už od roku 1922 v Nemecku. Vytvoril ju nemecký matematik a fyzik Walter Porstmann.

Obe rady majú dve spoločné základné vlastnosti:

1. Všetky formáty sú navzájom podobné pravouholníky.
2. Menší formát vzniká z väčšieho rozpolením, t. j. 
rozdelením na dva navzájom osovo súmerné pravouholníky.[^1]

Tieto vlastnosti nie sú náhodne zvolené. Majú jednak estetický význam a jednak svoje praktické využitie. Napríklad každý list papiera v danom systéme sa dá vyrobiť z najväčšieho kusu prostým rezaním a nevzniká žiadny odpad. 

Rady A aj B ďalej majú každá istú špeciálnu vlastnosť navyše:

* U rady A navyše platí, že obsah najväčšieho papiera A0 je $1\,\text{m}^2$.
* U najväčšieho formátu B0 rady B potom platí, že jeho kratšia strana má dĺžku $1\,\text{m}$.


> **Úloha 1.** Určte koeficient podobnosti (zmenšenia) dvoch po sebe 
> nasledujúcich formátov papiera a určte tiež pomer susedných strán, 
> ktoré musí každý z formátov dodržať.

![Označenie pre Úlohu 1](math4you_00044.svg)

\iffalse

*Riešenie.* Najprv si uvedomme, že pravouholníkom 
je obdĺžnik (pretože žiadnym rozpolením štvorca 
nemôže vzniknúť štvorec). Rozpolenie dotyčného 
obdĺžnika vykonávame pozdĺž osi dlhšej strany tohto 
obdĺžnika. Ak by sme polenie vykonali pozdĺž osi 
kratšej strany, nedostali by sme obdĺžnik podobný 
s pôvodným – dlhšia strana sa nezmení a kratšia sa 
skráti. 

Ak označíme $a$ dlhšiu stranu obdĺžnika, $b$ jeho 
kratšiu stranu a $k$ koeficient zmenšenia dvoch po 
sebe idúcich formátov, platí $k\cdot a = b$ a 
$k\cdot b = \frac{a}{2}$. Dosadením prvého 
vzťahu za $b$ v druhom vzťahu dostávame
$$
\begin{align*}
k^2 \cdot a &= \frac{a}{2} \quad / :a \\
k^2 &= \frac{1}{2} \qquad \rightarrow \qquad k = \frac{1}{\sqrt{2}}=\frac{\sqrt{2}}{2}.
\end{align*}
$$
Zo vzťahu $k\cdot a = b$ ďalej plynie, že pomer 
strán obdĺžnika $a:b$ je prevrátenou hodnotou 
koeficientu $k$, t. j. $\sqrt{2}$.

\fi

> **Úloha 2.** Vypočítajte rozmery najväčšieho formátu A0, ak viete, 
> že majú jeho dĺžky strán celočíselné veľkosti v mm a jeho obsah je 
> čo možno najbližšie jednému štvorcovému metru.

\iffalse

*Riešenie.* Z predchádzajúcej úlohy vieme, že rozmery 
listu formátu A0 sú $b_0$ (kratšia strana) a 
$b_0\cdot\sqrt{2}$ (dlhšia strana) pre neznámu dĺžku
$b_0$, ktorú je potrebné vypočítať. Vieme, že 
$$
b_0\cdot b_0\cdot \sqrt{2} = 1000000\,\text{mm}^2,
$$
a teda po vyjadrení $b_0$ a zaokrúhlení výsledku 
na jednotky dostávame hodnotu $b_0\doteq 841\,\text{mm}$. 
Dĺžka dlhšej strany formátu A0 je potom súčinom $841\cdot \sqrt{2} \doteq 1189\,\text{mm}$. 

\fi

> **Úloha 3.** Rada formátov B má okrem spoločných vlastností platných pre obe rady A aj B
> tiež tú vlastnosť, že dĺžka kratšej strany najväčšieho formátu B0 je 
> rovná jednému metru. Ukážte, že ak formát A0 bude mať obsah presne jeden meter štvorcový a ak pripustíme 
> u všetkých formátov neceločíselné rozmery, platí pre každé nezáporné celé 
> číslo $n$ vzťah
> $$
> S(\mathrm{B}(n+1))=\sqrt{S(\mathrm{A}(n)) \cdot S(\mathrm{A}(n+1))},
> $$
> t. j. obsah formátu $\mathrm{B}(n+1)$ je geometrickým priemerom obsahov 
> formátov $\mathrm{A}(n)$ a $\mathrm{A}(n+1)$.

\iffalse

*Riešenie.* Pretože kratšia strana formátu B0 meria 
$1\,\text{m}$, meria jeho dlhšia strana podľa 
riešenia Úlohy 1 (platného aj pre formát B, pretože 
vychádzame z rovnakých vlastností) $\sqrt{2}\,\text{m}$. 
Teda obsah formátu B0 je $\sqrt{2}\,\text{m}^2$ a 
každý nasledujúci list formátu $\mathrm{B}(n)$ má 
polovičný obsah oproti predchádzajúcemu, 
teda $S\left( \mathrm{B}(n) \right) = \frac{\sqrt{2}}{2^n}\,\text{m}^2$ 
pre každé nezáporné celé $n$.

Pretože ďalej $S(\mathrm{A}0)=1\,\mathrm{m}^2$ a každý nasledujúci list 
formátu $\mathrm{A}(n)$ má polovičný obsah oproti predchádzajúcemu, 
je $S\left( \mathrm{A}(n) \right) = \left( \frac{1}{2}\right)^n = \frac{1}{2^n}\,\text{m}^2$ 
pre každé $n$. Teda
$$
\begin{align*}
\sqrt{S(\mathrm{A}(n)) \cdot S(\mathrm{A}(n+1))} &= \sqrt{\frac{1}{2^n} \cdot \frac{1}{2^{n+1}} }  
=\sqrt{\frac{1}{2^n} \cdot \frac{1}{2^n} \cdot \frac{1}{2} } \\
&= \frac{1}{2^n} \cdot \frac{\sqrt{2}}{2} = \frac{\sqrt{2}}{2^{n+1}} = S(\mathrm{B}(n+1)).
\end{align*}
$$

\fi

## Skladanie papiera

Možno vás už niekedy napadla otázka, koľkokrát je možné preložiť 
papier formátu A4 napoly a možno ste si to aj sami vyskúšali. 
Pravdepodobne vás ale ani nenapadlo, že odpoveď na túto otázku 
môže dať matematik, ani papier nemusí vôbec prekladať.

Predstavme si nasledujúci jednoduchý model prekladania papiera.

![Model preloženia papiera](math4you_00044_2.svg)

Pri preložení papiera napolovicu sa nám vždy časť papiera spotrebuje na vytvorenie 
skladu. Jeho tvar si môžeme modelovať ako polovicu kružnice, ktorej polomer
je rovný hrúbke papiera. Navyše si tiež môžeme všimnúť, že papier sa pri prekladaní
vrství. Na začiatku máme len jednu vrstvu, po prvom preložení dve vrstvy, po druhom
preložení štyri vrstvy atď. V ďalších úlohách budeme pracovať s týmto modelom.

> **Úloha 4.** Aká by bola hrúbka navrstveného kancelárskeho papiera po štyroch, 
siedmych, desiatich, dvadsiatich jeden a štyridsiatich dvoch preloženiach? Predpokladajme, že hrúbka nášho
> listu papiera je $t_0=0{,}1\,\text{mm}$.

\iffalse

*Riešenie.* Je možné si ľahko všimnúť, že po $k$ preloženiach dostaneme celkom $2^k$ vrstiev papiera. Hrúbky
by tak boli
$$
\begin{align*}
t_4=&t_0\cdot 2^4=1{,}6\,\text{mm}\\
t_7=&t_0\cdot 2^{7}=12{,}8\,\text{mm}\\
t_{10}=&t_0\cdot 2^{10}=102{,}4\,\text{mm}\\
t_{21}=&t_0\cdot 2^{21}\approx 209{,}7\,\text{m}\\
t_{42}=&t_0\cdot 2^{42}\approx 439\,804\,\text{km}
\end{align*}
$$

\fi

Podľa výsledkov predchádzajúcej úlohy je vidieť, že pre 
prekladanie papiera musí existovať nejaký limit. 
Jednou z možností, ako tento limit poznať, je 
skúmanie koľko papiera sa nám pri prekladaní vlastne 
stráca pri vytváraní skladu.

> **Úloha 5.** Aké množstvo papiera sa "stratí" pri jeho skladaní?

\iffalse

*Riešenie.* Uvažujme papier o hrúbke $t$. Pri prvom 
preložení sa na sklade vytvorí 
polkružnica o polomere $t$ (pozri predchádzajúci obrázok), 
na preloženie teda 
potrebujeme $\pi t$ papiera. Pri druhom preložení
sa vytvoria dve polkružnice. Jedna o polomere $t$ a 
druhá o polomere $2t$, potrebujeme teda $\pi t + 2\pi t$ 
papiera a dohromady
$$
\pi t+ (\pi t+2\pi t)\,.
$$
Pri treťom preložení sa vytvoria polkružnice o 
polomeroch $t$, $2t$, $3t$ a $4t$. Stratíme teda
$\pi t +2\pi t + 3\pi t + 4\pi t$ papiera.
Celková strata bude
$$
\pi t+ (\pi t+2\pi t) + (\pi t +2\pi t + 3\pi t + 4\pi t)
$$
Analogicky po $n$ zloženiach stratíme
$$
\pi t+ (\pi t+2\pi t) + \cdots + (\pi t +2\pi t + \cdots  + 2^{n-1}\pi t)
$$
papiera. Vyňatím $\pi t$ si môžeme všimnúť, že máme v zátvorkách súčet prvých členov aritmetickej postupnosti
$$
\pi t\left[1+(1+2)+(1+2+3+4)+\cdots+(1+2+\cdots+2^{n-1}) \right]\,.
$$
Použitím opakovaného vzorca pre súčet prvých členov aritmetickej postupnosti dostaneme
$$
\frac{\pi t}{2}(1\cdot 2+2\cdot 3+4\cdot 5+\cdots+2^{n-1}\cdot(2^{n-1}+1))\,.
$$
Tu je možné $k$-tý člen všeobecne zapísať ako
$$
2^{k-1}\cdot\left(2^{k-1}+1\right)=(2^2)^{k-1}+2^{k-1}.
$$
Vzťah pre celkovú stratu papiera teda môžeme prepísať v tvare
$$
\frac{\pi t}{2}\left[\left((2^2)^0+(2^2)^1+\cdots+(2^2)^{n-1}\right)+\left(2^0+2^1+\cdots+2^{n-1}\right) \right]\,.
$$
Dostávame tak súčet prvých členov dvoch geometrických
postupností, môžeme teda použiť vzorec pre ich súčet a dostaneme
$$
\frac{\pi t}{2}\left( \frac{2^{2n}-1}{3} + 2^n-1 \right)\,.
$$
Po vyňatí $\frac 13$ zo zátvorky máme
$$
\frac{\pi t}{6}\left((2^n)^2+3\cdot 2^n-4\right)
$$
a rozkladom na súčin získame
$$
\frac{\pi t}{6}(2^n+4)(2^n-1)\,.
$$
Tento posledný vzťah vlastne vyjadruje akýsi odhad 
minimálnej dĺžky papiera hrúbky $t$, ktorý potrebujeme, aby sme ho mohli $n$-krát preložiť.

\fi

> **Úloha 6.** Koľkokrát je možné preložiť typický 
> kancelársky papier formátu A4 o hrúbke $0{,}1\,\text{mm}$? 

\iffalse

*Riešenie.* Využitím výsledku predchádzajúcej úlohy vieme, že hľadáme také najväčšie prirodzené $n$, aby platilo
$$
\frac{\pi \cdot 0{,}1}{6}(2^n+4)(2^n-1)<297.
$$
Presné riešenie tejto nerovnice by nebolo úplne jednoduché, 
ale našťastie nie je nutne potrebné. Stačí nám dosadiť 
nejaké vhodné $n$:
$$
\begin{align*}
\frac{\pi \cdot 0{,}1}{6}(2^6+4)(2^6-1)\doteq224{,}31;\\
\frac{\pi \cdot 0{,}1}{6}(2^7+4)(2^7-1)\doteq 877{,}76.
\end{align*}
$$
Podľa tohto modelu je teda možné papier danej veľkosti 
prehnúť maximálne šesťkrát. 

\fi

Pre zaujímavosť dodajme, že ako prvá rovnicu z 
Úlohy 5 odvodila stredoškolská študentka Britney 
Gallivan z Kalifornie, ktorá je momentálne držiteľkou 
svetového rekordu v Guinessovej knihe rekordov za 
najväčší počet preložení papiera napoly. Celkom 
preložila papier dvanásťkrát. Na to však nemohla 
použiť normálny papier formátu A4, ale použila 
toaletný papier dĺžky $1\,219$ metrov. Navyše použila 
inú techniku skladania (striedala smery).

## Literatúra
1. Niss, Mogens; Bluem Werner. *The Learning and Teaching of Mathematical Modelling*, Routledge 2020, 978-1-315-18931-4

2. *Most times to fold a piece of paper.* https://www.guinnessworldrecords.com/world-records/494571-most-times-to-fold-a-piece-of-paper

3. *Wikipedia. Paper size.*  https://en.wikipedia.org/wiki/Paper_size



[^1]: Dĺžky strán formátov, ktoré vznikli rozpolením, sú zaokrúhlené na celé milimetre nadol. Najčastejšie používaný formát A4 má rozmery $210 \times 297 \, \mathrm{mm}$.

