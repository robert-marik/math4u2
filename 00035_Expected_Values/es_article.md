---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- sucesiones y límites
- probabilidad
- valor estimado
- secuencia geométrica
is_finished: true
---




# ¿Qué billete de lotería es más rentable?

Muy a menudo en la vida nos encontramos en situaciones en las que el azar y la probabilidad desempeñan un papel. Imagina que te enfrentas a la elección entre varias opciones, por ejemplo, elegir un billete de lotería o invertir en un proyecto. Cada opción tiene sus riesgos y recompensas potenciales, pero la cuestión es cómo determinar cuál es la más ventajosa. Aquí es donde entra en juego el llamado *valor estimado*.

El valor estimado nos dice qué resultado podemos esperar por término medio cuando elegimos una opción determinada. Nos ayuda a estimar mejor lo que nos saldrá rentable a largo plazo. No es una predicción exacta, sino una herramienta que nos permite comprender mejor el riesgo y la recompensa, tanto en juegos sencillos como en decisiones de la vida real.

Consideremos, por ejemplo, dos billetes de lotería:

* Billete de lotería A: Cuesta 10 CZK y con una probabilidad de $0{,}1$ ganaremos 100 CZK, de lo contrario no ganaremos nada.
* Billete de lotería B: Cuesta 10 Kč y con una probabilidad de $0{,}2$ ganaremos 60 Kč, de lo contrario no ganaremos nada.

Para el billete A, esperamos que si compramos 10 billetes, uno de ellos ganará 100 CZK y nueve no ganarán nada. Por lo tanto, podemos esperar que cada billete nos proporcione una media de 10 CZK.

Del mismo modo, para el billete de lotería B, esperamos que si compramos 10 billetes, dos de ellos ganarán 60 CZK y ocho no ganarán nada. Por lo tanto, podemos esperar que cada billete de lotería nos proporcione una media de 12 CZK.

Así que vemos que el billete B es más ventajoso.

## Valor estimado

La ganancia media que se acaba de calcular se denomina *valor estimado* (o *valor medio*).

En general podemos decir que para una variable aleatoria $X$, que toma finitamente muchos valores $x_1,\,\dots,\,x_k$ con probabilidades $p_1,\,\dots,\,p_k$ calculamos su valor estimado
$$
EV=\sum_{i=1}^k x_ip_i\,.
$$

## ¿Cuál es el mejor billete de lotería? 

Veamos tres billetes de lotería. Perla Negra por valor de 50 CZK, 
Perla Negra por valor de 100 CZK y billete de lotería Rentiér por valor de 50 CZK. 

La estructura de premios del billete de lotería de 50 Kč Perla Negra, 
del que se han emitido $13\,000\,000$ unidades, es 
la siguiente. 

| Importe del premio en el billete de lotería (en CZK) | Número de billetes premiados | 
| ------------- | ------------- |  
| $50$  | $1\,820\,000$  |
| $100$  | $1\,040\,000$  |
| $150$  | $260\,000$  |
| $200$  | $130\,000$  |
| $300$  | $130\,000$  |
| $500$  | $104\,000$  |
| $1\,000$  | $5\,550$  |
| $2\,000$  | $2\,300$  |
| $4\,000$  | $480$  |
| $10\,000$  | $185$  |
| $20\,000$  | $84$  |
| $100\,000$  | $14$  |
| $1\,500\,000$  | $6$  |
| Celkem | $3\,492\,619$  |

La estructura de premios del billete de lotería Perla Negra de 
100 CZK es similar, con un total de $15\,000\,000$ 
unidades.

| Importe del premio en el billete de lotería (en CZK) | Número de billetes premiados | 
| ------------- | ------------- |  
| $100$  | $2\,400\,000$  |
| $200$  | $900\,000$  |
| $300$  | $450\,000$  |
| $500$  | $150\,000$  |
| $600$  | $150\,000$  |
| $900$  | $75\,000$  |
| $1\,000$  | $75\,000$  |
| $1\,500$  | $20\,000$  |
| $6\,000$  | $4\,000$  |
| $20\,000$  | $185$  |
| $50\,000$  | $84$  |
| $100\,000$  | $30$  |
| $200\,000$  | $13$  |
| $5\,000\,000$  | $6$  |
| Celkem | $4\,224\,318$  |

