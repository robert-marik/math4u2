---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- postupnosti a rady
- pravdepodobnosť
- očakávaná hodnota
- geometrická postupnosť
is_finished: true
---

# Ktorý žreb je výhodný?

Veľmi často sa v živote dostávame do situácií, kde hrajú úlohu náhoda a pravdepodobnosť. Predstavte si, že stojíte pred voľbou medzi niekoľkými možnosťami a to napríklad pri výbere žrebu alebo investície do projektu. Každá voľba má svoje riziká a potenciálne odmeny, otázkou však je, ako zistiť, ktorá z nich je najvýhodnejšia? Práve tu vstupuje do hry tzv. očakávaná hodnota.
Očakávaná hodnota nám hovorí, aký výsledok môžeme v priemere očakávať, keď sa rozhodneme pre danú možnosť. Pomáha nám lepšie odhadnúť, čo sa v dlhodobom horizonte oplatí. Nejde o presnú predpoveď, ale o nástroj, ktorý nám umožňuje lepšie porozumieť riziku a odmenám. Platí to ako v jednoduchých hrách, tak v reálnych životných rozhodnutiach.
Uvažujme napríklad dva žreby:

Žreb A: Stojí 10 Kč a s pravdepodobnosťou $0{,}1$ vyhráme 100 Kč, inak nevyhráme nič.

Žreb B: Stojí 10 Kč a s pravdepodobnosťou $0{,}2$ vyhráme 60 Kč, inak nevyhráme nič.

Pri žrebe A očakávame, že keď kúpime 10 žrebov, tak jeden z nich vyhrá 100 Kč a deväť nič. Môžeme teda očakávať, že každý žreb nám v priemere prinesie 10 Kč.
Podobne aj pri žrebe B očakávame, že keď kúpime 10 žrebov, tak dva z nich vyhrájú 60 Kč a osem nič. Môžeme teda očakávať, že každý žreb nám v priemere prinesie 12 Kč.
Vidíme teda, že žreb B je výhodnejší.

## Očakávaná hodnota

Práve vypočítaná priemerná výhra sa označuje ako *očakávaná hodnota* (alebo tiež *stredná hodnota*).

Všeobecne môžeme povedať, že pre náhodnú veličinu $X$, ktorá nadobúda konečne veľa hodnôt $x_1,\,\dots,\,x_k$ s pravdepodobnosťami $p_1,\,\dots,\,p_k$ vypočítame jej očakávanú hodnotu
$$
EV=\sum_{i=1}^k x_ip_i\,.
$$

## Ktorý žreb je najlepší? 

Pozrime sa na tri žreby. Čiernu perlu v hodnote 50 Kč, Čiernu perlu v hodnote 100 Kč a žreb Rentier v hodnote 50 Kč.
Štruktúra výhier pre žreb Čierna perla v hodnote 50 Kč, ktorých je celkom vydaných 13 000 00013\,000\,000
 $13\,000\,000$ kusov, vyzerá nasledovne.

| Výška výhry na žrebe (v Kč) | Počet výherných žrebov | 
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

Podobne vyzerá aj štruktúra výhier pre žreb Čierna perla v hodnote 100 Kč, ktorých je vydaných celkom $15\,000\,000$ kusov.

| Výška výhry na žrebe (v Kč) | Počet výherných žrebov | 
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

Do tretice sa pozrieme na žreb Rentier, ktorých je vydaných $8\,000\,000$ 
kusov a výhry sú dané tabuľkou nižšie.

| Výška výhry na žrebe (v Kč) | Počet výherných žrebov | 
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

Pričom hlavná výhra $3\,500\,000\,\text{Kč}$ sa nevypláca naraz, ale 
skladá sa z okamžitej výhry $500\,000\,\text{Kč}$ a renty $50\,000\,\text{Kč}$ 
počas 5 rokov.

> **Úloha 1.** Pri ktorom z uvedených žrebov je najväčšia šanca na výhru?

\iffalse

*Riešenie.* V prípade žrebu Čierna perla za 50 Kč je z celkového počtu $13\,000\,000$ 
kusov výherných $3\,492\,619$ žrebov (pozri posledný riadok tabuľky). 
Pravdepodobnosť, že náhodne vybraný žreb je výherný môžeme vypočítať ako
$$
P(V_1)=\frac{3\,492\,619}{13\,000\,000}=0{,}268633\,.
$$
Môžeme teda povedať, že pri kúpe jedného žrebu máme šancu na výhru zhruba $26{,}86\,\%$. 
Úpravou zlomku môžeme tiež zistiť, že šanca na získanie výherného žrebu je $1\colon 3{,}72$.

Podobne v prípade žrebu Čierna perla v hodnote 100 Kč dostaneme
$$
P(V_2)=\frac{4\,224\,318}{15\,000\,000}=0{,}2816212\,.
$$
Znamená to, že šanca na výhru je $28{,}16\,\%$ alebo tiež $1\colon 3{,}55$.

