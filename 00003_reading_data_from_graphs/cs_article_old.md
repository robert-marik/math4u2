---
keywords:
- kombinatorika, pravděpodobnost a statistika
- statistika
- finanční matematika
is_finished: true
difficulty: 1
time: 15
---

# Čtení údajů z grafu 

Český statistický úřad (ČSÚ) byl zřízen v roce 1969 a jako hlavní orgán státní statistické 
služby se zabývá získáváním údajů, zpracováváním, vytvářením a zveřejňováním statistických 
informací o různých aspektech vývoje České republiky a jejích částí. Na oficiálních stránkách 
ČSÚ <https://www.czso.cz/> tak můžeme zdarma nalézt grafy a tabulky shrnující 
např. populační vývoj, volební statistiky, dopravní nehodovost, vývoje cen bytů a vývoj nezaměstnanosti. 
Jeden z grafů budeme analyzovat v následujících úlohách.

![Sídlo ČSÚ v Praze (rok 2017)](03_graf_csu.jpg)


Na stránkách Českého statistického úřadu lze nalézt graf vývoje průměrné hrubé měsíční mzdy, 
který vidíme na Obrázku 2. Na vodorovné ose jsou vyznačena čtvrtletí sledovaných let, modré sloupce odpovídají 
tehdejší průměrné hrubé nominální mzdě, červená křivka sleduje vývoj nominální mzdy očištěné 
od sezónních vlivů. Obojí se odečítá se na levé svislé ose v korunách. 
Světle modrá křivka udává sleduje růst nominální mzdy (odečítá se na pravé svislé ose v procentech) 
a tmavě modrá křivka udává růst reálné mzdy (rovněž se odečítá na pravé svislé ose).

![Průměrná měsíční mzda a růst mezd](03_graf_1.jpg)

**Slovníček**

* Z *hrubé mzdy*, kterou platí zaměstnavatel zaměstnanci, jsou strženy částky za zdravotní
  a sociální pojištění a daň z příjmu. Zaměstnanec pak dostává *mzdu čistou*, která je o tyto výlohy nižší.

* *Nominální mzda* je hrubá měsíční mzda vyjádřená v korunách. *Nominální mzda očištěná od sezónních vlivů*
  je nominální mzda, která byla statisticky upravena tak, aby eliminovala vliv sezónních změn v zaměstnanosti a mzdách.

* Nominální mzda je konkrétní částka, zatímco *reálná mzda* vyjadřuje, kolik si toho za tuto částku může
  zaměstnanec koupit. Může se tak stát, že se sice zaměstnanci zvedne nominální mzda, ale protože
  všichni obchodníci více zdražují své zboží a služby (jinými slovy, je velká *inflace*), reálná mzda mu klesne.

* *Tempo růstu*, je míra dynamiky mzdového vývoje. Meziroční tempo růstu udává, jak vzrostly mzdy (nominální a reálná)
  za poslední rok. Například, pokud je meziroční tempo růstu mzdy 2%, znamená to, že mzda se za poslední rok zvýšila právě o 2%. 



>**Úloha 1.** Rozhodněte o každém z tvrzení, zda z grafu vyplývá, nebo ne.
>
>1. Od roku 2018 průměrná hrubá nominální mzda neklesla pod $30\,000\,\text{Kč}$.
>2. Jestliže se zvyšuje průměrná hrubá nominální mzda, pak se také zvyšuje index nominální mzdy.
>3. Růst reálné mzdy byl v roce 2020 nejnižší za posledních pět let.


\iffalse

*Řešení.* 

1. Tvrzení je pravdivé - všechny modré sloupce v tabulce přesahují od roku 2018 hladinu $30\,000\,\text{Kč}$,
   což je vidět z Obrázku 3.

![Průměrná měsíční mzda a růst mezd](03_graf_graf_2.jpg)

2. Tvrzení není pravdivé - např. při přechodu z třetího na čtvrté čtvrtletí roku 2021 došlo
   k navýšení průměrné hrubé nominální mzdy, ale k poklesu indexu nominální mzdy.

3. Tvrzení není pravdivé - hodnoty růstu reálné mzdy z let 2022 a 2023 jsou nižší.


\fi

>**Úloha 2.** Vymezte hodnoty, mezi kterými se pohybují hodnoty veličin za sledované období.

\iffalse

*Řešení.* Průměrná hrubá nominální mzda se za sledované období pohybuje mezi $22\,000$ - $50\,000\,\text{Kč}$. 
Růstu nominální mzdy je mezi $0\,\%$ a $13\,\%$, hodnoty růstu reálné mzdy se pohybují mezi $-12\,\%$ a $10\,\%$.

\fi

> **Úloha 3** Pokuste se vysvětlit rozdíly mezi růstem nominální a reálné mzdy cca od
> třetího čtvrtletí roku 2021. Co lze naopak říci o situaci z let 2015 - 2016, kdy
> byly obě hodnoty srovnatelné?

\iffalse

*Řešení.* Z grafu vidíme, že se od třetího čtvrtletí roku 2021 index reálné mzdy prudce propadl, 
zatímco zbylé dva ukazatele nikoliv (hrubá nominální mzda dokonce mírně rostla jako v předchozích obdobích). 
To ukazuje na možného viníka - vysokou inflaci. Podezření si můžeme potvrdit na stránkách 
ČSÚ <https://www.czso.cz/csu/czso/mira_inflace>, kde lze v 
tabulkách sledujících míru inflace dohledat začátek zvyšování růstu právě ve třetím čtvrtletí roku 2021. 

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| - | -: | -: | -: | -: | -: | -: | -: | -: | -: | -: | -: | -: |
| **2020** | 2,9 | 3,0 | 3,1 | 3,1 | 3,1 | 3,1 | 3,2 | 3,2 | 3,3 | 3,3 | 3,2 | 3,2 |
| **2021** | 3,0 | 2,9 | 2,8 | 2,8 | 2,8 | 2,8 | 2,8 | 2,8 | 3,0 | 3,2 | 3,5 | 3,8 |
| **2022** | 4,0 | 5,2 | 6,1 | 7,0 | 8,1 | 9,4 | 10,6 | 11,7 | 12,7 | 13,5 | 14,4 | 15,1 |
| **2023** | 15,7 | 16,2 | 16,4 | 16,2 | 15,8 | 15,1 | 14,3 | 13,6 | 12,7 | 12,1 | 11,4 | 10,7 |
| **2024** | 9,4 | 8,2 | 7,1 | 6,3 | 5,6 | 4,9 | 4,4 | 3,9 | 3,5 | 3,1 | 2,7 | 2,4 |

Lze očekávat, že v letech 2015 - 2016 byla míra inflace naopak nízká, což si lze opět ověřit na stejném místě jako v předchozím odstavci.

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| -- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| **2015** | 0,3 | 0,3 | 0,3 | 0,4 | 0,4 | 0,5 | 0,5 | 0,4 | 0,4 | 0,4 | 0,3 | 0,3 |
| **2016** | 0,4 | 0,4 | 0,4 | 0,4 | 0,4 | 0,3 | 0,3 | 0,3 | 0,3 | 0,4 | 0,5 | 0,7 |
| **2017** | 0,8 | 1,0 | 1,2 | 1,3 | 1,5 | 1,7 | 1,8 | 2,0 | 2,2 | 2,3 | 2,4 | 2,5 |
| **2018** | 2,4 | 2,4 | 2,3 | 2,3 | 2,3 | 2,3 | 2,3 | 2,3 | 2,3 | 2,2 | 2,2 | 2,1 |

\fi
