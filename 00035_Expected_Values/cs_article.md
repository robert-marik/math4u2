---
keywords:
- posloupnosti a řady
- pravděpodobnost
- očekávaná hodnota
- geometrická posloupnost
is_finished: true
difficulty: 2
time: 30
---

# Který los je výhodný?

Velmi často se v životě ocitáme v situacích, kde hrají roli náhoda a pravděpodobnost. Představte si, že stojíte před volbou mezi několika možnostmi, třeba při výběru losu nebo investici do projektu. Každá volba má svá rizika a potenciální odměny, otázkou ale je jak zjistit, která z nich je nejvýhodnější? Právě zde vstupuje do hry tzv. *očekávaná hodnota*.

Očekávaná hodnota nám říká, jaký výsledek můžeme v průměru očekávat, když se rozhodneme pro danou možnost. Pomáhá nám lépe odhadnout, co se v dlouhodobém horizontu vyplatí. Nejde o přesnou předpověď, ale o nástroj, který nám umožňuje lépe porozumět riziku a odměnám, a to jak v jednoduchých hrách, tak v reálných životních rozhodnutích.

Uvažme například dva losy:

* Los A: Stojí 10 Kč a s pravděpodobností $0{,}1$ vyhrajeme 100 Kč, jinak nevyhrajeme nic.
* Los B: Stojí 10 Kč a s pravděpodobností $0{,}2$ vyhrajeme 60 Kč, jinak nevyhrajeme nic.

U losu A očekáváme, že když koupíme 10 losů, tak jeden z nich vyhraje 100 Kč a devět nic. Můžeme tedy očekávat, že každý los nám v průměru přinese 10 Kč.

Podobně, u losu B očekáváme, že když koupíme 10 losů, tak dva z nich vyhrají 60 Kč a osm nic. Můžeme tedy očekávat, že každý los nám v průměru přinese 12 Kč.

Vidíme tedy, že los B je výhodnější.

## Očekávaná hodnota

Právě vypočtená průměrná výhra se označuje jako *očekávaná hodnota* (nebo také *střední hodnota*).

Obecně můžeme říci, že pro náhodnou veličinu $X$, která nabývá konečně mnoha hodnot $x_1,\,\dots,\,x_k$ s pravděpodobnostmi $p_1,\,\dots,\,p_k$ vypočteme její očekávanou hodnotu
$$
EV=\sum_{i=1}^k x_ip_i\,.
$$

## Který los je nejlepší? 

Podívejme se na tři losy. Černou perlu v hodnotě 50 Kč, 
Černou perlu v hodnotě 100 Kč a los Rentiér v hodnotě 50 Kč. 

Struktura výher pro los Černá perla v hodnotě 50 Kč, 
kterých je celkem vydáno $13\,000\,000$ kusů, vypadá 
následovně. 

| Výše výhry na losu (v Kč) | Počet výherních losů | 
| ------------- | ------------- |  
| $50$  | $1\,820\,000$  |
| $100$  | $1\,040\,000$  |
| $150$  | $260\,000$  |
| $200$  | $130\,000$  |
| $300$  | $130\,000$  |
| $500$  | $104\,000$  |
| $1\,000$  | $5\,550$  |
| $2\,000$  | $2\,300$  |
| $4\,000$  | $480$  |
| $10\,000$  | $185$  |
| $20\,000$  | $84$  |
| $100\,000$  | $14$  |
| $1\,500\,000$  | $6$  |
| Celkem | $3\,492\,619$  |

Podobně vypadá i struktura výher pro los Černá perla v 
hodnotě 100 Kč, kterých je vydáno celkem $15\,000\,000$ 
kusů.

| Výše výhry na losu (v Kč) | Počet výherních losů | 
| ------------- | ------------- |  
| $100$  | $2\,400\,000$  |
| $200$  | $900\,000$  |
| $300$  | $450\,000$  |
| $500$  | $150\,000$  |
| $600$  | $150\,000$  |
| $900$  | $75\,000$  |
| $1\,000$  | $75\,000$  |
| $1\,500$  | $20\,000$  |
| $6\,000$  | $4\,000$  |
| $20\,000$  | $185$  |
| $50\,000$  | $84$  |
| $100\,000$  | $30$  |
| $200\,000$  | $13$  |
| $5\,000\,000$  | $6$  |
| Celkem | $4\,224\,318$  |

