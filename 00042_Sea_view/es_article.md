---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- geometría en el plano
- trigonometría
is_finished: true
---

# Vistas al mar

¿Alguna vez, paseando por la orilla del mar,  
te has preguntado, mirando al horizonte, 
hasta dónde podrías llegar a ver realmente? ¿Y si hubiera 
algo al otro lado de la orilla, podría verlo?

Para ser más específicos, pasemos por un momento a 
uno de los destinos vacacionales más populares de Europa: 
Croacia, en la costa adriática, el monte Sveti Jure. 
Podemos leer la siguiente información sobre esta montaña[^1]: 

[^1]: www.chorvatsko.cz

*Sveti Jure* (San Jorge) es el pico más alto (1762 m sobre el nivel del mar) 
del Biokovo, una zona caliza que se extiende 36 km 
paralela a la costa y separa la Riviera de Makarska 
de la zona interior llamada Zahorie Dálmata. Se alza 
sobre la costa como un enorme muro de piedra. Debido a sus 
peculiaridades geológicas y belleza natural, parte 
de él fue declarado área paisajística protegida en 1981 
(Parque Natural del Biokovo con una superficie de 196 kilómetros cuadrados).

El pico de Sveti Jure se caracteriza por la construcción 
de una emisora de televisión, visible durante gran parte 
del recorrido a través del paisaje montañoso. La vista desde la cima del mar hacia 
el interior es inolvidable con buen tiempo y buena 
visibilidad. Lamentablemente, no hay posibilidad 
de refrigerios.

![Pico Sveti Jure.](sveti_jure.jpg)

> **Tarea 1.** Si nos situamos en la cima de Sveti Jure y miramos el mar, ¿a qué distancia de nosotros se encuentra un punto en el horizonte a nivel del mar?

\iffalse

*Solución.* Para simplificar, suponemos que la Tierra es 
una esfera con un radio de $6371\,\text{km}$. Sea $S$ el centro 
de la Tierra, el punto $V$ nuestra posición (la cima del Monte Sveti Jure) y $H$ 
cualquier punto de la superficie del mar en el horizonte. La intersección 
de la esfera con el plano $SVH$ es una circunferencia con el radio de la Tierra, 
cuya tangente es la recta $VH$. Por lo tanto, el ángulo 
$VHS$ es recto (véase la figura).

![Solución de la Tarea 1](math4you_00042_01.svg)

Sabemos que $\lvert SH \rvert = 6371\,\text{km}$ y 
$\lvert SV \rvert  = 6372{,}762\,\text{km}$ (sumamos 
la altura de la montaña al radio de la Tierra). 
Usando el teorema de Pitágoras para un triángulo rectángulo $VHS$ 
calculamos la longitud del lado $VH$: 
$$
\lvert VH \rvert = \sqrt{\lvert SV \rvert ^2 - \lvert SH \rvert ^2} \doteq 150\,\text{km}.
$$
Esta longitud también es la distancia buscada al horizonte.

\fi

>**Tarea 2.** ¿Es posible ver desde la cima del Sveti Jura, al otro lado 
del mar, la cima del Monte Calvo (1056 m s. n. m.) en 
la península italiana de Gargano? Monte Calvo está a aproximadamente 
210 km de Sveti Jure y no hay ningún obstáculo terrestre 
entre ambos lugares. Solo el horizonte 
impide una vista perfecta.

\iffalse

*Solución.* Resolveremos el problema considerando una montaña 
hipotética de la misma altura que Monte Calvo, cuyo pico 
esté en el horizonte. Por lo tanto, la vista de esta montaña queda oculta 
por el horizonte. Señalemos el pico de esta montaña con $M$ y señalemos además con 
$M_0$ la proyección perpendicular del punto $M$ al nivel del mar y con 
$V_0$ la proyección perpendicular del punto $V$.

![Solución de la Tarea 2](math4you_00042_02.svg)

Nuestro objetivo será determinar la distancia entre las dos montañas, es decir, la longitud 
del arco $M_0V_0$. Si es menor de $210\,\text{km}$ 
(la distancia real aproximada entre las montañas), Monte Calvo no será visible desde 
la cima de Sveti Jure.

Sea $\alpha$ el tamaño del ángulo $VSH$ y $\beta$ el tamaño del 
ángulo $MSH$; a partir de la longitud conocida de la hipotenusa y el lado 
del triángulo rectángulo $VHS$ obtenemos
$$
\cos\alpha = \frac{6371}{6372{,}762} \Longrightarrow \alpha \doteq 1^{\circ}\,20'\,51''.
$$
De manera similar, a partir de la longitud conocida de la hipotenusa y el lado 
en el triángulo rectángulo $MHS$ obtenemos
$$
\cos\beta = \arccos \frac{6371}{6372{,}056} \Longrightarrow \beta \doteq 1^{\circ}\,3'\,35''.
$$
La longitud del arco $M_0V_0$, que corresponde a un ángulo de 
tamaño $\alpha + \beta$, se determina entonces a partir de la proporcionalidad directa 
y la longitud conocida de todo el círculo:
$$
\frac{\alpha + \beta}{360^{\circ}}\cdot 2\pi\cdot 6371 \doteq 268\,\text{km}.
$$
La montaña de similar altura Monte Calvo está más cerca, su cima 
está por lo tanto sobre el horizonte y podemos verla (con buena 
visibilidad) desde la cima de Sveti Jure.

\fi

## Referencias y bibliografía

### bibliografía

* Chorvatsko.cz. *Sveti Jure* (online). Dostupné z https://www.chorvatsko.cz/stdal/svjure.html (cit. 12. 12. 2024).

### Fuente de las imágenes

* Sveti Jure, SKas – Vlastní dílo, CC SA 4.0, dostupné z https://upload.wikimedia.org/wikipedia/commons/7/70/The_highest_peak_Sv_Jure_\%281762_m\%29_in_Biokovo_Nature_Park.jpg (cit. 12. 12. 2024).



