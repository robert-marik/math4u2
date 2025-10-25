---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- geometría analítica
- optimización
- ecuación general de una recta
- ecuación general de un plano
is_finished: true
---

# Optimización 

## Programación lineal

La programación lineal es un método matemático utilizado para encontrar 
la mejor solución a un problema concreto. Es una técnica que se 
centra en maximizar o minimizar una función lineal bajo ciertas 
restricciones, que también se expresan como ecuaciones o inecuaciones lineales.

Esta área no empezó a atraer la atención de los matemáticos hasta después de la Primera Guerra 
Mundial. El primero de ellos fue Lenoid Kantorovich, quien, sin embargo, tuvo que 
abandonar este trabajo debido a la represión gubernamental de la época (y, posteriormente, al temor por su vida).
Porque en la Unión Soviética, con su economía controlada de forma centralizada, 
no era buena idea optimizar los procesos de producción (por
ejemplo, consiguió aumentar la eficacia de la producción hasta el 94% en una fábrica, sólo para que 
le dijeran que todas las fábricas tenían que aumentar su eficacia de la misma 
manera).

El verdadero punto de inflexión en el desarrollo de la programación lineal fue 
la publicación del llamado algoritmo simplex para resolver estos problemas en 
1947. Su autor es el matemático estadounidense George Dantzig, que empezó 
a trabajar en esta área durante la Segunda Guerra Mundial en un esfuerzo 
por optimizar ciertos procesos en el ejército de Estados Unidos. Lo llamaron
*métodos de programación con calculadoras de sobremesa*. En su 
primera conferencia técnica sobre el tema, habló de *programación en una estructura 
lineal*, que posteriormente se acortó a sólo *programación lineal*.
La palabra *programación* es una reminiscencia de la terminología militar, 
que se refiere a la planificación o programación del entrenamiento, la logística o 
el despliegue de equipos.

Ilustraremos los principios con los siguientes sencillos ejemplos.

## Optimización de la producción en una planta de torrefacción 

> **Tarea 1.**  Berenika y Petr abrieron una nueva cafetería con torrefacción, donde 
> empezaron a producir dos mezclas de café: de verano y exótico. La mezcla de verano 
> se elabora con granos de café etíope dulces en un 40\,\% y granos de café peruano jugosos en un 60\,\%  
> La mezcla exótica se elabora con los mismos  
> granos, pero en una proporción de 3:1 (esta vez hay más café etíope). Hay 
> $90\,\text{kg}$ de café etíope y $70\,\text{kg}$ de café peruano. Un kilo de la mezcla de verano se  
> vende por 650 CZK y un kilo de la mezcla exótica por 800 CZK. ¿Qué cantidad de 
> mezcla deben mezclar Berenice y Peter de los granos de café disponibles para 
> maximizar su beneficio?

\iffalse

*Solución.* Primero tenemos que matematizar todo el problema. Por lo tanto, 
empezamos indicando la cantidad de la mezcla de verano como $x$ y la cantidad 
de la mezcla exótica como $y$. Independientemente de la cantidad producida de cada  
mezcla, podemos expresar el beneficio $z$ de su venta mediante la fórmula
$$
z=650x+800y.
$$
Está claro que no se puede producir una cantidad negativa, es decir, hay que pagar obligatoriamente
$$
  x\geq0\quad \text{a zároveň}\quad y\geq0. \tag{1}
$$
Ahora bien, hay que tener en cuenta que no disponemos de una cantidad ilimitada de granos de café. El consumo total de café etíope, 
dadas las proporciones de mezcla de, puede expresarse como
$$
  0{,}4x+0{,}75y 
$$
y en el caso del café peruano es
$$
  0{,}6x+0{,}25y.
$$
Junto con la cantidad disponible obtenemos un par de condiciones
$$
  0{,}4x+0{,}75y\leq90 \quad\text{a zároveň}\quad\quad 0{,}6x+0{,}25y\leq70. \tag{2}