Do třetice se podíváme na los Rentiér, kterých je vydáno $8\,000\,000$ kusů 
a výhry jsou dány tabulkou níže.

| Výše výhry na losu (v Kč) | Počet výherních losů | 
| ------------- | ------------- |  
| $50$  | $960\,000$  |
| $100$  | $720\,000$  |
| $150$  | $160\,000$  |
| $250$  | $160\,000$  |
| $500$  | $70\,000$  |
| $1\,000$  | $1\,300$  |
| $2\,000$  | $500$  |
| $5\,000$  | $160$  |
| $10\,000$  | $80$  |
| $100\,000$  | $6$  |
| $3\,500\,000$  | $3$  |
| Celkem | $2\,072\,049$  |

Přičemž hlavní výhra $3\,500\,000\,\text{Kč}$  není vyplacena najednou, ale 
skládá se z okamžité výhry $500\,000\,\text{Kč}$ a renty $50\,000\,\text{Kč}$ 
po dobu 5 let.

> **Úloha 1.** U kterého z uvedených losů je největší šance, že 
> vyhrajeme?

\iffalse

*Řešení.* V případě losu Černá perla za 50 Kč je z celkového počtu $13\,000\,000$ 
kusů výherních $3\,492\,619$ losů (viz poslední řádek tabulky). 
Pravděpodobnost, že náhodně vybraný los je výherní můžeme vypočítat jako
$$
P(V_1)=\frac{3\,492\,619}{13\,000\,000}=0{,}268633\,.
$$
Můžeme tedy říci, že při koupi jednoho losu máme šanci na výhru zhruba $26{,}86\,\%$. 
Úpravou zlomku můžeme též zjistit, že šance na získání výherního losu je $1\colon 3{,}72$.

Podobně v případě losu Černá perla v hodnotě 100 Kč dostaneme
$$
P(V_2)=\frac{4\,224\,318}{15\,000\,000}=0{,}2816212\,.
$$
Tj. šance na výhru je $28{,}16\,\%$ nebo též $1\colon 3{,}55$.

V případě losu Rentiér pak máme
$$
P(V_3)=\frac{2\,072\,049}{8\,000\,000}=0{,}259\,,
$$
tedy šance na výhru je $25{,}9\,\%$ neboli $1\colon 3{,}86$.

Porovnání jednotlivých pravděpodobností výhry vidíme, že největší šanci na 
vítězný los máme při koupi losu Černá perla v hodnotě 100 Kč. 

V této souvislosti můžeme ještě uvážit, čemu říkáme výherní los. Za výherní los je 
většinou považován takový los, díky kterému získáme libovolný finanční obnos. 
Pokud jsme ale za za los zaplatili 100 Kč, tak výhra 100 Kč nám jej zaplatí zpět, ale nic jsme vlastně 
nevyhráli. Abychom tedy získali pravděpodobnost, že skutečně vyhrajeme, tak 
nebudeme v našich tabulkách výher uvažovat první řádek. Dostaneme tak upravené pravděpodobnosti výher
$$
\begin{aligned}
P(V_1)&=\frac{1\,672\,619}{13\,000\,000}=0{,}128633\\
P(V_2)&=\frac{1\,824\,318}{15\,000\,000}=0{,}1216212\\
P(V_3)&=\frac{1\,112\,049}{8\,000\,000}=0{,}139\,.
\end{aligned}
$$
Vidíme, že pokud uvážíme losy, které opravdu vyhrají částku větší než jejich cena, tak nejlepším je najednou los Rentiér, kde je šance na výhru $13{,}9\,\%$.

\fi

> **Úloha 2.** Jaká je očekávaná hodnota každého losu?

\iffalse

*Řešení.* Pro výpočet očekávané hodnoty podle definice potřebujeme znát pravděpodobnosti jednotlivých výher:

| Výše výhry na losu (v Kč) | Pravděpodobnost dané výhry | 
| ------------- | ------------- |  
| $50$  | $0{,}14$  |
| $100$  | $0{,}08$  |
| $150$  | $0{,}02$  |
| $200$  | $0{,}01$  |
| $300$  | $0{,}01$  |
| $500$  | $0{,}008$  |
| $1\,000$  | $0{,}000\,426\,9$  |
| $2\,000$  | $0{,}000\,176\,923$  |
| $4\,000$  | $0{,}000\,036\,923$  |
| $10\,000$  | $0{,}000\,014\,231$  |
| $20\,000$  | $0{,}000\,006\,461\,538$  |
| $100\,000$  | $0{,}000\,006\,461\,538$  |
| $1\,500\,000$  | $0{,}000\,000\,461\,538$  |

Označíme-li hodnoty jednotlivých výher $n_1$ až $n_{13}$ a jejich odpovídající pravděpodobnosti $p_1$ až $p_{13}$, dostaneme očekávánou hodnotu $EV(L_1)$ losu Černá perla
$$
EV(L_1)=\sum_{k=1}^{13}n_kp_k=29\,\text{Kč}.
$$

Vzhledem k tomu, jak se jednotlivé pravděpodobnosti počítají, můžeme očekávanou hodnotu spočítat též takto
$$
EV(L_1)=\frac{1}{13\,000\,000}\left(50\cdot 1\,820\,000+100\cdot1\,040\,000+ \cdots + 100\,000\cdot14+1\,500\,000\cdot6 \right).
$$

Tento přístup je výhodnější, jelikož nemusíme u tabulky výher počítat pravděpodobnost každé možné výhry. Pro los Černá perla v hodnotě 100 Kč pak dostaneme očekávanou hodnotu $EV(L_2)$:
$$
EV(L_2)=\frac{1}{15\,000\,000}\left(100\cdot 2\,400\,000+200\cdot 900\,000+ \cdots + 200\,000\cdot 13+5\,000\,000 \cdot 6 \right)=64\,\text{Kč}.
$$
A pro los Rentiér dostáváme očekávánou hodnotu $EV(L_3)$:
$$
EV(L_3)=\frac{1}{8\,000\,000}\left(50\cdot 960\,000+100\cdot 720\,000+ \cdots + 100\,000\cdot 6+3\,500\,000\cdot 3 \right)=29{,}25\,\text{Kč}.
$$

*Poznámka.* 

* Obvykle je u loterií uvedena celková částka na výhry a počet losů, očekávána hodnota je pak samozřejmě podíl těchto dvou čísel.
* Uvedené hodnoty jsou ve skutečnosti mnohdy ještě nižší, jelikož se z výher často platí daň. 
* Stejný přístup se dá použít i pro výpočet očekávané hodnoty balení různých karetních sběratelských her (Pokémon, Lorcana, Magic the Gathering nebo sportovní kartičky).

\fi

> **Úloha 3.** V předchozích příkladech jsme uvažovali 
hlavní výhru losu Rentiér v hodnotě $3\,500\,000\,\text{Kč}$. 
Je to ale opravdu skutečná hodnota výhry, vzhledem k tomu, 
že není vyplacena najednou? 

\iffalse

*Řešení.* Jednoduchá odpověď je, že není. 

Je nutné si uvědomit, že pokud bychom peníze dostali ihned, tak bychom je mohli uložit nebo nějak investovat. Pro zjištění jaká je hodnota 50 000 Kč, které dostaneme za měsíc se dá využít konceptu, kterému se říká *současná hodnota* (*present value*). Při jejím použití si klademe otázku, kolik peněz bychom museli dnes investovat, abychom za měsíc dostali požadovanou částku (např. uvažovaných 50 000 Kč). A tato hodnota je pak ta tzv. současná hodnota. 

Dejme tomu, že bychom danou částku $P_0$ mohli uložit na měsíc s měsíční úrokovou mírou $0{,}5\,\%$. Za měsíc bychom pak dostali částku $P_1=1{,}005P_0$. Současná hodnota je pak právě částka $P_0$, kterou musíme uložit tak, aby $P_1$ bylo $50\,000\,\text{Kč}$, tj. 
$$
P_0=\frac{50\,000}{1{,}005}=49\,751{,}24\,\text{Kč}.
$$