En tercer lugar, echemos un vistazo al billete de lotería Rentiér, del que se emiten $8\,000\,000$ unidades 
y cuyos premios figuran en la tabla siguiente.

| Importe del premio en el billete de lotería (en CZK) | Número de billetes premiados | 
| ------------- | ------------- |  
| $50$  | $960\,000$  |
| $100$  | $720\,000$  |
| $150$  | $160\,000$  |
| $250$  | $160\,000$  |
| $500$  | $70\,000$  |
| $1\,000$  | $1\,300$  |
| $2\,000$  | $500$  |
| $5\,000$  | $160$  |
| $10\,000$  | $80$  |
| $100\,000$  | $6$  |
| $3\,500\,000$  | $3$  |
| Celkem | $2\,072\,049$  |

El premio máximo de $3\,500\,000\,\text{Kč}$  no se paga de una vez, sino que 
consiste en un premio inmediato de $500\,000\,\text{Kč}$ y una renta de $50\,000\,\text{Kč}$ 
durante 5 años.

> **Tarea 1.** ¿Cuál de estos billetes de lotería tiene más probabilidades de 
> ser premiado?

\iffalse

*Solución.* En el caso del billete de lotería de 50 CZK Perla Negra, del número total de $13\,000\,000$ 
unidades, los billetes de lotería premiados son $3\,492\,619$  (véase la última fila de la tabla). 
Podemos calcular la probabilidad de que un billete seleccionado al azar sea ganador como
$$
P(V_1)=\frac{3\,492\,619}{13\,000\,000}=0{,}268633\,.
$$
Así que podemos decir que si compramos un billete de lotería, tenemos una probabilidad de ganar de $26{,}86\,\%$. 
Ajustando la fracción, también podemos hallar que la probabilidad de conseguir un billete de lotería premiado es de $1\colon 3{,}72$.

Del mismo modo, en el caso del billete de lotería de la Perla Negra por valor de 100 CZK, obtenemos
$$
P(V_2)=\frac{4\,224\,318}{15\,000\,000}=0{,}2816212\,.
$$
Es decir, la probabilidad de ganar es de $28{,}16\,\%$ nebo též $1\colon 3{,}55$.

En el caso del billete de lotería Rentiér, tenemos
$$
P(V_3)=\frac{2\,072\,049}{8\,000\,000}=0{,}259\,,
$$
por lo que la probabilidad de ganar es de $25{,}9\,\%$ neboli $1\colon 3{,}86$.

Comparando las probabilidades individuales de ganar, podemos ver que tenemos la mayor probabilidad de 
obtener un billete ganador si compramos el billete Perla Negra por valor de 100 coronas checas. 

En este contexto, podemos seguir considerando lo que llamamos un billete de lotería premiado. Un billete de lotería premiado 
se suele considerar en como un billete de lotería que nos reporta cualquier cantidad de dinero. 
Sin embargo, si hemos pagado 100 CZK por un billete de lotería, ganar 100 CZK nos devolverá el dinero, pero en realidad 
no hemos ganado nada. Por lo tanto, para obtener la probabilidad de que realmente ganemos, 
no tendremos en cuenta la primera fila de nuestras tablas de premios. Así obtenemos las probabilidades ajustadas de ganar
$$
\begin{aligned}
P(V_1)&=\frac{1\,672\,619}{13\,000\,000}=0{,}128633\\
P(V_2)&=\frac{1\,824\,318}{15\,000\,000}=0{,}1216212\\
P(V_3)&=\frac{1\,112\,049}{8\,000\,000}=0{,}139\,.
\end{aligned}
$$
Podemos ver que si consideramos los billetes de lotería que realmente ganan más que su precio, el mejor billete de lotería es el billete de lotería Rentiér, donde la probabilidad de ganar es de $13{,}9\,\%$.

\fi

> **Tarea 2.** ¿Cuál es el valor estimado de cada billete de lotería?

\iffalse

*Solución.* Para calcular el valor estimado por definición, necesitamos conocer las probabilidades de cada ganancia:

| Importe del premio en el billete de lotería (en CZK) | Probabilidad de una determinada ganancia | 
| ------------- | ------------- |  
| $50$  | $0{,}14$  |
| $100$  | $0{,}08$  |
| $150$  | $0{,}02$  |
| $200$  | $0{,}01$  |
| $300$  | $0{,}01$  |
| $500$  | $0{,}008$  |
| $1\,000$  | $0{,}000\,426\,9$  |
| $2\,000$  | $0{,}000\,176\,923$  |
| $4\,000$  | $0{,}000\,036\,923$  |
| $10\,000$  | $0{,}000\,014\,231$  |
| $20\,000$  | $0{,}000\,006\,461\,538$  |
| $100\,000$  | $0{,}000\,006\,461\,538$  |
| $1\,500\,000$  | $0{,}000\,000\,461\,538$  |

Considerando los valores de los premios individuales $n_1$ až $n_{13}$ y sus correspondientes probabilidades $p_1$ až $p_{13}$, se obtiene el valor estimado $EV(L_1)$ del billete de lotería Perla Negra
$$
EV(L_1)=\sum_{k=1}^{13}n_kp_k=29\,\text{Kč}.
$$

Teniendo en cuenta cómo se calculan las probabilidades, también podemos calcular el valor estimado de la siguiente manera
$$
EV(L_1)=\frac{1}{13\,000\,000}\left(50\cdot 1\,820\,000+100\cdot1\,040\,000+ \cdots + 100\,000\cdot14+1\,500\,000\cdot6 \right).
$$

Este enfoque es preferible, ya que no tenemos que calcular la probabilidad de cada posible ganancia en la tabla de ganancias. Para el billete de 100 CZK Perla Negra, obtenemos el valor estimado $EV(L_2)$:
$$
EV(L_2)=\frac{1}{15\,000\,000}\left(100\cdot 2\,400\,000+200\cdot 900\,000+ \cdots + 200\,000\cdot 13+5\,000\,000 \cdot 6 \right)=64\,\text{Kč}.
$$
Y para el billete Rentiér obtenemos el valor estimado $EV(L_3)$:
$$
EV(L_3)=\frac{1}{8\,000\,000}\left(50\cdot 960\,000+100\cdot 720\,000+ \cdots + 100\,000\cdot 6+3\,500\,000\cdot 3 \right)=29{,}25\,\text{Kč}.
$$

*Nota.* 

* Normalmente, en las loterías se indica el importe total que se puede ganar y el número de billetes, y el valor estimado es, por supuesto, el cociente de estas dos cifras.
* En realidad, las cifras indicadas suelen ser incluso inferiores, ya que a menudo se pagan impuestos sobre las ganancias. 
* El mismo método puede utilizarse para calcular el valor esperado de una baraja de diversos juegos de cartas coleccionables (Pokémon, Lorcana, Magic the Gathering o cartas deportivas).

\fi

> **Tarea 3.** En los ejemplos anteriores hemos considerado 
el premio mayor del billete de lotería Rentièr por valor de $3\,500\,000\,\text{Kč}$. 
Pero, ¿es éste realmente el valor real del premio, 
dado que no se paga de una sola vez? 

\iffalse

*Solución.* La respuesta sencilla es que no. 

Es importante recordar que si recibiéramos el dinero inmediatamente, podríamos ahorrarlo o invertirlo de alguna manera. Para averiguar cuál es el valor de las 50 000 CZK que recibiremos dentro de un mes, podemos utilizar un concepto llamado *valor actual*. Al utilizarlo, nos preguntamos cuánto dinero tendríamos que invertir hoy para obtener la cantidad que queremos dentro de un mes (por ejemplo, las 50 000 CZK que estamos considerando). Y este valor es entonces el llamado valor actual. 

Supongamos que podemos ahorrar la cantidad dada $P_0$ durante un mes con un tipo de interés mensual de $0{,}5\,\%$. Obtendríamos entonces $P_1=1{,}005P_0$ al mes. El valor actual es entonces sólo la cantidad de $P_0$, que necesitamos ahorrar para que $P_1$ bylo $50\,000\,\text{Kč}$, es decir, 
$$
P_0=\frac{50\,000}{1{,}005}=49\,751{,}24\,\text{Kč}.
$$