V prípade žrebu Rentiér potom máme
$$
P(V_3)=\frac{2\,072\,049}{8\,000\,000}=0{,}259\,,
$$
teda šanca na výhru je $25{,}9\,\%$ alebo $1\colon 3{,}86$.

Porovnaním jednotlivých pravdepodobností výhry vidíme, že najväčšiu šancu na víťazný žreb máme pri kúpe žrebu Čierna perla v hodnote 100 Kč.
V tejto súvislosti môžeme ešte uvážiť, čomu hovoríme výherný žreb. Za výherný žreb je väčšinou považovaný taký žreb, vďaka ktorému získame ľubovoľnú finančnú sumu. Pokiaľ sme ale za žreb zaplatili 100 Kč, tak výhra 100 Kč nám ju zaplatí späť, ale nič sme vlastne nevyhrali. Aby sme teda získali pravdepodobnosť, že skutočne vyhráme, tak nebudeme v našich tabuľkách výhier uvažovať prvý riadok. Dostaneme tak upravené pravdepodobnosti výhier 
$$
\begin{aligned}
P(V_1)&=\frac{1\,672\,619}{13\,000\,000}=0{,}128633\\
P(V_2)&=\frac{1\,824\,318}{15\,000\,000}=0{,}1216212\\
P(V_3)&=\frac{1\,112\,049}{8\,000\,000}=0{,}139\,.
\end{aligned}
$$
Vidíme, že pokiaľ uvážime žreby, ktoré naozaj vyhrájú čiastku väčšiu než ich cena, tak najlepším je zrazu žreb Rentier, kde je šanca na výhru $13{,}9\,\%$.

\fi

> **Úloha 2.** Aká je očakávaná hodnota každého žrebu?

\iffalse

*Riešenie.* Pre výpočet očakávanej hodnoty podľa definície potrebujeme poznať pravdepodobnosti jednotlivých výhier:

| Výška výhry na žreb (v Kč) | Pravdepodobnosť danej výhry | 
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

Ak označíme hodnoty jednotlivých výhier $n_1$ až $n_{13}$ a ich zodpovedajúce pravdepodobnosti $p_1$ až $p_{13}$, dostaneme očakávanú hodnotu $EV(L_1)$ žrebu Čierna perla
$$
EV(L_1)=\sum_{k=1}^{13}n_kp_k=29\,\text{Kč}.
$$

Vzhľadom k tomu, ako sa jednotlivé pravdepodobnosti počítajú, môžeme očakávanú hodnotu spočítať tiež takto
$$
EV(L_1)=\frac{1}{13\,000\,000}\left(50\cdot 1\,820\,000+100\cdot1\,040\,000+ \cdots + 100\,000\cdot14+1\,500\,000\cdot6 \right).
$$

Tento prístup je výhodnejší, keďže nemusíme pri tabuľke výhier počítať pravdepodobnosť každej možnej výhry. Pre žreb Čierna perla v hodnote 100 Kč potom dostaneme očakávanú hodnotu $EV(L_2)$:
$$
EV(L_2)=\frac{1}{15\,000\,000}\left(100\cdot 2\,400\,000+200\cdot 900\,000+ \cdots + 200\,000\cdot 13+5\,000\,000 \cdot 6 \right)=64\,\text{Kč}.
$$
A pre žreb Rentiér dostávame očakávanú hodnotu $EV(L_3)$:
$$
EV(L_3)=\frac{1}{8\,000\,000}\left(50\cdot 960\,000+100\cdot 720\,000+ \cdots + 100\,000\cdot 6+3\,500\,000\cdot 3 \right)=29{,}25\,\text{Kč}.
$$

*Poznámka.* 

* Zvyčajte je pri lotérií uvedená celková čiastka na výhry a počet žrebov a očakávaná hodnota je potom samozrejme podiel daných dvoch čísel.
* Uvedené hodnoty sú v skutočnosti mnohokrát ešte nižšie, keďže sa z výhier často platí daň.
* Rovnaký prístup sa dá použiť aj pre výpočet očakávanej hodnoty balenia rôznych kartových zberateľských hier (Pokémon, Lorcana, Magic the Gathering alebo športové kartičky).

\fi

> **Úloha 3.** V predchádzajúcich príkladoch sme uvažovali hlavnú výhru žrebu Rentier v hodnote $3\,500\,000\,\text{Kč}$. 
Je to však naozaj skutočná hodnota výhry, vzhľadom k tomu, že nie je vyplatená naraz? 

\iffalse

*Riešenie.* Jednoduchá odpoveď je, že nie je. 

