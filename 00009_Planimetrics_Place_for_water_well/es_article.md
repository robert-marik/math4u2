---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- geometría en el plano
- planimetría
- conjunto de puntos que comparten una propiedad
is_finished: true
---

# Ubicación de un pozo 

Si queremos tener un pozo en nuestra propiedad, debemos considerar cuidadosamente
su ubicación para mantener una distancia suficiente de posibles fuentes
de posible contaminación.


Estas distancias requeridas varían según el tipo de contaminación potencial.
Digamos que para entornos menos permeables, las distancias requeridas son las siguientes:

1. pozos negros, pequeñas depuradoras, acometidas de aguas residuales: 12 \text{ m}$;
2. depósitos de combustible líquido para calefacción individual situados en un edificio de viviendas o en un edificio auxiliar independiente: 7 \text{ m}$;
3. establos, fosas de orina y fosas de estiércol para el alojamiento a pequeña escala de ganado individual: 10 \text{ m}$;
4. vías públicas: $12 \text{ m}$;
5. lavaderos individuales para vehículos de motor y desagües y zanjas que salgan de ellos: 15 $.


> **Ejercicio.** Hay que construir un pozo en la parcela $P_1$ (que se muestra en
> el plano de la figura).  El plano muestra la ubicación de una casa (rectángulo)
> y un pozo negro (círculo) en la parcela $P_1$, y dónde se encuentran una
> casa (cuadrado), un pozo negro (círculo) y una zona de lavado de coches (rectángulo)
> se encuentran en la parcela vecina $P_2$.  El plano también muestra la > carretera que pasa por ambas parcelas.
> Marque en el plano la zona en la que
> puede colocarse de acuerdo con las normas.
> 
> ![Esquema de la ubicación](math4you_00009.png)

\iffalse

*Solución.* Marcamos en el plano las zonas donde no debe colocarse el pozo. 

Dado que el pozo debe estar a una distancia mínima de 12 m de un pozo negro, esta
zona prohibida en el plano se mostrará como un círculo centrado en 
un círculo marcado con un radio de 12 m mayor. Los límites de las
zonas prohibidas para ambos pozos negros están representados por los círculos $k_1$
y $k_2$ en la figura.

La zona prohibida relacionada con la carretera en el plano es la franja
delimitada por el borde de la carretera adyacente a las parcelas $P_1$ y $P_2$
y una línea paralela a ella a una distancia de 12 m (en la figura, es
es la línea $p$).

Por último, construimos la frontera de la zona prohibida relacionada con la
zona de lavado de coches.  El borde tiene la forma de un óvalo denotado $o$ en el
plano. Este óvalo consta de cuatro segmentos de línea, paralelos a los lados
del rectángulo a una distancia de 15 m y partes de cuatro círculos con
centro en los vértices del rectángulo de 15 m de radio.
La parte relevante de este óvalo está marcada en la figura.
Ahora es posible definir la zona adecuada para excavar un pozo. Es
la parte de la parcela $P_1$, que es la parte exterior en el sentido
que no se encuentra en ninguna de las zonas prohibidas. Su límite
en negrita en la figura.


![Solución](math4you_00009_res.jpg)

\fi
