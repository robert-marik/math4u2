---
keywords:
- statistika
- interpretace dat
- korelace
- kauzalita
is_finished: False
---

# Chybná interpretace dat/Když špatná interpretace dat kazí lidské životy/Figures don’t lie, but liars figure

Věděli jste, že všichni lidé, kteří se dožijí důchodu umřou? Platí tedy že důchody zabíjí? 

Statistiky jsou přesvědčivé. Lidé, organizace a celé země činí některá důležitá rozhodnutí na základě statistických údajů. Je tu ale jeden problém. Každý statistický soubor v sobě může mít něco skrytého, něco, co může výsledky obrátit vzhůru nohama.

Jedna studie ve Spojeném království zdánlivě ukazovala, že kuřáci mají po dobu dvaceti let vyšší míru přežití než nekuřáci. Rozdělení účastníků do věkových skupin ale ukázalo, že nekuřáci byli v průměru výrazně starší, a proto u nich byla během výzkumu větší pravděpodobnost úmrtí. Ve skutečnosti tedy žili déle. V tomto případě byly věkové skupiny matoucí proměnnou a jsou nezbytné pro správnou interpretaci dat.

Údaje můžeme seskupovat a rozdělovat různými způsoby, které ale můžou být zádějící.

Jediné, co můžeme pro správnou interpretaci dat udělat, je pečlivě prostudovat skutečné situace, které statistiky popisují, a zvážit, zda tu mohou být matoucí proměnné. V opačném případě zůstaneme zranitelní vůči těm, kteří by data používali k manipulaci s ostatními a prosazování svých vlastních záměrů a cílů.

## Korelace versus kauzalita

Korelace vypovídá o tom, že jsou dvě náhodné proměnné ve vzájemném vztahu. 
To znamená, že se dva jevy vyskytují spolu, ale nemusí být nutně jeden způbený druhým. 
Například umírají lidé, kteří dýchají kyslík. 

Kauzalita znamená, že souvislost je příčinná. Jeden jev je tedy příčinou druhého. 
Například máme studie, že už třicet minut pohybu střední intenzity denně snižuje riziko cukrovky o 30 %.

Korelace tedy neimplikuje kauzalitu. To, co spolu souvisí, nemusí být způsobeno jedno od druhého.
Rádi si z dat kolem nás tvoříme příběhy a vysvětlujeme si je. 
A hlavní způsob, jak se těmto interpretačních chybám vyhnout, je znát je. 

## Simpsonův paradox

Simpsonův paradox je statistický paradox, který je ale pouze zdánlivý. 
Jde o situaci, kdy stejný soubor dat může zdánlivě ukazovat opačné trendy v závislosti na jejich seskupení. 
K tomu často dochází, když souhrnná data skrývají podmíněnou proměnnou. 
To je skrytý faktor, který výrazně ovlivňuje výsledky. Paradox je nejlépe pochopitelný na skutečných příkladech:

..dodat příklady z wikipedie (ledvinove kameny, nebo přijímačky na Berkeley)

## Sally Clarkové

V roce 1999 se v Británii odehrál děsivý případ, na který dnes justice nerada vzpomíná. 
Ukázalo se, jak lehce je možné u soudu zkreslit statistická data a k čemu to může vést.

Sally Clarková byla právnička a právní zástupkyně narozená v roce 1964. 
V roce 1990 se provdala za svého kolegu, advokáta Steva Clarka, a v roce 1996 se jí narodilo první dítě. 
V následujících dvou letech se jí narodily dvě děti. Obě zemřely spontánně, bez reálného důvodu, do 8 týdnů po narození.

Během několika týdnů byla Clarková postavena před soud za vraždu svých dvou kojenců.

Obžaloba Clarkovou obvinila na základě pravděpodobnosti. 
Jako soudního "znalce" přivedli známého pediatra a profesora Roye Meadowa z Leedsu, 
který předložil jednoduchý argument, aby prokázal, že Clarková své děti skutečně zavraždila:

Z nemocničních záznamů vyplývá, že poměr úmrtí na SIDS u narozených dětí v bohatých nekuřáckých rodinách je přibližně stejný a to $1/8500$. 
Šance, že obě děti zemřou na SIDS, je pak $1/8500∗1/8500=1/73000000$

Pravděpodobnost že je Sally Clarková nevinná, je tedy 1 ku 73 milionům.
Vzhledem k této zdánlivě ohromující pravděpodobnosti porota usoudila, 
že nemá jinou možnost než Clarkovou v listopadu 1999 odsoudit. 

Renomovaný profesor-pediatr Meadow se dopustil ve svých výpočtech dvou ohromně jednoduchých chyb. 

> **Úloha 1.** Dokážete přijít alespoň na jednu chybu, kterou udělal?

*Řešení.* Jednou z chyb, kterou profesor Meadow, udělal, 
je to že považoval obě úmrtí za dvě nezávislé události, 
takže pravděpodobnost obou událostí vypočítal jako součin jejich pravděpodobností.

Takto můžeme postupovat u pravděpodobností událostí, 
kde výsledek jedné z nich nemá žádný vliv na výsledek druhé. 
Například pravděpodobnost, že při hodu mincí hodím dvě hlavy za sebou, 
je $1/2∗1/2=1/4$, protože výsledek prvního hodu nemá žádný vliv na hod druhý.

Úmrtí na SIDS jsou však často způsobena faktory prostředí nebo genetickými faktory, které jsou do značné míry společné pro dvě děti stejné matky. Jinými slovy, je velmi nepravděpodobné, že by tyto dvě události byly nezávislé.

