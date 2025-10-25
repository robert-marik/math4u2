---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- sucesiones y límites
- progresión geométrica
- fractal
- copo de nieve de Koch
is_finished: true
---

# Geometría fractal

Un fractal es un objeto cuya estructura geométrica se repite dentro de sí misma. La propiedad característica de los fractales es su autosemejanza. Ejemplos de fractales en la naturaleza son las nubes, los árboles o una cabeza de coliflor. La palabra "fractal" procede del latín "fractus", que significa roto o hecho añicos. Fue acuñada por Benoit B. Mandelbrot, considerado el padre de la geometría fractal, conocido por su libro La geometría fractal de la naturaleza (1982).

En el estudio de los fractales, su dimensión desempeña un papel importante. La dimensión topológica, conocida por la geometría euclidiana clásica, resultó insuficiente para describir los fractales. Por lo tanto, se necesitaba otro tipo de dimensión. Fue introducida por Felix Hausdorff, conocida como dimensión de Hausdorff. Para objetos simples, podemos entenderla como el número:

$$d=\frac{\ln N}{\ln\frac{1}{r}}, $$
donde $N$ es el número de partes de que se compone el objeto, formado por
autosemejanza con el coeficiente $r$ del
objeto original. Por ejemplo, para un cuadrado es cierto que puede estar
compuesto de cuatro cuadrados más pequeños que surgen de él por
autosemejanza con el coeficiente $r=\frac{1}{2}$, i.e.,
$$d=\frac{\ln 4}{\ln2}=2.$$
Así, para un cuadrado, su dimensión fractal (dimensión de Hausdorff) es la dimensión normal intuitiva (dimensión topológica).

## Copo de nieve de Koch

El *Copo de nieve* es una curva en el plano creada por un proceso iterativo
a partir de un triángulo equilátero.

Al principio, hay un triángulo equilátero con lados de
longitud 1. En cada paso posterior se realiza lo siguiente:


1. Cada segmento de línea se divide en tercios.
2. Sobre el tercio medio del segmento se construye un triángulo equilátero.
3. Se retira la base del triángulo construido (anteriormente el tercio
   del segmento de recta).

![La primera iteración del copo de nieve de Koch](math4you_00007.svg)

A partir de la figura, podemos ver que para determinar la longitud de un lado
del copo de nieve tras la primera iteración, necesitamos 4 lados del triángulo
que se formó reduciendo el lado del triángulo original
desde el paso cero con un coeficiente de autosimilitud $r=\frac{1}{3}$,
es decir,
$$
d=\frac{\ln4}{\ln3}\approx 1{,}26.
$$
Dado que el copo de nieve de Koch es una curva, cabría esperar que su dimensión fuera
$1$. Esta discrepancia se debe al hecho de que el copo de nieve de Koch está finalmente tan
fragmentado que el fractal resultante tiene una longitud pero limita una estructura plana de área finita.

> **Ejercicio 1.** Calcula el perímetro del copo de nieve de Koch después de
> la primera, segunda y tercera iteraciones.

\iffalse

*Solución.* Primero, tenemos un triángulo equilátero con un
perímetro $o_0=3$. En la primera iteración, cada uno de los tres segmentos de línea
en tercios, y el tercio central se sustituye por dos segmentos de longitud $\frac{1}{3}$.
Cada lado del triángulo original se amplía en $\frac{1}{3}$, lo que resulta en un perímetro después de
la primera iteración de
$$
o_1=3+3\cdot\frac{1}{3}=4.
$$
En la segunda iteración, cada lado del triángulo original se divide
en cuatro segmentos de línea de un tercio de la longitud original, que se
dividen a su vez en
tercios y ampliados en $\frac{1}{9}$. Esto conduce a un perímetro de
$$
o_2=3+3\cdot\frac{1}{3}+3\cdot\frac{4}{9}=\frac{16}{3}.
$$ 
En la tercera iteración, extendemos 16 segmentos de línea en cada lado
en $\frac{1}{27}$, lo que resulta en un perímetro de
$$
o_3=3+3\cdot\frac{1}{3}+3\cdot\frac{4}{9}+3\cdot\frac{16}{27}=3+1+\frac{4}{3}+\frac{16}{9}=\frac{64}{9}.
$$

\fi

> **Ejercicio 2.** ¿Cuál es el perímetro del copo de nieve de Koch después de la
> ¿n$-ésima iteración? Demuestra que el perímetro del copo de nieve de Koch
> es infinito.

\iffalse