$$
El conjunto de puntos que satisfacen las condiciones $(1)$ y $(2)$ se 
se representa en en la figura siguiente,  
con la recta límite $0{,}4x+0{,}75y=90$ dibujada en verde y la recta $0{,}6x+0{,}25y=70$ dibujada en azul.

![Área adaptada a las condiciones](00032_obr_1.svg)

En la zona sombreada están todos los puntos cuyas coordenadas $x$ 
y $y$ corresponden a posibles soluciones de nuestro problema. Pero, ¿cómo encontrar el punto con 
ganancia máxima, es decir, el punto en el que el valor de la expresión $z=650x+800y$ es máximo?

Podemos darnos cuenta de que esta expresión es la ecuación de un plano en el espacio tridimensional. 
Si consideramos sólo la parte de este plano que está por encima de la región sombreada, obtenemos un cuadrilátero 
en el espacio.

En lugar de dibujar una imagen espacial, dibujamos los llamados *contornos* en la imagen. Se trata de líneas con las ecuaciones
$$
650x+800y=c
$$
para el $c$.correspondiente. El significado de estas curvas de nivel es similar al de las curvas de nivel de 
un mapa. Sólo que en lugar de puntos de la misma altitud, nuestros 
contornos conectan puntos en los que obtenemos la misma ganancia.

Este procedimiento produce una imagen con contornos dibujados en marrón.

![Área adaptada a las condiciones dadas](00032_obr_2.svg)

Pero, ¿cómo determinamos el valor adecuado de $c$? Afortunadamente, no tenemos que hacer ningún cálculo 
complicado, sino que podemos hallarlo a partir de nuestra figura. Para $c=0$ obtenemos 
una línea que pasa por el origen, y como todos los contornos difieren sólo 
por el valor de $c$, todas las líneas marrones deben ser paralelas. A partir de aquí, 
podemos ver en que el máximo (los contornos se mueven hacia el noreste a medida que $c$  
aumenta) estará en el punto donde se cruzan las líneas azul y 
verde. 

Por lo tanto, las coordenadas de este punto pueden hallarse como solución de un sistema de ecuaciones lineales con dos incógnitas
$$
\begin{align*}
0{,}4x+0{,}75y&=90 \\
0{,}6x+0{,}25y&=70.
\end{align*}
$$
Es un punto con coordenadas $\left[\frac{600}{7},\frac{520}{7}\right]$. 
Sustituyendo estos valores en la expresión $z=650x+800y$ se obtiene el valor 
del beneficio máximo de aproximadamente $115\,143\,\text{Kč}$. Esto se conseguirá, 
si Berenika y Petr producen $600/7\,\text{kg}$, tj. 
přibližně $85{,}71\,\text{kg}$ letní směsi a $520/7\,\text{kg}$, es decir, 
aproximadamente $74{,}29\,\text{kg}$ de la mezcla exótica. 

*Nota.* El hecho de que la solución haya salido en la intersección de dos líneas límite 
no es una coincidencia. Para estos problemas, en los que todas las funciones son sólo lineales, 
la solución está siempre en uno de los vértices del polígono (si 
existe) que define todos los puntos admisibles. Esto también se puede utilizar en 
el caso de problemas con un número mucho mayor de incógnitas. 

Basta con encontrar todos los vértices y comparar los valores funcionales. Sin embargo, 
este uso de la llamada fuerza bruta tiene sus trampas: puede ser computacionalmente muy 
exigente y requiere tener garantizada la existencia de una solución. No obstante, 
esta idea de fue la base del primer algoritmo muy eficiente (y aún utilizado hoy en día) 
para resolver este tipo de problemas. Con él, se recorren sistemáticamente los vértices 
(es decir, no necesariamente todos).

\fi

## El mejor aparcamiento

