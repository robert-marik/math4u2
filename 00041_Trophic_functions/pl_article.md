---
keywords:
- function
- rational fractional function
- asymptote
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


# Trofické funkce v modelech dravce a kořisti

Při studiu přírody hrají neocenitelnou roli matematické modely. Tyto
modely otevírají cestu k předpovědím budoucího vývoje, ale plní i
další a důležitější role.

Používání ekologických modelů bývá někdy zmiňováno jako fyzikální postupy 
v ekologii, protože se studuje ekosystém z hlediska vývoje populací a
používají se k tomu matematické metody původně
odvozené na řešení fyzikálních úloh. Výstupy z modelů poté nesou například 
následující informace.

* **Predikce** Schopnost pracovat s matematickými modely ekosystémů
    umožňuje předpovídat budoucí vývoj. Může se jednat o vývoj v
    neměnném prostředí, nebo vývoj v prostředí, ve kterém se některý z
    parametrů mění. Znalost modelu potom umožní posoudit, jaký má tato
    změna vliv na ekosystém.
* **Porozumění principům** Matematické modely umožňují ekologům a
    vědcům zkoumat interakce mezi různými složkami ekosystémů a
    porozumět dynamice těchto systémů. Pomáhají tím identifikovat
    faktory ovlivňující strukturu a funkci těchto ekosystémů.
* **Optimalizace rozhodování** Matematické modelování ekosystémů může
     být použito k optimalizaci rozhodování v oblastech jako je
     ochrana biodiverzity nebo management lesů a rybolovu. 
     Pomáhá identifikovat nejlepší strategie pro
     dosažení vytyčených cílů.
  
Jedním ze základních vztahů v ekosystémech je vztah _dravce a
kořisti_. Tento vztah může být jedinou interakcí v ekosystému nebo
může být doplněn interakcemi dalšími. Důležitost modelování soužití
dravce a kořisti si objasníme na následujících historicky významných
modelech.

## Lotkův-Volterrův model

V roce 1926 publikoval jeden z prvních modelů dravce a kořisti italský
matematik Vito Voterra. Motivací k sestavení tohoto modelu byla
skutečnost, že během omezení rybolovu za první světové války v
úlovcích vzrostlo procento dravých ryb. Na tuto skutečnost upozornil
Volterru jeho zeť, mořský biolog Umberto D'Ancona, který si uvedený jev
nedokázal zdůvodnit. Dokonce čekal pravý opak: při omezení rybolovu
předpokládal zvýšení procentuálního podílu druhů menších ryb, které jsou
potravou pro dravce. Volterrův model toto chování vysvětluje jako
důsledek jednoduché představy interakce mezi dravými rybami a kořistí. 

Model obsahuje dvě rovnice. První rovnice 
popisující populaci kořisti obsahuje předpoklad, že tato populace 
přirozeně roste, ale růst je zpomalen
působením dravců. Více dravců vede k většímu zpomalení
růstu kořisti. Příliš mnoho dravců může vést dokonce k tomu, že velikost populace kořisti
bude klesat a kořist vymře. Rovnice věnovaná populaci dravců 
obsahuje předpoklad, že bez přítomnosti kořisti populace dravce vymírá. 
Čím více kořisti ale mají dravci k dispozici, tím spíše se toto vymírání
převrátí v nárůst populace dravce.

V systému popsaném výše vznikají přirozeně cykly. Dostatek kořisti
umožní nárůst populace dravců. Mnoho dravců poté působí na populaci
kořisti negativně do té míry, že populace kořisti začne vymírat. Toto
vymírání má za následek nedostatek potravy pro dravce a
ti začnou také vymírat. Po čase je populace dravce
redukována natolik, že kořist přítomnost dravce pociťuje
málo. Proto může její populace zase růst a namnožit se do původního stavu. To však
opět umožní růst populace dravce a uzavírá se cyklus. Velmi pěkně jsou
periodické změny velikosti obou populací patrné ze záznamů výkupu kožešin
sněžného zajíce a rysa v oblasti Hudsonova zálivu.

