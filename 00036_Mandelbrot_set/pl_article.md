---
keywords:
- complex numbers
- Gaussian plane
- sequences
- convergence
- absolute value
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

$$z_{n+1}=z_{n}^2+c,$$ 

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


---
---

### English source

# Mandelbrot Set

The Mandelbrot set is one of the most famous and beautiful fractals, 
fascinating mathematicians, scientists, and artists around the world. 
Although it looks like a complex pattern at first glance, 
it is based on a simple mathematical rule of repeated exponentiation and addition. 
What makes it so interesting is its infinite complexity 
and the beautiful patterns hidden in every detail.

![The Mandelbrot set; the color of points in its vicinity corresponds to the index of the first term in the sequence at which it is determined that the sequence goes to infinity.](Mandelbrot.png)

The use of the Mandelbrot set goes far beyond mathematics. 
It is used in computer graphics to create complex and realistic objects 
when modeling natural structures such as coastlines, mountains, or cloud formations. 
It can even be used in economics and physics to help simulate chaotic systems.

The Mandelbrot set is proof that even simple mathematical procedures can lead 
to incredibly complex and beautiful results with real-world applications.

## Creating a Set

Let us consider a relatively simple recurrent formula

$$z_{n+1}=z_{n}^2+c,$$ 

where the initial value is $z_0=0$ and $c$ represents an arbitrary complex number. 
The French-American mathematician Benoit Mandelbrot (1924–2010) 
was interested in when the sequence of numbers formed this way is bounded, 
i.e. for which $c$ in the complex plane the sequence converges or oscillates. 
If at some point the sequence diverges, he wanted to know how fast. 
It can be proven that if the absolute value of any term of the sequence $z_{n}$ exceeds 2, 
then this sequence is not bounded.

*The Mandelbrot set* is then the set of points $c$ in the complex plane for which the sequence created by the recurrent formula converges or oscillates. Thanks to the above fact, we know that for each term $z$ of this sequence, its absolute value $|z|$ must be less than or equal to two.

Verification of whether a given $c$ belongs to the Mandelbrot set is carried out by calculating individual iterations and observing the absolute values ​​of these iterations. To calculate the iterations, we use the recurrent formula

$$
z_{n+1}=z_{n}^2+c,\qquad z_0=0.
$$

For example, for $c=-i$ we obtain:

$$z_{1}=z_{0}^2-i=0^2-i=-i, \quad |z_1|=1,$$
$$z_{2}=z_{1}^2-i=(-i)^2-i=-1-i, \quad |z_2|=\sqrt{2},$$
$$z_{3}=z_{2}^2-i=(-1-i)^2-i=i, \quad |z_3|=1,$$
$$z_{4}=z_{3}^2-i=(i)^2-i=-1-i, \quad |z_4|=\sqrt{2}.$$

It is clear from the calculation that the results $-i$ and $-1-i$ will repeat indefinitely.
Therefore, the condition $|z|\leq2$ will always be satisfied, and therefore the number $-i$ belongs to the Mandelbrot set.

## Exercises

> **Exercise 1.** Verify whether the complex numbers $1$; $i$; $-1$; $1+i$ belong to the Mandelbrot set.

\iffalse

*Solution.* For simplicity, we will consider only the first few iteration steps. 
The image of a number $c$ in the Gaussian plane belongs to the Mandelbrot set if for all results 
of the iterative calculation the absolute value of the result is less than or equal to $2$.

Iterative process for $c=1$.
$$z_{1}=z_{0}^2+1=0^2+1=1, \quad |z_1|=1,$$
$$z_{2}=z_{1}^2+1=1^2+1=2, \quad |z_2|=2,$$
$$z_{3}=z_{2}^2+1=2^2+1=5, \quad |z_3|=5.$$
The calculation clearly shows that the condition $|z|\leq2$ was not met in the third iteration step, 
meaning that the number $1$ does not belong to the Mandelbrot set.