Je nutné si uvedomiť, že pokiaľ by sme peniaze dostali ihneď, tak by sme ich mohli uložiť alebo nejako investovať. Pre zistenie, aká je hodnota 50 000 Kč, ktoré dostaneme za mesiac sa dá využiť koncept, ktorému sa hovorí *súčasná hodnota* (*present value*). Pri jej použití si kladieme otázku, koľko peňazí by sme museli dnes investovať, aby sme za mesiac dostali požadovanú čiastku (napr. uvažovaných 50 000 Kč). A táto hodnota je potom tá tzv. súčasná hodnota.

Dajme tomu, že by sme danú čiastku $P_0$ mohli uložiť na mesiac s mesačnou úrokovou sadzbou $0{,}5\,\%$. Za mesiac by sme potom dostali čiastku $P_1=1{,}005P_0$. Súčasná hodnota je potom práve suma $P_0$, ktorú musíme uložit tak, aby $P_1$ bolo $50\,000\,\text{Kč}$, t. j. 
$$
P_0=\frac{50\,000}{1{,}005}=49\,751{,}24\,\text{Kč}.
$$

Pokiaľ by sme chceli určiť súčasnú hodnotu čiastky, ktorú získame za $n$ mesiacov, uvažujeme, že danú čiastku necháme uloženú po celý čas. Využijeme potom zložené úrokovanie a dostaneme súčasnú hodnotu $P_n$, ktorú získame za $n$ mesiacov ako
$$
P_0=\frac{P_n}{1{,}005^n}.
$$
Pripomeňme, že hlavná výhra žrebu Rentier sa skladá z čiastky $500\,000\,\text{Kč}$ a tridsiatich mesačných platieb vo výške $50\,000\,\text{Kč}$. Ak uvážime  mesačnú úrokovú mieru vo výške $0{,}5\,\%$, je súčasná hodnota $PV$ týchto splátok
$$
PV=\frac{50\,000}{1{,}005}+\frac{50\,000}{1{,}005^2}+\cdots+\frac{50\,000}{1{,}005^{29}}+\frac{50\,000}{1{,}005^{30}}\,.
$$
Môžeme si všimnúť, že sa jedná o súčet členov geometrickej postupnosti a výpočet si tak značne skrátiť
$$
PV=\frac{50\,000}{1{,}005}\cdot\frac{1-\left(\frac{1}{1{,}005}\right)^{30}}{1-\frac{1}{1{,}005}}=1\,389\,702{,}7\,\text{Kč}.
$$
Môžeme teda uvažovať, že hodnota hlavnej výhry je iba $1\,889\,702{,}7\,\text{Kč}$.

Ak použijeme túto čiastku pre výpočet očakávanej hodnoty žrebu Rentier, dostaneme
$$
EV(L_3)=28{,}65\,\text{Kč}.
$$

*Poznámka.* Predchádzajúce úvahy boli ešte značne zjednodušené, keďže nezahŕňali napríklad vplyv inflácie

\fi

> **Úloha 4.** Na základe výsledkov predchádzajúcich úloh vyberte žreb, ktorý je najlepší.

\iffalse

*Riešenie.* Na základe predchádzajúcich úloh môžeme žreby porovnať podľa rôznych kritérií:

1. Podľa pravdepodobnosti výhry.

Podľa tohto kritéria je najlepší žreb Čierna perla v hodnote 100 Kč, ktorý má šancu na výhru $28{,}16\,\%$, potom Čierna perla v hodnote 50 Kč so šancou $26{,}86\,\%$ a najhorší je žreb Rentier so šancou $25{,}9\,\%$.

2. Podľa pravdepodobnosti skutočnej výhry.

Ak uvážime skôr šancu, že vyhráme viac než sme zaplatili, dostaneme nasledovné iné poradie. Najlepší je žreb Rentier so šancou na výhru $13{,}9\,\%$, potom žreb Čierna perla v hodnote 50 Kč so šancou $12{,}86\,\%$ a posledná je Čierna perla v hodnote 100 Kč so šancou na výhru $12{,}16\,\%$.

3. Podľa očakávanej hodnoty.

Očakávaná hodnota žrebu Čierna perla v hodnote 50 Kč je 29 Kč. Na jednom žrebe teda priemerne stratíme 21 Kč. Podobne očakávaná hodnota žrebu Čierna perla v hodnote 100 Kč je 64 Kč, priemerne teda stratíme 36 Kč. A v prípade žrebu Rentier za 50 Kč je upravená očakávaná hodnota 28,65 Kč a teda priemerne stratíme 21,35 Kč.

Môžeme teda povedať, že (očakávateľne) sú všetky žreby stratové. Za najlepší však môžeme považovať žreb Čierna perla v hodnote 50 Kč, ktorý je stratový najmenej.

\fi

## Literatúra

* Novák, J., *Střední hodnota v úlohách na střední škole.* Učitel matematiky, 2, JČMF, 2024. 
* *Herní plán loterií SAZKA* [online] Dostupné z https://static.sazka.cz/kentico-media/sazka/media/content/herni-plany/hp-sazka-od-17-7-24-komplet-sazka.pdf, [cit. 1. 9. 2024]