Volterra svým modelem vysvětlil nejenom vznik cyklů, ale i to, že
omezením lovu se rovnovážná poloha, okolo které populace dravce a
kořisti oscilují, posune ve prospěch dravce a nikoliv kořisti. Tento
jev, kterého si všiml D'Ancona, se nazývá _Volterrův efekt_.

Stejný model jako Volterra navrhl již v roce 1910 americký matematik
Alfred J. Lotka, a proto se model dnes nazývá Lotkův-Volterrův model.

![Vlevo typický průběh velikosti populací dravce a kořisti. Po maximu kořisti následuje maximum dravce a poté propad obou populací. Vpravo liška ostrovní, která se z vrcholového predátora na svém ostrově stala kořistí na pokraji vyhubení.](1.jpg)


## Model obaleče smrkového

Podobné periodické výkyvy jako v Lotkově-Volterrově modelu je možné
pozorovat i v kanadských lesích. Zde přibližně po 30 až 40 letech
docházelo k masovému přemnožení obaleče smrkového (_Choristoneura
fumiferana_). Populace tohoto motýla je relativně malá, ale některé
roky se zvýší tisícinásobně a jeho housenky dokáží zahubit až 80% stromů v
lese a ten tak prakticky zničit. Jeden z posledních masových výskytů byl
od roku 2006 v Quebecu. Zde bylo do roku 2019 zasaženo cca 9,6 milionu
hektarů lesa [^1], což je více než rozloha Maďarska.

[^1]: Zdroj viz <https://www.nrcan.gc.ca>.

V roce 1978 navrhli vědci D. Ludwig, D. D. Jones a C. S. Holling model, který
dokázal nejenom modelovat vývoj populace obaleče, ale pomohl objasnit
i důvody, proč k popisovanému přemnožení dochází. Důvodem byla
predace. V tomto případě šlo o konzumaci housenek obaleče ptáky. Ptáci
sloužili v přírodě jako faktor omezující počty housenek, ovšem jenom
do jistého limitu. Když se les dostatečně rozrostl, poskytl dostatek
potravy i populaci housenek. Populace housenek se pak rozrostla do
takové míry, že ptáci dosáhli při konzumaci potravy své saturace a
nedokázali dál stavy housenek redukovat. Tím se role ptáků jako
predátorů stala méně významnou a populace housenek se mohla velmi
rychle množit a poté zdevastovat les.

V tomto případě je predace důležitá pro omezení populace
housenek. Protože ptáci jako predátoři mají mnohem pomalejší cyklus
rozmnožování než obaleč, je možné jejich populaci považovat za
konstantní. Díky saturaci poté ptáci dokáží omezit rychlost růstu
obaleče jen do omezené míry. Toto omezení však od určité velikosti
populace obaleče přestává stačit a dojde k jeho nekontrolovatelnému přemnožení.

## Model lišky ostrovní

Liška ostrovní (_Urocyon littoralis_) je jedinečný živočišný druh,
endemit žijící jenom na ostrůvcích okolo Kalifornie. Je velká jako
kočka a díky absenci přirozených nepřátel důvěřivá. Jako druh je
citlivá a zranitelná vlivem malé genetické variability a malé
odolnosti vůči nemocem zavlečeným z pevniny. Je to jedna z nejmenších
psovitých šelem. Na rozdíl od ostatních psovitých šelem ale umí šplhat po
stromech.

Vlivem činnosti člověka se populace lišky ostrovní dostala na přelomu
tisíciletí do velkých potíží. Na ostrově San Miguel klesla populace z
450 dospělých jedinců v roce 1994 na 15 v roce 1999 [^2]. Podobná situace
byla i na okolních ostrovech, z nichž každý je osídlen samostatným
poddruhem lišky ostrovní. Příčinou úhynu byl celý řetězec událostí:
produkce insekticidu DDT ve 40. letech 20. století měla za následek
vymření orla bělohlavého (_Haliaeetus leucocephalus_) a ten byl
nahrazen orlem skalním (_Aquila chrysaetos_). Predátora živícího
se rybami tímto na ostrově vystřídal predátor preferující savce. Toto bylo
pro lišky ostrovní fatální. Lišky, dříve vrcholní predátoři, se najednou staly 
kořistí a na přelomu tisíciletí se ocitly těsně před vyhubením. A na
rozdíl od Lotkova--Volterrova modelu nebylo možné doufat v návrat
lišek na původní stavy díky oscilacím, protože orli měli i
alternativní potravu v podobě divokých prasat a skunků.

