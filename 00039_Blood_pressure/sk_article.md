---
keywords:
- goniometria
- goniometrické funkcie
- sínus
- kosínus
- aproximácia
- krvný tlak
is_finished: false
---

# Krvný tlak 

## Goniometrické funkcie a periodické javy

Základné goniometrické funkcie sínus a kosínus sa často používajú na modelovanie svetelných, zvukových a elektromagnetických vĺn.
Dajú sa použiť aj na aproximáciu [^1] ďalších periodických javov, ako sú napríklad príliv a odliv alebo krvný tlak.
Pochopenie týchto funkcií (a ich jednotlivých častí) nám umožňuje efektívne predpovedať a analyzovať periodické javy a ich vlastnosti.
Môžeme napríklad vypočítať výšku morských vĺn alebo čas prílivu. V nasledujúcom texte sa zameriame na funkcie, ktoré aproximujú krvný tlak.

## Základné informácie o krvnom tlaku 

Srdce funguje ako pumpa, ktorá poháňa okysličenú krv do ciev celého tela, aby mu dodala potrebný kyslík a živiny.
Krvný tlak je tlak, ktorým pôsobí krv na stenu cievy, cez ktorú preteká.
Tento tlak je rôzny v rôznych častiach krvného obehu. Bežne sa krvný tlak chápe ako arteriálny (tepnový) tlak, teda tlak krvi vo veľkých tepnách.
Ak je váš krvný tlak príliš vysoký, zaťažuje vaše tepny (a srdce), čo môže viesť k srdcovému infarktu alebo mozgovej príhode.
Vysoký krvný tlak, odborne hypertenzia, sa zvyčajne nijako nepociťuje ani nepozoruje.
Nemá tendenciu spôsobovať zjavné príznaky či symptómy.
Jediný spôsob, ako zistiť hodnotu krvného tlaku, je nechať si ho zmerať.
Prvé meracie prístroje určovali krvný tlak podľa výšky stĺpca ortuti, preto sa jeho hodnota dodnes uvádza v milimetroch ortuti.
Zapisuje sa ako pomer dvoch čísel. Ak je vaša hodnota napríklad $120/80\,\text{mm}\,Hg$, krvný tlak sa číta ako $120$ na $80$.  

Vyššie číslo udáva systolický krvný tlak. Jedná sa o najvyššiu hodnotu, ktorú tlak dosiahne, keď srdce bije a vytláča krv do ciev.
Nižšie číslo je diastolický krvný tlak a je to naopak najnižšia úroveň tlaku v okamihu, keď sa srdcový sval medzi údermi uvoľňuje.
Nižšie uvedená tabuľka zobrazuje rozmedzie nízkeho, normálneho a vysokého krvného tlaku.  

![Tabuľka krevného tlaku](blood_pressure_chart_cz.png)

## Aproximácia funkcie krvného tlaku 

Pri sťahoch srdca sa krvný tlak cyklicky zvyšuje a znižuje.
Dĺžka trvania jedného srdcového tepu teda zodpovedá perióde funkcie, ktorá opisuje krvný tlak.
Každá perióda funkcie merania krvného tlaku teda zodpovedá jednému srdcovému tepu (udáva, ako dlho trvá, kým sa dokončí cyklus srdcového tepu)
Lokálne maximum funkcie predstavuje systolický tlak a lokálne minimum diastolický tlak.
Funkciu krvného tlaku môžeme približne nahradiť sínusovou alebo kosínusovou funkciou.

Všeobecný tvar funkcie sínus je
$$
f\left(x\right) = a\cdot\sin\left(bx + c\right) +d,
$$

kde $a$ je amplitúda, 
ktorá určuje, ako vysoko alebo nízko sa sínusoida pohybuje od svojej strednej hodnoty. 
Hodnota $b$ ovplyvňuje periódu funkcie (platí, že perióda je rovná $\frac{2\pi}{|b|}$.). 
Člen $c$ určuje posun v smere osy $x$ a $d$ posun ve směru osy $y$.   

