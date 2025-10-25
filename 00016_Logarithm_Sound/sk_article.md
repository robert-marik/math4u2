---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- exponenciálne a logaritmické funkcie
- logaritmus
- logaritmická rovnica
- exponenciálna rovnica
is_finished: true
---

# Zvuk

Zvuk je mechanické vlnenie, ktoré vnímame sluchom.
Výšku a dĺžku tónu vnímajú všetci ľudia približne rovnako, ale vnímanie hlasitosti je veľmi subjektívne.
Hlasitosť je daná amplitúdou kmitania prostredia, v ktorom sa šíri zvuková vlna. Vzhľadom na to, že amplitúda zvukového vlnenia sa nemeria jednoducho, používajú sa na objektívne porovnanie hlasitosti veličiny intenzita zvuku $I$ a hladina intenzity zvuku $L$.

*Intenzita zvuku* vyjadruje, koľko energie prenesú zvukové vlny za sekundu na plochu $1\,\text{m}^2$ kolmú na smer šírenia za jednotku času. Zdravý sluch dokáže pri frekvencii $1000\,\text{Hz}$ zaregistrovať najmenšiu intenzitu zvuku $I_0=10^{-12}\,\text{W}/\text{m}^2$, čo zodpovedá prahu počutia. Naopak, intenzita zvuku $10\,\text{W}/\text{m}^2$ je natoľko hlasitá, že zodpovedá prahu bolesti. Zvýšenie intenzity zvuku $I$ na desaťnásobok však neznamená, že by sme vnímali zvuk desaťkrát hlasnejšie. Preto sa na vyjadrovanie hlasitosti zvuku používa skôr hladina intenzity zvuku $L$, ktorá využíva logaritmickú škálu v decibeloch (dB).

*Hladina intenzity zvuku* $L$ v decibeloch je definovaná vzťahom
$$L=10\log{\frac{I}{I_0}},$$
kde $I$ je intenzita zvuku v danom mieste a $I_0=10^{-12}\,\text{W}/\text{m}^2$, čo zodpovedá prahu počutia. Hladine intenzity zvuku $60\,\text{dB}$ zodpovedá hlasitosť bežného rozhovoru, $90\,\text{dB}$ nameriame pri motorovej kosačke na trávu a $110\,\text{dB}$ na diskotéke. Pri dlhodobom počúvaní (hoci nás nič nebolí) hrozí nebezpečenstvo poškodenia sluchu pre hlasitosti vyššie ako $85\,\text{dB}$. Pri hlasitosti vyššej ako $100\,\text{dB}$ hrozí nebezpečenstvo poškodenia sluchu v priebehu niekoľkých minút.

Preskúmajme súvislosť medzi intenzitou zvuku a hladinou intenzity zvuku, teda hlasitosťou vnímanou sluchom.

>**Úloha 1.** Pri počúvaní reproduktora so zvukovým výkonom $20\,\text{W}$ je vo vzdialenosti $50\,\text{m}$ od neho intenzita zvuku $1{,}27\cdot10^{-3}\,\text{W}/\text{m}^2$ (pri rovnomernom vysielaní zvukovej vlny do voľného polopriestoru). Koľko decibelov nameriame na tomto mieste?

\iffalse

*Riešenie.* Na výpočet využijeme definičný vzťah $L=10\log{\frac{I}{I_0}},$
kde $I=1{,}27\cdot10^{-3}\,\text{W}/\text{m}^2$ je intenzita zvuku v danom mieste a $I_0=10^{-12}\,\text{W}/\text{m}^2$.
$$L=10\log{\frac{I}{I_0}}=10\log{\left(\frac{1{,}27\cdot10^{-3}}{10^{-12}}\right)}=10\log{\left(1{,}27\cdot10^{9}\right)}=91\;\text{dB}\,.$$

Hladina intenzity zvuku vo vzdialenosti $50$ m od reproduktora je $91$ dB, čo zodpovedá hluku motocykla alebo kosačky na trávu.

\fi

>**Úloha 2.** Ako sa zmení hladina intenzity zvuku, ak bude v mieste z predchádzajúceho príkladu dvojnásobná intenzita zvuku, t.j. $2\cdot1{,}27\cdot10^{-3}\,\text{W}/\text{m}^2$ ?

\iffalse

*Riešenie.* Použijeme rovnaký vzťah ako v predchádzajúcej úlohe:
$$L=10\log{\frac{I}{I_0}}=10\log{\left(\frac{2\cdot1{,}27\cdot10^{-3}}{10^{-12}}\right)}=10\log{\left(2{,}54\cdot10^{9}\right)}=94\;\text{dB}\,.$$
Z výpočtu je zrejmé, že dvojnásobnej intenzite zvuku nezodpovedá dvojnásobný počet decibelov. Hladina intenzity zvuku sa zvýši z
$91\,\text{dB}$ na $94\,\text{dB}\,$.