Iterative process for $c=i$.
$$z_{1}=z_{0}^2+i=0^2+i=i, \quad |z_1|=1,$$
$$z_{2}=z_{1}^2+i=i^2+i=-1+i, \quad |z_2|=\sqrt{2},$$
$$z_{3}=z_{2}^2+i=(-1+i)^2+i=-i, \quad |z_3|=1,$$
$$z_{4}=z_{3}^2+i=(-i)^2+i=-1+i, \quad |z_4|=\sqrt{2}.$$
The calculation shows that the values $-1+i$ and $i$ will repeat indefinitely. 
The condition $|z|\leq2$ will always be satisfied, therefore the number $i$ belongs to the Mandelbrot set.

Iterative process for $c=-1$.
$$z_{1}=z_{0}^2-1=0^2-1=-1, \quad |z_1|=1,$$
$$z_{2}=z_{1}^2-1=(-1)^2-1=0, \quad |z_2|=0,$$
$$z_{3}=z_{2}^2-1=0^2-1=-1, \quad |z_3|=1.$$
The values will repeat again and the condition $|z|\leq2$ will always be met, 
therefore the number $-1$ belongs to the Mandelbrot set.

Iterative process for $c=1+i$.
$$z_{1}=z_{0}^2+1+i=0^2+1+i=1+i, \quad |z_1|=\sqrt{2},$$
$$z_{2}=z_{1}^2+1+i=(1+i)^2+1+i=1+2i+i^2+1+i=1+3i, \quad |z_2|=\sqrt{10}.$$
It is clear from the calculation that the condition $|z|\leq2$ was not met in the second iteration step 
and the number $1+i$ does not belong to the Mandelbrot set.

\fi

> **Exercise 2.** Prove that if there exists $k\in \mathbb{N}$ such that $|z_k|>2$, then the sequence $z_n$ diverges.

\iffalse

*Solution.* By using the recurrent formula, we obtain the fraction
$$
\frac{|z_{n+1}|}{|z_n|}=\frac{|z^2_n+c|}{|z_n|}. 
\tag{1}
$$

Using the triangle inequality
$$
|a+b|\leq|a|+|b|,
$$ 
where $a=z^2+c$ and $b=-c$, we get
$$
|z^2+c-c|\leq|z^2+c|+|-c|=|z^2+c|+|c|
$$
and hence $|z^2+c|\geq|z^2|-|c|=|z|^2-|c|$.

Substituting into $(1)$ and modifying, we get
$$
\frac{|z^2_n+c|}{|z_n|}\geq \frac{|z_n|^2-|c|}{|z_n|}=|z_n|-\frac{|c|}{|z_n|}.
$$
Moreover, we know that there exists such $n$ that $|z_n|>|c|$ holds. For $|c|\leq2$, this follows from the assumption. For $c>2$, then for $n=2$ the following holds
$$
|z_2|=|c^2+c|\geq|c|^2-|c|=|c|(|c|-1)>|c|.
$$
So we can write
$$
\frac{|z^2_n+c|}{|z_n|}\geq \frac{|z_n|^2-|c|}{|z_n|}=|z_n|-\frac{|c|}{|z_n|}>|z_n|-1>1.
$$
And hence
$$
\frac{|z_{n+1}|}{|z_n|}>1,
$$
or $|z_{n+1}|>|z_n|$ and our sequence diverges.

\fi

## Literature 

*  Čápka Hartinger, David. *Mandelbrotova množina - lekce 3 [online]* https://www.itnetwork.cz/algoritmy/graficke/algoritmus-vykresleni-fraktalu-mandelbrotovy-mnoziny} [cit. 22. 9. 2023]

* Wikipedia. *Mandelbrot set [online]*. Available from https://en.wikipedia.org/wiki/Mandelbrot_set [cit. 22. 9. 2023].

* PantheraLeo1359531. *Mandelbrot set - figure [online]*. Available from https://commons.wikimedia.org/w/index.php?curid=103476207 [cit. 22. 9. 2023]