> **Úloha 1.** Porovnajte nasledujúce dve funkcie $$P_1(t)=25\cdot\sin\left(\frac{7\pi}{3}t\right)+105,\quad P_2(t)=30\cdot\cos\left(2\pi t\right)+125,$$
> ktoré aproximujú krvný tlak dvoch rôznych ľudí. Premenná $t$ predstavuje čas v sekundách.
Pre každú funkciu určte periódu funkcie (dĺžku jedného srdcového tepu)
a určite tepovú frekvenciu (počet úderov srdca za minútu).

\iffalse

*Riešenie.* Periódu $p_1$ funkcie $P_1$ môžeme vypočítať ako 
$$p_1=\frac{2\pi}{\frac{7\pi}{3}}=\frac{6}{7}\,\text{sekundy}.$$ 
Keďže doba trvania jedného srdečného tepu je $\frac{6}{7}$ sekundy, tepová frekvencia $f_1$ bude 
$$
f_1=\frac{60}{\frac{6}{7}}=70\,\text{úderov za minútu}.
$$  
Rovnako pre funkciu $P_2$ bude perióda 
$$
p_2=\frac{2\pi}{2\pi}=1\,\text{sekunda}.
$$ 
Tepová frekvencia je teda $f_2=60$ úderov za minutu.
 
\fi

> **Úloha 2.**  Nakreslite grafy funkcií zo zadania prvej úlohy. Ak máte možnosť, použite vhodný softvér (napríklad program GeoGebra).
Pomocou tabuľky krvného tlaku určte, ako sú na tom príslušní ľudia s hodnotou krvného tlaku.

\iffalse

*Riešenie.* Na vykreslenie grafu funkcie bude os $x$ predstavovať čas $t$ v sekundách.
Os $y$ bude predstavovať krvný tlak $P$ v milimetroch ortuti. Jednotky na osiach zvolíme tak, aby graf vyzeral prehľadne.
Vhodná voľba je napríklad taká, že jednej jednotke na osi $x$ zodpovedá sto jednotiek na osi $y$.
V riešení na obrázku je zvolený pomer jednotiek na osiach $1:125$.
Funkcia
$$
P_1=25\cdot\sin\left(\frac{7\pi}{3}t\right)+105
$$ 
osciluje okolo hodnoty $105$, amplitúda je rovná $25$.
Lokálne maximá funkcie budú mať teda funkčnú hodnotu $105+25=130$ (systolický tlak).
Lokálne minimá funkcie budú mať funkčnú hodnotu $105-25=80$ (diastolický tlak).

Funkcia 
$$
P_2=30\cdot\cos\left(2\pi t\right)+125
$$ 
osciluje okolo hodnoty $105$, amplitúda je rovná $30$.
Lokálne maximá funkcie budú mať teda funkčnú hodnotu $125+30=155$ (systolický tlak).
Lokálne minimá funkcie budú mať funkčnú hodnotu $125-30=95$ (diastolický tlak).

![Grafy funkcií z úlohy 1](graphs_u.png)

Funkcia $P_1$ je približne funkciou tlaku $130$ na $80$, podľa tabuľky z úvodu zodpovedá hodnotám medzi normálnym a vysokým tlakom (v niektorých krajinách sa považuje za normálny tlak, v niektorých krajinách je to už spodná hranica vysokého krvného tlaku). Funkcia $P_2$ zodpovedá tlaku $155$ na $95$, tento tlak je vysoký.

\fi

Vizualizácia takýchto grafov pomáha porozumieť zmenám krvného tlaku a pochopiť ďalšie periodické javy, čo je nevyhnutné ako v matematických štúdiách, tak v praktických aplikáciách.

