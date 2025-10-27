---
workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- diferenciální a integrální počet
- optimalizace
- kvadratická rovnice
- derivace
is_finished: true
difficulty: 3
time: 30
---

# Odpal golfového míčku

## Šikmý vrh

Šikmý vrh je nejobecnější způsob uvedení tělesa v homogenním tíhovém
poli do pohybu.  Předpokládejme, že hmotný bod byl šikmo vržen v
prostředí bez odporu počáteční rychlostí $v_0$, přičemž příslušný vektor počáteční rychlosti $\vec {v}_0$ svírá s
vodorovnou rovinou úhel $\alpha \in \left(0,\frac{\pi}{2}\right)$. V kartézské soustavě souřadnic bude pro tento vektor platit (viz obrázek)

$$\vec{v}_0=(v_0\cos\alpha;v_0\sin\alpha).$$

Pohyb tělesa je ovlivněn tíhovým zrychlením o velikosti $g$ mířícím
svisle dolů. Ve vodorovném směru na těleso nepůsobí žádná složka tíhového zrychlení, a proto je pohyb ve vodorovném směru rovnoměrný. Naopak, ve směru svislém se pohyb odehrává pod vlivem tíhového zrychlení. Proto pro vektor $\vec{v}=(v_x;v_y)$ okamžité rychlosti v čase $t \geq 0$ platí 

$$
\begin{aligned}
        v_x=v_x(t) &= v_0 \cos\alpha,\\
        v_y=v_y(t) &= v_0\sin\alpha-gt.
\end{aligned}
$$

Pro souřadnice $[x;y]$ polohy hmotného bodu v čase $t \geq 0$ tedy bude platit 

$$
\begin{aligned}
        x = x(t) &= v_0 t\cos\alpha,\\
        y = y(t) &= v_0t\sin\alpha-\frac{1}{2}gt^2,
\end{aligned}\tag{1}
$$

protože okamžitá rychlost v čase $t$ je derivací polohy v čase $t$. Přesněji, $v_x(t)=x'(t)$ a $v_y(t)=y'(t)$. 

![Šikmý vrh](math4you_00013.jpg)

## Odpal golfového míčku

Hráč golfu odpaluje míček počáteční rychlostí $v_0$ pod úhlem $\alpha \in \left(0,\frac{\pi}{2}\right)$. Předpokládejme, že na míček nepůsobí žádné odporové síly. Pohyb míčku tedy splňuje podmínky pro
pohyb šikmo vrženého tělesa v prostředí bez odporu vzduchu.

>**Úloha 1.**  Dokažte, že trajektorií golfového míčku je část paraboly.

\iffalse

*Řešení.* Chceme nalézt rovnici trajektorie ve tvaru $y=f(x)$. Proto je nutné převést parametrické vyjádření trajektorie (1) na rovnici obecnou. 

Nejprve vyjádříme z první rovnice čas $t=\frac{x}{v_0\cos\alpha}$ a
dosadíme ho do rovnice druhé:

$$
 y = v_0\sin\alpha\, \frac{x}{v_0\cos\alpha} -\frac{1}{2}g\frac{x^2}{v_0^2\cos^2\alpha}= -\frac{g}{2v_0^2\cos^2\alpha}\cdot x^2+\frac{\sin\alpha}{\cos\alpha}\cdot x\ .
$$

Odtud vidíme, že funkce $f$ popisující trajektorii míčku je kvadratická funkce 

$$
 f(x)=Ax^2+Bx, 
$$

kde 

$$
 A=-\frac{g}{2v_0^2\cos^2\alpha} \quad \text{a} \quad 
 B=\frac{\sin\alpha}{\cos\alpha}.
$$

Grafem funkce $f$ je parabola. Tím je dokázáno, že trajektorie golfového míčku je jistou částí této paraboly. 

\fi

>**Úloha 2.** Vypočítejte výšku vrhu, tj. maximální výšku $y_{max}$, do které se dostane odpálený míček.

\iffalse

*Řešení.* Pro výpočet výšky vrhu potřebujeme vypočítat extrém funkce $f$ z
předchozí úlohy:

$$
 f(x) = -\frac{g}{2v_0^2\cos^2\alpha}\cdot x^2+\frac{\sin\alpha}{\cos\alpha}\cdot x\ .
$$

Vypočítáme derivaci funkce $f$:

$$
f'(x) = -\frac{g}{2v_0^2\cos^2\alpha}\cdot2x+\frac{\sin\alpha}{\cos\alpha}\ .
$$

Pro nalezení stacionárního bodu položíme derivaci rovnu nule a
dostaneme rovnici

$$
\frac{g}{v_0^2\cos^2\alpha}\cdot x=\frac{\sin\alpha}{\cos\alpha}\ .
$$

Jejím řešením je

$$
x_{0}=\frac{v_0^2\sin\alpha\cos\alpha}{g}\ .
$$

