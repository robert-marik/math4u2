---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- rovnice a nerovnice
- řetězový zlomek
- kvadratická rovnice
is_finished: true
difficulty: 1
time: 40
---

# Zlatý řez a řetězový zlomek

Mějme úsečku $AB$ a na ní bod $C$. Řekneme, že bod $C$ dělí úsečku $AB$ v poměru zlatého řezu, 
jestliže pro délky uvažovaných úseček platí vztah
$$\frac{|AB|}{|AC|}=\frac{|AC|}{|CB|}.$$
Tento poměr se často značí řeckým písmenem $\varphi$ a má hodnotu přibližně $1{,}618$. 

![Úsečka rozdělená v poměru zlatého řezu](00027_1.jpg)

Pěkným příkladem využití zlatého řezu v běžném životě je platební karta. Ta má tvar tzv. zlatého 
obdélníku. To znamená, že délky jeho stran jsou v poměru zlatého řezu. Zlatý obdélník je oblíbený tvar díky jeho 
vyváženému vzhledu; není ani příliš dlouhý, ani příliš široký.

![Zlatý obdélník a zlatá spirála](00027_2.jpg)

Zlatý řez úzce souvisí s Fibonacciho posloupností. Členy Fibonacciho posloupnosti jsou čísla 
$1$, $1$, $2$, $3$, $5$, $8$, $13$, $21$, $34$, $55$, ..., kde každý další člen posloupnosti 
získáme součtem předchozích dvou členů. Jednotlivé prvky této posloupnosti označujeme také jako 
Fibonacciho čísla. A jaká je souvislost mezi Fibonacciho posloupností a zlatým řezem? Platí, že 
limita poměrů dvou po sobě jdoucích členů této posloupnosti je rovna právě zlatému řezu $\varphi$.

Pokud sestrojíme čtverce, jejichž délky stran odpovídají právě Fibonacciho číslům, je možné je 
pěkně uspořádat vedle sebe do tvaru obdélníku tak, jak je vidět na obrázku. Tento obdélník je blízký zlatému obdélníku. Do každého 
čtverce pak můžeme vepsat čtvrtkružnici. Dostaneme jistou spirálu, která je blízká tzv. zlaté spirále. Ta je 
speciálním případem logaritmické spirály.

V přírodě se zlatý řez objevuje právě ve formě Fibonacciho posloupnosti. Můžeme ho najít v 
uspořádání listů na stoncích. Listy vyrůstají nad sebou tak, aby si navzájem nestínily, přechod od 
jednoho listu k dalšímu má charakter šroubovitého výstupu kolem stonku. Podobné uspořádání můžeme 
najít u šupin borové šišky, semen slunečnice nebo u kůry ananasu. Logaritmickou spirálu najdeme 
také ve schránkách měkkýšů či ve svinutém lístku kapradiny. Tento tvar dále mají tornáda, cyklóny i 
galaxie.

Zlatý řez je hojně využíván v umění pro dosažení esteticky působivých a harmonických kompozic. 
Malíři a fotografové používají tento poměr k určení umístění klíčových prvků ve svých obrazech. 
Architekti často integrují poměr zlatého řez do návrhů budov.

## Řetězový zlomek

Řetězový zlomek je výraz typu

$$
 x = a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cfrac{1}{a_3 + \ddots}}},
$$

kde $a_0$ je celé číslo a $a_1, a_2, \dots\,$ jsou čísla přirozená. Řetězový 
zlomek může být konečný (někdy říkáme ukončený) i nekonečný (někdy říkáme neukončený). Je to podobné jako u desetinného rozvoje - ten také může být ukončený nebo neukončený.  

Lze ukázat, že zlatý řez je možné  vyjádřit nekonečným řetězovým zlomkem
$$\varphi = 1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \ddots}}}.$$

> **Úloha 1.**
> Vypočítejte přibližné hodnoty zlatého řezu pomocí následujících konečných řetězových zlomků
>
> 1. $$1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1}}}\,,$$
> 2. $$1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1}}}}\,.$$

\iffalse

*Řešení.* 

1. $$1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1}}}= 1 + \cfrac{1}{1 + \cfrac{1}{2}}= 1 + \cfrac{1}{\frac{3}{2}}=\frac{5}{3}\doteq1{,}67$$
2. $$1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1}}}}=1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{2}}}=1 + \cfrac{1}{1 + \cfrac{1}{\frac{3}{2}}}=1 + \cfrac{1}{\frac{5}{3}}=\frac{8}{5}=1{,}6$$

\fi

> **Úloha 2.**
> Vypočtěte přesnou hodnotu zlatého poměru $\varphi$.

