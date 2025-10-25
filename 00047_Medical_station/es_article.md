---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- funciones
- función lineal
- valor absoluto
- optimización
is_finished: true
---

# Puesto médico en una carrera de atletismo

Imagina que estás ayudando a organizar una gran carrera. Hay decenas de corredores preparándose para salir a la pista 
y tu tarea es decidir dónde colocar el puesto médico para que sea lo más útil posible. 
¿Debería estar cerca de la salida? ¿O mejor en algún punto intermedio? ¿Y si hay más puntos de control en la pista? 
¿Cuál sería el lugar adecuado, desde el que se pueda llegar a todos los demás con la misma facilidad?

Puede parecer sencillo, pero si lo piensas bien, te darás cuenta de que encontrar la mejor ubicación posible no es 
tan fácil. En las siguientes tareas analizaremos esta situación. Y quién sabe, quizá gracias a nosotros el corredor llegue 
sano y salvo a la meta.

>**Tarea 1.** En una pista de atletismo de 45 km hay tres puestos de control 
>y es necesario colocar puestos de socorristas. El primer puesto de control está 
>situado en el kilómetro 13, el segundo en el kilómetro 26 y el tercero en el kilómetro 37. 
>Dado que el puesto médico debe estar lo más cerca posible de los puestos de control, 
>la salida y la meta, el organizador de la carrera quiere instalarlo de manera que la suma de las distancias desde él 
>hasta las cinco ubicaciones mencionadas sea lo más pequeña posible.
>
>¿En qué kilómetro de la ruta debe el organizador instalar el puesto de socorro? 
>¿Es esa la única ubicación que debe elegir? Supongamos que la carrera termina en un lugar distinto 
>al de inicio y que no existe un trayecto más corto entre los puestos de socorro que el recorrido de la carrera.

\iffalse

*Solución.* Supongamos que hay un puesto médico en el kilómetro $x$ de la ruta de carrera. 
La distancia desde la salida es entonces igual a $x\,\text{km}$, desde el primer puesto 
$\lvert x - 13 \rvert\,\text{km}$, del segundo puesto de socorro $\lvert x - 26 \rvert\,\text{km}$, 
del tercer puesto $\lvert x-37 \rvert\,\text{km}$ y de la meta $(45-x)\,\text{km}$. 
Por lo tanto, queremos encontrar el valor mínimo de la función
$$
\begin{align*}
f(x) &= x + \lvert x - 13 \rvert + \lvert x - 26 \rvert + \lvert x-37 \rvert + (45-x) = \\
&= \lvert x - 13 \rvert + \lvert x - 26 \rvert + \lvert x-37 \rvert + 45
\end{align*}
$$
en el intervalo $\langle 0;45\rangle$.

La gráfica de la función $f$ en este intervalo es una línea quebrada compuesta por cuatro 
segmentos consecutivos que conectan sucesivamente los puntos $[0;121]$, 
$[13;82]$, $[26;69]$, $[37;80]$ y $[45;104]$. Las segundas coordenadas de los puntos mencionados 
se obtienen sustituyendo las primeras en la fórmula de la función $f$. 

 ![Gráfica de la función $f$](math4you_00047_01.svg)

De este gráfico se desprende que la función $f$ tiene su valor mínimo precisamente
en el punto $x=26$, es decir, justo en el segundo puesto. Allí (y en ningún otro lugar) es donde 
debería estar el puesto de los servicios médicos.

*Nota*.La tarea también se puede resolver de otra manera, sin funciones ni valores 
absolutos. Representemos el recorrido de la carrera con un segmento $SC$, en el que se sitúan
los puntos $K_1$, $K_2$ y $K_3$ de manera que su posición corresponda a la posición 
del primer, segundo y tercer punto de control del recorrido.

 ![Ubicación de los puntos $K_1$, $K_2$ y $K_3$ en el segmento $SC$](math4you_00047_02.svg)

Nuestra tarea consiste en colocar en el segmento $SC$ el punto $Z$ de tal manera que la suma 
$$
\lvert SZ \rvert + \lvert K_1Z \rvert + \lvert K_2Z \rvert + \lvert K_3Z \rvert + \lvert CZ \rvert \tag{$\star$}
$$
sea lo más pequeña posible. Examinaremos el valor de esta suma en función de, 
en cuál de los segmentos $SK_1$, $K_1K_3$ y $K_3C$ se encuentra el punto $Z$.