[^2]: Zdroj viz <https://www.iucnredlist.org/species/22781/13985603>.

Naštěstí se nesmírným úsilím podařilo lišky ostrovní jako druh
zachránit. Nejprve se podařilo správně identifikovat příčiny jejich 
úbytku. Poté již stačilo populaci lišek opětovně rozmnožit a zajistit
podmínky, ve kterých je populace stabilní. To zahrnovalo vybití
divokých prasat, přesídlení orlů skalních, návrat orlů bělohlavých,
umělé rozmnožení lišek, jejich návrat do přírody a jejich vakcinaci
proti zavlečeným chorobám. To vše se podařilo v rekordním čase, za
jednu dekádu. Jednalo se o jeden z nejúspěšnějších záchranných
programů pro savce.

## Trofické funkce

Důležitou komponentou modelů dravce a kořisti, ať se jedná o
kterýkoliv z výše uvedených případů, je _trofická funkce_. Tato funkce
modeluje působení jednoho predátora na populaci kořisti. Udává
rychlost, s jakou zpomaluje růst kořisti jeden dravec. Je-li $x$
velikost populace kořisti a $y$ rychlost, s jakou jeden dravec
zpomaluje růst kořisti (tj. množství kořisti ulovené dravcem za
jednotku času), můžeme tuto funkci matematicky zapsat ve tvaru
$$y=f(x).$$ 
Budeme se snažit najít přirozené předpoklady, které
trofická funkce musí splňovat. Poté se pro ni pokusíme najít vhodný
analytický tvar.

> **Úloha 1.** Předpoklady o působení dravce na kořist mají odraz ve
    vlastnostech, které musí mít trofická funkce. 
> 
> 1. Dravec v prostředí s chudou nabídkou potravy má i chudý
>    úlovek. Více kořisti znamená snazší dosah kořisti a tím i větší
>    úlovek.
> 1. Bez potravy dravec nic neuloví. Pokud je množství kořisti nulové,
>    je nulové i množství kořisti, které dravec uloví za jednotku času.
> 1. Dravci konzumují potravu jenom do své saturace. Je-li potravy
>    nadbytek, dravci neuloví za jednotku času více potravy než odpovídá
>    jejich saturaci.
> 
> Vyjádřete tyto vlastnosti pomocí pojmů, které používáme pro popis
>  vlastností funkcí. Jaké vlastnosti funkcí odpovídá každý z uvedených
>  bodů?

\iffalse

_Řešení._

1. Funkce $y=f(x)$ je rostoucí.

2. Funkce $y=f(x)$ prochází počátkem, tj. platí $f(0)=0$.

3. Funkce $y=f(x)$ je shora ohraničená. Jelikož je funkce rostoucí a 
shora ohraničená, tak má její graf vodorovnou asymptotu v nekonečnu.

\fi

## Trofická funkce Hollingova typu II

Trofická funkce udává, kolik kořisti zahubí jeden dravec za jednotku
času při dané velikosti populace kořisti. Musí tedy být definována na
množině nezáporných čísel a funkční hodnoty budou nezáporné (toto plyne 
i z bodů 1 a 2 v předchozí úloze). V předchozí části bylo ukázáno, že 
trofická funkce má procházet počátkem
a růst k vodorovné asymptotě (růst a ohraničenost shora). Tyto
vlastnosti nebudou splněny, pokud budeme hledat trofickou funkci mezi
lineárními funkcemi. Zkusíme tedy nejjednodušší nelineární funkci,
nepřímou úměrnost.

