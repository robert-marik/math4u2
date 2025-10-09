---
keywords:
- komplexní čísla
- Gaussova rovina
- posloupnosti
- konvergence
- absolutní hodnota
is_finished: true
difficulty: 3
time: 20
---

# Mandelbrotova množina

Mandelbrotova množina je jedním z nejznámějších a 
nejkrásnějších fraktálů, který fascinuje matematiky, 
vědce i umělce po celém světě. Ačkoli na první pohled 
vypadá jako složitý obrazec, je založena na 
jednoduchém matematickém pravidle opakovaného 
umocňování a sčítání. Co ji ale činí tak zajímavou, je 
její nekonečná složitost a nádherné vzory, které se 
skrývají v každém detailu.

![Mandelbrotova množina; barva bodů v jejím okolí odpovídá pořadí členu posloupnosti, u něhož je poprvé zjištěno, že tato posloupnost jde do nekonečna.](Mandelbrot.png)

Využití Mandelbrotovy množiny sahá daleko za hranice 
matematiky. Najdeme ji v počítačové grafice, kde se 
používá k vytváření složitých a realistických objektů
při modelování přírodních struktur, jako jsou pobřeží, hory 
nebo oblačnost. Dá se využít dokonce i v ekonomii a fyzice, kde 
pomáhá při simulaci chaotických systémů.

Mandelbrotova množina je důkazem, že i jednoduché 
matematické postupy mohou vést k neuvěřitelně 
komplexním a krásným výsledkům, které mají reálné 
využití.

## Vytvoření množiny

Představme si poměrně jednoduchý rekurentní vztah
$$
z_{n+1}=z_{n}^2+c,
$$ 
kde se za počáteční hodnotu dosadí $z_0=0$ a $c$ představuje libovolné 
komplexní číslo. Francouzsko-amerického matematika Benoita Mandelbrota (1924–2010) 
zajímalo, kdy je posloupnost takto vzniklých čísel omezená, tj. pro která $c$ 
z komplexní roviny posloupnost konverguje nebo osciluje. Pokud v nějakém bodě 
posloupnost diverguje, tak chtěl vědět, jak rychle. Lze dokázat, že 
překročí-li absolutní hodnota některého členu posloupnosti $z_{n}$ hodnotu 2, 
pak tato posloupnost omezená není. 

*Mandelbrotova množina* je pak množina bodů $c$ v komplexní rovině, pro něž posloupnost vytvořená rekurentní formulí konverguje nebo osciluje. Díky výše uvedenému faktu víme, že pro každý člen $z$ této posloupnosti musí platit, že jeho absolutní hodnota $|z|$ je menší nebo rovna dvěma. 

Ověření, zda dané $c$ patří do Mandelbrotovy množiny probíhá tak, že vypočteme jednotlivé iterace a sledujeme absolutní hodnoty těchto iterací. Pro výpočet iterací využijeme rekurentní vztah

$$
z_{n+1}=z_{n}^2+c,\qquad z_0=0.
$$

Např. pro $c=-i$ máme

$$z_{1}=z_{0}^2-i=0^2-i=-i, \quad |z_1|=1,$$
$$z_{2}=z_{1}^2-i=(-i)^2-i=-1-i, \quad |z_2|=\sqrt{2},$$
$$z_{3}=z_{2}^2-i=(-1-i)^2-i=i, \quad |z_3|=1,$$
$$z_{4}=z_{3}^2-i=(i)^2-i=-1-i, \quad |z_4|=\sqrt{2}.$$

Z výpočtu je patrné, že se budou neustále opakovat výsledky $-i$ a $-1-i$. 
Podmínka $|z|\leq2$ bude proto vždy splněna, a tedy číslo $-i$ do Mandelbrotovy 
množiny patří.

## Úlohy

> **Úloha 1.** Ověřte, zda komplexní čísla $1$; $i$; $-1$; $1+i$ patří do Mandelbrotovy množiny.

\iffalse

*Řešení.* Pro jednoduchost budeme uvažovat pouze několik prvních iteračních 
kroků. Platí, že obraz čísla $c$ v Gaussově rovině patří do Mandelbrotovy 
množiny, jestliže pro všechny výsledky iteračního výpočtu je absolutní 
hodnota výsledku menší nebo rovna $2$.

Iterační proces pro $c=1$.
$$z_{1}=z_{0}^2+1=0^2+1=1, \quad |z_1|=1,$$
$$z_{2}=z_{1}^2+1=1^2+1=2, \quad |z_2|=2,$$
$$z_{3}=z_{2}^2+1=2^2+1=5, \quad |z_3|=5.$$
Z výpočtu je patrné, že podmínka $|z|\leq2$ nebyla splněna už v třetím 
iteračním kroku a číslo $1$ do Mandelbrotovy množiny nepatří.

