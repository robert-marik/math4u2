---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- combinatoria, probabilidad y estadística
- combinatoria
is_finished: true
---





# Round robin: un sistema justo de competición

Imagina que organizas un torneo escolar de tenis  
de mesa, ajedrez, deportes electrónicos o fútbol sala. Quieres 
que sea lo más justo posible, que cada jugador tenga 
la oportunidad de enfrentarse a todos los demás. Para eso  
sirve el sistema de todos contra todos, también conocido como round 
robin.

Su principal ventaja es la equidad: la clasificación final depende 
únicamente del rendimiento de los jugadores o equipos, y no del azar 
del sorteo de los oponentes. Por otro lado, el número de partidos aumenta 
rápidamente con el número de participantes, por lo que planificar un torneo de este tipo 
puede ser todo un reto. Y aquí es donde entra en juego 
la combinatoria, la matemática del cálculo de posibilidades.

## Torneo de fútbol sala

> **Tarea 1.** Se han inscrito 9 equipos en el torneo de fútbol  
> sala. Se juega por el sistema de liguilla, es decir, cada equipo 
> juega un partido contra cada uno de los demás. El equipo recibe 2 puntos por 
> cada victoria en un partido, 1 punto por un empate y 0 
> puntos por una derrota. La clasificación general del equipo se decide por la suma final 
> de puntos de todos los partidos.
>
> ¿Cuántos partidos hay que jugar en un torneo? ¿De cuántas 
> maneras se puede elaborar el calendario del torneo si solo hay 
> un campo disponible en el que se juegan los partidos 
> sucesivamente?



*Solución.* El número total de partidos jugados corresponde 
número de todas las parejas no ordenadas formadas a partir de nueve 
equipos. En otras palabras, corresponde al número de todas las combinaciones 
de dos elementos sin repetición formadas a partir de nueve elementos. 
Hay un total de
$$
\binom{9}{2} = 36.
$$
Para determinar el número de formas de organizar el torneo, buscamos 
en realidad el número total de combinaciones de 36 partidos, 
por lo que el número total de posibles calendarios del torneo es
$$
36! =371\,993\,326\,789\,901\,217\,467\,999\,448\,150\,835\,200\,000\,000 \doteq 3{,}72\cdot 10^{41}.
$$
Cabe señalar que si reuniéramos un número comparable 
de granos de arena, cada uno con un volumen 
del orden de $10^{-13}\,\text{m}^3$, el montón tendría 
un volumen del orden de $10^{28}\,\text{m}^3$, que es 
aproximadamente diez veces el volumen del Sol. Por lo tanto 
más que un montón, se trataría de un cuerpo celeste 
relativamente masivo.



> **Tarea 2.** Demuestra que si algún equipo en 
> el torneo de la tarea anterior obtuvo un total de 13 puntos, entonces 
> necesariamente se encuentra entre los cuatro mejores equipos del torneo.



*Solución.* Resolveremos el problema mediante un sistema de desempate. Supongamos que 5 
equipos obtienen 13 o más puntos. Dado que en cada 
partido se reparten 2 puntos entre los dos equipos, en todo el 
torneo se reparten un total de $2\cdot 36 = 72$ puntos. Sin embargo, 
entre los 5 equipos se reparten al menos 65 puntos, por lo que entre 
los cuatro equipos restantes deben repartirse como máximo los 7 
puntos restantes. 

Pero estos cuatro equipos jugarán entre sí un total de 
$\binom{4}{2}=6$ partidos y, por lo tanto, deben repartirse un total de 
12 puntos, por lo que en total habría que repartir al menos 
77 puntos, lo cual no es posible, por lo que obtenemos una contradicción. 

Por lo tanto, solo puede haber un máximo de cuatro equipos con 13 o más puntos.



## Una competición más justa

Para la próxima edición del torneo de fútbol sala de las tareas anteriores 
esta vez se inscribieron 7 equipos. Sin embargo, al elaborar el calendario 
del torneo, el organizador estableció una nueva condición: 
ningún equipo podía jugar dos partidos seguidos, 
para que los jugadores no tuvieran que jugar cansados y el torneo fuera más justo. 

Libor ideó un algoritmo para crear la secuencia deseada 
de partidos. Se basa en la siguiente tabla.  

![Tabla para crear un programa de torneo justo](math4you_00050.svg)

