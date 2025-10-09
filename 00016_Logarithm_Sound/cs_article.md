---
keywords:
- exponenciály a logaritmy
- logaritmus
- logaritmická rovnice
- exponenciální rovnice
is_finished: true
difficulty: 2
time: 30
---

# Zvuk

Zvuk je mechanické vlnění, které vnímáme sluchem. 
Výšku a délku tónu vnímají všichni lidé přibližně 
stejně, vjem hlasitosti je ale velice subjektivní. 
Hlasitost je dána amplitudou kmitání prostředí, v  
kterém se šíří zvuková vlna. Vzhledem k tomu, že 
se amplituda zvukového vlnění neměří snadno, 
používají se k objektivnímu porovnávání hlasitosti 
veličiny intenzita zvuku $I$ a hladina intenzity 
zvuku $L$.

*Intenzita zvuku* vyjadřuje, kolik energie 
přenesou zvukové vlny za sekundu na plochu $1\,\text{m}^2$ 
kolmou na směr šíření za jednotku času. Zdravý sluch 
dokáže při frekvenci $1000\,\text{Hz}$ 
zaregistrovat nejmenší intenzitu zvuku $I_0=10^{-12}\,\text{W}/\text{m}^2$,
což odpovídá prahu slyšení.
Naopak intenzita zvuku $10\,\text{W}/\text{m}^2$ 
je natolik hlasitá, že odpovídá prahu bolesti. 
Zvýšení intenzity zvuku $I$ na desetinásobek ale 
neodpovídá tomu, že bychom vnímali zvuk desetkrát hlasitěji. 
Proto se k vyjadřování 
hlasitosti zvuku spíše používá hladina intenzity 
zvuku $L$, která využívá logaritmické škály v 
decibelech (dB).

*Hladina intenzity zvuku* $L$ v decibelech je 
definována vztahem 
$$L=10\log{\frac{I}{I_0}},$$
kde $I$ je intenzita zvuku v daném místě a
$I_0=10^{-12}\,\text{W}/\text{m}^2$, což odpovídá prahu
slyšení. Hladině intenzity zvuku $60\,\text{dB}$
odpovídá hlasitost běžného rozhovoru, $90\,\text{dB}$ naměříme u
motorové sekačky na trávu a
$110\,\text{dB}$ na diskotéce. Při dlouhodobém 
poslechu (přestože nás nic nebolí) hrozí nebezpečí 
poškození sluchu pro hlasitosti vyšší jak $85\,\text{dB}$. Od
hlasitosti vyšší jak $100\,\text{dB}$
hrozí nebezpečí poškození sluchu v řádu minut.

Prozkoumejme souvislost mezi intenzitou zvuku a hladinou intenzity
zvuku, tj. hlasitostí vnímanou sluchem.

>**Úloha 1.** Při poslechu reproduktoru o zvukovém výkonu $20\,\text{W}$ je 
>ve vzdálenosti $50\,\text{m}$ od něj intenzita zvuku $1{,}27\cdot10^{-3}\,
>\text{W}/\text{m}^2$ (při rovnoměrném vysílání zvukové vlny do volného 
>poloprostoru). Kolik decibelů naměříme v tomto místě?

\iffalse

*Řešení.* Pro výpočet využijeme definičního vztahu $L=10\log{\frac{I}{I_0}},$
kde $I=1{,}27\cdot10^{-3}\,\text{W}/\text{m}^2$ je intenzita zvuku v 
daném místě a $I_0=10^{-12}\,\text{W}/\text{m}^2$.
$$L=10\log{\frac{I}{I_0}}=10\log{\left(\frac{1{,}27\cdot10^{-3}}{10^{-12}}\right)}=10\log{\left(1{,}27\cdot10^{9}\right)}=91\;\text{dB}\,.$$

Hladina intenzity zvuku $50$ m od reproduktoru je $91$ dB, což odpovídá 
hluku motocyklu nebo sekačce na trávu.

\fi

>**Úloha 2.** Jak se změní hladina intenzity zvuku, jestliže v místě z 
>předchozího příkladu bude dvojnásobná intenzita zvuku, tj. $2\cdot1{,}27\cdot10^{-3}\,\text{W}/\text{m}^2$ ?

\iffalse

*Řešení.* Použijeme stejný vztah jako v minulé úloze:
$$L=10\log{\frac{I}{I_0}}=10\log{\left(\frac{2\cdot1{,}27\cdot10^{-3}}{10^{-12}}\right)}=10\log{\left(2{,}54\cdot10^{9}\right)}=94\;\text{dB}\,.$$
Z výpočtu je patrné, že dvojnásobné intenzitě zvuku neodpovídá 
dvojnásobný počet decibelů. Hladina intenzity zvuku se zvedne z
$91\,\text{dB}$ na $94\,\text{dB}\,$.