![Vlevo dvě typické trofické funkce, nazývané funkce Hollingova typu. Funkce
typu II roste stále pomaleji. Funkce typu III roste ze začátku pomalu, růst se zrychluje a poté opět zpomaluje. Vpravo funkce typu II jako část
transformovaného grafu nepřímé úměrnosti. (vlastní obrázek)](2.svg)

> **Úloha 2.** Vyjděte z grafu funkce $y=\frac 1x$. Na této funkci
>    provádějte transformace, které mění graf způsobem popsaným níže.
>
> 1. Přeškálujte graf $k$-krát ve svislém směru. Tím se nezmění monotonie
>    ani poloha vodorovné asymptoty, ale můžeme měnit rychlost růstu.
> 1. Převraťte graf okolo vodorovné osy a posuňte o $S$ nahoru. Tím
>    docílíme toho, že pro kladné $x$ bude funkce rostoucí a poroste k
>    asymptotě $S$.
> 1. Po uvedených transformacích má graf v nule svislou asymptotu a
>    jeden průsečík s vodorovnou osou vpravo od počátku. Posuňte graf
>    doleva tak, aby se svislá asymptota dostala vlevo od svislé osy a
>    průsečík s osou $x$ se posunul do počátku.

\iffalse

_Řešení._ Funkce, jejíž graf vznikne přeškálováním grafu funkce
$y=\frac{1}{x}$ ve svislém směru $k$-krát je $$y=\frac{k}{x}.$$
Převrácení dosáhneme vynásobením funkce fakorem $-1$ a posunu docílíme
přičtením hodnoty $S$. Těmito úpravami dostáváme funkci $$y=S-\frac{k}{x}.$$ Posun
doleva o $b$ zajistíme substitucí výrazu $x+b$ za $x$. Tím dostáváme
funkci $$y=S-\frac {k}{x+b}.$$ Po převedení na společného jmenovatele
má funkce tvar 
$$y=\frac{Sx+Sb}{x+b}-\frac{k}{x+b}=\frac{Sx + (Sb-k)}{x+b}.$$ 
Má-li platit $f(0)=0,$ musí být splněna podmínka
$$Sb-k=0.$$ 
Tato podmínka ukazuje, že tři konstanty nejsou nezávislé,
ale je mezi nimi uvedená vazba.

\fi

*Poznámka.* V předchozí úloze jsme odvodili analytický tvar pro
  jednu ze základních trofických funkcí. Jedná se o rostoucí funkci,
  která z počátku roste směrem k vodorovné asymptotě a rychlost růstu
  postupně klesá. Taková funkce se nazývá Hollingova funkce II
  typu. Bývá obvyklé ji psát ve tvaru $$f(x)=\frac {Sx}{x+b},\tag{1}$$
  kde $S$ je hladina saturace a $b$ konstanta, jejíž význam objasníme
  v následující úloze.

> **Úloha 3.** Ukažte, že pro velikost populace rovnu $b$ 
je hodnota trofické funkce (1) rovna polovině hodnoty 
saturace.

\iffalse

_Řešení._ Přímým dosazením do (1) dostáváme
$$f(b)=\frac{Sb}{b+b}=\frac {Sb}{2b}=\frac S2.$$ 
Tím je tvrzení dokázáno.

\fi

Následující úkol ukazuje opačný proces, kdy z trofické funkce ve tvaru
(1) odvodíme tvar ukazující postupné transformace funkce $y=\frac 1x$.

> **Úloha 4.** Upravte předpis funkce $$y=\frac {6x}{x+2}$$ do základního tvaru, tj. tak, abychom mohli vyčíst postupné transformace funkce $y=\frac 1x$ na graf zadané funkce.

\iffalse 

_Řešení._ Úlohu vyřešíme tak, že zlomek šikovně upravíme. V čitateli vytvoříme násobek
jmenovatele, zlomek rozdělíme na dva a zkrátíme:

$$\frac {6x}{x+2} = \frac {6(x+2)-12}{x+2}=\frac {6(x+2)}{x+2}-\frac {12}{x+2}=6-12\frac 1{x+2}$$

Tento výpočet ukazuje, že graf uvedené funkce obdržíme rozšířením
grafu funkce ve svislém směru dvanáctkrát, převrácením okolo vodorovné
osy, posunutím o šest jednotek nahoru a dvě jednotky doleva.

Stejného výsledku bychom docílili i tak, že bychom jmenovatele vydělili čitatelem.

\fi

> **Úloha 5.** Sestavte trofickou funkci, pokud víte, že rychlost
    konzumace potravy při saturaci predátorů je $6$, a že konzumace probíhá
    poloviční rychlostí pro populaci kořisti o velikosti $210$.

\iffalse

*Řešení.* Díky poznámce před třetí úlohou o obecném tvaru trofické funkce víme, že předpis bude tvaru
$$
y=\frac{Sx}{x+b},
$$
kde $S$ je hodnota saturace predátora, tj.
$$
y=\frac{6x}{x+b}\,.
$$
Hodnotu parametru $b$ můžeme rovnou říci díky Úloze 3, ale můžeme ji též rychle dopočítat z druhé podmínky ze zadání, jelikož víme, že
$$
3=\frac{6\cdot 210}{210+b}
$$
a odtud plyne $b=210$. Předpis výsledné funkce je tedy
$$
y=\frac{6x}{x+210}.
$$


\fi

## Literatura a odkazy

### Literatura

* Wikipedia, <https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations> March 3, 2024
* R Mařík, Dynamické modely populací, <https://robert-marik.github.io/dmp/uvod.html>, March 3, 2024
* D. Ludwig, D.D. Jones, C.S. Holling: Qualitative analysis of insect outbreak systems: the spruce budworm and forest, Journal of Animal Ecology 47(1): 315–332, February 1978.

### Zdroje obrázků

* <https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations#/media/File:Lotka_Volterra_dynamics.svg>
* <https://www.npr.org/sections/thetwo-way/2016/08/11/489695842/once-nearly-extinct-california-island-foxes-no-longer-endangered> Kevork Djansezian/AP 

---
---

### English source


# Trophic Functions in Predator–Prey Models

Mathematical models play an invaluable role in studying nature. These models not only allow us to predict future developments, but they also serve several other important purposes.

The use of ecological models is sometimes referred to as applying physical methods in ecology, since ecosystems are studied in terms of population dynamics using mathematical techniques originally developed for solving problems in physics. The outputs of such models can provide insights such as the following:

* **Prediction.** The ability to work with mathematical models of ecosystems makes it possible to forecast future developments. These may concern a stable environment or one in which certain parameters are changing. Understanding the model then allows us to assess how such changes will affect the ecosystem.
* **Understanding Principles.** Mathematical models help ecologists and scientists examine the interactions between various components of ecosystems and gain insight into their dynamics. This in turn helps identify the factors that shape the structure and function of these ecosystems.
* **Decision-making Optimization.** Mathematical modelling can also be used to improve decision-making in areas such as biodiversity conservation or the management of forests and fisheries. It helps identify the most effective strategies to achieve specific goals.

One of the fundamental ecological relationships is the _predator–prey interaction_. This relationship may be the only interaction in a given ecosystem, or it may be accompanied by others. The importance of modelling predator–prey coexistence will be illustrated using several historically significant models.

## The Lotka-Volterra Model

In 1926, Italian mathematician Vito Volterra published one of the first mathematical models of predator–prey interactions. He was motivated by an observation made during World War I, when fishing restrictions led to an increased percentage of predatory fish in the catch. This surprising trend was pointed out to Volterra by his son-in-law, marine biologist Umberto D'Ancona, who had expected the opposite: he assumed that reduced fishing pressure would increase the proportion of smaller fish species, which serve as prey for predators. Volterra’s model explained this phenomenon as a result of simple interactions between predatory fish and their prey.