Cada campo en la fila $i$ y la columna $j$ 
corresponde al partido entre el equipo $(i+1)$ y el equipo $j$. La secuencia 
de partidos buscada corresponderá al orden de los campos que 
Libor selecciona gradualmente. Para mayor claridad, marcaremos estos campos 
según los equipos cuyo partido representan, es decir, $[1;2]$, 
$[3;5]$, etc. A continuación, marcaremos la diagonal más larga 
que comienza en el campo $[1;2]$ y termina en el campo $[6;7]$ como 
$D_1$, la diagonal más corta que comienza en el campo $[1;3]$ y 
termina en el campo $[5;7]$ como $D_2$, etc.

El algoritmo de Libor es el siguiente:
- primero seleccionamos los campos de la primera columna y la última fila, es decir, $[1;7]$;
- a continuación, seleccionamos por orden los campos de la diagonal $D_1$ en las columnas pares de izquierda a derecha;
- a continuación, seleccionamos por orden los campos restantes de la diagonal $D_1$ en las columnas impares de izquierda a derecha;
- a continuación, seleccionamos de izquierda a derecha todos los campos de la diagonal $D_2$;
- a continuación, seleccionamos de izquierda a derecha todos los campos de la diagonal $D_3$, y, a continuación $D_4$, etc.

Para el torneo de siete equipos, obtendremos el siguiente 
orden de partidos

$$
[1;7],\quad[2;3],\quad[4;5],\quad[6;7],\quad[1;2],\quad[3;4],\quad[5;6],
$$
$$
[1;3],\quad[2;4],\quad[3;5],\quad[4;6],\quad[5;7],\quad[1;4],\quad[2;5],
$$
$$
[3;6],\quad[4;7],\quad[1;5],\quad[2;6],\quad[3;7],\quad[1;6],\quad[2;7].
$$

> **Tarea 3.** Utilizando el algoritmo de Libor, escribe 
> la secuencia de partidos para un torneo en el que participan 9 
> equipos y compruebe que no se repita el mismo 
> equipo  en dos partidos consecutivos.



*Solución.* Al aplicar el algoritmo, obtenemos la siguiente secuencia de 36 campos y es evidente que cada dos campos consecutivos tienen todos los componentes diferentes.
$$
[1;9],\quad [2;3],\quad [4;5],\quad [6;7],\quad [8;9],\quad [1;2],\quad [3;4],\quad [5;6],\quad [7;8],\quad [1;3],\quad [2;4],\quad [3;5],
$$
$$
[4;6],\quad [5;7],\quad [6;8],\quad [7;9],\quad [1;4],\quad [2;5],\quad [3;6],\quad [4;7],\quad [5;8],\quad [6;9],\quad [1;5],\quad [2;6],
$$
$$
[3;7],\quad [4;8],\quad [5;9],\quad [1;6],\quad [2;7],\quad [3;8],\quad [4;9],\quad [1;7],\quad [2;8],\quad [3;9],\quad [1;8],\quad [2;9].
$$



> **Tarea 4.** ¿El algoritmo de Libor se aplica en general a 
> cualquier número de equipos inscritos? Si no es así, ¿a 
> cuáles? ¿Y pueden elaborar ustedes mismos la 
> secuencia requerida para estos casos?



*Solución.* Denotemos por $n$ el número de equipos inscritos (del 
contexto de la tarea se desprende que $n>1$). A partir del algoritmo 
de Libor, derivamos la siguiente secuencia de campos, que 
dividiremos en varias secciones consecutivas según su 
aparición en la tabla (en la diagonal $D_1$ debemos 
distinguir entre la paridad $n$):
$$
\begin{alignat*}{2}
&[1;n], &&\quad\text{(1. pole)}\\[3mm]
&[2;3],[4;5],\ldots , [n-1;n], &&\quad\text{(1. část diagonály } D_1\text{, liché } n) \\
&[1;2],[3;4],\ldots , [n-2;n-1], &&\quad\text{(2. část diagonály } D_1\text{, liché } n)\\[3mm]
&[2;3],[4;5],\ldots , [n-2;n-1], &&\quad\text{(1. část diagonály } D_1\text{, sudé } n) \\
&[1;2],[3;4],\ldots , [n-1;n], &&\quad\text{(2. část diagonály } D_1\text{, sudé } n)\\[3mm]
&[1;3],[2;4],\ldots , [n-2;n], &&\quad\text{(diagonála } D_2)\\
&[1;4],[2;5],\ldots , [n-3;n], &&\quad\text{(diagonála } D_3)\\
&\vdots &&\\
&[1;i+1],[2;i+2],\ldots , [n-i;n], &&\quad\text{(diagonála } D_i, \text{ kde } i\leq n-2)\\
&[1;i+2],[2;i+3],\ldots , [n-(i+1);n], &&\quad\text{(diagonála } D_{i+1})\\
&\vdots &&\\
&[1;n-1],[2;n]. &&\quad\text{(diagonála } D_{n-2})
\end{alignat*}
$$

Dos campos consecutivos que pertenecen a la misma sección no pueden contener el 
mismo número. En ambas partes de la diagonal $D_1$ podemos escribir dos campos 
consecutivos arbitrarios en la forma $[j,j+1]$ y $[j+2,j+3]$ y en 
cualquier diagonal $D_i$ para $i>1$ dos campos consecutivos arbitrarios 
tienen de nuevo la forma $[j,j+i]$ y $[j+1,j+i+1]$. Por lo tanto, basta con verificar 
en qué condiciones el último miembro de una sección puede contener el mismo número 
que el primer miembro de la sección siguiente. Estos casos especiales se evaluarán 
por separado.

**1. campo – 1. parte de la diagonal $D_1$.** El campo $[2;3]$ se conecta independientemente de la paridad $n$ al campo $[1;n]$. Por lo tanto, la condición requerida de que los cuatro componentes sean diferentes no se cumple para $n=2$ y $n=3$. 

**Parte 1 – Parte 2 de la diagonal $D_1$.** Para los valores impares de $n$ el campo $[1;2]$ se une al campo $[n-1;n]$, de donde obtenemos los casos ya mencionados $n=2$ y ~$n=3$. Para los valores pares de $n$ los campos $[n-2;n-1]$ y $[1;2]$ se unen, aquí debemos excluir además el caso $n=4$.  

**Parte 2 de la diagonal $D_1$ – diagonal $D_2$.** Para los valores impares de $n$ se suceden los campos $[n-2;n-1]$ y $[1;3]$. Por lo tanto, la condición de diversidad de los componentes no se cumple para $n\in\{2;3;4;5\}$. Si $n$ es par, se suceden los campos $[n-1;n]$ y $[1;3]$. Todos los números $n$ no excluidos hasta ahora cumplen la condición examinada.

**Diagonal $D_i$ – diagonal $D_{i+1}$.** El campo $[1;i+2]$ se une al campo $[n-i;n]$. De este modo, obtenemos cuatro posibles igualdades en las que no se cumplirá la condición dada: 
$$
n-i = 1, \qquad n-i = i + 2, \qquad n = 1, \qquad n = i+2.
$$ 
La tercera igualdad no puede ser cierta. La primera igualdad significaría que 
$i=n-1$, pero $i$ puede tomar como máximo el valor $n-2$. Si se cumpliera 
la cuarta igualdad, $i$ tomaría el valor $n-2$; sin embargo, la diagonal $D_{n-2}$ es 
la última sección con la que termina la sucesión, ya que no hay ninguna otra
diagonal que la continúe. Por último, la segunda igualdad se puede reescribir en la forma 
$i = \frac{n-2}{2}$. Si $n$ es impar, no puede ser válida; sin embargo, para cualquier 
$n$ par existe incluso un $i$ único tal que será válida. 
Por lo tanto, el algoritmo falla para cualquier $n$; par; por ejemplo, para $n=14$ es 
$i=6$, el último término de la diagonal $D_6$ es $[8;14]$ y el primer término de la diagonal 
$D_7$ es $[1;8]$.

El algoritmo de Libor funciona sin reservas para los valores impares de $n$ con excepción de 3 y 
5. Sin embargo, cabe añadir que también funciona de forma trivial para $n=2$ (dos equipos 
juegan un único partido en todo el torneo). Para los valores pares restantes de $n$, $n=3$ y $n=5$ 
ahora deberíamos intentar encontrar las secuencias requeridas de otra manera. 
Sin embargo, primero observemos que para $n=3$ y $n=4$ esto es imposible, porque

