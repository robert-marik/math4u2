---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- exponenciálne a logaritmické funkcie
- exponenciálna funkcia
- logaritmická funkcia
- rádioaktivita
is_finished: true
---

# Smrtiaci byt v Kramatorsku

Byt číslo 85, dom číslo 7, ulica Mariyi Pryimachenko, Kramatorsk (bývalý ZSSR, teraz Ukrajina), bol skutočne prekliaty a prinášal svojim nájomníkom len nešťastie. V rokoch 1980 až 1989 tu žili dve rodiny, ktoré bezmocne sledovali, ako ich deti umierajú na leukémiu. V roku 1980 náhle zomrela 18-ročná dcéra, následne v roku 1982 aj jej 16-ročný brat a matka. Ani jedno z týchto úmrtí nepritiahlo pozornosť úradov a byt bol pridelený novým nájomníkom. Tí však tiež nemali šťastie, keďže ich syn tiež čoskoro zomrel na leukémiu.

![Dom v Kramatorsku, kde dochádzalo k záhadným úmrtiam](house_no_7.jpg)

## Nehoda v lome Karansky

Až po ďalšom úmrtí a vďaka vytrvalosti nového nájomníka bol byt prekontrolovaný. Inšpektori boli šokovaní. Zistili, že v detskej izbe je silný zdroj rádioaktívneho žiarenia. Veľká časť steny bola vyrezaná a preskúmaná. Dôkladné vyšetrenie odhalilo žiarič v paneli, ktorý sa používal v lomoch. Označenie na žiariči ukázalo, že bol stratený koncom 70. rokov v lome Karansky.


V lomoch sa rádioaktívne materiály môžu používať napríklad na určenie hustoty hornín alebo úrovne naplnenia nepriehľadných nádob. Napriek tomu, že manipulácia s týmito materiálmi podlieha prísnym predpisom, občas dôjde k nehode. Podobná nehoda sa stala začiatkom roku 2023 v Austrálii. Tam sa žiarič stratil počas prepravy na vzdialenosť 1 400 kilometrov. Pátranie bolo skutočne ako hľadanie ihly v kope sena. Žiarič je valec o veľkosti gombíkovej batérie, veľký 8 milimetrov. Našťastie bol austrálsky žiarič nájdený na ceste, po ktorej prebiehala preprava. Bohužiaľ, ukrajinský žiarič také šťastie nemal a skončil v paneli, ktorý bol použitý pri stavbe nešťastného domu.

![Žiarič podobného typu stratený v roku 2023 v Austrálii](australia-capsule-size.png)

> **Úloha 1.** Panel tvoriaci stenu detskej izby obsahuje rádioaktívny žiarič. Nešťastnou náhodou sa nachádza priamo vedľa jednej z detských postelí. Skúste odhadnúť, o koľko by sa znížila dávka žiarenia, keby sa detská posteľ presunula na opačnú stranu postihnutej izby. Predpokladajte, že žiarič vyžaruje rovnomerne vo všetkých smeroch. Taktiež predpokladajte, že vzdialenosť žiariča od detskej postele bola pol metra, a že po presunutí postele na opačnú stranu izby sa vzdialenosť zväčší na tri metre, teda šesťnásobne.

\iffalse

*Riešenie.* Podľa zadania úlohy môžeme predpokladať, že žiarenie je rovnomerne rozložené na guľovej ploche.

Povrch gule s polomerom $r$ je daný vzorcom:

$$S = 4 \pi r^2.$$

Z toho vyplýva, že guľová plocha so šesťnásobným polomerom má 36-krát väčší povrch. Celkový výkon žiariča je teda rozložený na 36-krát väčšiu plochu. Preto je intenzita žiarenia vo vzdialenosti šesťnásobku vzdialenosti 36-krát nižšia.

\fi

> **Úloha 2.** Cézium použité ako zdroj rádioaktívneho žiarenia v opísanom incidente má polčas rozpadu 30 rokov. Určte, ako dlho by trvalo, kým by sa rádioaktivita znížila rovnakým násobkom ako po presťahovaní postele v predchádzajúcej úlohe.

\iffalse

*Riešenie.* Z fyziky vieme, že aktivita žiariča a množstvo nerozpadnutého materiálu sú úmerné a obe exponenciálne klesajú s časom podľa rovnice:

$$N(t) = N_0\mathrm{e}^{-\lambda t},\tag{1}$$

kde

* $N(t)$ označuje množstvo nerozpadnutej látky v čase $t$;
* $N_0$ je počiatočné množstvo látky;
* $\lambda$ je premenová (rozpadová) konštanta, ktorá charakterizuje predpokladanú rýchlosť premeny;
* $t$ je čas.

Je teda potrebné nájsť, v akom čase bude množstvo rádioaktívneho materiálu 36-krát menšie. Zlogaritmovaním oboch strán rovnice (1) dostaneme:

$$
-\lambda t = \ln \frac{N(t)}{N_0}\tag{2}.
$$

Keďže množstvo sa za tridsať rokov zmenší na polovicu ($N(30)=\frac{1}{2}N_0$), máme:

$$
-\lambda\,30 = \ln \frac 12
$$

a

$$
\lambda = \frac 1{30}\ln 2.
$$ 

Dosadením do rovnice (2) dostaneme: 

$$-\frac 1{30}t\ln 2 = \ln \frac{N(t)}{N_0}$$

a

$$t = -30 \frac{\ln \frac{N(t)}{N_0}}{\ln 2}.$$

Pre čas, kde platí
$\frac{N(t)}{N_0}=\frac {1}{36}$. Dostaneme:

$$t = -30 \frac{\ln \frac{1}{36}}{\ln 2} =
30 \frac{\ln {36}}{\ln 2} \doteq 155.$$

Úroveň žiarenia klesne na úroveň zodpovedajúcu presunutiu postele na druhú stranu izby približne po 155 rokoch.

\fi

## Odkazy a literatúra

### Literatúra

* Wikipedie, Kramatorsk radiological accident,
  <https://en.wikipedia.org/wiki/Kramatorsk_radiological_accident>,
  September 28, 2023

* <https://www.irozhlas.cz/zpravy-svet/australie-radiace-nebezpeci-varovani-radioaktivita-cesium-137-ozareni_2301311701_har>,
  September 28, 2023

* <https://edition.cnn.com/2023/02/01/australia/australia-radioactive-capsule-found-intl-hnk/index.html>, September 28, 2023

### Zdroje obrázkov

* Artemka, Own work, <https://commons.wikimedia.org/wiki/File:%D0%A3%D0%BB%D0%B8%D1%86%D0%B0_%D0%9C%D0%B0%D1%80%D0%B8%D0%B8_%D0%9F%D1%80%D0%B8%D0%B9%D0%BC%D0%B0%D1%87%D0%B5%D0%BD%D0%BA%D0%BE,_7.jpg>, September 28, 2023

* <https://edition.cnn.com/2023/02/01/australia/australia-radioactive-capsule-found-intl-hnk/index.html>, September 28, 2023
                                                      