> **Tarea 2.** Un promotor local ha decidido comprar 
> una fábrica de cintas de vídeo y casetes. 
> La fábrica no tiene ningún uso hoy en día, por lo que será 
> demolida para dar paso a un aparcamiento P+R  
> para coches y un aparcamiento 
> para camiones. Sin embargo, el promotor está resolviendo ahora 
> el problema de cómo establecer la capacidad para los distintos tipos de 
> coches. El espacio total disponible será de $480\,\text{m}^2$. 
> Una plaza de aparcamiento para un coche ocupará $12\,\text{m}^2$, 
> mientras que para un camión será de $30\,\text{m}^2$. 
>
>Sin embargo, la Autoridad de Edificación también exige que la capacidad para 
>coches personales sea al menos el doble que para 
>camiones, pero también debe haber al menos 6 
>plazas de aparcamiento para camiones. 
>
>Determinar el número óptimo de plazas de aparcamiento para coches y 
>amiones, que cumplirá todas 
>las condiciones anteriores y al mismo tiempo maximizará el beneficio de un 
>aparcamiento lleno, si por cada plaza de aparcamiento para coches 
>coches se pagará 100 CZK y por camiones 400 CZK.

\iffalse

*Solución.* Podemos proceder de forma similar al ejemplo  
anterior, pero teniendo en cuenta que esta vez 
el número de plazas de aparcamiento debe ser entero. 
Si designamos como $x$ el número de plazas de aparcamiento
para coches y como $y$ el número de plazas de aparcamiento 
para camiones, entonces nuestro objetivo es maximizar el beneficio 
$z$ dado por 
$$
z=100x+400y.
$$
Además, de estas condiciones se derivan las siguientes limitaciones.

| Condición  | Justificación | 
| ------------- | ------------- | 
| $y\geq 6$  | requisito de número mínimo de camiones  | 
| $2y\leq x$  | requisito de tipos de plazas de aparcamiento  | 
| $12x+30y\leq480$ | capacidad de suelo disponible  | 
| $x,y\in\mathbb{N}\cup\{0\}$  | los números deben ser números naturales o eventualmente cero | 

El conjunto que satisface todas estas condiciones se 
representa en la figura siguiente. Se trazan las líneas 
$y=6$ (en verde), $2y=x$ (en marrón), $12x+30y=480$ 
(en azul) y los contornos $100x+400y=c$ para distintos 
valores $c$ (en rojo). Cuanto mayor es $c$, más "arriba a la derecha" están los contornos.

En rosa se dibuja un polígono que 
cumple todas las condiciones menos la última. 
Los puntos negros son entonces todos los puntos que también satisfacen esta 
condición, es decir, que sólo tienen números naturales 
como coordenadas (el cero está descartado).

![Área adaptada a las condiciones](00032_obr_3.svg)

La figura muestra que el máximo estará en 
que sea el punto superior derecho. Pero, 
¿cuáles son sus coordenadas? 

Como es la intersección de las líneas azul y marrón, 
podemos determinar sus coordenadas resolviendo el sistema 
de ecuaciones
$$
\begin{align*}
2y&=x\\  
12x+30y&=480 
\end{align*}
$$
Su solución es el par $[160/9,80/9]$, pero
no es entero.

Si observamos detenidamente la figura y tenemos en cuenta la dirección 
podemos estimar que el máximo que buscamos se obtiene para $y=8$. Al mismo tiempo, vemos que 
el punto negro con este valor se encuentra sobre la recta azul. Así, tras introducir 
$y=8$ en la ecuación de esta recta, obtenemos $x=20$. 

Por tanto, el beneficio máximo de $5200$ CZK se alcanzará en 
caso en el que se construyan $20$ de plazas de aparcamiento 
para coches y $8$ de plazas de aparcamiento para camiones. 

Como comprobación, podemos, por supuesto, determinar todos los 
puntos enteros que satisfacen las restricciones y verificar que 
ninguno de ellos tiene un valor de $100x+400y$ mayor que 
o igual a $5200$.

\fi

