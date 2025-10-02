---
keywords:
- geometry
- Pythagorean theorem
- perpendicular bisector
is_finished: False
---

### Instructions for translators


1. Open this file on GitHub server. If you see `https://um.mendelu.cz/...` in
   URL, click `View on GitHub` to open this file on github.com.
1. If you see this file on GitHub server, you can edit the content of the file.
   Open the file in an editor. You can use simple editor (pres `e` on GitHub).
   However, an advanced VS Code editor (press `.` on GitHub) is better, since it
   provides preview how the Markdown code renders. Alternatively press pencil
   for simple editor or press triangle next to the pencil to get access to VS
   Code described as `github.dev`. 
1. Fix the keywords in the preamble.
1. Depending on which language version you want to use as a source for your
   translation, delete either English or Czech version below.
1. Translate to your language. Keep Markdown marking and math notation. If you
   use a tool to get first version of the translation, make sure that the markup
   is preserved. 
1. In VS Code you can open the preview in another window by pressing `Ctrl+V`
   and `K`. Keep the preview open as you work, or close using a mouse.
1. Instead of saving, you have to commit and push the changes to the repository.
   Fill the Message under `Source control` (describe your changes, such as
   "Polish translation started") and then press Commit&Push.
1. Make sure that your changes appear in the commit history. In rare cases
   (if you work with simultaneously with someone else) you have to download
   /Pull/ and merge his and yours changes. Usualy Sync (Pull & Push) should
   work.
1. When you finish the translation, change `is_finished: False` in header to `is_finished: True`.

### Instrukce pro překladatele

1. Otevřete tento soubor na serveru GitHub. Pokud máte soubor otevřen na `https://um.mendelu.cz/...`, otevřete jej na serveru github.com.
1. Pokud tento soubor vidíte na serveru GitHub, můžete obsah souboru upravit.
   Otevřete soubor v editoru. Můžete použít jednoduchý editor (stiskněte `e` na GitHubu).
   Lepší je však pokročilý editor VS Code (stikněte `.` na GitHubu), protože poskytuje náhled, jak se kód Markdown interpretuje. Případně stiskněte tužku
   pro jednoduchý editor nebo stiskněte trojúhelníček vedle tužky, abyste získali přístup k editoru VS
   Code popsaný jako `github.dev`. 
1. Opravte klíčová slova v preambuli.
1. V závislosti na tom, kterou jazykovou verzi chcete použít jako zdrojový kód pro svůj
   překladu, odstraňte níže uvedenou anglickou nebo českou verzi.
1. Přeložte do svého jazyka. Ponechte značení Markdown a matematický zápis. Pokud
   použijete nástroj typu DeepL pro získání první verze překladu, ujistěte se, že zápis matematických výrazů
   byl zachován. 
1. Ve VS Code můžete náhled otevřít v jiném okně stisknutím `Ctrl+V`.
   a `K`. Během práce nechte náhled otevřený nebo jej zavřete pomocí myši.
1. Místo uložení musíte změny zaregistrovat a odeslat do úložiště.
   Vyplňte zprávu v poli `Zpráva` (popište své změny, např.
   "Zahájen překlad do polštiny") a poté stiskněte tlačítko Commit&Push.
1. Ujistěte se, že se vaše změny objeví v historii revizí. Ve výjimečných případech
   (pokud pracujete současně s někým jiným) musíte stáhnout
   /Pull/ a sloučit jeho a vaše změny. Obvykle by synchronizace (Pull & Push) měla
   fungovat.
1. Po dokončení překladu změňte `is_finished: False` v záhlaví na `is_finished: True`.


---
---

### Czech source


# Záchrana trosečníka

Letadlo hledá na otevřeném moři pozici trosečníka, který 
má na svém voru zařízení vysílající tísňový signál. 
Zařízení má pouze omezený dosah. Při letu nad mořem 
posádka letadla signál zachytí, ale po chvíli jej ztratí. 
Pilot proto letadlo stočí a podaří se mu signál na kratší 
dobu opět zachytit. 

Trajektorie celého letu je i s naznačeným směrem a místy 
zachycení (body $A_1$ a $A_2$) a ztrát (body $B_1$ a 
$B_2$) signálu znázorněn na mapě.

