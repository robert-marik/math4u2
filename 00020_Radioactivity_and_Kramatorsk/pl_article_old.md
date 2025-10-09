---
keywords:
- wykładniki i logaritmy
- funkcja wykładnicza
- funkcja logarytmiczna
- radioaktywność
is_finished: true
---

# Śmiertelne mieszkanie w Kramatorsku


Mieszkanie numer 85, budynek 7, ulica Mariyi Pryimachenko, Kramatorsk (dawniej ZSRR, obecnie Ukraina), było naprawdę przeklęte i przyniosło swoim lokatorom tylko nieszczęście. W latach 1980-1989 mieszkały tu kolejno dwie rodziny, które bezradnie patrzyły, jak ich dzieci umierają na białaczkę. 18-letnia córka zmarła nagle w 1980 roku, a następnie jej 16-letni brat i matka w 1982 roku. Żadna z tych śmierci nie przyciągnęła uwagi władz, a mieszkanie zostało przekazane nowym lokatorom. Niestety, oni również nie mieli szczęścia, ponieważ ich syn wkrótce zmarł na białaczkę.

![Dom w Kramatorsku, w którym dochodziło do tajemniczych zgonów](house_no_7.jpg)

## Wypadek w kamieniołomie Karansky

Dopiero po kolejnej śmierci, dzięki uporowi nowego najemcy, mieszkanie zostało skontrolowane. Inspektorzy byli zszokowani. Odkryli, że pokój dziecięcy był silnym źródłem promieniowania radioaktywnego. Duża część ściany została wycięta i zbadana. Dokładne badanie ujawniło emiter promieniowania w panelu, taki jak używany w kamieniołomach. Oznaczenie na emiterze ujawniło, że został on utracony pod koniec lat 70 tych w kamieniołomie Karansky.

W kamieniołomach materiały radioaktywne mogą być wykorzystywane na przykład do określania gęstości skał lub poziomu napełnienia nieprzezroczystych pojemników. Pomimo faktu, że obchodzenie się z tymi materiałami podlega surowym przepisom, czasami dochodzi do wypadku. Podobny wypadek miał miejsce na początku 2023 roku w Australii. Tam emiter zaginął podczas transportu na odległość 1400 kilometrów. Poszukiwania przypominały szukanie igły w stogu siana. Emiter jest cylindrem wielkości baterii guzikowej, o wielkości 8 milimetrów. Na szczęście australijski emiter został znaleziony na drodze, po której poruszał się transport. Niestety, ukraiński emiter nie miał tyle szczęścia i skończył w panelu, który został użyty do budowy feralnego domu.

![Źródło promieniowania podobnego typu zagubione w 2023 roku w Australii](australia-capsule-size.png)

> **Zadanie 1.** Panel tworzący ścianę pokoju dziecięcego zawiera
> radioaktywny emiter. Niefortunnym zbiegiem okoliczności znajduje się on tuż obok jednego z łóżek dziecięcych. Spróbuj oszacować, o ile
> dawka promieniowania zostałaby zmniejszona, gdyby łóżko dziecka zostało przeniesione na
przeciwną stronę zagrożonego pomieszczenia. Załóżmy, że emiter promieniuje równomiernie we wszystkich kierunkach. Załóżmy również, że odległość
> nadajnika od łóżka dziecka wynosiła pół metra, a po przeniesieniu
> łóżeczka na przeciwległą stronę pokoju, odległość wzrasta do trzech metrów, czyli sześciokrotnie.

\iffalse

*Rozwiązanie.* Zgodnie z treścią zadania możemy założyć, że promieniowanie jest równomiernie rozłożone na obszarze kulistym.


Pole powierzchni kuli o promieniu $r$ jest określone wzorem:

$$S = 4 \pi r^2.$$

Z tego wynika, że powierzchnia kulista o sześciokrotnie większym promieniu ma 36 razy większą powierzchnię. Dlatego całkowita moc emitera
jest rozłożona na 36 razy większej powierzchni. W związku z tym natężenie promieniowania w sześciokrotnie większej odległości jest 36 razy niższe.

\fi

> **Zadanie 2.** Cez użyty jako źródło promieniowania radioaktywnego w opisanym zdarzeniu ma okres połowicznego rozpadu wynoszący 30 lat. Określ, ile czasu zajęłoby zmniejszenie radioaktywności o taki sam współczynnik, jak po przeniesieniu złoża, jak w poprzednim zadaniu.

\iffalse

*Rozwiązanie.* Z fizyki wiemy, że aktywność grzejnika i ilość nierozłożonego materiału są proporcjonalne i oba maleją wykładniczo z czasem zgodnie z równaniem:

$$N(t) = N_0\mathrm{e}^{-\lambda t},\tag{1}$$

* $N(t)$ oznacza ilość nierozpadłej substancji w chwili $t$;
* $N_0$ to początkowa ilość substancji;
* $\lambda$ to stała rozpadu, która charakteryzuje przewidywaną szybkość przemiany;
* $t$ to czas.

Konieczne jest zatem ustalenie, w którym momencie ilość materiału radioaktywnego jest 36 razy mniejsza. Biorąc logarytm z obu stron równania (1), otrzymujemy:

$$
-\lambda t = \ln \frac{N(t)}{N_0}\tag{2}.
$$

Ponieważ ilość zmniejsza się o połowę w ciągu trzydziestu lat ($N(30)=\frac{1}{2}N_0$), mamy:

$$
-\lambda\,30 = \ln \frac 12
$$

oraz

$$
\lambda = \frac 1{30}\ln 2.
$$ 

Podstawiając do równania (2), otrzymujemy:

$$-\frac 1{30}t\ln 2 = \ln \frac{N(t)}{N_0}$$

oraz 

$$t = -30 \frac{\ln \frac{N(t)}{N_0}}{\ln 2}.$$

Musimy określić czas, który zapewnia $\frac{N(t)}{N_0}=\frac {1}{36}$. Otrzymujemy:

$$t = -30 \frac{\ln \frac{1}{36}}{\ln 2} =
30 \frac{\ln {36}}{\ln 2} \doteq 155.$$

Poziom promieniowania spada do poziomu odpowiadającego przeniesieniu łóżka na drugą stronę pokoju po około 155 latach.

\fi

## Źródła i literatura

### Literatura

* Wikipedia, Kramatorsk radiological accident,
  <https://en.wikipedia.org/wiki/Kramatorsk_radiological_accident>,
  September 28, 2023

* <https://www.irozhlas.cz/zpravy-svet/australie-radiace-nebezpeci-varovani-radioaktivita-cesium-137-ozareni_2301311701_har>,
  September 28, 2023

* <https://edition.cnn.com/2023/02/01/australia/australia-radioactive-capsule-found-intl-hnk/index.html>, September 28, 2023

### Źródła obrazu

* Artemka, praca własna, <https://commons.wikimedia.org/wiki/File:%D0%A3%D0%BB%D0%B8%D1%86%D0%B0_%D0%9C%D0%B0%D1%80%D0%B8%D0%B8_%D0%9F%D1%80%D0%B8%D0%B9%D0%BC%D0%B0%D1%87%D0%B5%D0%BD%D0%BA%D0%BE,_7.jpg>, September 28, 2023

* <https://edition.cnn.com/2023/02/01/australia/australia-radioactive-capsule-found-intl-hnk/index.html>, September 28, 2023
                                                      