*Solución.* De los cálculos anteriores, vemos que cada segmento de línea
es un tercio de la longitud del segmento de línea de la iteración,
y al mismo tiempo cada segmento es en la siguiente iteración
ampliado en un tercio, es decir, el segmento se extiende a $\frac{4}{3}$
de su longitud anterior. El perímetro del copo de nieve de Koch después de la
n$-ésima iteración puede expresarse mediante la suma de una serie geométrica
con la razón común de $\frac{4}{3}$ para $n\in\mathbb{N}$:
$$
o_n=3+\left(\frac{4}{3}\right)^0+\left(\frac{4}{3}\right)^1+\left(\frac{4}{3}\right)^2+\cdots+\left(\frac{4}{3}\right)^{n-1}=3+\sum_{i=1}^n\left(\frac{4}{3}\right)^{i-1}.
$$   
Si continuáramos así indefinidamente, obtendríamos una serie geométrica infinita en el segundo término de la suma anterior.
Como el cociente de la sucesión geométrica correspondiente es mayor que uno, la serie es divergente, y el perímetro del copo de nieve de Koch es
infinito.

\fi

> **Ejercicio 3.** Calcula el área del copo de nieve de Koch después de la
> primera y segunda iteraciones.

\iffalse

*Solución.* Al principio, vamos a darnos cuenta de que la altura de un
triángulo equilátero de lado $a$ es
$\frac{\sqrt{3}}{2}a$, y su área viene dada por
$$
S=\frac{\sqrt{3}}{4}a^2.
$$
El área del triángulo equilátero inicial es
$S_0=\frac{\sqrt{3}}{4}$. En la primera iteración, dividimos los tres
segmentos de línea en tercios y colocamos un triángulo equilátero más pequeño
de lado $\frac{1}{3}$ en el tercio medio. El área resultante tras la primera iteración es
$$
S_1=\frac{\sqrt{3}}{4}+3\cdot\frac{\sqrt{3}}{4}\cdot\left(\frac{1}{3}\right)^2=\frac{\sqrt{3}}{4}\cdot\frac{4}{3}.
$$ 
En la segunda iteración, cada lado del triángulo original se divide
en cuatro segmentos, y un triángulo equilátero más pequeño con lado
longitud $\frac{1}{9}$ se coloca en cada segmento.
El área después de la segunda iteración aumentará a 
$$
S_2=\frac{\sqrt{3}}{4}+3\cdot\frac{\sqrt{3}}{4}\cdot\left(\frac{1}{3}\right)^2+3\cdot4\cdot\frac{\sqrt{3}}{4}\cdot\left(\frac{1}{9}\right)^2=\frac{\sqrt{3}}{4}\left(1+\frac{1}{3}+\frac{1}{3}\cdot\frac{4}{9}\right)=\frac{\sqrt{3}}{4}\cdot\frac{40}{27}.
$$

\fi

> **Ejercicio 4.** ¿Cuál es el área del copo de nieve de Koch después de la $n$-ésima
> iteración? ¿Cuántas veces mayor es el área del copo de nieve de Koch
> respecto al triángulo equilátero original?

\iffalse

*Solución.* De las consideraciones anteriores se deduce que el
número de segmentos, en los que añadimos un nuevo triángulo, es cuatro veces mayor
en cada iteración. Al mismo tiempo, el lado de nuestro nuevo triángulo
se reduce a un tercio de su tamaño anterior, por lo que su área disminuye a
una novena parte.  Obtenemos términos de una sucesión geométrica con una razón de
$\frac{4}{9}$, y el área del copo de nieve Koch después de la $n$-ésima
iteración está formada por el área del triángulo original y la suma
de los primeros $n$ términos de esa secuencia geométrica:
$$S_n=\frac{\sqrt{3}}{4}\left[1+\frac{1}{3}+\frac{1}{3}\cdot\frac{4}{9}+\dots+\frac{1}{3}\left(\frac{4}{9}\right)^{n-1}\right]=\frac{\sqrt{3}}{4}\left[1+\frac{1}{3}\sum_{i=1}^n\left(\frac{4}{9}\right)^{i-1}\right].$$
Como el cociente de la progresión geométrica es menor que uno, continuando hasta el infinito, obtenemos una serie geométrica convergente. Utilizando la fórmula de su suma, obtenemos el área del copo de nieve de Koch tras un número infinito de iteraciones.
$$S=\frac{\sqrt{3}}{4}\left(1+\frac{1}{3}\cdot\frac{1}{1-\frac{4}{9}}\right)=\frac{\sqrt{3}}{4}\left(1+\frac{1}{3}\cdot\frac{9}{5}\right)=\frac{8}{5}\cdot\frac{\sqrt{3}}{4}= 1{,}6 \cdot S_0.$$

El copo de nieve de Koch tiene un perímetro infinito que encierra un área finita
que es aproximadamente 1,6 veces mayor que el área del triángulo equilátero original.

\fi

## Bibliografía

* MathWorld. *Koch snowflake* [online]. Accesible de <https://mathworld.wolfram.com/KochSnowflake.html> [cit. 13. 7. 2023].
* *Koch curve* [online]. Accesible de <https://cs.wikipedia.org/wiki/Kochova_k%C5%99ivka> [cit. 13. 7. 2023].