![Trajektorie letu letadla](math4you_00043_01.svg)

Během obou dob, kdy posádka přijímala signál, letadlo 
neměnilo svou výšku, mezi body $B_1$ a $A_2$ snížilo svou 
výšku o $500\,\text{m}$.

> **Úloha 1.** Konstrukčně určete v mapě pozici $X$ 
> trosečníka.

\iffalse

*Řešení.* Omezený dosah trosečníkova tísňového signálu určuje v 
prostoru nad hladinou polokouli, jejíž střed je polohou 
trosečníka. Vodorovné řezy této polokoule jsou kruhy, které se 
na mapě jeví jako soustředné se středem v bodě $X$. 

Protože letadlo mezi body $A_1$ a $B_1$ nemění svou výšku, je 
$A_1B_1$ tětivou jisté kružnice $k_1$ se středem v bodě $X$. 
Ten tak musí ležet na ose úsečky $A_1B_1$. Ze stejného důvodu 
musí bod $X$ ležet i na ose úsečky $A_2B_2$; je totiž středem 
jisté kružnice $k_2$, jíž je tato úsečka tětivou. 

![Řešení Úlohy 1](math4you_00043_02.svg)

\fi

> **Úloha 2.** V lokalitě se nachází dopravní loď (pozice $L$). 
> Může také zaznamenat trosečníkův tísňový signál, nebo je 
> příliš daleko?
>
> a) Velikosti úseček $LX$ a $A_1X$, $A_2X$ z řešení Úlohy 1 
> přeneste na měřítko. Užitím takto určených vzdáleností 
> (zaokrouhlených na celý nejmenší dílek stupnice) vyřešte 
> úlohu početně.
> 
> b) Vyjděte z řešení Úlohy 1 a úlohu vyřešte znovu, tentokrát 
> pouze užitím geometrických konstrukcí.


\iffalse

*Řešení.*

a) K vyřešení úlohy potřebujeme znát dosah trosečníkova 
zařízení, což je poloměr $r$ polokoule zmíněné v řešení 
předešlé úlohy. Přenesením úseček $A_1X$ a $A_2X$ na měřítko a 
zaokrouhlením jejich délek na desetiny kilometru dostáváme 
$\lvert A_1X \rvert \doteq 2{,}9\,\text{km}$ 
a $\lvert A_2X \rvert \doteq 3{,}4\,\text{km}$. Tyto délky jsou 
zřejmě poloměry $r_1$ a $r_2$ kružnic $k_1$ a $k_2$.

Uvažme takový průmět polokoule, ve kterém se kružnice $k_1$ a 
$k_2$ zobrazí po řadě jako rovnoběžné úsečky $K_1L_1$ a 
$K_2L_2$ takové, že mají stejnou osu $o$, jejich délky jsou po 
řadě $2r_1$ a $2r_2$ a jejich vzdálenost je $0{,}5\,\text{km}$. 
Označme dále střed polokoule $S$, střed úsečky $K_1L_1$ jako 
$S_1$ a střed úsečky $K_2L_2$ jako $S_2$. Viz obrázek, ve 
kterém je pro názornost vyznačena také mořská hladina přímkou $h$.

![Pomocný průmět polokoule při řešení Úlohy 2a)](math4you_00043_03.svg)

Z Pythagorovy věty aplikované na trojúhelníky $SS_1K_1$ a 
$SS_2L_2$ vyplývají rovnosti
$$
\begin{align*}
r^2 &= r_1 ^2 + \lvert SS_1 \rvert ^2 \\
r^2 &= r_2 ^2 + \lvert SS_2 \rvert ^2.
\end{align*}
$$

Platí však $\lvert SS_1 \rvert = \lvert SS_2 \rvert + 0{,}5$. 
Dosazením do první rovnice a porovnáním obou stran dostáváme 
lineární rovnici s jedinou neznámou $\lvert SS_2 \rvert$, 
kterou vyřešíme:
$$
\begin{align*}
r_2 ^2 + \lvert SS_2 \rvert ^2 &= r_1 ^2 + \left( \left\lvert SS_2 \right\rvert + 0{,}5 \right) ^2 \\[1mm]
\left\lvert SS_2 \right\rvert &=  r_2^2 - r_1^2 - 0{,}25
\end{align*}
$$