\fi

>**Úloha 3.** Ze vztahu pro hladinu intenzity zvuku najděte 
>hodnotu $\Delta L$, o kterou se 
>změní hladina intenzity zvuku $L$, jestliže se intenzita zvuku 
>zdvojnásobí z hodnoty $I$ na $2I$.

\iffalse

*Řešení.* Jedná se o zobecnění předchozí úlohy.$$\Delta L=10\log{\frac{2I}{I_0}}-10\log{\frac{I}{I_0}}=10\cdot\left(\log{\frac{2I}{I_0}}-\log{\frac{I}{I_0}}\right)=10\log\left(\frac{\frac{2I}{I_0}}{\frac{I}{I_0}}\right)=10\log2\doteq 3\;\text{dB}$$
Při zdvojnásobení intenzity zvuku se hladina intenzity zvuku zvětší přibližně o $3\,\text{dB}\,$.

\fi

>**Úloha 4.** Intenzita zvuku je nepřímo úměrná druhé mocnině vzdálenosti 
>od zdroje zvuku. O jakou hodnotu se změní hladina intenzity zvuku,
>jestliže se vzdálenost od zdroje zvuku zdvojnásobí? 

\iffalse

*Řešení.* Jelikož intenzita zvuku $I$ je nepřímo úměrná druhé mocnině 
vzdálenosti, dostáváme  $$I=\frac{k}{l^2},$$ kde $l$ je vzdálenost od 
zdroje zvuku. Při zdvojnásobení vzdálenosti bude intenzita zvuku
$$\tilde{I}=\frac{k}{(2l)^2}=\frac{1}{4}\cdot\frac{k}{l^2}=\frac{1}{4}I\,.$$
Intenzita zvuku se zmenší na $\frac{1}{4}$ původní hodnoty.

$$\Delta L=10\log{\frac{\frac{1}{4}I}{I_0}}-10\log{\frac{I}{I_0}}=10\cdot\left(\log{\frac{\frac{1}{4}I}{I_0}}-\log{\frac{I}{I_0}}\right)=10\log\left(\frac{\frac{\frac{1}{4}I}{I_0}}{\frac{I}{I_0}}\right)=10\log\frac{1}{4}\doteq -6\;\text{dB}\,.$$
Hladina intenzity zvuku se zmenší přibližně o $6\,\text{dB}$, jestliže 
zdvojnásobíme svou vzdálenost od zdroje zvuku. 

\fi

>**Úloha 5.** Ze vztahu pro hladinu intenzity zvuku $L=10\log{\frac{I}{I_0}}$ 
>vyjádřete intenzitu zvuku $I$.

\iffalse

*Řešení.* Nejprve musíme osamostatnit logaritmickou funkci
$\frac{L}{10}=\log{\frac{I}{I_0}}$ a následně využijeme inverzní
funkci k logaritmické, tj. exponenciální funkci:
$$10^{\frac{L}{10}}=\frac{I}{I_0}.$$
Odtud vyjádříme intenzitu zvuku
$$I=I_0 \cdot 10^{\frac{L}{10}}.$$

\fi

>**Úloha 6.** Kolikrát se zvětší intenzita zvuku, jestliže se hladina 
>intenzity zvuku zvýší o $20\,\text{dB}$? 

\iffalse

*Řešení.* Hodnota hladiny intenzity 
zvuku se změní z hodnoty $L_1=L$ na $L_2=L+20\,\text{dB}$. Příslušné intenzity označíme $I_1$ a $I_2$.
Využijeme vztahu $I=I_0 \cdot 10^{\frac{L}{10}}$ a vyjádříme podíl $\frac{I_2}{I_1}$:
$$\frac{I_2}{I_1}=\frac{I_0 \cdot 10^{\frac{L_2}{10}}}{I_0 \cdot 10^{\frac{L_1}{10}}}=\frac{10^{\frac{L+20}{10}}}{10^{\frac{L}{10}}}=10^{\frac{L+20}{10}-\frac{L}{10}}=10^2=100.$$

Při vzrůstu hladiny intenzity zvuku o $20\,\text{dB}$ se intenzita zvuku 
zvětší stokrát.

\fi

## Literatura 
1. Kubera, Miroslav; Nečas, Tomáš; Beneš, Vojtěch. *Online učebnice fyziky pro gymnázia - Zvuk.* Dostupné z <https://e-manuel.cz/kapitoly/mechanicke-vlneni/vyklad/zvuk/> [cit. 24.10.2023].
