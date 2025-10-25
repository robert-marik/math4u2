---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- combinatoria, probabilidad y estadística
- estadística
- tratamiento de datos
- media aritmética
- media geométrica
- análisis de regresión
- GeoGebra
is_finished: true
---

# Propagación inicial de una epidemia

La epidemia reciente más conocida es la pandemia de la enfermedad vírica 
COVID-19, causada por el coronavirus SARS-CoV-2. Esta epidemia estalló en 
diciembre de 2019 en la ciudad de Wu-chan, en la provincia central china de Hubei. 

El inicio de la epidemia de COVID-19 en Europa está fechado en enero de 2020. Los primeros 
casos confirmados se notificaron en Francia el 24 de enero de 2020. Se trataba de 
tres pacientes que habían regresado recientemente de China, donde la epidemia ya estaba en 
pleno apogeo.

A continuación, la enfermedad se propagó a la República Checa antes del 1 de marzo de 2020, cuando 
confirmó los tres primeros casos. A 18 de marzo de 2020, ya se habían confirmado 
464 casos en el país.

La propagación de la enfermedad es exponencial al principio de la epidemia. Más adelante, la propagación suele ralentizarse y seguir un curso diferente (lineal, logístico, etc.).

## Evolución típica de una epidemia

A partir de los datos, intentamos modelizar el número de personas infectadas en 
función de los días transcurridos desde el inicio de la epidemia. La tabla muestra los datos que describen el número de personas infectadas en función de los días transcurridos desde el inicio de la epidemia.

| Día $(n)$  | Número de infectados ($a_n$) | 
| ------------- | ------------- |  
| $1$  | $3$  | 
| $2$  | $3$  | 
| $3$  | $5$  | 
| $4$  | $6$  | 
| $5$  | $9$  | 
| $6$  | $20$  | 
| $7$  | $27$  | 
| $8$  | $33$  | 
| $9$  | $39$  | 
| $10$  | $64$  | 
| $11$  | $95$  | 
| $12$  | $117$  | 
| $13$  | $142$  | 
| $14$  | $190$  | 
| $15$  | $299$  | 
| $16$  | $384$  | 

*Nota.* Estos son datos reales de la República Checa a 1 de marzo de 2020.

> **Tarea 1.** Calcular la relación entre el número de personas infectadas en un día con respecto al 
> día anterior.

\iffalse

*Solución.* Si denominamos $q_n$ a la relación entre el número de infectados en el día $n$-ésimo y el número de infectados en el día $n-1$-ésimo obtenemos la relación
$$
q_n=\frac{a_n}{a_{n-1}}, \qquad n\geq2.
$$
Así podemos calcular todos los datos y completar la tabla.

| Día $(n)$  | Número de infectados ($a_n$) | Proporción del número de infectados |
| ------------- | ------------- |  --------|
| $1$  | $3$  | $-$ |
| $2$  | $3$  |$1{,}000$ |
| $3$  | $5$  | $1{,}667$|
| $4$  | $6$  | $1{,}200$|
| $5$  | $9$  | $1{,}500$|
| $6$  | $20$  | $2{,}222$|
| $7$  | $27$  | $1{,}350$|
| $8$  | $33$  | $1{,}222$|
| $9$  | $39$  | $1{,}182$|
| $10$  | $64$  | $1{,}641$|
| $11$  | $95$  | $1{,}484$|
| $12$  | $117$  | $1{,}232$|
| $13$  | $142$  | $1{,}214$|
| $14$  | $190$  | $1{,}338$|
| $15$  | $299$  | $1{,}574$|
| $16$  | $384$  |$1{,}284$|

El valor calculado de la relación entre el número de infectados en un día con respecto al día anterior puede interpretarse como el índice de propagación de la enfermedad. Para un aumento o una disminución estrictamente exponenciales, este cociente sería constante. Sólo trabajamos con datos "medidos", por lo que el valor del cociente es sólo una aproximación. Así que analicemos más detenidamente esta proporción.

\fi

> **Tarea 2.** Calcula la media aritmética y geométrica de la relación entre el número de 
> infectados. ¿Cuál es la más adecuada en este caso?

\iffalse

*Solución.* La media aritmética de $\bar{q}$ viene dada por
$$
\bar{q}=\frac{q_2+\cdots+q_{16}}{15}=1{,}40731.
$$
Análogamente, para la media geométrica $G$ se aplica
$$
G=\sqrt[15]{q_2\cdot \cdots \cdot q_{16}}=1{,}38191.
$$
En este caso es mejor utilizar la media geométrica.

La media aritmética puede verse afectada por valores atípicos (para 
nosotros, por ejemplo, el valor de $q_6$), que pueden sesgar la interpretación del crecimiento 
o descenso medio. En cambio, la media geométrica mitiga este efecto. 

Además, en el caso de crecimiento exponencial (si nos limitamos al tipo básico de la forma $k\cdot a^x$) se multiplica por un factor constante (es decir, la razón de dos valores medidos después de un intervalo fijo es una constante).
La media geométrica representa directamente esta naturaleza multiplicativa de los cambios. Por ejemplo, si 
tenemos dos mediciones consecutivas con proporciones
$$
q_1=2, \qquad q_2=0{,}5,
$$
entonces la media aritmética $\bar{q}=1{,}25$ indicaría un crecimiento estable, 
mientras que la media geométrica $G=1$ refleja correctamente un crecimiento neto cero.