Vyjádřením $r$ z druhé rovnice a následným dosazením dostáváme
$$
r = \sqrt{r_2 ^2 + \left(r_2^2 - r_1^2 - 0{,}25 \right)^2 } \doteq 4{,}5\,\text{km}.
$$

Vzdálenost lodi od trosečníka je délkou úsečky $LX$. Přenesením 
této úsečky na měřítko vyčteme $\lvert LX \rvert \doteq 4{,}
0\,\text{km}$, úsečka je tedy kratší než dosah $r$ trosečníkova 
signálu. Loď proto může tento signál zaznamenat.

b) K odvození konstrukčního řešení úlohy (tj. sestrojení 
poloměru $r$ polokoule) využijeme stejný pomocný průmět 
polokoule jako v Úloze 2a. Střed polokoule $S$ je průsečíkem 
společné osy $o$ úseček $K_1L_1$ a $K_2L_2$ a osy úsečky 
$L_1L_2$, neboť ta je tětivou obrysové půlkružnice $k$. Hledaný 
poloměr $r$ je pak např. velikostí úsečky $SK_1$,  viz obrázek.

![Pomocný průmět polokoule při řešení Úlohy 2b)](math4you_00043_04.svg)

Při samotném provedení konstrukce přenášíme vzdálenosti $r_1$ a 
$r_2$ z řešení Úlohy 1 (kde připomínáme, že platí 
$r_1=\lvert A_1X\rvert$ a $r_2=\lvert A_2X\rvert$), vzdálenost 
středů kružnic $|S_1S_2|=d_{0{,}5}$, kde $d_{0{,}5}$ označuje 
vzdálenost na mapě odpovídající $0{,}5\,\text{km}$, kterou 
nanášíme z měřítka.

Průmět polokoule na mapě ohraničuje kružnice $l$ se středem v 
bodě $X$ a poloměrem $r$, který přeneseme z pomocného průmětu. 
Po sestrojení této kružnice je vidět, že se loď nachází v 
dosahu nouzového signálu.

![Řešení Úlohy 2b)](math4you_00043_05.svg)

\fi


---
---

### English source


# Rescuing a Castaway

A plane is searching the open sea for a castaway who has a device on their raft that emits a distress signal.
The device has only a limited range. While flying over the sea, the crew picks up the signal, but after a short time, it is lost. The pilot turns the aircraft around, and they manage to receive the signal again, though only briefly.

The trajectory of the entire flight, including the direction of travel and the points where the signal was picked up (points $A_1$ a $A_2$) and lost (points $B_1$ and $B_2$) is shown on the map.

![Flight trajectory of the aircraft](math4you_00043_01.svg)

During both periods when the crew received the signal, the aircraft maintained a constant altitude.
Between points $B_1$ and $A_2$, the aircraft descended by $500,\text{m}$.

> **Exercise 1.** Use a geometric construction on the map to determine the position $X$ of the castaway.

\iffalse

*Solution.* The limited range of the castaway’s distress signal defines a hemisphere above the sea surface, with the center located at the castaway’s position. Horizontal cross-sections of this hemisphere are circles that appear on the map as concentric circles centered at point $X$. 

Since the aircraft maintained a constant altitude between points $A_1$ and $B_1$, the segment $A_1B_1$ forms a chord of a certain circle $k_1$ with center at point $X$. Therefore, point $X$ must lie on the perpendicular bisector of segment $A_1B_1$.
For the same reason, point $X$ must also lie on the perpendicular bisector of segment $A_2B_2$, since this segment is a chord of another circle $k_2$ centered at $X$.

![Solution to Exercise 1](math4you_00043_02.svg)

\fi

> **Exercise 2.** There is a cargo ship in the area (position $L$).
> Can it also receive the castaway’s distress signal, or is it too far away?
>
> a) Transfer the lengths of segments $LX$, $A_1X$, and $A_2X$ from the solution to Exercise 1 to the scale provided. Using these distances (rounded to the nearest smallest unit of the scale), solve the problem numerically.
> 
> b) Using the construction from Exercise 1, solve the problem again—this time relying solely on geometric constructions.