The model consists of two equations. The first describes the prey population, assuming that it grows naturally, but this growth is limited by the presence of predators. A higher number of predators slows the prey population’s growth more significantly. If there are too many predators, the prey population may even begin to decline and eventually go extinct.
The second equation describes the predator population. It assumes that without prey, the predators die out. However, the more prey is available, the more this trend reverses, allowing the predator population to grow.

This system naturally produces cycles. An abundance of prey allows the predator population to increase. As predator numbers grow, they put increasing pressure on the prey population, eventually driving it to decline. This leads to a food shortage for predators, which in turn causes a decline in their own numbers. Eventually, the predator population becomes so small that the prey population experiences less pressure and can grow again, eventually reaching its original level. This, in turn, allows the predator population to recover, and the cycle repeats.
These periodic fluctuations in population sizes can be clearly observed in historical fur-trade records of snowshoe hares and lynxes in the Hudson Bay area.

Volterra’s model explained not only the emergence of such cycles, but also why restricting hunting or fishing can shift the equilibrium point—around which both populations oscillate—in favor of the predator rather than the prey. This phenomenon, observed by D'Ancona, is known as the _Volterra effect_.

The same model had actually been proposed earlier, in 1910, by American mathematician Alfred J. Lotka. For this reason, it is now known as the _Lotka–Volterra model_.

![On the left, a typical pattern of predator and prey population sizes. A maximum of prey is followed by a maximum of predator and then a decline in both populations. On the right, the island fox, which has gone from being a top predator on its island to a prey endangered by extinction](1.jpg)

## The Spruce Budworm Model

Similar periodic fluctuations as those described by the Lotka–Volterra model can also be observed in Canadian forests. Approximately every 30 to 40 years, there has been a massive outbreak of the spruce budworm (_Choristoneura fumiferana_). This moth species typically exists in relatively low numbers, but in certain years, its population increases by a factor of a thousand. During such outbreaks, the larvae can destroy up to 80% of the trees in a forest, effectively devastating the entire area. One of the most recent large-scale infestations began in 2006 in Quebec. By 2019, around 9.6 million hectares of forest [^1] had been affected—an area larger than the size of Hungary.

[^1]: source at <https://www.nrcan.gc.ca>.

In 1978, scientists D. Ludwig, D. D. Jones, and C. S. Holling proposed a model that not only described the population dynamics of the spruce budworm but also helped explain the mechanisms behind these outbreaks. The key factor was predation—specifically, birds feeding on the budworm larvae. In the natural ecosystem, birds helped keep the budworm population in check, but only up to a certain point. Once the forest had grown large enough, it provided ample food for the budworms as well. Their population then increased so much that the birds became saturated and could no longer consume larvae at a rate sufficient to limit their numbers. As a result, the birds’ role as predators diminished, and the budworm population exploded, ultimately causing extensive forest damage.

In this case, predation plays a crucial role in limiting the budworm population. However, because birds reproduce much more slowly than budworms, their population can be considered constant for modelling purposes. Once birds reach their saturation point, they can only reduce the budworm population growth to a limited extent. Beyond a certain threshold, this control becomes ineffective, leading to uncontrolled population growth and a full outbreak.

## The Island Fox Model

The island fox (_Urocyon littoralis_) is a unique species, an endemic mammal that lives only on a few small islands off the coast of California. Roughly the size of a domestic cat, the island fox is unusually trusting due to the absence of natural predators in its habitat. As a species, it is highly sensitive and vulnerable, with low genetic variability and limited resistance to diseases introduced from the mainland. It is one of the smallest canids in the world, and unlike most other members of the dog family, it can climb trees.


