---
keywords:
- štatistika
- finačná matematika
is_finished: True
---

# Čítanie údajov z grafu 

Český štatistický úrad (ČSÚ) bol zriadený v roku 1969 a ako hlavný orgán štátnej štatistickej služby sa zaoberá získavaním údajov, ich spracovaním, tvorbou a zverejňovaním štatistických informácií o rôznych aspektoch vývoja Českej republiky a jej častí. Na oficiálnych stránkach ČSÚ https://www.czso.cz/ sú bezplatne dostupné grafy a tabuľky sumarizujúce napríklad populačný vývoj, volebné štatistiky, dopravnú nehodovosť, vývoj cien bytov a vývoj nezamestnanosti. Jeden z týchto grafov bude predmetom analýzy v nasledujúcich úlohách.

![Sídlo ČSÚ v Prahe (rok 2017)](03_graf_csu.jpg)

Na stránkach Českého štatistického úradu možno nájsť graf vývoja priemernej hrubej mesačnej mzdy, ktorý vidíme na obrázku 2. Na vodorovnej osi sú vyznačené štvrťroky sledovaných rokov. Modré stĺpce zodpovedajú vtedajšej priemernej hrubej nominálnej mzde, červená krivka znázorňuje vývoj nominálnej mzdy očistenej od sezónnych vplyvov. Obe hodnoty sa odčítavajú na ľavej zvislej osi v korunách. Svetlomodrá krivka znázorňuje rast nominálnej mzdy (odčítava sa na pravej zvislej osi v percentách) a tmavomodrá krivka znázorňuje rast reálnej mzdy (rovnako sa odčítava na pravej zvislej osi).

![Vývoj priemernej mesačnej mzdy a jej rast](03_graf_1.jpg)

**Slovník pojmov**

* Zo *hrubej mzdy*, ktorú vypláca zamestnávateľ zamestnancovi, sa odpočítavajú odvody na zdravotné
a sociálne poistenie a tiež daň z príjmu. Zamestnanec preto dostáva *čistú mzdu*, ktorá je o tieto položky nižšia.

* *Nominálna mzda* je hrubá mesačná mzda vyjadrená v peňažných jednotkách. *Nominálna mzda očistená od sezónnych vplyvov*
je nominálna mzda upravená štatistickými metódami s cieľom odstrániť vplyv sezónnych zmien v zamestnanosti a mzdách.

* Nominálna mzda je konkrétna číselná hodnota, zatiaľ čo *reálna mzda* vyjadruje kúpnu silu tejto čiastky, teda množstvo tovarov a služieb, ktoré si za ňu môže zamestnanec obstarať. Môže nastať situácia, že sa nominálna mzda zvýši, avšak pri vysokej *inflácii* (rast cien tovarov a služieb) reálna mzda klesá.

* *Tempo rastu* predstavuje mieru dynamiky vývoja miezd. Medziročné tempo rastu udáva relatívny prírastok miezd (nominálnych aj reálnych) za posledný rok. Napríklad, ak je medziročné tempo rastu mzdy 2%, znamená to, že mzda sa v porovnaní s predchádzajúcim rokom zvýšila práve o 2%.

>**Úloha 1.** Rozhodnite o každom z tvrdení, či z grafu vyplýva, alebo nie.
>
>1. Od roku 2018 priemerná hrubá nominálna mzda neklesla pod $30\,000\,\text{Kč}$.
>2. Ak sa zvyšuje priemerná hrubá nominálna mzda, potom sa tiež zvyšuje index nominálnej mzdy.
>3. Rast reálnej mzdy bol v roku 2020 najnižší za posledných päť rokov.

\iffalse

*Riešenie.* 

1. Tvrdenie je pravdivé – všetky modré stĺpce v tabuľke od roku 2018 presahujú hladinu $30\,000\,\text{Kč}$,
   čo je vidno na Obrázku 3.

![Vývoj priemernej mesačnej mzdy a jej rast](03_graf_graf_2.jpg)

