---
keywords:
- exponentes y logaritmos
- logaritmos
- ecuación logarítmica
- ecuación exponencial
is_finished: true
---


# Sonido

El sonido es una onda mecánica que percibimos por el oído. Todas las personas perciben el tono y la duración de un tono aproximadamente de la misma manera, pero la percepción del volumen es muy subjetiva.  La sonoridad viene determinada por la amplitud de la oscilación en el medio a través del cual se propaga la onda sonora.  Dado que la amplitud de las ondas sonoras no es fácil de medir, las cantidades de intensidad sonora $I$ y nivel de intensidad sonora $L$ se utilizan para comparar la sonoridad de forma objetiva.

*La intensidad del sonido* expresa cuánta energía transfieren las ondas sonoras a una unidad de superficie perpendicular a la dirección de propagación del sonido por unidad de tiempo. Un oído sano puede detectar la menor intensidad sonora $I_0=10^{-12}\,\text{W}/\text{m}^2$ a una frecuencia de $1000\,\text{Hz}$, que corresponde al umbral de audición.
Por otra parte, la intensidad sonora de $10\,\text{W}/\text{m}^2$ es lo suficientemente fuerte como para corresponder al umbral del dolor. Sin embargo, aumentar diez veces la intensidad sonora $I$ no corresponde a percibir el sonido diez veces más fuerte.  Por lo tanto, para expresar la sonoridad se utiliza más bien el nivel de intensidad sonora $L$ que utiliza una escala logarítmica en decibelios (dB).

*El nivel de intensidad sonora* $L$ en decibelios se define mediante la ecuación $$L=10\log{\frac{I}{I_0}},$$
donde $I$ es la intensidad sonora en el lugar dado y $I_0=10^{-12}\,\text{W}/\text{m}^2$, que corresponde al umbral de audición. El nivel de intensidad sonora de $60\,\text{dB}$ corresponde al volumen de una conversación normal, $90\,\text{dB}$ es el volumen de un cortacésped y $110\,\text{dB}$ es el volumen de una discoteca.

A partir de un volumen superior a $85\,\text{dB}$ existe riesgo de daño auditivo en escuchas prolongadas (aunque no nos duela). A partir de un volumen superior a $100\,\text{dB}$, existe el riesgo de sufrir daños auditivos en cuestión de minutos. Exploremos la relación entre la intensidad sonora y el nivel de intensidad sonora, es decir, el volumen percibido por el oído.

>**Ejercicio 1.** La intensidad sonora es de $1{,}27\cdot10^{-3}\,\text{W}/\text{m}^2$ 
mientras escuchamos un altavoz con una potencia sonora de  $20\,\text{W}$
a una distancia de $50\,\text{m}$ del mismo (supongamos una transmisión uniforme de la onda sonora en el semiespacio libre). ¿Cuántos decibelios medimos en este lugar?

\iffalse

*Solución.* Utilizamos la definición de nivel de intensidad sonora $L=10\log{\frac{I}{I_0}},$ para el cálculo, donde $I=1{,}27\cdot10^{-3}\,\text{W}/\text{m}^2$ es la intensidad sonora en el lugar dado y $I_0=10^{-12}\,\text{W}/\text{m}^2$.
$$L=10\log{\frac{I}{I_0}}=10\log{\left(\frac{1{,}27\cdot10^{-3}}{10^{-12}}\right)}=10\log{\left(1{,}27\cdot10^{9}\right)}=91\;\text{dB}\,.$$

El nivel de intensidad sonora es de $91$ dB a una distancia de $50$ m del altavoz, que corresponde al nivel de ruido de una motocicleta o un cortacésped.

\fi

>**Ejercicio 2.** ¿Cómo cambiará el nivel de intensidad sonora si hay un doble de intensidad sonora en el lugar del ejemplo anterior, es decir, $2\cdot1{,}27\cdot10^{-3}\,\text{W}/\text{m}^2$ ?

\iffalse

*Solución.* Utilizamos la misma fórmula que en el ejercicio anterior:
$$L=10\log{\frac{I}{I_0}}=10\log{\left(\frac{2\cdot1{,}27\cdot10^{-3}}{10^{-12}}\right)}=10\log{\left(2{,}54\cdot10^{9}\right)}=94\;\text{dB}\,.$$
El cálculo muestra que el doble de intensidad sonora no corresponde al doble de decibelios. El nivel de intensidad sonora aumentará de
$91\,\text{dB}$ to $94\,\text{dB}\,$.

yfi