Si queremos determinar el valor actual de la cantidad que recibiremos en $n$ meses, consideramos que mantenemos la cantidad ahorrada durante todo el tiempo. Entonces utilizamos el interés compuesto para obtener el valor actual $P_0$ de la cantidad $P_n$, que recibiremos en $n$ meses como
$$
P_0=\frac{P_n}{1{,}005^n}.
$$
Recordemos que el premio mayor del billete de lotería Rentiér consiste en $500\,000\,\text{Kč}$ y treinta pagos mensuales de $50\,000\,\text{Kč}$. Considerando un tipo de interés mensual del $0{,}5\,\%$, el valor actual $PV$ de estos pagos sería
$$
PV=\frac{50\,000}{1{,}005}+\frac{50\,000}{1{,}005^2}+\cdots+\frac{50\,000}{1{,}005^{29}}+\frac{50\,000}{1{,}005^{30}}\,.
$$
Podemos observar que se trata de la suma de los miembros de una sucesión geométrica y así acortar considerablemente el cálculo
$$
PV=\frac{50\,000}{1{,}005}\cdot\frac{1-\left(\frac{1}{1{,}005}\right)^{30}}{1-\frac{1}{1{,}005}}=1\,389\,702{,}7\,\text{Kč}.
$$
Así que podemos considerar que el valor del premio es de sólo $1\,889\,702{,}7\,\text{Kč}$.

Si utilizamos esta cantidad para calcular el valor estimado del billete de lotería Rentiér, obtenemos
$$
EV(L_3)=28{,}65\,\text{Kč}.
$$

*Nota.* Las consideraciones anteriores no dejan de ser muy simplistas, ya que no incluyen, por ejemplo, el efecto de la inflación.

\fi

> **Tarea 4.** Basándose en los resultados de las tareas anteriores, seleccione el billete que sea mejor.

\iffalse

*Solución.* Basándonos en las tareas anteriores, podemos comparar los billetes de lotería según diferentes criterios:

1. Según la probabilidad de ganar.

Según este criterio, el mejor billete de lotería sería el Perla Negra de 100 CZK con una posibilidad de ganar $28{,}16\,\%$, después el Perla Negra de 50 CZK con una posibilidad de $26{,}86\,\%$ y el peor billete de lotería sería el Rentiér con una posibilidad de $25{,}9\,\%$.

2. Según la probabilidad de ganar realmente.

Si consideramos más bien la posibilidad de ganar más de lo que hemos pagado, obtenemos el siguiente orden diferente. El mejor billete de lotería sería el billete de lotería Rentiér con una probabilidad de ganar de $13{,}9\,\%$, después el billete de lotería Perla Negra de 50 CZK con una probabilidad de ganar de $12{,}86\,\%$ y el último sería el billete de lotería Perla Negra de 100 CZK con una probabilidad de ganar de $12{,}16\,\%$.

3. Según el valor estimado.

El valor estimado del billete de lotería Perla Negra de 50 coronas checas es de 29 coronas checas. Por lo tanto, se perdería una media de 21 coronas checas por billete. Del mismo modo, el valor estimado del billete de lotería Perla Negra de 100 CZK es de 64 CZK, por lo que perderíamos una media de 36 CZK. Y en el caso del billete de lotería Rentiér de 50 CZK, el valor estimado ajustado es de 28,65 CZK, por lo que perderíamos 21,35 CZK de media.

Así que podemos decir que (como era de esperar) todos los billetes de lotería son perdedores. Sin embargo, podemos considerar que el mejor billete de lotería es el Perla Negra por valor de 50 CZK, que es el menos perdedor. 

\fi

## Bibliografía

* Novák, J., *Střední hodnota v úlohách na střední škole.* Učitel matematiky, 2, JČMF, 2024. 
* *Herní plán loterií SAZKA* [online] Dostupné z https://static.sazka.cz/kentico-media/sazka/media/content/herni-plany/hp-sazka-od-17-7-24-komplet-sazka.pdf, [cit. 1. 9. 2024]