Vysoký krvný tlak je nebezpečný stav a hlavný rizikový faktor srdcových ochorení a mŕtvice. Zdravý životný štýl, napríklad strava s vysokým obsahom ovocia a zeleniny a nízkym obsahom sodíka, ako aj fyzická aktivita, môže pomôcť predchádzať vysokému krvnému tlaku. Vysoká hodnota z jediného merania nemusí nutne znamenať, že máte vysoký krvný tlak, pretože na krvný tlak môže počas dňa pôsobiť mnoho faktorov, napríklad teplota, doba posledného jedla alebo stres.
Vďaka tomu, že sme si funkcie $P_1$ a $P_2$ vykreslili, vidíme na prvý pohľad, aké sú medzi nimi rozdiely. Niekedy však môžu mať dve funkcie dané na prvý pohľad rôznymi predpismi ten istý graf. Spoznali by ste napríklad na prvý pohľad, že tomu tak je u nasledujúcich dvoch funkcií?

$$
y=\sin\frac{3x}{5},\qquad y=\cos\left(\frac{3x}{5}-\frac{\pi}{2}\right)
$$ 
Tieto funkcie majú rovnaký graf a veľkosť ich periódy je 
$$
\frac{2\pi}{\frac{3}{5}}=\frac{10\pi}{3}.
$$

Ale pozor, graf funkcie $y=\cos\left(\frac{3x}{5}-\frac{\pi}{2}\right)$ nie je oproti grafu funkcie 
$y=\cos\frac{3x}{5}$ posunutý v smere osi $x$ o $\frac{\pi}{2}$, 
ako by sa z predpisu funkcie na prvý pohľad mohlo zdať, ale o štvrtinu periódy tejto funkcie.
To môžeme vidieť, ak si predpis vhodne upravíme:
$$
y=\cos\left(\frac{3x}{5}-\frac{\pi}{2}\right)=\cos\left(\frac{3}{5}\left(x-\frac{5\pi}{6}\right)\right)
$$

Na porovnanie dvoch takýchto funkcií by teda bolo lepšie,
keby sme mohli jednu previesť na druhú.
Týmto sa práve bude zaoberať nasledujúca úloha.

> **Úloha 3.** Vyjadrite funkciu $P_1$ z Úlohy 1. 
> pomocou funkcie kosínus namiesto funkcie sínus. 

\iffalse

*Řešení.*  Pro funkce $\sin x$ a $\cos x$ v základním tvaru platí 
$$
\sin x=\cos\left(x-\frac{\pi}{2}\right),
$$ 
kde $\frac{\pi}{2}$ je čtvrtina periody.
Perioda funkce $P_1$ je $p_1=\frac{6}{7}$, čtvrtina periody je 
$$
\frac{p_1}{4}=\frac{6}{28}=\frac{3}{14}.
$$
Platí tedy 
$$
\sin\left(\frac{7\pi}{3}t\right)=\cos\left(\frac{7\pi}{3}\left(t-\frac{3}{14}\right)\right)
$$
a funkci $P_1$ můžeme vyjádřit následovně
$$
P_1=25\cdot\cos\left(\frac{7\pi}{3}t-\frac{1}{2}\pi\right)+105.
$$ 

\fi

V předchozí úloze bychom mohli funkce také zaměnit a vyjadřovat funkci $P_2$ pomocí funkce sinus.

> **Úloha 4.** Najděte předpis funkce, která aproximuje funkci krevního tlaku zdravého člověka v klidu.
> Jeho srdeční frekvence je $50$ tepů za minutu. Maximální krevní tlak je $110\,\text{mm}\,\text{Hg}$ a minimální $70\,\text{mm}\,\text{Hg}$. 

\iffalse

*Řešení.*  K aproximaci funkce krevního tlaku použijeme například funkci sinus (řešení pro funkci kosinus by bylo obdobné). 

Amplituda funkce je $\frac{110-70}{2}=20$ a funkce osciluje kolem hodnoty $\frac{110+70}{2}=90$. 

Perioda funkce je 
$$
p=\frac{60}{50}=\frac{6}{5},
$$ 
tj. jeden srdeční tep trvá $1{,}2$ sekundy. 
Ze vztahu 
$$
p=\frac{2\pi}{b} = 1{,}2
$$
pro periodu $p$ funkce dostáváme $b= \frac{5}{3}\pi$. 

