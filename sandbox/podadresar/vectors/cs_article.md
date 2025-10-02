---
keywords:
- vektory
- skalární součin
is_finished: False
---

# Vektory

Vektory jsou důležité v matematice i fyzice. 
V matematice se jimi zabývá lineární algebra, 
vektor je většinou definován jako orientovaná úsečka v n-dimenzionálním prostoru. 
Teoreticky ale vektor může být cokoliv u čeho má smysl to sčítat a násobit konstantou.

Ve fyzice je vektor šipka v prostoru, která je definována délkou a směrem. 
Veličiny jako rychlost a zrychlení pohybujícího se objektu, 
síly na něj působící, posunutí, elektromagnetické pole, to vše lze popsat vektory. 
Směr vektoru znázorňuje směr veličiny a délka vektoru reprezentuje velikost veličiny. 
Přestože má vektor velikost a směr, nemá polohu. 
Dvě stejně velké šipky mířící stejným směrem znázorňují ten samý vektor. 

Dalším oborem, kde se pojem vektor vyskytuje je informatika. 
Tam je vektorem často myšlen jen uspořádaný seznam položek (nemusí to být jen čísla). 
Vektory jsou efektivním způsobem, jak organizovat a ukládat objekty 
a kolekce objektů v kontejnerech pro použití například v aplikacích strojového učení.

V informatice ale existuje i oblast, kde se vektory používají tím způsobem, 
jakým jsou definovány v matematice či fyzice. Touto oblastí je prostředí počítačových her. 
Zvládnutí práce s vektory je dokonce jedním ze základních stavebních kamenů k tomu, stát se programátorem her.

Poznámka: Takových základních stavebních kamenů je třeba samozřejmě mnohem více. 
Kromě pčíslušného programovacího nástroje je třeba také znát matice transformací, 
jako je posunutí, otočení atd., které pak na vektory uplatňujeme. 
V následujících úlohách se chceme zaměřit jen na operace s vektory.

V závislosti na tom, zda vytváříte 2D nebo 3D hru mají vektory dva nebo tři rozměry 
a obecně se používají k reprezentaci geometrických vlastností objektů v herním světě.
Pro jednoduchost budeme pracovat pouze v dvourozměrném prostoru (v rovině), tedy v Kartézské souřadné soustavě. 

## Body a směrové vektory

V následujících příkladech budeme rozlišovat zadání bodů a vektorů. Současně budeme ale pamatovat na to, 
že bod $A = [a_1;a_2]$ také můžeme brát jako koncový bod vektoru $\overrightarrow{a} = (a_1;a_2)$. 

Bod má souřadnice, na rozdíl od vektoru není určen délkou a směrem. 
Bod $[0,0]$ nebo vektor $(0, 0)$ pro nás bude středem herního světa. 

Běžným případem použití vektorů je výpočet vektoru, který udává směr jednoho objektu vůči druhému. 
Vezměme si jednoduchý příklad pohybu jednoho objektu $A = [a_1;a_2]$ směrem k druhému $B = [b_1;b_2]$. 
Vektor $\overrightarrow{u}=\overrightarrow{AB}= (b_1-a_1; b_2-a_2)$ nazýváme směrový vektor.

> **Úloha 1.** Ve 2D hře máme postavu $A$ a postavu $B$ stojící na různých místech.
> Postava B jde postupně ve směru vektoru $\overrightarrow{u}$,
> poté ve směru vektoru $\overrightarrow{v}$ a poté ve směru vektoru $\overrightarrow{w}$.
> Vyjádřete vektor, který musí ujít postava $A$, jestli má jít přímo k nové pozici postavy $B$.

*Řešení.* Je jasné, že postava $B$ celkem ušla $\overrightarrow{u}+\overrightarrow{v}+\overrightarrow{w}$. 
Postavy $A$ a $B$ ale na začátku stály na různých místech, 
zbývá nám tedy určit vektor s počátečním bodem v $A$ a koncovým bodem v $B$, tedy směrový vektor $\overrightarrow{AB}$.
Víme že bod $A$ můžeme brát jako koncový bod vektoru $\overrightarrow{a}$
a bod $B$ jako koncový bod vektoru $\overrightarrow{b}$.
Pak tedy vektor $\overrightarrow{AB} = b-a$ (protože bod a vektor mají stejné souřadnice, 
používá se často i zápis $\overrightarrow{AB} = B-A$). Celkově tedy postava $A$ musí ujít $\overrightarrow{b}-\overrightarrow{a}+\overrightarrow{u}+\overrightarrow{v}+\overrightarrow{w}$.

U každé postavy v herním světě se používá i vektor ve smyslu seznamu položek. 
Jednou z položek je třeba jméno postavy, její úloha, poloha. 
Další vlastností každé postavy v herním světě je směr, 
kterým je tato postava natočena. 
K určení směru natočení se používá takzvaný normalizovaný směrový vektor, 
tedy směrový vektor délky $1$. 

