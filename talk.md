# Vývoj

Používáme osvědčené postupy a nástroje osvědčené při spolupráci a vývoji softwarových produktů.

* Tiketovací systém zajišťuje transparentní předávání mezi jednotlivými fázemí zpracování.
* Použití formátů Markdown a LaTeX garantuje nulové riziko zastarání textů po technické stránce.
* Správa zdrojových textů na serveru GitHub umožní bez námahy použít pro vývoj materiálů vyspělou a osvědčenou infrastrukturu.

## Tiketovací systém

Návrh materiálu, diskuse o případných změnách a předávání mezi jednotlivými fázemi zpracování 
(návrh, schválení, vytvoření elektronické verze, překlad do angličitny, proofrereading anglické verze) se děje
prostřednctvím tiketovacího systému. K tomuto používáme tiketovací systém, který je součástí CMS Drupal. Stejný systém je použit i v dalších částech projektu 
a pracovníci jsou s prací dobře beznámeni.

## Markdown

Jako nosič informace a základní formát pro psaní textů je použit značkovací jazyk Markdown.

* Je snadno zpracovatelný, čitelný i v základní podobě a snadno transformovatelný do široké škály formátů. Vzhledem k jednoduchosti nehrozí případné zastarání datového formátu.
* Obsahuje podporu systému LaTeX, který zajišťuje vysokou kvalitu matematických vzorců a nulové riziko zastarání.
* Přes omezené vyjadřovací schopnosti oproti kancelářským textovým procesorům Markdown stále obsahuje dostatečné formátovací prostředky pro vytvoření učebních materiálů.
* Markdown je defacto standard při psaní technických textů, dokumentace k programům a podobně.
* Dokumenty je možné zpracovávat dávkově a transformovat do html s responzivním designem pro čtení na obrazovce nebo do LaTeXu pro tištěný výstup vysoké kvality. Přitom jsou pro
  autory odflitrovány složitosti HTML nebo LaTeXu.
* Snadná transformace a možnost dávkového zpracování minimalizuje riziko technologického zastarávání materiálů. Vždy bude možné změnou šablony snadno vygenerovat výstupy v jiném designu nebo dokonce v jiném formátu.
* Použití Markdownu umožňuje oddělit obsah a formu, přičemž formu je možno následně volit z široké škály možností. Například je možné využít některý z populárních frameworků a vzhledově tak přiblížit dokumenty jiným stránkám na Internetu. Díky tomu nepůsobí texty cizím a neznámým dojmem. V současnosti používáme framework Bootstrap.


## Git, GitHub

* Git je verzovací systém pro správu dokumentů, který umožňuje správu včetně zaznamenávání revizí.
* Git je v současnosti nejpopulárnějším a nejrozšířenějším systémem a je možné jej používat v cloudu. V projektu používáme GitHub, akademickou licenci.
* GitHub obsahuje všechny nástroje pro pořizování a úpravy kódu. Obsahuje cloudovou verzi programu VSCode, což je v současnosti jeden z nejpoužívanějších programátorských textových editorů.
* Necloudová verze Gitu je k dispozicina všech běžných operačních systémech. Uživatel není nucen pracovat v cloudovém prostředí, ale může pracovat na svém lokálním počítači ve svém oblíbeném programovém prostředí a změny nahrávat na server.
* Pokud více autorů pracuje současně s repozitářem, změny se automaticky slučují (pokud nedojde ke konfliktu mezi verzemi).
* Aktuální nebo libovolnou historickou podobu textů je možno stáhnout na lokální počítač a pomocí skriptů transformovat do finální podoby. Díky tomu je možno snadno aktualizovat šablony nebo design, aniž by se muselo otevírat a upravovat 4x50 dokumentů.
