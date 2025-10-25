---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- geometria v rovine
- planimetria
- množina bodov danej vlastnosti
is_finished: true
---

# Umiestnenie studne na pozemku

Ak chceme mať studňu na našom pozemku, musíme starostlivo zvážiť jej umiestnenie, aby sme udržali dostatočnú vzdialenosť od možných zdrojov kontaminácie. Tieto požadované vzdialenosti sa líšia v závislosti od typu možnej kontaminácie. Predpokladajme, že pre menej priepustné prostredia sú požadované vzdialenosti uvedené nasledovne:

1. žumpy, malé čistiarne odpadových vôd, kanalizačné prípojky: $12 \text{ m}$;
2. nádrže na kvapalné palivo pre individuálne vykurovanie umiestnené v obytnom dome alebo samostatnej pomocnej budove: $7 \text{ m}$;
3. stajne, močovkové jamy a hnojiská pre drobný chov jednotlivých hospodárskych zvierat: $10 \text{ m}$;
4. verejné pozemné komunikácie: $12 \text{ m}$;
5. individuálne umývacie plochy pre motorové vozidlá, od nich vedúce odtokové rúry a priekopy: $15 \text{ m}$.


> **Úloha.** Na pozemku $P_1$ (znázornenom na pláne na obrázku) je potrebné vybudovať studňu. Plán ukazuje, kde sa nachádza dom (obdĺžnik) a žumpa (kruh) na pozemku $P_1$, a 
> kde sa nachádza dom (štvorec), žumpa (kruh) a umývacia plocha (obdĺžnik) na susednom pozemku  $P_2$.  Plán tiež zobrazuje cestu, ktorá prechádza okolo oboch pozemkov. 
>Označte na pláne miesto, kde možno podľa pravidiel umiestniť studňu.
> 
> ![Plán pozemku](math4you_00009.png)

\iffalse

*Riešenie.* Na pláne vyznačíme oblasti, kde nesmie byť umiestnená studňa 

Keďže studňa musí byť vzdialená aspoň 12 m od žumpy, táto zakázaná oblasť bude na pláne zobrazená ako kruh sústredný s vyznačeným kruhom s polomerom o 12 m väčším. Hranice zakázaných oblastí pre obe žumpy sú znázornené kruhmi $k_1$
a $k_2$ na obrázku.

Zakázanou oblasťou súvisiacou s cestou je na pláne pás, ktorého hranicu tvorí krajnica cesty priliehajúca k pozemkom $P_1$ a $P_2$
a priamka rovnobežná s ňou vo vzdialenosti 12m (na obrázku je to priamka $p$).

Nakoniec vytvoríme hranicu zakázanej oblasti súvisiacej s umývacou plochou pre auto. Hranica má tvar elipsy označenej na pláne ako $o$. Táto elipsa pozostáva zo štyroch úsečiek rovnobežných so stranami obdĺžnika vo vzdialenosti 15 m a štyroch kružníc so stredmi vo vrcholoch obdĺžnika s polomerom 15 m. Na obrázku je označená iba príslušná časť tejto elipsy.
Teraz je možné definovať oblasť vhodnú na vyhĺbenie studne. Ide o tú vonkajšiu časť   pozemku $P_1$, ktorá  neleží v žiadnej zo zakázaných oblastí. Jej hranica je na obrázku označená tučnou čiarou.

![Riešenie](math4you_00009_res.jpg)

\fi