Normalizované směrové vektory se používají i k uchovávání informace, 
jakým směrem se vyskytují ostatní postavy nebo objekty.

Poznámka: Důvod, proč jsou v herním světě používány normalizované verze směrových vektorů vysvětlíme později.

> **Úloha 2.** Mějme postavy $A = [-5;2]$, $B = [1;-2]$, $C = [4;-1]$.
> Určete normalizované směrové vektory postav A a B směrem k ostatním postavám.
> Nakreslete odpovídající obrazek.

*Řešení.* Pro směrový vektor $\overrightarrow{AB}$ platí $\overrightarrow{AB}= (1-(-5); -2-2) = (6;-4)$. 
Pokud ho chceme normalizovat, stačí ho vydělit jeho délkou 
$\left | \overrightarrow{AB} \right | = \sqrt{6^2+(-2)^2} = \sqrt{52}.$
Normalizovaný vektor k vektoru $\overrightarrow{AB}$ značíme $\widehat{AB}$ a platí

$$
\widehat{AB} = \frac{1}{\sqrt{52}}(6;-4) = \left(\frac{3}{\sqrt{13}};-\frac{2}{\sqrt{13}}\right) 
$$.

Obdobně

$$
\widehat{AC} = \frac{\overrightarrow{AC}}{\left | \overrightarrow{AC} \right | } = \frac{1}{\sqrt{90}}(9;-3) = \left(\frac{3}{\sqrt{10}};-\frac{1}{\sqrt{10}}\right), 
$$

$$\widehat{BC} = \left(\frac{3}{\sqrt{10}};\frac{1}{\sqrt{10}}\right),$$

$$\widehat{BA} = \left(-\frac{3}{\sqrt{13}};\frac{2}{\sqrt{13}}\right).$$

Vektor $\widehat{BA}$ jsme nemuseli počítat, protože má stejnou velikost jako vektor $\widehat{AB}$ a opačný směr. Jejich souřadnice se tedy liší jen v opačném znaménku.

![Obrázek k řešení příkladu 2](vectors_1.png) 


> **Úloha 3.** Mějme polohu postavy $A = [a_1;a_2]$ a postavy $B = [b_1;b_2]$ stojících na různých místech. Určete
> a) normalizovaný směrový vektor $\widehat{BA}$,
> b) kde se bude postava $B$ nacházet poté, co ujde tři jednotkové délky směrem k postavě $A$?

*Řešení.* a) To co jsme počítali v předchozím příkladu s konkrétními souřadnicemi nyní zapíšeme obecně. Tedy 

$$\widehat{BA} = \frac{\overrightarrow{BA}}{\left | \overrightarrow{BA} \right | } = 
\frac{\overrightarrow{(a_1-b_1;a_2-b_2)}}{\sqrt{(a_1-b_1)^2+(a_2-b_2)^2}}.$$

b) Z předchozího máme spočítaný směrový vektor jednotkové délky. Nyní stačí vynásobit ho třemi a přičíst k poloze postavy $B$. Dostáváme

$$B+3\widehat{BA} = [b_1;b_2] +3\frac{\overrightarrow{(a_1-b_1;a_2-b_2)}}{\sqrt{(a_1-b_1)^2+(a_2-b_2)^2}}.$$

## Skalární součin a jeho použití 

Výsledkem skalárního součinu dvou vektorů je skalár, tedy reálné číslo. 

> **Úloha 4.** Určete skalární součiny normalizovaných směrových vektorů z úlohy 2.

*Řešení.* 
$$
\widehat{AB} \cdot \widehat{AC} = \left(\frac{3}{\sqrt{13}};-\frac{2}{\sqrt{13}}\right) \cdot \left(\frac{3}{\sqrt{10}};-\frac{1}{\sqrt{10}}\right) = 
\frac{9}{\sqrt{130}}+\frac{2}{\sqrt{130}} = \frac{11}{\sqrt{130}}
\dot=0{,}96
$$

$$
\widehat{BA} \cdot \widehat{BC} = \left(-\frac{3}{\sqrt{13}};\frac{2}{\sqrt{13}}\right) \cdot \left(\frac{3}{\sqrt{10}};\frac{1}{\sqrt{10}}\right) = 
-\frac{9}{\sqrt{130}}+\frac{2}{\sqrt{130}} = -\frac{7}{\sqrt{130}}
\dot= -0{,}054
$$

Skalární součin dvou normalizovaných vektorů je velmi užitečný, 
protože určuje, do jaké  míry dva vektory směřují stejným nebo podobným směrem! 
Skalární součin může totiž v tomto případě nabývat hodnot v rozmezí -1 až 1, 
přičemž 1 znamená, že oba vektory směřují přesně stejným směrem, 
a -1, že směřují opačným směrem, zatímco hodnota blízká 0 znamená, 
že svírají úhel $90^{\circ}$.
Důvodem rozsahu hodnot [-1, 1] je to, že se pohybujeme v rozmezí funkčních hodnot funkce kosinus.
Pro skalární součin dvou vektorů totiž také platí vztah