* para $n=3$ debemos ordenar tres campos $[1;2]$, $[1;3]$, $[2;3]$, pero cada 
una de estas ordenaciones no cumple la condición especificada;
* para $n=4$ elegiremos sin perjuicio de la generalidad el primer campo $[1;2]$, al que necesariamente 
debe seguir el campo $[3;4]$ y luego nuevamente $[1;2]$, lo cual no es posible.

Para los demás $n$ ya sabemos cómo encontrar las sucesiones con las propiedades requeridas. 
Dado que hay más (y más algoritmos con los que podemos encontrarlas), daremos 
al menos algunos ejemplos que obtenemos modificando el algoritmo original  
de Libor. Para $n=5$ lo modificamos de la siguiente manera:

* Primero seleccionamos los campos de la primera columna y la última fila, es decir, $[1;5]$;
* a continuación, seleccionamos sucesivamente los campos de la diagonal $D_1$ en las columnas pares de izquierda a derecha;
* a continuación, seleccionamos sucesivamente los campos restantes de la diagonal $D_1$ en las columnas impares de izquierda a derecha;
* a continuación, seleccionamos de derecha a izquierda todos los campos de la diagonal $D_3$;
* a continuación, seleccionamos de derecha a izquierda todos los campos de la diagonal $D_2$.

La secuencia resultante tiene la forma
$$
[1;5],\quad [2;3],\quad [4;5],\quad [1;2],\quad [3;4],\quad [2;5],\quad [1;4],\quad [3;5],\quad [2;4],\quad [1,3].
$$

Para los números pares $n$ distintos de 2 y 4, calculamos el número $k=\frac{n-2}{2}$. (Precisamente 
este número era «problemático» en la discusión del caso general) 
A continuación, aplicamos el algoritmo de Libor con la diferencia de que, al seleccionar 
los campos, intercambiamos el orden de las diagonales $D_{k+1}$ y $D_{k+2}$. Teniendo en cuenta que 
el resto del algoritmo es el mismo, comprobemos solo las conexiones diferentes 
de las secciones afectadas.

**Diagonal $D_k$ – diagonal $D_{k+2}$.** Al campo $[n-k;n]$ le sigue 
el campo $[1;k+3]$. Sustituyendo por $k$, ajustando y comparando los posibles componentes coincidentes 
obtenemos cuatro igualdades
$$
\frac{n+2}{2} = 1, \qquad \frac{n+2}{2} = \frac{n+4}{2}, \qquad n = 1, \qquad n = \frac{n+4}{2}.
$$
La segunda y tercera igualdad no pueden ser válidas y la primera (o cuarta) igualdad se 
cumple precisamente cuando $n=0$ (o $n=4$), lo que tampoco es válido.

**Diagonal $D_{k+2}$ – diagonal $D_{k+1}$.** Al campo $[n-(k+2);n]$ 
le sigue el campo $[1;k+2]$. Sustituyendo y modificando, deducimos de nuevo cuatro 
igualdades cuya validez infringiría la condición dada:
$$
\frac{n-2}{2} = 1, \qquad \frac{n-2}{2} = \frac{n+2}{2}, \qquad n = 1, \qquad n = \frac{n+2}{2}.
$$
Sin embargo, ninguna de las ecuaciones anteriores puede ser válida, ya que $n$ no puede ser 4, 
1 ni 2.

**Diagonal $D_{k+1}$ – diagonal $D_{k+3}$.** Al campo $[n-(k+1);n]$ 
le sigue el campo $[1;k+4]$. Al igual que en los dos casos anteriores, 
podemos deducir cuatro ecuaciones
$$
\frac{n}{2} = 1, \qquad \frac{n}{2} = \frac{n+6}{2}, \qquad n = 1, \qquad n = \frac{n+6}{2}.
$$
Las tres primeras igualdades mencionadas no pueden ser válidas por las razones expuestas 
anteriormente. La cuarta igualdad es válida para $n=6$; sin embargo, para este número no existe 
la diagonal $D_{k+3}$, ya que $k+3 = \frac{6-2}{2} + 3 = 5$. (Recordemos, 
que para $n=6$ solo se definen las diagonales $D_1$–$D_4$.) El algoritmo 
para $n=6$ termina así con la selección de los miembros de la diagonal $D_{k+1}=D_3$.

El algoritmo modificado construye así la secuencia de campos requerida para los valores pares de $n$  
distintos de 2 y 4. Por lo tanto, los únicos valores naturales de $n>1$, para los que no existe ninguna secuencia 
con las propiedades especificadas son 3 y 4.