Si se cumple $Z\in SK_1$, se puede modificar la suma $(\star)$ de la siguiente manera:
$$
\overbrace{\lvert SZ \rvert + \lvert CZ \rvert}^{45}{} + \lvert K_1Z \rvert + {}\overbrace{\lvert K_2Z \rvert}^{\lvert K_1Z \rvert + 13}{} + {}\overbrace{\lvert K_3Z \rvert}^{\lvert K_1Z \rvert + 24} = 3\cdot \lvert K_1Z \rvert + 82.
$$
Para $Z\in K_1K_3$ modificaremos la expresión examinada de la siguiente manera:
$$
\overbrace{\lvert SZ \rvert + \lvert CZ \rvert}^{45}{}  + {}\overbrace{\lvert K_1Z \rvert + \lvert K_3Z \rvert}^{24}{} + \lvert K_2Z \rvert = \lvert K_2Z \rvert + 69.
$$
Y, por último, para $Z\in K_3C$ modificamos la suma $(\star)$ de la siguiente manera:
$$
\overbrace{\lvert SZ \rvert + \lvert CZ \rvert}^{45}{}  + \overbrace{\lvert K_1Z \rvert}^{\lvert K_3Z \rvert + 24}{} + {}\overbrace{\lvert K_2Z \rvert}^{\lvert K_3Z \rvert + 11}{} + \lvert K_3Z \rvert = 3\cdot \lvert K_3Z \rvert + 80.
$$

Si comparamos las tres expresiones, vemos que el valor más pequeño lo tendrá 
la suma $(\star)$ precisamente cuando $Z\in K_1K_3$ y además $Z=K_2$ (el valor de la suma 
será en ese caso $69$). Por lo tanto, el puesto médico debe estar 
en el lugar del segundo puesto de control.

\fi

>**Tarea 2.** ¿Cómo cambiaría la solución de la tarea anterior si hubiera  
cuatro puestos, concretamente en los kilómetros 17, 30, 35 y 40?

\iffalse

*Solución.* Al igual que en la solución de la tarea 1, elaboramos la fórmula de la función
$$
\begin{align*}
g(x) &= x + \lvert x-17 \rvert + \lvert x-30 \rvert + \lvert x-35 \rvert + \lvert x-40 \rvert + 45-x =\\
&=\lvert x-17 \rvert + \lvert x-30 \rvert + \lvert x-35 \rvert + \lvert x-40 \rvert + 45,
\end{align*}
$$
cuya gráfica es una línea quebrada compuesta por cinco segmentos 
consecutivos que conectan sucesivamente los puntos $[0;167]$, $[17;99]$, $[30;73]$, 
$[35;73]$, $[40;83]$ y $[45;103]$. 

 ![Gráfica de la función $g$](math4you_00047_03.svg)

Ahora se puede ver en el gráfico que la función $g$ 
alcanza sus valores mínimos en cualquier punto del intervalo $\langle 30;35 \rangle$.Por lo tanto, 
el puesto médico puede estar en cualquier lugar entre el segundo y el tercer puesto 
de control.

*Nota.* También podemos resolver este problema de forma similar a la segunda solución 
de la tarea anterior. En el segmento $SC$ colocamos los puntos $K_1$, $K_2$, $K_3$, $K_4$ 
como se muestra en la figura. 

 ![Ubicación de los puntos $K_1$, $K_2$ a $K_3$ en el segmento $SC$](math4you_00047_04.svg)

Ahora vamos a examinar el valor de la suma $\lvert SZ \rvert + \lvert K_1Z \rvert + \lvert K_2Z \rvert + \lvert K_3Z \rvert + \lvert K_4Z \rvert + \lvert CZ \rvert$ 
en función de en cuál de las cinco partes del segmento $SC$ se encuentra el punto $Z$. 

No vamos a resolver la tarea en detalle de esta manera, pero al menos mencionaremos 
el caso $Z\in K_2K_3$, para el cual podemos modificar la suma obtenida a

$$
\overbrace{\lvert SZ \rvert + \lvert CZ \rvert}^{45}{} + \overbrace{\lvert K_1Z \rvert + \lvert K_4Z \rvert}^{23}{} + \overbrace{\lvert K_2Z \rvert + \lvert K_3Z \rvert}^{5}=73.
$$
Así, se puede ver que para cualquier punto $Z\in K_2K_3$ la suma tiene el 
mismo valor.

\fi

Podemos generalizar la tarea.

> **Tarea 3.** En la pista de carreras hay $n$ puestos diferentes. 
> ¿Dónde debemos colocar el puesto médico para que la suma de las distancias 
> del puesto médico a todos los puestos de control, a la salida y a la 
> meta sea lo más pequeña posible?

\iffalse

*Solución.* Supongamos que el puesto sanitario se encuentra en el kilómetro $x$ 
de una ruta de $d\,\text{km}$ de longitud y que los puestos de control se encuentran sucesivamente 
en los kilómetros $x_1$, $x_2$, $\ldots$, $x_n$ de la ruta.  
Se cumple que $0 < x_1 < x_2 < \ldots x_n < d$. 