\fi

> **Tarea 3.** Diseña una función que aproxime el número de infecciones 
> de cada día. Crea un gráfico en Geogebra (u otro programa).

\iffalse

*Solución.* Se utiliza el método de ensayo y error para crear una función exponencial que 
represente adecuadamente nuestros datos, por ejemplo, utilizando medias 
obtenidas. Utilizaremos la notación habitual para escribir la función, que también se utiliza 
en Geogebra y en la siguiente figura. En el gráfico, $x$ representa el tiempo en días e $y$ representa el número 
de infecciones. 

Con la media aritmética obtenemos la función $y=1{,}40731^x$, con la media 
geométrica $y=1{,}38191^x$.  Estas funciones están bastante alejadas de los puntos marcados, 
por lo que las modificamos ligeramente: $y=2\cdot1{,}40731^x$, $y=2\cdot1{,}38191^x$. Las gráficas de las funciones propuestas se muestran en la figura. Por supuesto, se pueden obtener funciones exponenciales aún más exactas.

![Funciones exponenciales propuestas por ensayo y error](00034_obr_1.svg)

\fi

>**Tarea 4.** Tras utilizar el análisis de regresión de los datos, se puede obtener una función 
> más adecuada que describa el comportamiento del número de infecciones, que es de la forma 
> $y=1{,}9466\cdot \mathrm{e}^{0{,}3376x}$. Compara su función en Geogebra (u 
> otro software adecuado) con esta función. Calcula los valores 
> de las funciones propuestas para los días 14 a 16, redondeando el resultado al 
> número entero más próximo. Compárelos con los valores de la tabla.

*Nota.* La función exponencial obtenida mediante el análisis de regresión puede crearse en 
la hoja de cálculo o en Geogebra. En Geogebra, se requiere un comando en el que 
se especifiquen los puntos obtenidos de la hoja de cálculo: `Regresión Exponencial({(1,3), (2,3), (3,5),...,(16,384)})`.

\iffalse

*Solución.* Las tres funciones están en la imagen de abajo. Con sólo mirar 
podemos ver que todas las funciones son similares para empezar, pero para otros valores 
la función $y=1{,}9466\cdot \mathrm{e}^{0{,}3376x}$ parece ser la más apropiada 
para describir los datos obtenidos. 

![Comparación de las funciones propuestas con la función según el análisis de regresión](00034_obr_2.svg)

También podemos cuantificar esta observación utilizando los datos de la tabla.

| Día $(n)$  | Número de infectados ($a_n$) | Número mediante la función $y=2\cdot1{,}40731^x$ | Número mediante la función $y=2\cdot1{,}38191^x$ |Número mediante la función $y=1{,}9466\cdot \mathrm{e}^{0{,}3376x}$ |
| ------------- | ------------- |  -------- | --------| --------|
| $14$  | $190$  | $239$ | $185$ | $220$ |
| $15$  | $299$  | $336$ | $256$ | $308$ |
| $16$  | $384$  | $473$ | $354$ | $432$ |

Como indicador de la precisión con la que nuestras funciones representan los datos, podemos considerar cuánto difieren los valores entre sí. De este modo, obtenemos sucesivamente
$$
\begin{align*}
|239-190|+|336-299|+|473-384|&=175\\
|185-190|+|256-299|+|354-384|&=92\\
|220-190|+|308-299|+|432-384|&=87.
\end{align*}
$$

Sin embargo, normalmente se utilizan los cuadrados de estas diferencias para evaluar la precisión. Esto se debe a que las diferencias pequeñas (inferiores a 1) se reducen mediante la multiplicación y las diferencias grandes se incrementan.

En este caso, obtenemos
$$
\begin{align*}
(239-190)^2+(336-299)^2+(473-384)^2&=11691\\
(185-190)^2+(256-299)^2+(354-384)^2&=4174\\
(220-190)^2+(308-299)^2+(432-384)^2&=3285.
\end{align*}
$$
Así pues, en este caso, la tercera curva resultó ser la mejor. Esto no es casualidad, ya que la curva generada por la regresión es la que tiene el menor error.

\fi

> **Tarea 5.** ¿Se propagará la epidemia de forma continua según la función propuesta? ¿Qué 
> podría influir en su comportamiento futuro?

\iffalse

*Solución.* Para mantener el curso exponencial de la epidemia, las condiciones de propagación de la enfermedad no deben 
variar. En la práctica, la gente empezará a protegerse con equipos 
de protección, a minimizar el contacto con otras personas o a vacunarse, lo que reducirá el aumento 
del número de infectados. La epidemia alcanzará su punto álgido y el número 
de infectados empezará a disminuir. Además, para que se produzca un crecimiento exponencial sostenido, tendría que 
haber un número ilimitado de individuos que puedan infectarse con la enfermedad.

\fi

## Bibliografía

* European Centre for Disease Prevention and Control *Novel Coronavirus: three cases reported in France*. Dostupné z https://www.flickr.com/photos/ecdc_eu/50321985653/in/dateposted/ [cit. 08.08.2024]

* Ministerstvo zdravotnictví ČR. *Onemocnění aktuálně - COVID 19*. Dostupné https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19 [cit. 30.8.2023]






