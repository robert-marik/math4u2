
# Math4u projekt

Pracovní listy pro projekt Math4you. 

Tikety apod na <https://math4u.vsb.cz/>

# Markdown, základy syntaxe

## Hlavička

```
---
keywords:
- klicove slovo
- dalsi klicove slovo
is_finisshed: True
---
```

## Nadpisy
```
# Hlavní

## Podnadpis

### Ještě nižší úroveň nadpisu
```

## Obrázky

```
![Popisek, překládá se](jmeno_souboru_nepreklada_se.jpg)
```

## Odkazy

V této větě je odkaz na [Wikipedii](https://cs.wikipedia.org/wiki/Hlavn%C3%AD_strana).

```
V této větě je odkaz na [Wikipedii](https://cs.wikipedia.org/wiki/Hlavn%C3%AD_strana).
```

## Odrážky a číslování

```
Koupit:

* rohlíky
* chleba
* jogurty
  * vanilkový
  * oříškový
  * rumový
  
Zaplatit

1. obědy děckám
1. poplatek za psa
1. příspěvek JČMF
1. popelnice
```


Koupit:

* rohlíky
* chleba
* jogurty
  * vanilkový
  * oříškový
  * rumový
  
Zaplatit:

1. obědy děckám
1. poplatek za psa
1. příspěvek JČMF
1. popelnice

## Poznámky pod čarou[^1]

[^1]: Toto je moje poznámka pod čarou.

```
This is link[^1] to my footnote.

Another text

[^1]: The footnote is at the end.
```

## Matematika

* Pomocí dolarů nebo dvojice dolarů.
* Zpravidla není nutné překládat.
* Někdy může dělat neplechu zlom řádku před dolarem nebo mezi dolary.

Pythagorova věta $$a^2+b^2=c^2$$ udává vztah mezi odvěsnami $a$ a $b$ a přeponou $c$ v pravoúhlém trojúhelníku. 
Druhá mocnina přepony vystupuje i v rovnici $$E=mc^2, \tag{E}$$ jejímž autorem je Einstein. Na rovnici (E) se budeme 
odkazovat ručně a nebudeme se spoléhat na automatické číslování. 

```
Pythagorova věta $$a^x+b^2=c^2$$ udává vztah mezi odvěsnami $a$ a $b$ a přeponou $c$ v pravoúhlém trojúhelníku. 
Druhá mocnina přepony vystupuje i v rovnici $$E=mc^2, \tag{E}$$ jejímž autorem je Einstein. Na rovnici (E) se budeme 
odkazovat ručně a nebudeme se spoléhat na automatické číslování. 
```

## Tabulky

| First Header  | Second Header | Tvrzení | Autor |
| ------------- | ------------- | --- | --- |
| Content Cell  | Content Cell  | $E=mc^2$ | Einstein |
| Content Cell  | Content Cell  | $\sqrt{2}\not\in\mathbb{Q}$ | Pythagoras | 


```
| First Header  | Second Header | Tvrzení | Autor |
| ------------- | ------------- | --- | --- |
| Content Cell  | Content Cell  | $E=mc^2$ | Einstein |
| Content Cell  | Content Cell  | $\sqrt{2}\not\in\mathbb{Q}$ | Pythagoras | 
```