Hodnotu $c$ můžeme zvolit libovolně, nejjednodušší je zvolit $c = 0.$ 
Dosazením výše uvedených hodnot do obecného tvaru funkce dostáváme 
$$
P(t) = 20\cdot\sin\left(\frac{5\pi}{3}t\right)+90.
$$ 

Tato funkce přibližně modeluje krevní tlak osoby se zadanými hodnotami jako funkci času (v sekundách). 

\fi

## Auskultační technika měření krevního tlaku 

Na závěr ještě uveďme, jak se v realitě tlak opravdu měří. Jedna z přesných metod je tzv. auskultační technika. 
Při této metoda se používá tonometr, skládající se z gumové manžety, nafukovacího vaku a manometru (mechnické měřidlo tlaku), a fonendoskop. 

Gumovou manžeta tonometru se nasadí zhruba na polovinu paže. Tlak v manžetě se zvýší tak, aby převyšoval tlak v tepně. 
Tím se z manžety stane uměle vytvořená překážka krevnímu průtoku. 
Postupným pomalým snižováním tlaku v manžetě dojde v určitém okamžiku k obnovení průtoku krve. 

Tlak v manžetě však na počátku způsobí deformaci tepny, díky níž je proudění pronikající krve turbulentní. 
Hodnota tlaku, při níž začínají být ve fonendoskopu slyšitelné srdeční ozvy, odpovídá hodnotě systolického krevního tlaku.

Ozvy jsou slyšitelné do té doby, dokud tlak v manžetě postačuje k deformaci tepny a tím k udržení turbulentního proudění. 
Jakmile tlak v manžetě poklesne natolik, že již nestačí tepnu deformovat, 
obnoví se původní proudění krve a ozvy přestanou být slyšitelné. 
Tlak při poslední slyšitelné ozvě odpovídá hodnotě diastolického krevního tlaku. 
 
### Zpřesnění 

Zbývá dodat, že realističtější vyjádření funkce krevního tlaku je náročnější 
a vyžaduje součty goniometrických funkcí s různými periodami. 

Na následujícím obrázku vidíme konkrétní příklad takového součtu a příslušný graf. 
Současně je na obrázku znázorněno měření krevního tlaku. Rychlost vypouštění manžety je přibližně konstantní. 
Tlak v manžetě tedy klesá konstantní rychlostí (opět přibližně) a na obrázku je znázorněn přímkou.

![Příklad součtu sinu a kosinu s různými periodami](cuff_pressure_cz.png)
 
Zpřesňování průběhu funkce krevního tlaku pomocí součtů sinů a kosinů už souvisí s tzv. Fourierovou větou, 
která říká, že spojitou periodickou funkci lze vyjádřit jako součet nekonečného počtu funkcí sinus a kosinus, 
přičemž každý z těchto členů má určitou amplitudu a periodu. 

Tento výsledek získal v roce 1822 francouzský matematik Joseph Fourier jako součást řešení rovnice vedení tepla.
Jedná se o klíčový koncept pro analýzu a pochopení jakýchkoli periodických jevů. 
Fourierova věta je základem zpracování signálů. 


[^1]: Aproximace znamená přibližné, ale věrné vyjádření  čísla nebo funkce, ale také fyzikálního zákona či přírodního jevu.
 
## Literatura

* https://www.vaia.com/en-us/textbooks/math/calculus-an-applied-approach-8-edition/chapter-8/problem-72-health-the-function-p100-20-cos-5-pi-t-3-approxim/
* https://www.vaia.com/en-us/textbooks/math/precalculus-9-edition/chapter-4/problem-90-the-function-p100-20-cos-frac5-pi-t3-approximates/#short-answer
* https://www.bloodpressureuk.org/your-blood-pressure/understanding-your-blood-pressure/what-do-the-numbers-mean/
 

  

 


---
---

### English source

Not available on July 10. If you want to start from English
translation, wait until it appears on <https://um.mendelu.cz/math4u/site/> anc copy the English text by hand.