La función $f$, cuyo mínimo vamos a buscar ahora en el intervalo $\langle 0;d \rangle$ 
tiene la forma
$$
\begin{align*}
f(x) &= x + \lvert x - x_1 \rvert +  \lvert x - x_2 \rvert + \ldots + \lvert x - x_n \rvert + (d-x) =\\
{} &= \lvert x - x_1 \rvert +  \lvert x - x_2 \rvert + \ldots + \lvert x - x_n \rvert + d.
\end{align*}
$$
Expresemos ahora esta función en intervalos individuales $\langle 0;x_1 )$, $\langle x_1;x_2 )$, $\ldots$ , $\langle x_{n-1};x_n )$, $\langle x_n;d \rangle$ 
de manera que en su fórmula no aparezcan expresiones con valores 
absolutos. En la tabla se expresan en estos intervalos las expresiones individuales 
con valores absolutos y en su última fila se expresa 
toda la función $f(x)$ 

|                           | $\langle 0;x_1 )$ | $\langle x_1;x_2 )$ | $\langle x_2;x_3 )$ | $\ldots$ | $\langle x_{n-1};x_n )$ | $\langle x_n;d \rangle$ |
|---------------------------|-------------------|---------------------|---------------------|----------|--------------------------|--------------------------|
| $\lvert x - x_1 \rvert$   | $x_1 - x$         | $x - x_1$           | $x - x_1$           | $\ldots$ | $x - x_1$                | $x - x_1$                |
| $\lvert x - x_2 \rvert$   | $x_2 - x$         | $x_2 - x$           | $x - x_2$           | $\ldots$ | $x - x_2$                | $x - x_2$                |
| $\lvert x - x_3 \rvert$   | $x_3 - x$         | $x_3 - x$           | $x_3 - x$           | $\ldots$ | $x - x_3$                | $x - x_3$                |
| $\vdots$                  | $\vdots$          | $\vdots$            | $\vdots$            | $\ddots$ | $\vdots$                 | $\vdots$                 |
| $\lvert x - x_{n-1} \rvert$ | $x_{n-1} - x$     | $x_{n-1} - x$       | $x_{n-1} - x$       | $\ldots$ | $x - x_{n-1}$            | $x - x_{n-1}$            |
| $\lvert x - x_n \rvert$   | $x_n - x$         | $x_n - x$           | $x_n - x$           | $\ldots$ | $x_n - x$                | $x - x_n$                |
| **$f(x)$**                | $-nx + k_0$       | $-(n-2)x + k_1$     | $-(n-4)x + k_2$     | $\ldots$ | $(n-2)x + k_{n-1}$       | $nx + k_n$               |


Para las constantes $k_i$ de la última fila se aplica lo siguiente
$$
\begin{align*}
k_0 &=x_1+x_2+\ldots + x_n +d \\
k_1 &=-x_1+x_2+\ldots + x_n +d \\
\vdots & \\
k_n &=-x_1-x_2-\ldots - x_n +d.
\end{align*}
$$

Centrémonos ahora en las directrices de las rectas que forman las gráficas 
lineales obtenidas .  Observemos que cada directriz siguiente es dos veces 
mayor que la anterior. Resolveremos el problema por separado para $n$ impar y $n$ par.

Para los valores impares de $n$ esto significa que ninguna de estas directrices es nula. 
Si designamos $m=\frac{n+1}{2}$, en el intervalo $\left\langle x_{m-1}; x_{m} \right) $ 
 la gráfica de la función tiene una directriz de $-1$ y en el siguiente intervalo 
$\left\langle x_{m}; x_{m+1} \right) $ la gráfica tiene una directriz de 1. Además, esto 
significa que para los valores impares de $n$ toda la función $f$ es decreciente en el intervalo $\left\langle 0; x_{m} \right)$ 
(porque las pendientes de todas las funciones parciales son negativas) y en 
el intervalo $\left\langle x_{m};d \right\rangle$ es creciente (porque 
estas directrices son positivas). De aquí se deduce que en el punto $x_{m}$ debe haber 
un mínimo de la función $f$, y, por lo tanto, para los valores impares de $n$ el puesto 
sanitario debe estar en la ubicación $\frac{n+1}{2}$.

Para $n$ par, una de las directrices es nula, concretamente la directriz de la gráfica 
de la función parcial en el intervalo $\left\langle x_{p}; x_{p+1} \right) $, donde $p=\frac{n}{2}$. 
En el intervalo $\left\langle 0; x_{p} \right)$ toda la función $f$ 
es decreciente, en el intervalo $\left\langle x_{p}; x_{p+1} \right) $ 
es constante y en el intervalo  $\left\langle x_{p+1}; d \right\rangle $ 
es creciente. La función $f$ alcanza sus valores más bajos en cualquier punto 
del intervalo $\left\langle x_{p}; x_{p+1} \right\rangle $. Por lo tanto, para $n$ par
podemos construir el puesto médico en cualquier lugar entre $\frac{n}{2}
$ y el puesto $(\frac{n}{2}+1)$.

\fi