$$
\vec{p} \cdot \vec{q}=\left | \vec{p} \right |\left | \vec{q} \right |\cos\alpha  
$$

> **Úloha 5.** Pozorovatel v počátku se dívá na objekt $A=[3;1]$,
> určete úhel $\alpha$ o jaký se musí otočit,
> aby směr jeho pohledu mířil přímo na objekt $B=[1;2]$.

*Řešení.* Body $A$ a $B$ budeme opět brát jako koncové body vektorů $a=(3;1)$ a $b=(1;2)$.
Ze vztahu, který platí pro skalární součin dvou vektorů vyjádříme $\cos\alpha$, 
tedy

$$ \cos\alpha =\frac{\vec{a} \cdot \vec{b}}{\left | \vec{a} \right |\left | \vec{b} \right |} $$

Po dosazení získáváme 

$$ \cos\alpha = \frac{\vec{(3;1)} \cdot \vec{(1;2)}}{\sqrt{3^2+1^2} \cdot \sqrt{1^2+2^2}} = \frac{3 \cdot 1 + 1 \cdot 2}{\sqrt{10} \cdot \sqrt{5}} = \frac{5}{\sqrt{50}} =\sqrt{\frac{25}{50}} = \frac{1}{\sqrt{2}}.$$

Buď si pamatujeme, že je to $\cos\45^{\circ}$, který je roven \frac{1}{\sqrt{2}}$, nebo hodnotu úhlu $\alpha$ vypočítáme jako $\arccos \frac{1}{\sqrt{2}}$. Pozorovatel se tedy musí otočit o úhel $45^{\circ}$.

Pokud by v zadání úlohy byly dané normalizované směrové vektory, 
jejich skalární součin by byl roven $\cos\alpha$, pro potřebnou rotaci by pak nebylo třeba dopočítávat úhel $\alpha$, 
protože v příslušné transformační matici vystupují právě kosiny a siny tototo úhlu.

Řekněme, že vytvářím hru, ve které se hráč snaží schovat před nějakými strážemi. 
Bude nás tedy zajimat, zda strážný vidí či nevidí jednotlivé hráče. 

Chceme, aby měl strážný zorné pole, jak jsme zvyklí ve většině her. 
U člověka se udává velikost zorného úhlu pro vidění oběma očima přibližně $180^{\circ}$. 
To by pro strážného bylo až příliš, takže řekněme že chceme aby jeho zorný úhel byl $170^{\circ}$. 

> **Úloha 6.** Zorný úhel strážného je $170^{\circ}$, jakých hodnot budou nabývat skalární součiny mezi jeho směrem pohledu a normalizovanými směrovými vektory k objektům, které strážný vidí?

*Řešení.* Od směru pohledu strážce k hranici zorného pole (směrem doprava i doleva) máme $85^{\circ}$. Stačí tedy vypočítat $\cos 85^{\circ} \dot= 0,087$. Skalární součiny mezi směrem pohledu strážného a normalizovanými směrovými vektory k objektům, které vidí budou nabývat hodnot mezi $0,087$ a $1$.

Do seznamu položek příslušnému strážci tedy ke směru pohledu přidáme rozmezí, 
které bude určovat jeho zorné pole. Pomocí něj pak můžeme kontrolovat, 
zda strážný hráče vidí či nevidí. 
Pro jednoduchost předhozí výsledek zaokrouhlíme na jedno desetiné místo 
a zorné pole strážného tedy omezíme hodnotou $0,1$. 

> **Úloha 7.** Určete zda strážný, umístěný v počátku, vidí hráče $A=[3;-2]$,
> jestliže směr pohledu strážného je $\left(\frac{1}{\sqrt{5}};\frac{2}{\sqrt{5}}\right)$
> a hranice pro omezení zorného pole je dána hodnotou $0,1$.

*Řešení.* Směr pohledu strážného je už normalizovaný vektor. Stačí tedy normalizovat směrový vektor od strážného k hráči $A$. Díky tomu že strážný je v počátku, stačí normalizovat vektor $\vec{a}=(3;-2)$. Platí 

$$\hat{a}=\frac{\left(3;-2\right)}{3^2+(-2)^2} = \frac{\left(3;-2\right)}{15} = \left(\frac{3}{15};\frac{-2}{15}\right).$$  

Poté už můžeme vypočítat příslušný skalární součin těchto normalizovaných vektorů, tedy 

$$\left(\frac{1}{\sqrt{5}};\frac{2}{\sqrt{5}}\right) \cdot \left(\frac{3}{\sqrt{15}};\frac{-2}{\sqrt{15}}\right) = \frac{3}{\sqrt{75}} - \frac{4}{\sqrt{75}} = -\frac{1}{\sqrt{75}} \dot= -0,12.$$ 

Strážný hráče $A$ nevidí.

Na procvičení: V čem se situace z předchozího příkladu změní, pokud strážce není v počátku?

Literatura:


