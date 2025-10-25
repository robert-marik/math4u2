---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- komplexné čísla
- Gaussova rovina
- postupnosti
- konvergencia
- absolútna hodnota
is_finished: true
---

# Mandelbrotova množina

Mandelbrotova množina je jedným z najznámejších a najkrajších fraktálov, ktorý fascinuje matematikov, vedcov aj umelcov po celom svete. Hoci na prvý pohľad vyzerá ako zložitý obrazec, je založená na jednoduchom matematickom pravidle opakovaného umocňovania a sčítania. To, čo ju robí takou zaujímavou, je jej nekonečná zložitosť a nádherné vzory, ktoré sa skrývajú v každom detaile.

![Mandelbrotova množina; farba bodov v jej okolí zodpovedá poradiu člena postupnosti, u ktorého sa prvýkrát zistí, že táto postupnosť ide do nekonečna.](Mandelbrot.png)

Využitie Mandelbrotovej množiny siaha ďaleko za hranice matematiky. Nachádza sa v počítačovej grafike, kde sa používa na tvorbu zložitých a realistických objektov pri modelovaní prírodných štruktúr, ako sú pobrežia, hory alebo oblačnosť. Dá sa využiť dokonca aj v ekonómii a fyzike, kde pomáha pri simuláciách chaotických systémov.

Mandelbrotova množina je dôkazom, že aj jednoduché matematické postupy môžu viesť k neuveriteľne komplexným a krásnym výsledkom, ktoré majú reálne využitie.

## Vytvorenie množiny

Predstavme si pomerne jednoduchý rekurentný vzťah
$$
z_{n+1}=z_{n}^2+c,
$$ 
kde za počiatočnú hodnotu dosadíme $z_0 = 0$ a $c$ predstavuje ľubovoľné komplexné číslo. Francúzsko-amerického matematika Benoita Mandelbrota (1924–2010) zaujímalo, kedy je postupnosť takto vzniknutých čísel ohraničená, t. j. pre ktoré $c$ z komplexnej roviny postupnosť konverguje alebo osciluje. Ak v nejakom bode postupnosť diverguje, zaujímalo ho aj to, ako rýchlo. Dá sa dokázať, že ak absolútna hodnota niektorého člena postupnosti $z_{n}$ presiahne hodnotu 2, potom táto postupnosť ohraničená nie je.

*Mandebrotova množina* je teda množina bodov $c$ v komplexnej rovine, pre ktoré postupnosť vytvorená vyššie uvedenou rekurentnou formulou konverguje alebo osciluje. Vďaka uvedenému faktu vieme, že pre každý člen $z$ tejto postupnosti musí platiť, že jeho absolútna hodnota $|z|$ je menšia alebo rovná dvom.

Overenie, či dané $c$ patrí do Mandelbrotovej množiny, prebieha tak, že vypočítame jednotlivé iterácie a sledujeme absolútne hodnoty týchto iterácií. Pre výpočet iterácií použijeme rekurentný vzťah

$$
z_{n+1}=z_{n}^2+c,\qquad z_0=0.
$$

Napr. pre $c=-i$ máme

$$z_{1}=z_{0}^2-i=0^2-i=-i, \quad |z_1|=1,$$
$$z_{2}=z_{1}^2-i=(-i)^2-i=-1-i, \quad |z_2|=\sqrt{2},$$
$$z_{3}=z_{2}^2-i=(-1-i)^2-i=i, \quad |z_3|=1,$$
$$z_{4}=z_{3}^2-i=(i)^2-i=-1-i, \quad |z_4|=\sqrt{2}.$$

Z výpočtu je jasné, že sa budú stále opakovať hodnoty $-i$ a $-1-i$. Podmienka $|z|\leq2$ bude teda vždy splnená, a preto číslo $-i$ do Mandelbrotovej množiny patrí.

## Úlohy

> **Úloha 1.**  Overte, či komplexné čísla $1$; $i$; $-1$; $1+i$ patria do Mandelbrotovej množiny.

\iffalse

*Riešenie.* 
Pre jednoduchosť uvažujeme len niekoľko prvých iteračných krokov. Obraz čísla $c$ v Gaussovej rovine patrí do Mandelbrotovej množiny vtedy, ak pre všetky výsledky iteračného výpočtu je absolútna hodnota výsledku menšia alebo rovná $2$.

