---
keywords:
- números complejos
- plano de Gauss
- secuencias
- convergencia
- valor absoluto
is_finished: true
---

# Conjunto de Mandelbrot

El conjunto de Mandelbrot es uno de los fractales 
 más famosos y bellos, que fascina a matemáticos, 
científicos y artistas de todo el mundo. Aunque a primera vista 
parece un patrón complejo, se basa en 
una sencilla regla matemática de suma y multiplicación  
repetida. Pero lo que lo hace tan interesante es 
su infinita complejidad y los bellos patrones que se 
esconden en cada detalle.

![Conjunto de Mandelbrot. El color de los puntos de su vecindad corresponde al orden del miembro de la secuencia que se encuentra primero que se dirige al infinito.](Mandelbrot.png)

El uso del conjunto de Mandelbrot va mucho más allá de 
matemáticas. Se puede encontrar en gráficos por ordenador, donde se 
utiliza para crear objetos complejos y realistas
al modelar estructuras naturales como costas, montañas 
o nubes. Incluso puede emplearse en economía y física, donde 
ayuda a simular sistemas caóticos.

El conjunto de Mandelbrot es la prueba de que incluso procedimientos 
matemáticos sencillos pueden conducir a resultados 
increíblemente complejos y bellos que tienen aplicaciones 
reales.

## Creación de un conjunto

Imaginemos una relación recurrente relativamente sencilla
$$
z_{n+1}=z_{n}^2+c,
$$ 
donde el valor inicial es $z_0=0$ y $c$ es un número 
complejo arbitrario. El matemático franco-estadounidense Benoit Mandelbrot (1924–2010) 
se interesó por saber cuándo la secuencia de números así generada está acotada, es decir, para qué $c$ 
del plano complejo la secuencia converge u oscila. Si en algún punto 
la sucesión diverge, quería saber a qué velocidad. Se puede demostrar que 
si el valor absoluto de cualquier miembro de la secuencia $z_{n}$ es superior a 2, 
entonces la secuencia no está acotada. 

El *conjunto de Mandelbrot* es entonces el conjunto de puntos $c$ del plano complejo para los que la sucesión generada por la fórmula de recurrencia converge u oscila. Gracias al hecho anterior, sabemos que para cada miembro $z$ de esta sucesión, debe cumplirse que su valor absoluto $|z|$ sea menor o igual que dos. 

Para verificar si un $c$ dado pertenece al conjunto de Mandelbrot, se calculan las iteraciones individuales y se observan los valores absolutos de estas iteraciones. Para calcular las iteraciones, utilizamos la relación recurrente

$$
z_{n+1}=z_{n}^2+c,\qquad z_0=0.
$$

Por ejemplo, para $c=-i$ tenemos

$$z_{1}=z_{0}^2-i=0^2-i=-i, \quad |z_1|=1,$$
$$z_{2}=z_{1}^2-i=(-i)^2-i=-1-i, \quad |z_2|=\sqrt{2},$$
$$z_{3}=z_{2}^2-i=(-1-i)^2-i=i, \quad |z_3|=1,$$
$$z_{4}=z_{3}^2-i=(i)^2-i=-1-i, \quad |z_4|=\sqrt{2}.$$

El cálculo muestra que los resultados de $-i$ y $-1-i$ se repetirán continuamente. 
Por lo tanto, siempre se cumplirá la condición $|z|\leq2$ y, por lo tanto, el número $-i$ pertenece al conjunto 
de Mandelbrot.

## Tareas

> **Tarea 1.** Verificar que los números complejos $1$; $i$; $-1$; $1+i$ pertenecen al conjunto de Mandelbrot.

\iffalse

*Solución.* Por simplicidad, consideraremos sólo los primeros pasos 
de los cálculos iterativos. Se sostiene que la imagen de un número $c$ en el plano de Gauss pertenece al conjunto 
de Mandelbrot si para todos los resultados de un calculo iterativo el valor 
absoluto del resultado es menor o igual a $2$.

Proceso iterativo para $c=1$.
$$z_{1}=z_{0}^2+1=0^2+1=1, \quad |z_1|=1,$$
$$z_{2}=z_{1}^2+1=1^2+1=2, \quad |z_2|=2,$$
$$z_{3}=z_{2}^2+1=2^2+1=5, \quad |z_3|=5.$$
El cálculo muestra que la condición $|z|\leq2$ no se cumplió en el tercer 
paso de iteración y el número $1$ no pertenece al conjunto de Mandelbrot.

