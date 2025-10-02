---
keywords: 
 - geometrická posloupnost
 - fraktál
 - Kochova vločka
is_finished: True
difficulty: 2
time: 35
---

# Fraktální geometrie

Fraktál je objekt, jehož geometrická struktura se opakuje v něm
samém. Charakteristickou vlastností fraktálů je jejich
soběpodobnost. Příkladem fraktálů v přírodě mohou být mraky, stromy
nebo hlávka květáku. Slovo fraktál pochází z latinského slova fractus,
v překladu zlomený, rozbitý. Vymyslel ho Benoit B. Mandelbrot,
považovaný za otce fraktální geometrie, kterou proslavil svou knihou
*The Fractal Geometry of Nature* (1982).

Při zkoumání fraktálů hraje důležitou roli jejich dimenze. Dimenze,
tzv. topologická dimenze, která je známá z klasické euklidovské
geometrie, při popisu fraktálů nestačila, proto bylo potřeba zavést i
jiný typ dimenze. Felix Hausdorff zavedl novou fraktální dimenzi, též
označovanou Hausdorffova dimenze. Pro jednoduché objekty ji můžeme
chápat jako číslo
$$d=\frac{\ln N}{\ln\frac{1}{r}}, $$
kde $N$ je počet částí z kterých se objekt skládá a které vzniknou
pomocí stejnolehlosti s koeficientem $r$ z původního
objektu. Například pro čtverec platí, že jej můžeme složit ze čtyř
menších čtverců, které z něj vzniknou pomocí stejnolehlosti s
koeficientem $r=\frac{1}{2}$, tedy
$$d=\frac{\ln 4}{\ln2}=2.$$
Pro čtverec je tedy jeho fraktální dimenze stejná jako normální
intuitivní dimenze.

## Kochova vločka

*Kochova vločka* je křivka v rovině, která vzniká iteračním procesem z
 rovnostranného trojúhelníku.

Na začátku je rovnostranný trojúhelník se stranami délky 1. V každém
dalším kroku se pak provede následující:

1. Každá úsečka se rozdělí na třetiny.
2. Nad prostřední třetinou úsečky se sestrojí rovnostranný trojúhelník.
3. Základna trojúhelníka (dřívější prostřední třetina úsečky) se odstraní. 


![První iterace Kochovy vločky](math4you_00007.svg)

Z obrázku můžeme vidět, že pro určení délky jedné strany vločky v
první iteraci, potřebujeme 4 strany trojúhelníka, který vznikl
zmenšením strany trojúhelníka v nultém kroku pomocí stejnolehlosti s
koeficintem $r=\frac{1}{3}$, tedy
$$
d=\frac{\ln4}{\ln3}\approx 1{,}26.
$$
Jelikož Kochova vločka je křivka, očekávali bychom, že její dimenze je
$1$. Tento rozpor je dán tím, že Kochova vločka je na konci natolik
členitá, že výsledný fraktál má nekonečnou délku, ale ohraničuje útvar
konečného obsahu.

> **Úloha 1.** Vypočítejte obvod Kochovy vločky po první, druhé a třetí iterací.

\iffalse

*Řešení.* Na začátku máme rovnostranný trojúhelník s obvodem
$o_0=3$. V první iteraci rozdělíme tři úsečky na třetiny, prostřední
třetinu z nich odebereme a nahradíme ji dvěma úsečkami délky
$\frac{1}{3}$. Každou stranu trojúhelníka jsme prodloužili o
$\frac{1}{3}$ a výsledný obvod po první iteraci tak je
$$o_1=3+3\cdot\frac{1}{3}=4.$$

V druhé iteraci dostaneme na každé straně původního trojúhelníka čtyři
úsečky třetinové délky, které rozdělíme na třetiny a prodloužíme je o
$\frac{1}{9}$. Získáme tak obvod
$$o_2=3+3\cdot\frac{1}{3}+3\cdot\frac{4}{9}=\frac{16}{3}.$$ 
Při třetí iteraci budeme prodlužovat na každé straně 16 úseček o $\frac{1}{27}$ a proto obvod po třetí iteraci bude 
$$o_3=3+3\cdot\frac{1}{3}+3\cdot\frac{4}{9}+3\cdot\frac{16}{27}=3+1+\frac{4}{3}+\frac{16}{9}=\frac{64}{9}.$$

\fi

> **Úloha 2.** Jaký je obvod Kochovy vločky po $n$-té iteraci? Ukažte, že obvod Kochovy vločky bude nekonečný.

\iffalse