Due to human activity, the island fox population declined dramatically around the turn of the millennium. On San Miguel Island, the number of adult individuals dropped from 450 in 1994 to just 15 in 1999[^2]. A similar situation
occurred on the surrounding islands, each of which is home to its own subspecies of island fox. The decline was caused by a chain of events: the production of the insecticide DDT in the 1940s led to the extinction of bald eagles (_Haliaeetus leucocephalus_) in the area. In their absence, golden eagles (_Aquila chrysaetos_) moved in. Unlike the fish-eating bald eagle, the golden eagle prefers mammals, which proved catastrophic for the island fox.
Once the top predator on the islands, the fox suddenly became prey—and by the early 2000s, the species was on the brink of extinction. Unlike in the Lotka–Volterra model, there was no hope that the fox population would naturally rebound due to predator–prey oscillations, because the eagles had alternative food sources such as wild pigs and skunks.

[^2]: For source see <https://www.iucnredlist.org/species/22781/13985603>.

Fortunately, the island fox was saved through an extraordinary conservation effort. Once the causes of the decline were correctly identified, the recovery could begin. Conservationists focused on increasing the fox population and stabilizing its environment. This involved eradicating wild pigs, relocating golden eagles, reintroducing bald eagles, breeding foxes in captivity, releasing them into the wild, and vaccinating them against introduced diseases.
All of this was achieved in record time—within a single decade. It became one of the most successful mammal recovery programs in history.

## Trophic Functions

An essential component of predator–prey models—regardless of which of the above examples we consider—is the _trophic function_. This function describes the effect of a single predator on a prey population. It expresses the rate at which one predator slows the growth of the prey population. If we let $x$ be the size of the prey population and $y$ the rate at which one predator slows the prey's growth (i.e., the amount of prey caught by one predator per unit of time), then this relationship can be written mathematically as: $$y=f(x).$$ 
We will try to identify some natural assumptions that any trophic function should meet. Then we will attempt to find a suitable general form of such a function.

> **Exercise 1.** The assumptions about how a predator affects its prey are reflected in the properties that the trophic function must satisfy.
> 
> 1. A predator in an environment with little food will also catch little prey. More prey means easier access and therefore a greater catch.
> 1. Without food, the predator cannot catch anything. If there is no prey available, the amount of prey caught per unit time is zero.
> 1. Predators consume food only up to a certain saturation point. If prey is overly abundant, a predator will not catch more per unit time than its maximum capacity.
> 
> Express these statements using the mathematical terminology used to describe functions. What function properties correspond to each point above?

\iffalse

_Solution._

1. The function $y=f(x)$ is increasing.

2. The function $y=f(x)$ goes through the origin, i.e., $f(0)=0$.

3. The function $y=f(x)$ is bounded above. Since the function is increasing and 
is bounded above, its graph has a horizontal asymptote as $x$ approaches infinity.

\fi


## Holling Type II Trophic Function

The trophic function expresses how much prey a single predator consumes per unit time, given the size of the prey population. Therefore, the function must be defined for non-negative values only, and its outputs must also be non-negative (this follows from points 1 and 2 in the previous exercise). 
In the previous section, we established that the trophic function should pass through the origin and grow toward a horizontal asymptote—that is, the function should increase but be bounded above. These properties cannot be met by a linear function, so we turn to the simplest nonlinear case: an inverse proportionality.

![On the left, two typical trophic functions, called Holling's functions. The growth rate of the function
of type II slows down. The type III function grows slowly at first, accelerates and then slows down again. On the right, the type II function as part of
transformed graph of inverse proportionality. (own figure)](2.svg)

> **Exercise 2.** Start with the graph of the function $y=\frac 1x$ and apply the following transformations:
>
> 1. Scale the graph vertically by a factor of $k$. This will not change the function’s monotonicity or the position of its horizontal asymptote, but it will adjust the growth rate.
> 1. Flip the graph around the horizontal axis and shift it upward by $S$. This transformation makes the function increasing for positive $x$, and it will approach the asymptote $S$ as $x$ increases.
> 1. After these transformations, the graph has a vertical asymptote at zero and
> one intersection with the horizontal axis to the right of the origin. Move the graph
> to the left so that the vertical asymptote is to the left of the vertical axis and
> the intersection with the $x$-axis is shifted to the origin.

\iffalse

_Solution._ 

1. The function obtained by vertically scaling $y=\frac{1}{x}$ by a factor of $k$ is: $$y=\frac{k}{x}.$$