\iffalse

*Solution.*

a) To solve the problem, we need to determine the range of the castaway’s device, which is the radius $r$ of the hemisphere mentioned in the solution to the previous exercise. 
By transferring the segments $A_1X$ and $A_2X$ to the scale and rounding their lengths to the nearest tenth of a kilometer, we get $\lvert A_1X \rvert \doteq 2{.}9\,\text{km}$ and $\lvert A_2X \rvert \doteq 3{.}4\,\text{km}$. These lengths are clearly the radii $r_1$ a $r_2$ of the circles $k_1$ a $k_2$.

Let us consider a projection of the hemisphere in which the circles $k_1$ and $k_2$ appear as parallel segments $K_1L_1$ and $K_2L_2$, such that they share the same perpendicular bisector $o$, their lengths are $2r_1$ and $2r_2$ respectively, and the vertical distance between them is $0{.}5\,\text{km}$.
Let $S$ be the center of the hemisphere, $S_1$ the midpoint of segment $K_1L_1$, and $S_2$ the midpoint of $K_2L_2$. See the figure below, where the sea level is also marked as a straight line $h$ for clarity.

![Auxiliary projection of the hemispehre used in solving Exercise 2a)](math4you_00043_03.svg)

Using the Pythagorean theorem on triangles $SS_1K_1$ and $SS_2L_2$, we obtain the following equations:
$$
\begin{align*}
r^2 &= r_1 ^2 + \lvert SS_1 \rvert ^2 \\
r^2 &= r_2 ^2 + \lvert SS_2 \rvert ^2.
\end{align*}
$$

We also know that $\lvert SS_1 \rvert = \lvert SS_2 \rvert + 0{.}5$. 
Substituting this into the first equation and comparing both expressions, we obtain a linear equation with a single unknown $\lvert SS_2 \rvert$, which we solve as follows:
$$
\begin{align*}
r_2 ^2 + \lvert SS_2 \rvert ^2 &= r_1 ^2 + \left( \left\lvert SS_2 \right\rvert + 0{.}5 \right) ^2 \\[1mm]
\left\lvert SS_2 \right\rvert &=  r_2^2 - r_1^2 - 0{.}25
\end{align*}
$$

Solving for $r$ using the second equation and substituting, we get:
$$
r = \sqrt{r_2 ^2 + \left(r_2^2 - r_1^2 - 0{.}25 \right)^2 } \doteq 4{.}5\,\text{km}.
$$

The distance from the ship to the castaway is given by the length of segment $LX$.
By transferring this segment to the scale, we find $\lvert LX \rvert \doteq 4{.}0,\text{km}$,
which is less than the range $r$ of the castaway’s signal.
Therefore, the ship can receive the signal.

b) To construct a geometric solution to the problem (i.e., to determine the radius $r$ of the hemisphere), we use the same auxiliary projection of the hemisphere as in Exercise 2a. 
The center of the hemisphere $S$ is the intersection of the common perpendicular bisector $o$ of segments $K_1L_1$ and $K_2L_2$ with the perpendicular bisector of segment $L_1L_2$, since $L_1L_2$ is a chord of the semicircle outline $k$. The desired radius $r$ is, for example, the length of segment $SK_1$ — see the figure.

![Auxiliary projection of the hemispehre used in solving Exercise 2b)](math4you_00043_04.svg)

To carry out the construction, we transfer the distances $r_1$ and $r_2$ from the solution to Exercise 1 (recall that $r_1=\lvert A_1X\rvert$ a $r_2=\lvert A_2X\rvert$), as well as the distance between the centers of the circles, $|S_1S_2|=d_{0{.}5}$, where $d_{0{.}5}$ is the map distance corresponding to $0{.}5\,\text{km}$, taken from the scale.

The projection of the hemisphere on the map is bounded by a circle $l$ with center at point $X$ and radius $r$, which we transfer from the auxiliary projection.
Once this circle is drawn, it is clear that the ship is within range of the distress signal.

![Solution to Exercise 2b)](math4you_00043_05.svg)

\fi