2. Tvrdenie nie je pravdivé – napríklad pri prechode z tretieho na štvrtý štvrťrok 2021 došlo k zvýšeniu priemernej hrubej nominálnej mzdy, avšak k poklesu indexu nominálnej mzdy.

3. Tvrdenie nie je pravdivé – hodnoty rastu reálnej mzdy za roky 2022 a 2023 sú nižšie.


\fi

>**Úloha 2.** Vyjadrite hodnoty, medzi ktorými sa pohybujú hodnoty veličín za sledované obdobie.

\iffalse

*Riešenie.* Priemerná hrubá nominálna mzda sa za sledované obdobie pohybuje približne medzi $22\,000$ - $50\,000\,\text{Kč}$. 
Rast nominálnej mzdy sa pohybuje medzi $0\,\%$ a $13\,\%$, hodnoty rastu reálnej mzdy sú v intervale od $-12\,\%$ do $10\,\%$.

\fi

> **Úloha 3** Pokúste sa vysvetliť rozdiely medzi rastom nominálnej a reálnej mzdy približne od tretieho štvrťroka 2021. Čo možno povedať o situácii v rokoch 2015 – 2016, keď boli obe hodnoty porovnateľné?

\iffalse

*Riešenie.*
Z grafu je vidieť, že od tretieho štvrťroka 2021 index reálnej mzdy prudko klesol, zatiaľ čo ostatné dva ukazovatele (vrátane hrubej nominálnej mzdy) ostali stabilné alebo mierne rástli, ako v predchádzajúcich obdobiach. Tento jav poukazuje na možnú príčinu – vysokú infláciu. Túto hypotézu je možné overiť na stránkach ČSÚ <https://www.czso.cz/csu/czso/mira_inflace>, kde sú dostupné tabuľky sledujúce mieru inflácie, ktorá začala prudko rásť práve v treťom štvrťroku 2021.

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| - | -: | -: | -: | -: | -: | -: | -: | -: | -: | -: | -: | -: |
| **2020** | 2,9 | 3,0 | 3,1 | 3,1 | 3,1 | 3,1 | 3,2 | 3,2 | 3,3 | 3,3 | 3,2 | 3,2 |
| **2021** | 3,0 | 2,9 | 2,8 | 2,8 | 2,8 | 2,8 | 2,8 | 2,8 | 3,0 | 3,2 | 3,5 | 3,8 |
| **2022** | 4,0 | 5,2 | 6,1 | 7,0 | 8,1 | 9,4 | 10,6 | 11,7 | 12,7 | 13,5 | 14,4 | 15,1 |
| **2023** | 15,7 | 16,2 | 16,4 | 16,2 | 15,8 | 15,1 | 14,3 | 13,6 | 12,7 | 12,1 | 11,4 | 10,7 |
| **2024** | 9,4 | 8,2 | 7,1 | 6,3 | 5,6 | 4,9 | 4,4 | 3,9 | 3,5 | 3,1 | 2,7 | 2,4 |

V rokoch 2015 – 2016 boli hodnoty rastu nominálnej a reálnej mzdy porovnateľné, čo naznačuje, že inflácia v tomto období bola nízka alebo stabilná, a teda rast nominálnej mzdy sa premietal do rastu kúpnej sily.

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| -- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| **2015** | 0,3 | 0,3 | 0,3 | 0,4 | 0,4 | 0,5 | 0,5 | 0,4 | 0,4 | 0,4 | 0,3 | 0,3 |
| **2016** | 0,4 | 0,4 | 0,4 | 0,4 | 0,4 | 0,3 | 0,3 | 0,3 | 0,3 | 0,4 | 0,5 | 0,7 |
| **2017** | 0,8 | 1,0 | 1,2 | 1,3 | 1,5 | 1,7 | 1,8 | 2,0 | 2,2 | 2,3 | 2,4 | 2,5 |
| **2018** | 2,4 | 2,4 | 2,3 | 2,3 | 2,3 | 2,3 | 2,3 | 2,3 | 2,3 | 2,2 | 2,2 | 2,1 |

\fi
