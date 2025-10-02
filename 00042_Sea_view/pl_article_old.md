---
keywords:
- geometry
- trigonometry
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


# Výhled na moře

Už se vám někdy při letní procházce po mořském pobřeží 
stalo, že jste se zastavili, zadívali se na horizont a 
zamysleli se: Jak daleko vlastně dohlédnu? A co když je 
na druhé straně břehu něco — mohu to spatřit?

Pro konkrétnost se na chvíli přenesme do jedné z 
nejoblíbenějších evropských dovolenkových destinací – do 
Chorvatska, na břeh Jaderského moře k hoře Sveti Jure. O 
této hoře se můžeme dočíst následující informace[^1]: 

[^1]: www.chorvatsko.cz

*Sveti Jure* (Svatý Jiří) je nejvyšší vrchol (1762 m n. m.) 
vápencového Biokova, které se vypíná v délce 36 km 
souběžně s mořským pobřežím a odděluje Makarskou riviéru 
od vnitrozemské oblasti zvané Dalmatské Záhoří. Tyčí se 
nad pobřežím jako mohutná kamenná hradba. Díky svým 
geologickým zvláštnostem a přírodním krásám byla jeho 
část vyhlášena v roce 1981 chráněnou krajinnou oblastí 
(Park prirode Biokovo o rozloze 196 čtverečních kilometrů).

Pro vrchol Sveti Jure je charakteristická stavba 
televizního vysílače, kterou lze sledovat již většinu 
cesty hornatou krajinou. Pohled z vrcholu na moře i do 
vnitrozemí je při jasném počasí a dobré viditelnosti 
nezapomenutelný. Bohužel tu není žádná možnost 
občerstvení.

![Vrchol Sveti Jure.](sveti_jure.jpg)

> **Úloha 1.** Stojíme-li na vrcholu Sveti Jure a díváme se na moře, jak daleko je od nás bod na horizontu na mořské hladině?

\iffalse

*Řešení.* Pro jednoduchost předpokládáme, že je Země 
koulí o poloměru $6371\,\text{km}$. Označme $S$ střed 
Země, bod $V$ naši polohu (vrchol hory Sveti Jure) a $H$ 
libovolný bod na mořské hladině na horizontu. Řezem 
zeměkoule rovinou $SVH$ je kružnice o poloměru Země, 
jejíž tečnou je přímka $VH$. Z toho vyplývá, že je úhel 
$VHS$ pravý, viz obrázek.

![Řešení úlohy 1](math4you_00042_01.svg)

Víme, že $\lvert SH \rvert = 6371\,\text{km}$ a 
$\lvert SV \rvert  = 6372{,}762\,\text{km}$ (k poloměru 
Země přičítáme nadmořskou výšku hory). 
Užitím Pythagorovy věty pro pravoúhlý trojúhelník $VHS$ 
pak vypočítáme délku odvěsny $VH$: 
$$
\lvert VH \rvert = \sqrt{\lvert SV \rvert ^2 - \lvert SH \rvert ^2} \doteq 150\,\text{km}.
$$
Tato délka je zároveň hledaná vzdálenost k horizontu.

\fi

**Úloha 2.** Je možné z vrcholu Sveti Jure vidět přes 
moře vrchol hory Monte Calvo (1056\,m\,n.\,m.) na 
italském poloostrově Gargano? Monte Calvo je od Sveti 
Jure vzdálená přibližně 210\,km a mezi oběma lokacemi se 
nenachází žádná suchozemská překážka. Dokonalému výhledu 
tak brání pouze horizont.

\iffalse

*Řešení.* Úlohu budeme řešit tak, že uvážíme hypotetickou 
horu stejné výšky jako je Monte Calvo, jejíž vrchol se 
nachází na horizontu. Výhled na tuto horu je tak zakryt 
horizontem. Označme vrchol této hory $M$ a dále označme 
$M_0$ kolmý průmět bodu $M$ do úrovně mořské hladiny a 
$V_0$ kolmý průmět bodu $V$.

![Řešení úlohy 2](math4you_00042_02.svg)

Naším cílem bude určit vzdálenost obou hor, tj. délku 
oblouku $M_0V_0$. Bude-li menší než $210\,\text{km}$ 
(přibližná skutečná vzdálenost hor), nepůjde vidět z 
vrcholu Sveti Jure ani hora Monte Calvo.

Označme $\alpha$ velikost úhlu $VSH$ a $\beta$ velikost 
úhlu $MSH$; ze známé délky přepony a odvěsny v pravoúhlém 
trojúhelníku $VHS$ dostáváme
$$
\cos\alpha = \frac{6371}{6372{,}762} \Longrightarrow \alpha \doteq 1^{\circ}\,20'\,51''.
$$
Obdobně ze známé délky přepony a odvěsny v pravoúhlém 
trojúhelníku $MHS$ dostáváme
$$
\cos\beta = \arccos \frac{6371}{6372{,}056} \Longrightarrow \beta \doteq 1^{\circ}\,3'\,35''.
$$
Délku oblouku $M_0V_0$, který je příslušný úhlu o 
velikosti $\alpha + \beta$, pak určíme z přímé úměrnosti 
a známé délky celé kružnice:
$$
\frac{\alpha + \beta}{360^{\circ}}\cdot 2\pi\cdot 6371 \doteq 268\,\text{km}.
$$
Stejně vysoká hora Monte Calvo je blíže, její vrchol se 
proto nachází nad horizontem a můžeme ji (za dobré 
viditelnosti) z vrcholu Sveti Jure spatřit.