Pokud bychom chtěli určit současnou hodnotu částky, kterou obdržíme za $n$ měsíců, uvažujeme, že danou částku necháme uloženou po celou dobu. Využijeme pak složeného úročení a dostaneme současnou hodnotu $P_0$ částky $P_n$, kterou obdržíme za $n$ měsíců jako
$$
P_0=\frac{P_n}{1{,}005^n}.
$$
Připomeňme, že hlavní výhra losu Rentiér se skládá z částky $500\,000\,\text{Kč}$ a třiceti měsíčních plateb o velikosti $50\,000\,\text{Kč}$. Uvážíme-li měsíční úrokovou míru ve výši $0{,}5\,\%$, je současná hodnota $PV$ těchto splátek
$$
PV=\frac{50\,000}{1{,}005}+\frac{50\,000}{1{,}005^2}+\cdots+\frac{50\,000}{1{,}005^{29}}+\frac{50\,000}{1{,}005^{30}}\,.
$$
Můžeme si všimnout, že se jedná o součet členů geometrické posloupnosti a výpočet si tak značně zkrátit
$$
PV=\frac{50\,000}{1{,}005}\cdot\frac{1-\left(\frac{1}{1{,}005}\right)^{30}}{1-\frac{1}{1{,}005}}=1\,389\,702{,}7\,\text{Kč}.
$$
Můžeme tedy uvažovat, že hodnota hlavní výhry je pouze $1\,889\,702{,}7\,\text{Kč}$.

Použijeme-li tuto částku pro výpočet očekávané hodnoty losu Rentiér, dostaneme
$$
EV(L_3)=28{,}65\,\text{Kč}.
$$

*Poznámka.* Předchozí úvahy byly ještě značně zjednodušené, jelikož nezahrnovaly například vliv inflace.

\fi

> **Úloha 4.** Na základě výsledků předchozích úloh vyberte los, který je nejlepší.

\iffalse

*Řešení.* Na základě předchozích úloh můžeme losy porovnat dle různých kritérií:

1. Podle pravděpodobnosti výhry.

Podle tohoto kritéria je nejlepší los Černá perla v hodnotě 100 Kč, který má šanci na výhru $28{,}16\,\%$, pak Černá perla v hodnotě 50 Kč s šancí $26{,}86\,\%$ a nejhorší je los Rentiér s šancí $25{,}9\,\%$.

2. Podle pravděpodobnosti skutečné výhry.

Uvážíme-li spíše šanci, že vyhrajeme více než jsme zaplatili, dostaneme následujícíjiné pořadí. Nejlepší je los Rentiér s šancí na výhru $13{,}9\,\%$, pak los Černá perla v hodnotě 50 Kč s šancí $12{,}86\,\%$ a poslední je Černá perla v hodnotě 100 Kč s šancí na výhru $12{,}16\,\%$.

3. Podle očekávané hodnoty.

Očekávaná hodnota losu Černá perla v hodnotě 50 Kč je 29 Kč. Na jednom losu tedy průměrně ztratíme 21 Kč. Podobně očekáváná hodnota losu Černá perla v hodnotě 100 Kč je 64 Kč, průměrně tedy ztratíme 36 Kč. A v případě losu Rentiér za 50 Kč je upravená očekávaná hodnota 28,65 Kč a tedy průměrně ztratíme 21,35 Kč.

Můžeme tedy říci, že (očekávatelně) jsou všechny losy ztrátové. Za nejlepší ale můžeme považovat los Černá perla v hodnotě 50 Kč, který je ztrátový nejméně. 

\fi

## Literatura

* Novák, J., *Střední hodnota v úlohách na střední škole.* Učitel matematiky, 2, JČMF, 2024. 
* *Herní plán loterií SAZKA* [online] Dostupné z https://static.sazka.cz/kentico-media/sazka/media/content/herni-plany/hp-sazka-od-17-7-24-komplet-sazka.pdf, [cit. 1. 9. 2024]