Vzhledem k tomu, že se jedná o konkávní kvadratickou  funkci, musí být nalezený stacionární bod $x_{0}$ i bodem jejího (lokálního i globálního) maxima. 
 
Výšku vrhu $y_{max}$ vypočítáme dosazením $x_{0}$ do funkce $f$. Po jednoduchých úpravách obdržíme: 

$$
 y_{max}=f(x_{0})=\frac{v_0^2\sin^2\alpha}{2g}\ .
$$

\fi

> **Úloha 3.** Určete, jaký musí být úhel $\alpha$, aby (při dané počáteční rychlosti) míček doletěl do maximální vzdálenosti.

\iffalse

*Řešení.* Pro výpočet úhlu maximálního dostřelu potřebujeme získat $x$-ovou
souřadnici $x_d$ místa dopadu jako funkci úhlu $\alpha$ a tuto funkci
maximalizovat, tj. najdeme maximum funkce $x_d(\alpha).$ Vzhledem k
tomu, že při dopadu míčku bude jeho výška nulová, položíme ve vztahu 

$$
 y = -\frac{g}{2v_0^2\cos^2\alpha}\cdot x^2+\frac{\sin\alpha}{\cos\alpha}\cdot x
$$

$y=0$ a vyřešíme získanou rovnici: 

$$
 0 = -\frac{g}{2v_0^2\cos^2\alpha}\cdot x^2+\frac{\sin\alpha}{\cos\alpha}\cdot x\ ,
$$

$$
 0 = x\cdot\left(-\frac{g}{2v_0^2\cos^2\alpha}\cdot x+\frac{\sin\alpha}{\cos\alpha}\right)\ .
$$

Tato rovnice v součinovém tvaru má dvě řešení. První 
řešení $x=0$ odpovídá místu odpalu míčku a druhé řešení $x_d$ místu dopadu. 
Snadno se vidí, že 

$$
x_d = x_d(\alpha) = \frac{2v_0^2\sin\alpha\cos\alpha}{g}=\frac{v_0^2}{g}\sin2\alpha\ .
$$ 

Nyní je nutné nalézt maximum funkce $x_d(\alpha)$. 
To je ale snadné, neboť pro $\alpha \in \left(0,\frac{\pi}{2}\right)$ je hodnota $\sin 2\alpha$ maximální, právě když 
$\alpha=\frac{\pi}{4}$. 

Maximálního dostřelu tedy docílíme při odpalu míčku pod úhlem
$\alpha=\frac{\pi}{4}$ a míček dopadne do vzdálenosti

$$
x_d \left(\frac{\pi}{4} \right) =\frac{v_0^2}{g}\sin\left(2\cdot \frac{\pi}{4} \right)=\frac{v_0^2}{g}\ .
$$ 

Funkci $x_d(\alpha) = \frac{v_0^2}{g}\sin2\alpha$ jsme mohli získat i snadněji využitím 
symetrie paraboly. Vrchol paraboly totiž leží uprostřed trajektorie míčku. 
Proto pro místo dopadu $x_{d}$ platí $x_d(\alpha) = 2\cdot x_{max}$. 
Tím se vyhneme řešení kvadratické rovnice v součinovém tvaru získané dosazením $y=0$ do funkce $y=f(x)$.

\fi

> **Doplňující otázky k rozmyšlení.** Rozmyslete si, jak by se situace změnila v případě, že golfový míček odpalujeme z vyvýšeného místa, které se nachází ve výšce $h$ nad okolním terénem. 
>
>1) Bude trajektorií stále nějaká část paraboly? 
>2) Do jaké maximální výšky míček vyletí? 
>3) Jak daleko míček doletí? 
>4) Pod jakým úhlem je třeba (při dané počáteční rychlosti) míček odpálit, aby dolétl co nejdále? 

\iffalse

*Odpověď na otázku 1.*
Pro souřadnice $[x,y]$ polohy hmotného bodu v čase $t \geq 0$ bude v tomto případě platit

$$
\begin{aligned}
       x &= v_0 t\cos\alpha,\\
       y &= h+v_0t\sin\alpha-\frac{1}{2}gt^2.
\end{aligned}\tag{2}
$$

Podobně jako v úloze 1 bychom došli k závěru, že trajektorie je částí grafu funkce  

$$
 y = f(x) = h+v_0\sin\alpha\, \frac{x}{v_0\cos\alpha} -\frac{1}{2}g\frac{x^2}{v_0^2\cos^2\alpha}= h-\frac{g}{2v_0^2\cos^2\alpha}\cdot x^2+\frac{\sin\alpha}{\cos\alpha}\cdot x\ , 
$$

což je opět funkce kvadratická (dokonce pouze posunutá o $h$ ve směru osy $y$). 