Může být pravda, že existuje šance 1:8500, 
že náhodné dítě z bohaté britské rodiny zemře na SIDS.
Šance, že sourozenec oběti SIDS zemře také na SIDS, už ale nemůže být 1:8500, 
protože sourozenec sdílí mnoho společných rizikových faktorů.

## Podmíněná pravděpodobnost

Ve statistice máme pro danou událost, kterou chceme měřit jako pravděpodobnost události (např. úmrtí kojence na SIDS), dva termíny, které ji popisují:

Matematicky zapíšeme, že pravděpodobnost události $E$ je $P(E)$  
a pravděpodobnost události $E$ v případě že nastane událost $I$ jako  $P(E|I)$.
  
Zde je $I$ předběžná pravděpodobnost, že první dítě zemře na SIDS, $1$ ku $8500$. 
Posteriorní pravděpodobnost že zemře druhé dítě na SIDS vzhledem k tomu, 
že zemřel tímto způsobem i sourozenec je mnohem vyšší. 
Často totiž existují environmentální či genetické faktory, které tato úmrtí spojují.

Toto chybné použití nezávislosti jasně ukazuje, 
že údaj $1$ ku $73$ milionům je chybný. 
Meadowův argument se stále může zdát poměrně přesvědčivý.  
Stále se zdá, že existuje poměrně vysoká pravděpodobnost, 
že Sally Clarková udělala něco špatně.

Zde se objevuje druhá, jemnější chyba: záměna podmiňovacího způsobu.

Meadow vypočítal pravděpodobnost úmrtí dvou dětí za předpokladu 
že je matka nevinná. Poté dospěl k závěru, že tato pravděpodobnost je tak nízká,
že Sally Clarková musí být vina.

Meadow se však spletl v jedné klíčové věci. 
Vzhledem k důkazům (dvě děti jsou mrtvé) existují pouze dvě možnosti:

Ano, pravděpodobnost, že dva synové matce náhodně zemřou, 
za předpokladu že je matka nevinná, je velmi nízká.

Ale alternativou je, že matka je vrah. 
A šance, že by matka zavraždila obě své děti, je také velmi nízká.

Můžeme definovat dvě události:

D: událost, že dvě nemluvňata zemřou (z jakékoli příčiny).
I: událost, že matka je nevinná z vraždy.
 
Meadow tvrdí, že $P(D|I)=1/73000000$

Prozatím to berme jako pravdu.

To, co by měla porota ve skutečnosti zkoumat, je, 
zda je matka vzhledem k důkazům 
(dvě nemluvňata, která zemřela z jakékoli příčiny) nevinná; 
to znamená, že by měla zvážit pravděpodobnost $P(I|D)$.
 
S použitím Bayesova zákona platí, že  
$P(I|D)=\frac{P(D|I)∗P(I)}{P(D).}$
 
Je zřejmé, že, $P(I)$ je poměrně vysoká. Pravděpodobnost, že matka náhodně zavraždí své dvě děti, je poměrně malá, takže pravděpodobnost, že je nevinná, se blíží $1$.

Navíc $P(D)$ je poměrně nízká. Pravděpodobnost, že dvě děti náhodně zemřou z jakékoli příčiny, je malá, takže toto číslo se blíží nule.
Pro naše účely předpokládejme, že $P(I)=1$. Mohli bychom z toho udělat $0,99999$ 
nebo jakoukoli jinou skutečnou šanci, že matka své dvě děti náhodně nezabila.
Nyní odhadněme, jaká je  $P(D)$. Podle úřadu vlády Spojeného království 
úmrtnost dětí mladších pěti let přibližně $7$ na $100 000$. 
Extrapolací, $P(D)$ je $70$ z $1 000 000$.

Podle Bayesova zákona platí, že  
$P(I|D)=\frac{1/73000000}{70/1000000}=1/73000000∗1000000/70=70/73.$

Je zřejmé, že tato čísla mají určité nedostatky. Již jsme zjistili, že údaj 1 ku 73 milionům je chybný. Pointa však zůstává v platnosti - správným vyjádřením podmíněných pravděpodobností je skutečná vypočtená šance Clarkovy neviny mnohem vyšší.

Sally Clark byla nakonec osvobozena, ale po propuštění na základě odvolání v roce 2003 upadla do depresí a v březnu 2007 zemřela doma na otravu alkoholem.

Tato událost je připomínkou toho, 
jak snadno se můžeme nechat oklamat statistikami "zdravého rozumu". 
Ve skutečnosti se jedná o chybu, kterou použila obžaloba, 
když předpokládala rovnost $P(B|A)=P(A|B)$ pro dvě události A a B.
Tato chyba je tak běžná, že ji mnozí statistici označují jako "chybu žalobce".

V tomto případě se tímto jednoduchým statistickým trikem nechala oklamat celá porota.

Meadowova výpověď o tom, jak je takový souběh událostí vysoce nepravděpodobný, zapříčinil její odsouzení k doživotí za mřížemi – navzdory tomu, 
že nebyla prokázána žádná souvislost mezi chováním matky a úmrtími dětí!

O něco později se do případu vložila Royal Statistical Society, 
tedy prominentní britská statistická společnost. 
Opakovaně předkládala soudu důkazy o nepodloženosti Meadowových výpočtů, 
a výrazně se tak podílela na přezkoumání celého případu. 
I díky nově nalezeným důkazům o infekci jednoho ze Sallyiných synů, 
což s jeho smrtí nejspíše souviselo, 
se nakonec nevinná žena po několika letech za mřížemi dostala ven. 
Jednalo se o velké vítězství rozumu a statistiky.
V důsledku bylo přehodnoceno i několik dalších případů, 
v nichž se Meadow výrazně účastnil.




Literatura:

https://www.ted.com/talks/mark_liddell_how_statistics_can_be_misleading/transcript?language=cs