2. The inversion is achieved by multiplying the function by a factor of $-1$ and the shift is achieved by
by adding the value of $S$. These adjustments give the function $$y=S-\frac{k}{x}.$$

3. The shift to the left by $b$ is achieved by substituting the expression $x+b$ for $x$. This gives us
the function $$y=S-\frac{k}{x+b}.$$ When converted to the common denominator the function takes the form 
$$y=\frac{Sx+Sb}{x+b}-\frac{k}{x+b}=\frac{Sx + (Sb-k)}{x+b}.$$ To ensure $f(0)=0$, we must have: $$Sb-k=0$$. This condition shows that the three constants are not independent,
but there is a relationship between them.

\fi

*Note.* In the previous exercise, we derived the general form of one of the basic trophic functions. It is an increasing function that starts at the origin and gradually grows toward a horizontal asymptote. The growth rate slows down over time. Such a function is called the _Holling Type II function. It is commonly written in the form: $$f(x)=\frac {Sx}{x+b} (1),\tag{1}$$
where $S$ is the saturation level and $b$ is a constant whose meaning will be explained in the next exercise.

> **Exercise 3.** Show that when the prey population size is equal to $b$, the value of the trophic function (1) is equal to half of the saturation level.

\iffalse

_Solution._ By directly substituting $x=b$ into (1), we get
$$f(b)=\frac{Sb}{b+b}=\frac {Sb}{2b}=\frac S2.$$ 
This proves the statement.

\fi     

The following exercise illustrates the reverse process, where from a trophic function in form
(1) we will derive a form that reveals how it can be obtained through successive transformations of the function $y=\frac {1}{x}$.


> **Exercise 4.** Rewrite the function $$y=\frac{6x}{x+2}$$ into the basic form, so that the function can be seen as a result of successive transformations of the graph of $y=\frac{1}{x}$.

\iffalse

_Solution._ To solve this, we cleverly rewrite the fraction. In the numerator, we create a multiple of the denominator, split the expression into two fractions, and simplify:

$$\frac {6x}{x+2} = \frac {6(x+2)-12}{x+2}=\frac {6(x+2)}{x+2}-\frac {12}{x+2}=6-12\frac 1{x+2}$$

This calculation shows that the graph of the given function is obtained by scaling
the graph of the function $y=\frac{1}{x}$ vertically by a factor of 12, by inverting it around the horizontal
axis, shifting it 6 units upward and 2 units to the left.

The same result could also be obtained by performing polynomial division of the numerator by the denominator.

\fi

> **Exercise 5.** Construct a trophic function, given that the rate of food consumption at predator saturation is $6$, and that the consumption rate is half of that when the prey population is $210$.

\iffalse

*Solution.* From the note before Exercise 3, we know the general form of the trophic function is:
$$
y=\frac{Sx}{x+b},
$$
where $S$ is the saturation value of the predator, so we substitute $S=6$:
$$
y=\frac{6x}{x+b}.
$$
We can tell the value of the parameter $b$ straight away based on the result of Exercise 3, but we can also quickly compute it from the second condition in the problem statement. We know that
$$
3=\frac{6\cdot 210}{210+b}
$$
and from there we get $b=210$. So the final form of the function is
$$
y=\frac{6x}{x+210}.
$$


\fi

## References

### Literature


* Wikipedia, <https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations> March 3, 2024
* R Mařík, Dynamické modely populací (in Czech), <https://robert-marik.github.io/dmp/uvod.html>, March 3, 2024
* D. Ludwig, D.D. Jones, C.S. Holling: Qualitative analysis of insect outbreak systems: the spruce budworm and forest, Journal of Animal Ecology 47(1): 315–332, February 1978.

### Image Sources

* <https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations#/media/File:Lotka_Volterra_dynamics.svg>
* <https://www.npr.org/sections/thetwo-way/2016/08/11/489695842/once-nearly-extinct-california-island-foxes-no-longer-endangered> Kevork Djansezian/AP 