*Odpověď na otázku 2.*
Při výpočtu maximální dosažené výšky odpáleného míčku dojdeme ke vztahu 

$$
x_{max}=\frac{v_0^2\sin\alpha\cos\alpha}{g}\ , 
$$

který je stejný jako vztah dříve odvozený. To souvisí s tím, že derivace konstantní funkce je funkce nulová (rozmyslete si). 

 Dosazením $x_{max}$ do funkce $f$ pak dojdeme k tomu, že 

$$
 y_{max}=f(x_{max})=h+\frac{v_0^2\sin^2\alpha}{2g}\ .
$$

*Odpověď na otázku 3.*
Ve vztahu 

$$
 y = h-\frac{g}{2v_0^2\cos^2\alpha}\cdot x^2+\frac{\sin\alpha}{\cos\alpha}\cdot x 
$$

položíme $y=0$ a získáme opět kvadratickou rovnici

$$
 -\frac{g}{2v_0^2\cos^2\alpha}\cdot x^2+\frac{\sin\alpha}{\cos\alpha}\cdot x + h = 0. 
$$

 Tentokrát však tato rovnice není v součinovém tvaru, a proto ji budeme řešit použitím obecného vzorce pro řešení kvadratické rovnice. Nejprve však bude dobré z rovnice odstranit zlomky vynásobením výrazem $-2v_0^2 \cos^2\alpha$. Získáme tak kvadratickou rovnici 

 $$
 gx^2-2v_0^2\sin\alpha \cos\alpha \cdot x - 2hv_0^2 \cos^2\alpha = 0.
 $$

Tato rovnice má dvě řešení: 

$$
x_{1,2}=\frac{2v_0^2\sin\alpha \cos\alpha \pm \sqrt{4v_0^4\sin^2\alpha \cos^2\alpha+8ghv_0^2\cos^2\alpha}}{2g}
$$
 
Úpravou posledního vztahu bychom dostali 

$$
x_{1,2}=\frac{v_0\cos\alpha}{g} \cdot \left( v_0\sin\alpha \pm \sqrt{v_0^2\sin^2\alpha+2gh}\right). 
$$

Není těžké si rozmyslet, že jeden z kořenů (konkrétně ten se znaménkem mínus) je záporný, a proto odpálený golfový míček doletí do vzdálenosti 

$$
x_d = \frac{v_0\cos\alpha}{g} \cdot \left( v_0\sin\alpha + \sqrt{v_0^2\sin^2\alpha+2gh}\right).
$$

Všimněme si, že v případě $h=0$ dostaneme vztah 

$$
x_d = \frac{v_0\cos\alpha}{g} \cdot \left( v_0\sin\alpha + \sqrt{v_0^2\sin^2\alpha}\right)=
\frac{v_0\cos\alpha}{g} \cdot 2v_0\sin\alpha=
\frac{v_0^2}{g} \sin 2\alpha, 
$$

který byl odvozen už dříve. 

*Odpověď na otázku 4.*
Zde je situace mnohem složitější. Museli bychom totiž maximalizovat funkci 

$$
x_d(\alpha) = \frac{v_0\cos\alpha}{g} \cdot \left( v_0\sin\alpha + \sqrt{v_0^2\sin^2\alpha+2gh}\right), 
$$

což by bylo poměrně komplikované. Pomocí metod diferenciálního počtu bychom mohli zjistit, že maximum nastává pro úhel $\alpha$ splňující rovnost  

$$
\sin\alpha = \frac{v_0}{\sqrt{2v_0^2+2gh}}. 
$$

Vidíme, že v tomto případě do optimálního úhlu mluví počáteční rychlost $v_0$ golfového míčku, výška $h$ místa, ze kterého míček odpalujeme, a dokonce i gravitační zrychlení $g$. 

Můžeme si ale všimnout, že v případě $h=0$ se poslední vztah změní na 

$$
\sin\alpha = \frac{v_0}{\sqrt{2v_0^2}}=\frac{\sqrt{2}}{2},  
$$

což odpovídá dříve nalezenému optimálnímu úhlu $\alpha=\frac{\pi}{4}$. 

\fi

## Literatura

1. Kubera, Miroslav; Nečas, Tomáš; Beneš, Vojtěch. *Online učebnice
   fyziky pro gymnázia - Vrhy* [online]. Dostupné z
   <https://e-manuel.cz/kapitoly/pouziti-pohybovych-zakonu/vyklad/vrhy/>
   [cit. 27.9.2023].
2. Moc, Ondřej; Eisenmann, Petr. *Šikmý vrh z rozhledny*
   [online]. Dostupné z
   <https://mfi.upol.cz/files/26/2602/mfi_2602_129_137.pdf>
   [cit. 27.9.2023]

## Odkazy
* Vrh šikmý - https://cs.wikipedia.org/wiki/Vrh_%C5%A1ikm%C3%BD