Iterační proces pro $c=i$.
$$z_{1}=z_{0}^2+i=0^2+i=i, \quad |z_1|=1,$$
$$z_{2}=z_{1}^2+i=i^2+i=-1+i, \quad |z_2|=\sqrt{2},$$
$$z_{3}=z_{2}^2+i=(-1+i)^2+i=-i, \quad |z_3|=1,$$
$$z_{4}=z_{3}^2+i=(-i)^2+i=-1+i, \quad |z_4|=\sqrt{2}.$$
Z výpočtu je patrné, že se budou neustále opakovat výsledky $-1+i$ a $i$. 
Podmínka $|z|\leq2$ bude vždy splněna, proto číslo $i$ do Mandelbrotovy 
množiny patří.

Iterační proces pro $c=-1$.
$$z_{1}=z_{0}^2-1=0^2-1=-1, \quad |z_1|=1,$$
$$z_{2}=z_{1}^2-1=(-1)^2-1=0, \quad |z_2|=0,$$
$$z_{3}=z_{2}^2-1=0^2-1=-1, \quad |z_3|=1.$$
Výsledky se budou opět opakovat a podmínka $|z|\leq2$ bude vždy splněna, 
proto číslo $-1$ do Mandelbrotovy množiny patří.

Iterační proces pro $c=1+i$.
$$z_{1}=z_{0}^2+1+i=0^2+1+i=1+i, \quad |z_1|=\sqrt{2},$$
$$z_{2}=z_{1}^2+1+i=(1+i)^2+1+i=1+2i+i^2+1+i=1+3i, \quad |z_2|=\sqrt{10}.$$
Z výpočtu je patrné, že podmínka $|z|\leq2$ nebyla splněna už v druhém 
iteračním kroku a číslo $1+i$ do Mandelbrotovy množiny nepatří.

\fi

> **Úloha 2.** Dokažte, že existuje-li $k\in \mathbb{N}$ takové, že $|z_k|>2$, pak posloupnost $z_n$ diverguje.

\iffalse

*Řešení.* Užitím rekurentního vztahu získáme podíl
$$
\frac{|z_{n+1}|}{|z_n|}=\frac{|z^2_n+c|}{|z_n|}. 
\tag{1}
$$

Použijeme-li trojúhelníkovou nerovnost
$$
|a+b|\leq|a|+|b|,
$$ 
kde $a=z^2+c$ a $b=-c$, dostaneme
$$
|z^2+c-c|\leq|z^2+c|+|-c|=|z^2+c|+|c|
$$
a odtud $|z^2+c|\geq|z^2|-|c|=|z|^2-|c|$.

Dosazením do $(1)$ a úpravou dostaneme
$$
\frac{|z^2_n+c|}{|z_n|}\geq \frac{|z_n|^2-|c|}{|z_n|}=|z_n|-\frac{|c|}{|z_n|}.
$$
Navíc víme, že existuje takové $n$, že platí $|z_n|>|c|$. Pro $|c|\leq2$ to plyne z předpokladu. Pro $c>2$ pak pro $n=2$ platí 
$$
|z_2|=|c^2+c|\geq|c|^2-|c|=|c|(|c|-1)>|c|.
$$
Můžeme tedy psát
$$
\frac{|z^2_n+c|}{|z_n|}\geq \frac{|z_n|^2-|c|}{|z_n|}=|z_n|-\frac{|c|}{|z_n|}>|z_n|-1>1.
$$
A odtud tedy
$$
\frac{|z_{n+1}|}{|z_n|}>1,
$$
neboli $|z_{n+1}|>|z_n|$ a naše posloupnost diverguje.

\fi

## Literatura 

*  Čápka Hartinger, David. *Mandelbrotova množina - lekce 3 [online]* https://www.itnetwork.cz/algoritmy/graficke/algoritmus-vykresleni-fraktalu-mandelbrotovy-mnoziny} [cit. 22. 9. 2023]

* Wikipedie. *Mandelbrotova množina [online]*. Dostupné z https://cs.wikipedia.org/wiki/Mandelbrotova_mno%C5%BEina [cit. 22. 9. 2023].

* PantheraLeo1359531. *Mandelbrotova množina - obrázek [online]*. Dostupné z https://commons.wikimedia.org/w/index.php?curid=103476207 [cit. 22. 9. 2023]