*Řešení.* Z výpočtů výše vidíme, že každý úsek má třetinovou délku
oproti úseku v předchozím kroku a zároveň ho o jeden díl prodloužíme,
tj. úsečka se prodlouží na $\frac{4}{3}$ původní délky. Obvod Kochovy
vločky po $n$-té iteraci můžeme vyjádřit jako součet členů geometrické posloupnosti s
kvocientem $\frac{4}{3}$ pro $n\in\mathbb{N}$:
$$o_n=3+\left(\frac{4}{3}\right)^0+\left(\frac{4}{3}\right)^1+\left(\frac{4}{3}\right)^2+\cdots+\left(\frac{4}{3}\right)^{n-1}=3+\sum_{i=1}^n\left(\frac{4}{3}\right)^{i-1}.$$ 
Pokud bychom tímto způsobem pokračovali do nekonečna, 
tak bychom ve druhém členu součtu dostali nekonečnou geometrickou řadu. 
Vzhledem k tomu, že kvocient příslušné geometrické posloupnosti je větší 
než jedna, daná řada bude divergentní a obvod Kochovy vločky bude nekonečný.

\fi

> **Úloha 3.** Vypočítejte obsah Kochovy vločky po první a druhé iteraci.

\iffalse

*Řešení.* Na začátku si uvědomme, že výška v rovnostranném
trojúhelníku se stranou délky $a$ je délky $\frac{\sqrt{3}}{2}a$ a
obsah rovnostranného trojúhelníka je
$$S=\frac{\sqrt{3}}{4}a^2.$$ 
Obsah výchozího rovnostranného trojúhelníku je
$S_0=\frac{\sqrt{3}}{4}$. V první iteraci rozdělíme tři úsečky na
třetiny a na prostřední třetinu umístíme rovnostranný trojúhelník se
stranou délky $\frac{1}{3}$. Výsledný obsah po první iteraci tedy bude
$$S_1=\frac{\sqrt{3}}{4}+3\cdot\frac{\sqrt{3}}{4}\cdot\left(\frac{1}{3}\right)^2=\frac{\sqrt{3}}{4}\cdot\frac{4}{3}.$$ 
V druhém kroku budeme mít na každé straně původního trojúhelníku
čtyřnásobný počet úseček, kam budeme umisťovat trojúhelník se stranou
délky $\frac{1}{9}$. Obsah po druhé iteraci se zvětší na
$$S_2=\frac{\sqrt{3}}{4}+3\cdot\frac{\sqrt{3}}{4}\cdot\left(\frac{1}{3}\right)^2+3\cdot4\cdot\frac{\sqrt{3}}{4}\cdot\left(\frac{1}{9}\right)^2=\frac{\sqrt{3}}{4}\left(1+\frac{1}{3}+\frac{1}{3}\cdot\frac{4}{9}\right)=\frac{\sqrt{3}}{4}\cdot\frac{40}{27}.$$

\fi

> **Úloha 4.** Jaký je obsah Kochovy vločky po $n$-té iteraci? Kolikrát
> větší obsah má Kochova vločka vzhledem k původnímu rovnostrannému
> trojúhelníku?

\iffalse

*Řešení.* Z předchozích úvah plyne, že počet úseček, kam přidáváme
nový trojúhelník, je v každé iteraci čtyřnásobně větší. Zároveň se nám
strana nového trojúhelníku zmenšuje na třetinu předchozí velikosti,
proto se jeho obsah zmenšuje na devítinu. Získáváme tak členy
geometrické posloupnosti s kvocientem $\frac{4}{9}$ a obsah Kochovy
vločky po $n$-té iteraci je tvořen obsahem původního 
trojúhelníka a součtem prvních $n$ členů dané geometrické posloupnosti:
$$S_n=\frac{\sqrt{3}}{4}\left[1+\frac{1}{3}+\frac{1}{3}\cdot\frac{4}{9}+\dots+\frac{1}{3}\left(\frac{4}{9}\right)^{n-1}\right]=\frac{\sqrt{3}}{4}\left[1+\frac{1}{3}\sum_{i=1}^n\left(\frac{4}{9}\right)^{i-1}\right].$$
Jelikož kvocient geometrické posloupnosti je menší než 
jedna, tak pokračováním do nekonečna dostaneme 
konvergentní geometrickou řadu. Použitím vzorečku pro 
její součet dostaneme obsah Kochovy vločky po 
nekonečném počtu kroků
$$S=\frac{\sqrt{3}}{4}\left(1+\frac{1}{3}\cdot\frac{1}{1-\frac{4}{9}}\right)=\frac{\sqrt{3}}{4}\left(1+\frac{1}{3}\cdot\frac{9}{5}\right)=\frac{8}{5}\cdot\frac{\sqrt{3}}{4}= 1{,}6 \cdot S_0.$$
Kochova vločka má nekonečný obvod omezující konečnou plochu, která má
obsah přibližně 1,6-krát větší než obsah původního rovnostranného trojúhelníku.

\fi

## Literatura

* MathWorld. *Koch snowflake* [online]. Dostupné z <https://mathworld.wolfram.com/KochSnowflake.html> [cit. 13. 7. 2023].
* *Kochova křivka* [online]. Dostupné z <https://cs.wikipedia.org/wiki/Kochova_k%C5%99ivka> [cit. 13. 7. 2023].