Proceso iterativo para $c=i$.
$$z_{1}=z_{0}^2+i=0^2+i=i, \quad |z_1|=1,$$
$$z_{2}=z_{1}^2+i=i^2+i=-1+i, \quad |z_2|=\sqrt{2},$$
$$z_{3}=z_{2}^2+i=(-1+i)^2+i=-i, \quad |z_3|=1,$$
$$z_{4}=z_{3}^2+i=(-i)^2+i=-1+i, \quad |z_4|=\sqrt{2}.$$
El cálculo muestra que los resultados de $-1+i$ y $i$ se repetirán continuamente. 
La condición $|z|\leq2$ se cumplirá siempre, por lo que el número $i$ pertenece 
al conjunto de Mandelbrot.

Proceso iterativo para $c=-1$.
$$z_{1}=z_{0}^2-1=0^2-1=-1, \quad |z_1|=1,$$
$$z_{2}=z_{1}^2-1=(-1)^2-1=0, \quad |z_2|=0,$$
$$z_{3}=z_{2}^2-1=0^2-1=-1, \quad |z_3|=1.$$
Los resultados se repetirán de nuevo y siempre se cumplirá la condición $|z|\leq2$, 
por lo tanto el número $-1$ pertenece al conjunto de Mandelbrot.

Proceso iterativo para $c=1+i$.
$$z_{1}=z_{0}^2+1+i=0^2+1+i=1+i, \quad |z_1|=\sqrt{2},$$
$$z_{2}=z_{1}^2+1+i=(1+i)^2+1+i=1+2i+i^2+1+i=1+3i, \quad |z_2|=\sqrt{10}.$$
El cálculo muestra que la condición $|z|\leq2$ no se cumplió en el segundo 
paso iterativo y que el número $1+i$ no pertenece al conjunto de Mandelbrot.

\fi

> **Tarea 2.** Demostrar que si existe $k\in \mathbb{N}$ tal que $|z_k|>2$, entonces la sucesión $z_n$ diverge.

\iffalse

*Solución.* Utilizando la relación de recurrencia, obtenemos la proporción
$$
\frac{|z_{n+1}|}{|z_n|}=\frac{|z^2_n+c|}{|z_n|}. 
\tag{1}
$$

Si utilizamos la desigualdad triangular
$$
|a+b|\leq|a|+|b|,
$$ 
donde $a=z^2+c$ a $b=-c$, obtenemos
$$
|z^2+c-c|\leq|z^2+c|+|-c|=|z^2+c|+|c|
$$
y a partir de ahí $|z^2+c|\geq|z^2|-|c|=|z|^2-|c|$.

Sumando a $(1)$ y modificando para obtener
$$
\frac{|z^2_n+c|}{|z_n|}\geq \frac{|z_n|^2-|c|}{|z_n|}=|z_n|-\frac{|c|}{|z_n|}.
$$
Además, sabemos que existe $n$, tal que $|z_n|>|c|$ se cumple. Para $|c|\leq2$ esto se deduce de la suposición. Para $c>2$ entonces para $n=2$ se cumple 
$$
|z_2|=|c^2+c|\geq|c|^2-|c|=|c|(|c|-1)>|c|.
$$
Así que podemos escribir
$$
\frac{|z^2_n+c|}{|z_n|}\geq \frac{|z_n|^2-|c|}{|z_n|}=|z_n|-\frac{|c|}{|z_n|}>|z_n|-1>1.
$$
Y así desde aquí
$$
\frac{|z_{n+1}|}{|z_n|}>1,
$$
o $|z_{n+1}|>|z_n|$ y nuestra secuencia diverge.

\fi

## Bibliografía 

*  Čápka Hartinger, David. *Mandelbrotova množina - lekce 3 [online]* https://www.itnetwork.cz/algoritmy/graficke/algoritmus-vykresleni-fraktalu-mandelbrotovy-mnoziny} [cit. 22. 9. 2023]

* Wikipedie. *Mandelbrotova množina [online]*. Dostupné z https://cs.wikipedia.org/wiki/Mandelbrotova_mno%C5%BEina [cit. 22. 9. 2023].

* PantheraLeo1359531. *Mandelbrotova množina - obrázek [online]*. Dostupné z https://commons.wikimedia.org/w/index.php?curid=103476207 [cit. 22. 9. 2023]