\fi

>**Úloha 3.** Zo vzťahu pre hladinu intenzity zvuku nájdite hodnotu $\Delta L$, o ktorú sa zmení hladina intenzity zvuku $L$, ak sa intenzita zvuku zdvojnásobí z hodnoty $I$ na $2I$.

\iffalse

*Riešenie.* Jedná sa o zovšeobecnenie predchádzajúcej úlohy.
$$\Delta L=10\log{\frac{2I}{I_0}}-10\log{\frac{I}{I_0}}=10\cdot\left(\log{\frac{2I}{I_0}}-\log{\frac{I}{I_0}}\right)=10\log\left(\frac{\frac{2I}{I_0}}{\frac{I}{I_0}}\right)=10\log2\doteq3\;\text{dB}$$
Pri zdvojnásobení intenzity zvuku sa hladina intenzity zvuku zväčší o $3\,\text{dB}\,$.

\fi

>**Úloha 4.** Intenzita zvuku je nepriamo úmerná druhej mocnine vzdialenosti od zdroja zvuku. O akú hodnotu sa zmení hladina intenzity zvuku, ak sa vzdialenosť od zdroja zvuku zdvojnásobí?

\iffalse

*Riešenie.* Keďže intenzita zvuku $I$ je nepriamo úmerná druhej mocnine vzdialenosti, dostávame  $$I=\frac{k}{l^2},$$ kde $l$ je vzdialenosť od zdroja zvuku. Pri zdvojnásobení vzdialenosti bude intenzita zvuku
$$\tilde{I}=\frac{k}{(2l)^2}=\frac{1}{4}\cdot\frac{k}{l^2}=\frac{1}{4}I\,.$$
Intenzita zvuku sa zmenší na $\frac{1}{4}$ pôvodnej hodnoty.

$$\Delta L=10\log{\frac{\frac{1}{4}I}{I_0}}-10\log{\frac{I}{I_0}}=10\cdot\left(\log{\frac{\frac{1}{4}I}{I_0}}-\log{\frac{I}{I_0}}\right)=10\log\left(\frac{\frac{\frac{1}{4}I}{I_0}}{\frac{I}{I_0}}\right)=10\log\frac{1}{4}\doteq-6\;\text{dB}\,.$$
Hladina intenzity zvuku sa zmenší o $6\,\text{dB}$, ak zdvojnásobíme svoju vzdialenosť od zdroja zvuku.

\fi

>**Úloha 5.** Zo vzťahu pre hladinu intenzity zvuku $L=10\log{\frac{I}{I_0}}$ vyjadrite intenzitu zvuku $I$.

\iffalse

*Riešenie.* Najprv musíme osamostatniť logaritmickú funkciu
$\frac{L}{10}=\log{\frac{I}{I_0}}$ a následne použijeme inverznú funkciu k logaritmickej, teda exponenciálnu funkciu:
$$10^{\frac{L}{10}}=\frac{I}{I_0}.$$
Odtiaľ vyjadríme intenzitu zvuku:
$$I=I_0 \cdot 10^{\frac{L}{10}}.$$

\fi

>**Úloha 6.** Koľkokrát sa zväčší intenzita zvuku, ak sa hladina intenzity zvuku zvýši o $20\,\text{dB}$?

\iffalse

*Riešenie.* Hodnota hladiny intenzity zvuku sa zmení z hodnoty $L_1=L$ na $L_2=L+20\,\text{dB}$. Využijeme vzťah $I=I_0 \cdot 10^{\frac{L}{10}}$ a vyjadríme podiel $\frac{I_2}{I_1}$:
$$\frac{I_2}{I_1}=\frac{I_0 \cdot 10^{\frac{L_2}{10}}}{I_0 \cdot 10^{\frac{L_1}{10}}}=\frac{10^{\frac{L+20}{10}}}{10^{\frac{L}{10}}}=10^{\frac{L+20}{10}-\frac{L}{10}}=10^2=100.$$

Pri vzraste hladiny intenzity zvuku o $20\,\text{dB}$ sa intenzita zvuku zväčší stokrát.

\fi

## Literatúra 
1. Kubera, Miroslav; Nečas, Tomáš; Beneš, Vojtěch. *Online učebnice fyziky pro gymnázia - Zvuk.* Dostupné z <https://e-manuel.cz/kapitoly/mechanicke-vlneni/vyklad/zvuk/> [cit. 24.10.2023].