>**Ejercicio 3.** From the formula for the sound intensity level, find the value $\Delta L$, by which the sound intensity level $L$, changes if the sound intensity is doubled from $I$ to $2I$.

\iffalse

*Solución.* Se trata de una generalización del problema anterior.$$\Delta L=10\log{\frac{2I}{I_0}}-10\log{\frac{I}{I_0}}=10\cdot\left(\log{\frac{2I}{I_0}}-\log{\frac{I}{I_0}}\right)=10\log\left(\frac{\frac{2I}{I_0}}{\frac{I}{I_0}}\right)=10\log2\doteq3\;\text{dB}$$
Al duplicar la intensidad sonora, el nivel de intensidad sonora aumenta en $3\,\text{dB}\,$.

Se trata de una generalización del problema anterior.$$\Delta L=10\log{\frac{2I}{I_0}}-10\log{\frac{I}{I_0}}=10\cdot\left(\log{ \frac{2I}{I_0}}-\log{\frac{I}{I_0}}\right)=10\log\left(\frac{\frac{2I}{I_0}}{\frac{I} {I_0}}\right)=10\log2\doteq3\;\text{dB}$$
El nivel de intensidad sonora aumenta en $3\,\text{dB}\,$ cuando la intensidad sonora se duplica.

\fi

>**Ejercicio 4.** La intensidad del sonido es inversamente proporcional al cuadrado de la distancia a la fuente sonora. ¿Cuánto cambia el nivel de intensidad del sonido si se duplica la distancia a la fuente sonora? 

\iffalse

*Solución.* Como la intensidad sonora $I$ es inversamente proporcional al cuadrado de la distancia, obtenemos $$I=\frac{k}{l^2},$$ donde $l$ es la distancia a la fuente sonora. Cuando la distancia se duplica, la intensidad del sonido será
$$\tilde{I}=\frac{k}{(2l)^2}=\frac{1}{4}\cdot\frac{k}{l^2}=\frac{1}{4}I\,.$$
La intensidad del sonido se reduce a $\frac{1}{4}$ de su valor original.

$$\Delta L=10\log{\frac{\frac{1}{4}I}{I_0}}-10\log{\frac{I}{I_0}}=10\cdot\left(\log{\frac{\frac{1}{4}I}{I_0}}-\log{\frac{I}{I_0}}\right)=10\log\left(\frac{\frac{\frac{1}{4}I}{I_0}}{\frac{I}{I_0}}\right)=10\log\frac{1}{4}\doteq-6\;\text{dB}\,.$$
El nivel de intensidad sonora se reduce en $6\,\text{dB}$ if 
si doblamos la distancia a la fuente sonora.

\fi

>**Ejercicio 5.** A partir de la fórmula del nivel de intensidad sonora $L=10\log{\frac{I}{I_0}}$,
expresa la intensidad sonora $I$.

\iffalse

*Solución.* En primer lugar, aislamos la función logarítmica 
$\frac{L}{10}=\log{\frac{I}{I_0}}$ y, a continuación, utilizamos la función inversa del logaritmo, es decir, la función exponencial:
$$10^{\frac{L}{10}}=\frac{I}{I_0}.$$
A partir de aquí, expresamos la intensidad sonora
$$I=I_0 \cdot 10^{\frac{L}{10}}.$$

\fi

>**Ejercicio 6.** ¿En cuántas veces aumentará la intensidad del sonido si el nivel de intensidad del sonido aumenta en $20\,\text{dB}$?

\iffalse

*Solución.* El valor del nivel de intensidad sonora cambia de $L_1=L$ to $L_2=L+20\,\text{dB}$. Utilizamos la fórmula $I=I_0 \cdot 10^{\frac{L}{10}}$ 
y expresamos el cociente $\frac{I_2}{I_1}$:
$$\frac{I_2}{I_1}=\frac{I_0 \cdot 10^{\frac{L_2}{10}}}{I_0 \cdot 10^{\frac{L_1}{10}}}=\frac{10^{\frac{L+20}{10}}}{10^{\frac{L}{10}}}=10^{\frac{L+20}{10}-\frac{L}{10}}=10^2=100.$$

Cuando el nivel de intensidad del sonido aumenta en $20\,\text{dB}$, la intensidad del sonido aumentará cien veces.

\fi

## Bibliografía
1. Kubera, Miroslav; Nečas, Tomáš; Beneš, Vojtěch. *Online učebnice fyziky pro gymnázia - Zvuk.* Disponible de <https://e-manuel.cz/kapitoly/mechanicke-vlneni/vyklad/zvuk/> [cit. 24.10.2023].