\fi

## Odkazy a literatura

### Literatura

* Chorvatsko.cz. *Sveti Jure* (online). Dostupné z https://www.chorvatsko.cz/stdal/svjure.html (cit. 12. 12. 2024).

### Zdroje obrázků

* Sveti Jure, SKas – Vlastní dílo, CC SA 4.0, dostupné z https://upload.wikimedia.org/wikipedia/commons/7/70/The_highest_peak_Sv_Jure_\%281762_m\%29_in_Biokovo_Nature_Park.jpg (cit. 12. 12. 2024).

---
---

### English source


# A Sea View

Have you ever gone for a summer walk along the seashore, stopped, looked out at the horizon, and wondered: How far can I actually see? And what if there’s something on the far shore—could I see it?

To make this question more concrete, let’s travel for a moment to one of Europe’s most popular holiday destinations: Croatia, to the shores of the Adriatic Sea near Mount Sveti Jure. Here’s what we can read about this mountain[^1]: 

[^1]: www.chorvatsko.cz

*Sveti Jure* (Saint George) is the highest peak (1762 m above sea level) of the Biokovo limestone range, which stretches for 36 km along the coast and separates the Makarska Riviera from the inland region known as the Dalmatian Hinterland. It rises above the coast like a massive stone wall. Thanks to its unique geology and natural beauty, part of the area was designated a nature park in 1981 (Biokovo Nature Park, covering 196 square kilometres).

A distinctive feature of the Sveti Jure summit is a television transmitter, which can be seen from much of the surrounding mountainous terrain. On a clear day with good visibility, the view from the top—both toward the sea and inland—is unforgettable. Unfortunately, there are no refreshments available at the summit.

![Sveti Jure summit.](sveti_jure.jpg)

> **Exercise 1.** If we stand on the summit of Sveti Jure and look out to sea, how far away is the point on the horizon where the sea meets the sky?

\iffalse

*Solution.* For simplicity, let’s assume the Earth is a sphere with a radius of $6371\,\text{km}$. Let $S$ be the center of the Earth, $V$ our location (the summit of Mount Sveti Jure), and $H$ any point on the sea surface that lies on the horizon. The cross-section of the Earth through the plane $SVH$ is a circle with the Earth’s radius, and the line $VH$ is a tangent to this circle. This means that angle $VHS$ is a right angle (see figure below).

![Solution to Exercise 1](math4you_00042_01.svg)

We know that $\lvert SH \rvert = 6371\,\text{km}$ and 
$\lvert SV \rvert  = 6372{.}762\,\text{km}$ (since we add the mountain’s elevation to the Earth’s radius). 
Using the Pythagorean theorem in the right triangle $VHS$ we calculate the length of the leg $VH$:
$$
\lvert VH \rvert = \sqrt{\lvert SV \rvert ^2 - \lvert SH \rvert ^2} \doteq 150\,\text{km}.
$$
This length is the distance to the horizon that we were looking for.

\fi

> **Exercise 2.** Is it possible to see the summit of Mount Monte Calvo (1056 m above sea level) on the Italian Gargano Peninsula from the summit of Sveti Jure? Monte Calvo is approximately 210 km away from Sveti Jure, and there are no land obstacles between the two locations. The only thing that could block the view is the curvature of the Earth.

\iffalse

*Solution.* We will solve this problem by imagining a hypothetical mountain of the same height as Monte Calvo, with its summit located exactly on the horizon. In such a case, the mountain would be just hidden behind the horizon. Let us label the summit of this hypothetical mountain as $M$, its vertical projection onto sea level as $M_0$, and the projection of point $V$ (Sveti Jure) as $V_0$.

![Solution to Exercise 2](math4you_00042_02.svg)

Our goal is to determine the distance between the two mountains, i.e., the length of the arc $M_0V_0$. If this length is shorter than $210\,\text{km}$ 
(the actual distance), then Monte Calvo will be above the horizon and visible from Sveti Jure.

Let $\alpha$ be the angle $VSH$ and $\beta$ the angle $MSH$. From the known lengths of the hypotenuse and the adjacent side in the right triangle $VHS$ we get:
$$
\cos\alpha = \frac{6371}{6372{.}762} \Longrightarrow \alpha \doteq 1^{\circ}\,20'\,51''.
$$
Similarly, from triangle $MHS$:
$$
\cos\beta = \arccos \frac{6371}{6372{.}056} \Longrightarrow \beta \doteq 1^{\circ}\,3'\,35''.
$$
The arc length $M_0V_0$, corresponding to the angle $\alpha + \beta$, can then be calculated using direct proportion and the known circumference of the circle:
$$
\frac{\alpha + \beta}{360^{\circ}}\cdot 2\pi\cdot 6371 \doteq 268\,\text{km}.
$$
Since the real mountain Monte Calvo is located closer than that, its summit lies above the horizon, and we can (in good visibility conditions) see it from the top of Sveti Jure.

\fi

## Literature and References

### Literature

* Chorvatsko.cz. *Sveti Jure* (online). Available at: https://www.chorvatsko.cz/stdal/svjure.html (accessed December 12, 2024).

### Sources of figures

* Sveti Jure, SKas – Own work, CC SA 4.0, available at: https://upload.wikimedia.org/wikipedia/commons/7/70/The_highest_peak_Sv_Jure_\%281762_m\%29_in_Biokovo_Nature_Park.jpg (accessed December 12, 2024).

