---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- analytická geometrie
- kvadratická rovnice
- soustavy rovnic
- rovnice kružnice
is_finished: true
difficulty: 2
time: 20
---

# Optimalizace výnosů

Při rozhodování o investicích nestačí spoléhat na jednoduché lineární modely – trh je 
totiž dynamický a plný nejistot. Sestavení optimálního investičního portfolia tak 
vyžaduje přístup, který zohlední nejen očekávaný výnos, ale i riziko a další omezení, 
jako jsou dostupné finanční prostředky nebo požadavky na diverzifikaci. Výnosy jednotlivých 
aktiv nelze předem přesně určit – jejich chování je ovlivněno mnoha faktory, a proto je třeba 
využít modely založené na kvadratických funkcích. Právě tento přístup – dnes známý jako moderní 
teorie portfolia – položil základy pro nový pohled na investování. Za zásadní přínos v této oblasti 
byli v roce 1990 oceněni Nobelovou cenou Harry Markowitz, William Sharpe a Merton Miller.

Tyto problémy tak vedou na úlohy tzv. *kvadratického programování*, což je oblast matematické optimalizace, 
která se zabývá hledáním extrémů (obvykle minima nebo maxima) kvadratické funkce na množině bodů vymezené 
lineárními rovnicemi a nerovnicemi.

## Influencer touží po úspěchu

Neznámý influencer by rád pomocí propagace příspěvků a placené reklamy zvýšil počet svých sledujících 
na Instagramu a TikToku. Podle dostupných informací přepokládá, že investovaných 10 000 Kč do propagace
na Instagramu mu přinese 1000 sledujících a stejná částka investovaná do reklamy na TikToku mu přinese také
1000 sledujících na této sociální síti. Díky výhodné nabídce může utratit maximálně 20 000 Kč za propagaci 
na Instagramu a 10 000 Kč za reklamu na TikToku.

> **Úloha 1.** Kolik peněz má influencer utratit za reklamu a propagaci na jednotlivých sociálních sítích, 
> pokud se chce co nejvíce přiblížit tomu, aby měl 3 000 sledujících na Instagramu a 2 000 sledujících 
> na TikToku?

\iffalse

*Řešení.* Označíme-li $x$ velikost investice do propagace na Instagramu v desítkách tisíc a podobně $y$ 
velikost investice do reklamy na TikToku, tak optimální hodnota celkových nákladů musí splňovat podmínky 
$$
0\leq x \leq 2 \qquad\text{a}\qquad 0\leq y\leq 1,
$$
tj. leží v obdélníku. Do stejné soustavy souřadnic můžeme též vyznačit i bod, který značí
cílovou hodnotu počtu sledujících. Je-li $x$ počet sledujících na Instagramu v tisících a $y$
počet sledujících v tisících na TikToku, tak se jedná bod o souřadnicích $[3,2]$.

Hledáme tedy bod, který leží uvnitř daného obdélníku a má nejmenší vzdálenost od bodu $[3,2]$.

Vzdálenost libovolného bodu $[x,y]$ od bodu $[3,2]$ je dána vztahem 
$$
v(x,y)=\sqrt{(x-3)^2+(y-2)^2}.
$$
Jelikož odmocnina je rostoucí funkce, tak je-li $0\leq a<b$ pak nutně také $\sqrt{a}<\sqrt{b}$.
Abychom tedy minimalizovali hodnotu $\sqrt{(x-3)^2+(y-2)^2}$ stačí minimalizovat hodnotu $(x-3)^2+(y-2)^2$.

Pro libovolné $c>0$ rovnost 
$$
  (x-3)^2+(y-2)^2=c
$$
odpovídá kružnici se středem v bodě $[3,2]$ a poloměrem $\sqrt{c}$, tj. naším úkolem je najít 
kružnici s nejmenším možným poloměrem, která má neprázdný průnik s daným obdélníkem. Situace
je znázorněna na obrázku, z kterého můžeme řešení uhádnout. 

![K řešení Úlohy 1](math4you_00051_01.svg)

Odtud vidíme, že řešením je bod $[2,1]$. Je to však skutečně pravda? Z obrázku vidíme, že výsledná kružnice 
se dotkne daného obdélníku v pravém horním vrcholu. To znamená, že průnik této kružnice s přímkou určující horní stranu 
obdélníku a průnik kružnice s přímkou určující pravou stranu obdélníku musí být stejný. Jinými slovy, soustavy
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
musí mít alespoň jedno společné řešení. Vyřešit každou soustavu zvlášť nemůžeme, protože bychom dostali kvadratickou 
rovnici o 2 neznámých. Avšak dosazením $x=2$ a $y=1$ dostaneme dvojici rovnic
$$
\begin{align*}
  (x-3)^2+1&=c\\ 
  1+(y-2)^2&=c,
\end{align*}
$$
z čehož plyne, že nutně 
$$
  (x-3)^2+1=1+(y-2)^2
$$
neboli 
$$
  (x-3)^2=(y-2)^2,
$$
což po odmocnění dává
$$
|x-3|=|y-2|.
$$
Tato rovnost je očividně splněna pro bod $[2,1]$. Vidíme tedy, že nejblíže se svému cíli dostane, investuje-li
maximální částku 20 000 Kč za propagaci na Instagramu a 10 000 Kč za reklamu na TikToku.

\fi

> **Úloha 2.** Jak se změní řešení Úlohy 1, je-li cílová hodnota 1 000 
> sledujících na Instagramu a 3 000 na TikToku?

\iffalse

*Řešení.* V tomto případě minimalizujeme vzdálenost od bodu 
bodu $[1,3]$. Situace tak vypadá následovně.

![K řešení Úlohy 2](math4you_00051_02.svg)

Řešením tedy bude bod ležící na přímce $y=1$, což nás přivádí k soustavě
$$
\begin{align*}
(x-1)^2+(y-3)^2&=c\\ 
y&=1.
\end{align*}
$$ 
Jedná se o soustavu kvadratické a lineární rovnice o 3 neznámých, ze které snadno uděláme kvadratickou 
rovnici o 2 neznámých
$$
(x-1)^2+4=c.
$$
Z obrázku vidíme, že hledaná kružnice s nejmenším poloměrem se daného obdélníku pouze dotkne, 
tj. číslo $c$ musí být takové, že kvadratická rovnice má pouze 1 řešení (nemá-li žádné, je 
poloměr malý a kružnice má prázdný průnik s obdélníkem, má-li dvě různá řešení, pak nutně existuje 
kružnice s o něco menším poloměrem, která má opět neprázdný průnik s obdélníkem). Řešení kvadratické 
rovnice je
$$
x_{1,2}=\pm\sqrt{c-4}+1.
$$
Řešení bude jediné (resp. obě řešení splynou), pouze pro $c=4$. V takovém případě bude $x=1$, tj. řešením je bod 
$[1,1]$. Tentokrát tedy stačí utratit 10 000 Kč za propagaci na Instagramu a 10 000 Kč za reklamu na TikToku.

\fi