\iffalse

*Řešení.* 
Předpokládejme, že úsečka $AB$ má délku $1$. Tuto úsečku rozdělíme bodem $C$ v poměru zlatého řezu. Potom platí

$$
 \varphi=\frac{|AB|}{|AC|}=\frac{|AC|}{|CB|}.
$$

Označme $x=|AC|$, tedy $x$ bude délka delšího úseku úsečky $AB$. Potom pro délku úsečky $CB$ platí $|CB|=1-x$ a tím získáme vztah
$$\frac{1}{x} = \frac{x}{1-x},\tag{1}$$
který má smysl pro $x\neq0 \text{ a } x\neq1$. 
Úpravou (1) dostaneme kvadratickou rovnici
$$x^2 + x - 1 = 0,$$
jejíž kořeny jsou
$$x_{1,2} = \frac{-1 \pm \sqrt{5}}{2}.$$
V našem případě $x$ je délka úsečky, proto záporná hodnota $x$ nemá smysl. Máme tedy jediné vyhovující řešení rovnice (1)
$$x_1 = \frac{-1 + \sqrt{5}}{2}.$$
Nyní můžeme vypočítat hodnotu zlatého řezu $\varphi$:
$$\varphi=\frac{|AB|}{|AC|}=\frac{1}{x} = \frac{1}{\frac{-1 + \sqrt{5}}{2}}=\frac{2}{\sqrt{5}-1}.$$
Usměrněním zlomku pak dostaneme
$$\varphi=\frac{\sqrt{5}+1}{2}\doteq1{,}618.$$

\fi

> **Úloha 3.**
> Řešte rovnici (inspirovanou zlatým řezem) obsahující konečný řetězový zlomek. 
>
> $$
 x = 1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{x}}} 
>$$
>
\iffalse

*Řešení.* Nejprve rovnici postupně zjednodušíme.
$$
\begin{aligned}
x &= 1 + \cfrac{1}{1 + \cfrac{1}{\frac{x+1}{x}}} \\ %\qquad\text{pro }x\neq0\\
x &= 1 + \cfrac{1}{1 + \cfrac{x}{x+1}} \\ %\qquad\text{pro }x\neq-1\\
x &= 1 + \cfrac{1}{\frac{x+1+x}{x+1}}\\
x &= 1 + \frac{x+1}{2x+1}\\
x &= \frac{3x+2}{2x+1}\\
\end{aligned}
$$

Všimněme si, že výraz na pravé straně zadané rovnice i následně provedené úpravy mají smysl právě pro všechna $x \in \mathbb{R} \setminus \{0,-1,-\frac{1}{2}\}$. 
Pro taková $x$ jednoduchou úpravou získáme kvadratickou rovnici 
$$2x^2 - 2x - 2 = 0.$$
Její kořeny jsou
$$x_{1,2} = \frac{1 \pm \sqrt{5}}{2}.$$
Vidíme, že jedním z řešení je opět zlatý řez.

\fi

### Doplňující informace k řetězovým zlomkům

>**Vyjádření reálného čísla řetězovým zlomkem.** Lze ukázat, že každé číslo $x \in \mathbb{R}$ je možné vyjádřit řetězovým zlomkem. Navíc, pokud je číslo $x$ racionální, je tento řetězový zlomek konečný (ukončený), zatímco pro iracionální $x$ je řetězový zlomek nekonečný (neukončený).  

>**Geometrická interpretace řetězového zlomku.** Uvažujme kladné racionální číslo $x$ a jeho vyjádření (konečným) řetězovým zlomkem 
>
>$$
x = a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cfrac{1}{{\ddots+ \cfrac{1}{a_n}}}}}.
>$$
>
>Na příkladě si ukážeme geometrický význam čísel $a_0, a_1, a_2, \dots, a_n$. 
>
>Uvažujme například zlomek $\frac{23}{16}$. Není těžké si rozmyslet, že tento zlomek lze psát ve tvaru řetězového zlomku následovně: 
>
>$$
 \frac{23}{16}=1 + \cfrac{1}{2 + \cfrac{1}{3 + \cfrac{1}{2}}}