Iteračný proces pre $c=1$.
$$z_{1}=z_{0}^2+1=0^2+1=1, \quad |z_1|=1,$$
$$z_{2}=z_{1}^2+1=1^2+1=2, \quad |z_2|=2,$$
$$z_{3}=z_{2}^2+1=2^2+1=5, \quad |z_3|=5.$$
Podmienka $|z|\leq2$ bola porušená už v treťom kroku, preto číslo $1$ nepatrí do Mandelbrotovej množiny.

Iteračný proces pre $c=i$.
$$z_{1}=z_{0}^2+i=0^2+i=i, \quad |z_1|=1,$$
$$z_{2}=z_{1}^2+i=i^2+i=-1+i, \quad |z_2|=\sqrt{2},$$
$$z_{3}=z_{2}^2+i=(-1+i)^2+i=-i, \quad |z_3|=1,$$
$$z_{4}=z_{3}^2+i=(-i)^2+i=-1+i, \quad |z_4|=\sqrt{2}.$$

Z výpočtu je jasné, že sa budú neustále opakovať výsledky $-1+i$ a $i$ a podmienka $|z|\leq2$ je vždy splnená. Preto číslo $i$ patrí do Mandelbrotovej množiny.

Iteračný proces pre $c=-1$.
$$z_{1}=z_{0}^2-1=0^2-1=-1, \quad |z_1|=1,$$
$$z_{2}=z_{1}^2-1=(-1)^2-1=0, \quad |z_2|=0,$$
$$z_{3}=z_{2}^2-1=0^2-1=-1, \quad |z_3|=1.$$
Výsledky sa cyklicky opakujú a platí $|z|\leq2$, preto číslo $-1$ patrí do Mandelbrotovej množiny.

Iteračný proces pre $c=1+i$.
$$z_{1}=z_{0}^2+1+i=0^2+1+i=1+i, \quad |z_1|=\sqrt{2},$$
$$z_{2}=z_{1}^2+1+i=(1+i)^2+1+i=1+2i+i^2+1+i=1+3i, \quad |z_2|=\sqrt{10}.$$
Podmienka $|z|\leq2$ bola porušená už v druhom kroku, preto číslo $1+i$ nepatrí do Mandelbrotovej množiny.

\fi

> **Úloha 2.** 
Dokážte, že ak existuje $k\in \mathbb{N}$ také, že $|z_k|>2$, potom postupnosť $z_n$ diverguje.

\iffalse

*Riešenie.* Použijeme rekurentný vzťah:
$$
\frac{|z_{n+1}|}{|z_n|}=\frac{|z^2_n+c|}{|z_n|}. 
\tag{1}
$$

Aplikujeme trojuholníkovú nerovnosť:
$$
|a+b|\leq|a|+|b|,
$$ 
kde $a=z^2+c$ a $b=-c$, dostaneme
$$
|z^2+c-c|\leq|z^2+c|+|-c|=|z^2+c|+|c|
$$
a odtiaľ $|z^2+c|\geq|z^2|-|c|=|z|^2-|c|$.

Dosadíme do $(1)$ a úpravou dostaneme
$$
\frac{|z^2_n+c|}{|z_n|}\geq \frac{|z_n|^2-|c|}{|z_n|}=|z_n|-\frac{|c|}{|z_n|}.
$$

Naviac vieme, že existuje také $n$, že platí $|z_n|>|c|$. Pre $|c|\leq2$ to plynie z predpokladu. Pre $c>2$ potom pre $n=2$ platí 
$$
|z_2|=|c^2+c|\geq|c|^2-|c|=|c|(|c|-1)>|c|.
$$
Môžeme teda zapísať
$$
\frac{|z^2_n+c|}{|z_n|}\geq \frac{|z_n|^2-|c|}{|z_n|}=|z_n|-\frac{|c|}{|z_n|}>|z_n|-1>1.
$$
A odtiaľ potom
$$
\frac{|z_{n+1}|}{|z_n|}>1,
$$
alebo $|z_{n+1}|>|z_n|$ a naša postupnosť diverguje.

\fi

## Literatúra 

*  Čápka Hartinger, David. *Mandelbrotova množina - lekce 3 [online]* https://www.itnetwork.cz/algoritmy/graficke/algoritmus-vykresleni-fraktalu-mandelbrotovy-mnoziny} [cit. 22. 9. 2023]

* Wikipedie. *Mandelbrotova množina [online]*. Dostupné z https://cs.wikipedia.org/wiki/Mandelbrotova_mno%C5%BEina [cit. 22. 9. 2023].

* PantheraLeo1359531. *Mandelbrotova množina - obrázek [online]*. Dostupné z https://commons.wikimedia.org/w/index.php?curid=103476207 [cit. 22. 9. 2023]
