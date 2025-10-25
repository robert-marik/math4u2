---
keywords:
- geometría analítica
- ecuación cuadrática
- sistemas de ecuaciones
- ecuación de una circunferencia
is_finished: true
---






# Optimización del rendimiento

A la hora de tomar decisiones de inversión, no basta con basarse en modelos lineales simples, ya que el mercado es 
dinámico y está lleno de incertidumbres. Por lo tanto, la creación de una cartera de inversiones óptima 
requiere un enfoque que tenga en cuenta no solo el rendimiento esperado, sino también el riesgo y otras restricciones, 
como los fondos disponibles o los requisitos de diversificación. Los rendimientos de los distintos 
activos no pueden determinarse con exactitud de antemano, ya que su comportamiento se ve influido por muchos factores, por lo que es necesario 
utilizar modelos basados en funciones cuadráticas. Este enfoque, conocido hoy en día como 
teoría moderna de carteras, sentó las bases para una nueva visión de la inversión. Por su contribución fundamental en este ámbito 
Harry Markowitz, William Sharpe y Merton Miller fueron galardonados con el Premio Nobel en 1990.

Estos problemas conducen a tareas de lo que se conoce como «programación cuadrática», un campo de la optimización matemática, 
que se ocupa de buscar extremos (normalmente mínimos o máximos) de funciones cuadráticas en un conjunto de puntos definido  
por ecuaciones y desigualdades lineales.

## Los influencers ansían el éxito

Un influencer desconocido desea aumentar el número de seguidores en Instagram y TikTok mediante la promoción
de publicaciones y anuncios pagados. Según la información disponible, calcula que una inversión de 10 000 CZK en promoción
en Instagram le reportará 1000 seguidores y que la misma cantidad invertida en publicidad en TikTok le reportará también
1000 seguidores en esta red social. Gracias a una oferta ventajosa, puede gastar un máximo de 20 000 CZK en promoción 
en Instagram y 10 000 CZK en publicidad en TikTok.

> **Tarea 1.** ¿Cuánto dinero debe gastar un influencer en publicidad y promoción en cada red social 
> si quiere acercarse lo más posible a tener 3000 seguidores en Instagram y 2000 seguidores 
> en TikTok?



*Solución.* Si designamos con $x$ el tamaño de la inversión en promoción en Instagram en decenas de miles y, de forma similar, con $y$ 
el tamaño de la inversión en publicidad en TikTok, entonces el valor óptimo de los costes totales debe cumplir las condiciones 
$$
0\leq x \leq 2 \qquad\text{a}\qquad 0\leq y\leq 1,
$$
es decir, se encuentra dentro del rectángulo. En el mismo sistema de coordenadas también podemos marcar el punto que indica
el valor objetivo del número de seguidores. Si $x$ es el número de seguidores en Instagram en miles y $y$
el número de seguidores en TikTok en miles, entonces se trata del punto con coordenadas $[3,2]$.

Por lo tanto, buscamos el punto que se encuentra dentro del rectángulo dado y que tiene la menor distancia desde el punto $[3,2]$.

La distancia entre cualquier punto $[x,y]$ y el punto $[3,2]$ viene dada por la relación 
$$
v(x,y)=\sqrt{(x-3)^2+(y-2)^2}.
$$
Dado que la raíz cuadrada es una función creciente, si $0\leq a<b$ entonces necesariamente también $\sqrt{a}<\sqrt{b}$.
Por lo tanto, para minimizar el valor $\sqrt{(x-3)^2+(y-2)^2}$ basta con minimizar el valor $(x-3)^2+(y-2)^2$.

Para cualquier $c>0$ la igualdad 
$$
  (x-3)^2+(y-2)^2=c
$$
corresponde a una circunferencia con centro en el punto $[3,2]$ y radio $\sqrt{c}$, es decir, nuestra tarea consiste en encontrar 
la circunferencia con el radio más pequeño posible que tenga una intersección no vacía con el rectángulo dado. La situación
se muestra en la figura, a partir de la cual podemos estimar la solución. 

![Solución de la Tarea 1](math4you_00051_01.svg)

De aquí vemos que la solución es el punto $[2,1]$. Pero, ¿es realmente cierto? En la imagen vemos que la circunferencia resultante 
toca el rectángulo dado en el vértice superior derecho. Esto significa que la intersección de esta circunferencia con la recta que determina el lado superior 
del rectángulo y la intersección de la circunferencia con la recta que determina el lado derecho del rectángulo deben ser iguales. En otras palabras, los sistemas
$$
\begin{align*}
(x-3)^2+(y-2)^2&=c\\  
y&=1
\end{align*}
$$
a 
$$
\begin{align*}
  (x-3)^2+(y-2)^2&=c\\ 
  x&=2
\end{align*}
$$
deben tener al menos una solución común. No podemos resolver cada sistema por separado, porque obtendríamos una ecuación 
cuadrática con dos incógnitas. Sin embargo, sustituyendo $x=2$ a $y=1$ dostaneme dvojici rovnic
$$
\begin{align*}
  (x-3)^2+1&=c\\ 
  1+(y-2)^2&=c,
\end{align*}
$$
de lo que se deduce que necesariamente 
$$
  (x-3)^2+1=1+(y-2)^2
$$
o 
$$
  (x-3)^2=(y-2)^2,
$$
lo que, tras elevar al cuadrado, da
$$
|x-3|=|y-2|.
$$
Esta igualdad se cumple claramente para el punto $[2,1]$. Por lo tanto, vemos que se acercará más a su objetivo si invierte
la cantidad máxima de 20 000 CZK en promoción en Instagram y 10 000 CZK en publicidad en TikTok.



> **Tarea 2.** ¿Cómo cambia la solución de la tarea 1 si el objetivo es alcanzar 1000 
> seguidores en Instagram y 3000 en TikTok?



*Solución.* En este caso, minimizamos la distancia desde el punto 
$[1,3]$. La situación se presenta de la siguiente manera.

![Solución de la Tarea 2](math4you_00051_02.svg)

La solución será, por lo tanto, un punto situado en la recta $y=1$, lo que nos lleva al sistema
$$
\begin{align*}
(x-1)^2+(y-3)^2&=c\\ 
y&=1.
\end{align*}
$$ 
Se trata de un sistema de ecuaciones cuadráticas y lineales con tres incógnitas, del que fácilmente podemos obtener una ecuación 
cuadrática con dos incógnitas
$$
(x-1)^2+4=c.
$$
En la imagen vemos que la circunferencia buscada con el radio más pequeño solo toca el rectángulo dado, 
es decir, el número $c$ debe ser tal que la ecuación cuadrática solo tenga una solución (si no tiene ninguna, 
el radio es pequeño y la circunferencia tiene una intersección vacía con el rectángulo; si tiene dos soluciones diferentes, entonces necesariamente existe 
una circunferencia con un radio ligeramente menor que, de nuevo, tiene una intersección no vacía con el rectángulo). La solución de la ecuación 
cuadrática es
$$
x_{1,2}=\pm\sqrt{c-4}+1.
$$
La solución será única (o ambas soluciones se fusionarán), solo para $c=4$. En tal caso $x=1$, es decir, la solución es el punto 
$[1,1]$. Por lo tanto, en este caso basta con gastar 10 000 CZK en promoción en Instagram y 10 000 CZK en publicidad en TikTok.