>$$
>
>Čísla $a_0=1$, $a_1=2$, $a_2=3$ a $a_3=2$ mají pěkný geometrický význam. 
>
>Uvažujme obdélník se stranami $23$ a $16$, do kterého vepíšeme co největší čtverec, tj. čtverec o straně $16$ (na obrázku níže je tento čtverec znázorněn žlutě). Tento čtverec se do našeho obdélníku vejde pouze jeden, tj. $a_0=1$. Poté nám zbyde obdélník o stranách $16$ a $7$. Do tohoto obdélníku opět vepíšeme co možná největší čtverec, tj. čtverec o straně $7$. Tyto čtverce (na obrázku je vidíme znázozněné šedou barvou) se tam ale vejdou dva, tj. $a_1=2$. Nyní si snadno rozmyslíme, že dosud nemáme pokrytý obdélník o stranách $7$ a $2$. Do tohoto obdélníku vepíšeme čtverec o straně $2$ (větší se tam nevejde). Tyto čtverce se tam ale vejdou tři (červená barva), tj. $a_2=3$. Nakonec nám zbyde malý obdélník o stranách $2$ a $1$, který jsme schopni (již beze zbytku) vyplnit dvěma čtverci (zelené, o straně 1), tzn. $a_3=2$. 
>
>![Řetězový zlomek - geometrická interpretace](retez_zlomek.svg)

>**Úloha k přemýšlení 1.** Jak by to dopadlo, kdybychom výše popsaným způsobem chtěli pomocí čtverců vyplnit zlatý obdélník? Jak by to v tomto případě souviselo s vyjádřením zlatého řezu (nekonečným) řetězovým zlomkem? Připomeňme, že 
>
>$$
 \varphi = 1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \ddots}}}.
>$$

\iffalse

*Řešení.* 

![Zlatý obdélník](zlaty_obdelnik.svg)

\fi

>**Úloha k přemýšlení 2.** Formát papíru A (A0, A1, A2, $\dots$) má jednu pěknou vlastnost: Přeložíme-li papír na polovinu (překládáme delší stranu), dostaneme menší formát se stejným poměrem stran jako měl původní papír. Vypočtěte poměr stran tohoto papíru. 

\iffalse 

*Řešení.* Označme si delší stranu jako $x$ a kratší jako $y$. Po přeložení na polovinu dostaneme obdélník s rozměry $y$ a $\frac{x}{2}$. Protože přeložený papír má mít stejný poměr stran jako papír původní, dostaneme rovnici 

$$
 \frac{x}{y} = \frac{y}{\frac{x}{2}}, 
$$

ze které po úpravě dostaneme 

$$
 x^2=2y^2. 
$$

Proto pro poměr stran (jedná se o kladná čísla) původního papíru musí platit 

$$
 \frac{x}{y}= \sqrt{2}. 
$$

\fi

>**Úloha k přemýšlení 3.** Co by se stalo, kdybychom chtěli obdobným způsobem vyplnit list papíru formátu A? Pokud jste předchozí úlohu nevyřešili, prozradíme, že poměr stran papíru formátu A je $\sqrt{2}$.  

\iffalse

*Řešení.* Představme si obdélníkový papír s poměrem stran $\sqrt{2}$. Pro jednoduchost předpokládejme, že jeho rozměry jsou $\sqrt{2}$ a $1$. Do tohoto obdélníku se vejde jeden čtverec o straně $1$. Nepokrytý zůstane obdélník o stranách $1$ a $\sqrt{2}-1$. Do něj můžeme vepsat dva čtverce o straně $\sqrt{2}-1$, protože pro poměr jeho stran platí  

$$
 \frac{1}{\sqrt{2}-1}=\sqrt{2}+1 \doteq 2,41. 
$$

Snadno spočítáme, že nyní zůstane nepokrytý obdélník o rozměrech $\sqrt{2}-1$ a $1-2(\sqrt{2}-1)=3-2\sqrt{2}$. Pro poměr stran tohoto obdélníku platí 

$$
 \frac{\sqrt{2}-1}{3-2\sqrt{2}}=\frac{(\sqrt{2}-1)(3+2\sqrt{2})}{(3-2\sqrt{2})(3+2\sqrt{2})}=\sqrt{2}+1. 
$$

Poměr vyšel stejný jako v předchozím kroku, což znamená, že se do posledně zmíněného obdélníku opět vejdou dva čtverce, atd. 

Vše souvisí s tím, že platí 

$$
 \sqrt{2}=1 + \cfrac{1}{2 + \cfrac{1}{2 + \cfrac{1}{2 + \ddots}}}.
$$

![Formát A4](format_A4.svg)

\fi

## Literatura

* Wikipedia. *Golden ratio* [online]. Dostupné z https://en.wikipedia.org/wiki/Golden_ratio [cit. 10.\,11.\,2023].
* Wikipedia. *Řetězový zlomek* [online]. Dostupné z https://cs.wikipedia.org/wiki/Řetězový_zlomek [cit. 10.\,11.\,2023].
* Czech Digital Mathematics Library. *Řetězové zlomky* [online]. Dostupné z  https://www.dml.cz/handle/10338.dmlcz/404015
