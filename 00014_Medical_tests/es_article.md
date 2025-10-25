---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- combinatoria, probabilidad y estadística
- probabilidad condicional
- frecuencia de aparición
is_finished: true
---

# Pruebas diagnósticas en medicina

Todas las personas se someten a muchas pruebas diagnósticas a lo largo de su vida, ya sea en la consulta del médico o en casa. No importa si se trata de una prueba de COVID-19, de la enfermedad celíaca, de un cribado mamográfico general o de una prueba de embarazo casera. En cualquier caso, queremos saber si el resultado de la prueba es fiable. Para cada una de estas pruebas se facilitan dos datos básicos:

- *La prueba de sensibilidad*: la probabilidad de que la prueba detecte la enfermedad cuando la tenga.
- *La prueba de sensibilidad*: la probabilidad de que la prueba sea negativa cuando no tengo la enfermedad.

La llamada *prevalencia de la enfermedad*, es decir, la relación entre el número de individuos que padecen la enfermedad y el número de todos los individuos de la población, también es importante para la evaluación.

## Interpretación de los resultados de las pruebas

En farmacias y droguerías se venden varias pruebas caseras para detectar alergias e intolerancias, como el COVID-19 o las pruebas de embarazo.  Por ejemplo, en el prospecto de una prueba para la enfermedad celíaca (intolerancia al gluten) se indica que la sensibilidad de la prueba es de $96{,}3\,\%$ y la especificidad de la prueba es de $89{,}7\,\%$. Sabemos que el número de celíacos en la población es de aproximadamente $1\,\%$, por lo que la prevalencia de la enfermedad es de $1/100$.

Nos interesará sobre todo la pregunta: Si doy positivo, ¿cuál es la probabilidad de que realmente sea celíaco? Intente adivinar primero la respuesta.  En el siguiente ejercicio, realizaremos el cálculo exacto.

> **Problema 1.** La sensibilidad de la prueba es del $96{,}3\,\%$, la especificidad de la prueba es del $89{,}7\,\%$
> y la prevalencia de la enfermedad es de $1/100$. ¿Cuál es la probabilidad de que un paciente que dé positivo en la prueba de la celiaquía padezca realmente la enfermedad?

\iffalse

*Solución.* Este es un ejemplo de problema de probabilidad condicional
que puede resolverse fácilmente utilizando el teorema de Bayes:

Sea $A$ un suceso aleatorio y sea $B_1,\dots, B_n$ un conjunto completo de sucesos. Si $P(A)>0$, $P(B_1)>0,\dots,P(B_n)>0$, entonces
$$
P(B_k|A)=\frac{P(A\cap B_k)}{P(A)}=\frac{P(A|B_k)P(B_k)}{\sum_{i=1}^{n}P(A|B_i)P(B_i)},\quad k=1,\dots,n.
$$

El símbolo $P(B|A)$ denota la probabilidad de que ocurra el suceso $B$ dado que ha ocurrido el suceso $A$.

Definamos las siguientes probabilidades:

 - $P(C)$ la probabilidad de que sea positivo (tengo la enfermedad),
 - $P(N)$ la probabilidad de que sea negativo (no tengo la enfermedad),
 - $P(+|C)$ la probabilidad de que la prueba sea positiva si soy positivo,
 - $P(-|C)$ la probabilidad de que la prueba sea negativa si soy positivo,
 - $P(+|N)$ la probabilidad de que la prueba sea positiva si soy negativo,
 - $P(-|N)$ la probabilidad de que la prueba sea negativa si soy negativo,
 - $P(C|+)$ la probabilidad de que sea positivo si la prueba es positiva.
  
Como la prevalencia es de $1/100$, entonces
$$
P(C)=0{,}01 \qquad P(N)=0{,}99
$$
y a partir de los datos dados
$$
P(+|C)=0{,}963 \qquad  P(-|C)=0{,}037 \qquad P(+|N)=0{,}103 \qquad P(-|N)=0{,}897.
$$

Según el teorema de Bayes, se cumple que

$$
\begin{aligned}
P(C|+)&=\frac{P(+|C)P(C)}{P(+|C)P(C)+P(+|N)P(N)}=\\
&=\frac{0{,}963\cdot0{,}01}{0{,}963\cdot0{,}01+0{,}103\cdot0{,}99}=0{,}086.
\end{aligned}
$$

Por lo tanto, la probabilidad de que un paciente que dé positivo tenga realmente la enfermedad es sólo $0{,}086$, es decir, $8{,}6\,\%$ .

\fi

*Nota.* Es muy probable que muchos alumnos no adivinen correctamente este resultado antes del cálculo. Esto no es sorprendente, ya que los estudios han demostrado que hasta el 95%  de los médicos no pueden responder correctamente a este tipo de preguntas.

> **Problema 2.** ¿Cuál es la probabilidad de que un paciente que da negativo sea realmente negativo?

\iffalse

*Solución.* Utilizaremos la notación del ejercicio anterior y el teorema de Bayes. Obtenemos 
$$
\begin{aligned}
P(N|-)&=\frac{P(-|N)P(N)}{P(-|N)P(N)+P(-|C)P(C)}=\\
&=\frac{0{,}897\cdot0{,}99}{0{,}897\cdot0{,}99+0{,}037\cdot0{,}01}=0{,}999583.
\end{aligned}
$$
Por lo tanto, la probabilidad de que un paciente con un resultado negativo esté realmente sano es de
$0{,}999583$, es decir, $99{,}96\,\%$.

\fi

## Interpretación sin probabilidad

Intentemos resolver de nuevo el primer ejercicio, pero reformularemos la tarea para evitar el concepto de probabilidad condicional.

> **Problema 3.** De cada 100 000 personas, unas 1 000 son celíacas. De estas 1 000 personas, la prueba detecta la celiaquía en 960 casos. De las 99 000 personas restantes que no son celíacas, 10 200 también darán positivo. Imaginemos el grupo de esas personas que dan positivo. ¿Qué proporción de ellas es realmente celíaca?

\iffalse

*Solución.* En total, tenemos $$960+10\,200=11\,160$$  
resultados positivos, pero sólo $960$ son verdaderos casos positivos, por lo que:

$$ \frac{960}{11\,160}=0,086 \quad\Longrightarrow\quad 8{,}6\,\%. $$

Vemos de nuevo que la proporción de personas que tienen la enfermedad entre las que dieron positivo es $8{,}6\, \%$.  

En este cálculo, hemos simplificado trabajando con números enteros y redondeando a la decena más próxima.  Así, hemos sacrificado un poco de precisión en aras de la simplicidad.  Además, hemos supuesto que todo saldría como predice la probabilidad, es decir, que exactamente 1 000 personas son celíacas.  Esto no siempre es cierto. Aunque este método es más sencillo y a menudo más fácil de entender, no suele aparecer en los libros de texto. Sin embargo, con este enunciado del ejercicio, el porcentaje de aciertos de los médicos en la estimación del resultado es casi del 100%.

\fi

## Bibliografía

1. Singh P., Arora A., Strand T.A., Leffler D.A., Catassi C., Green P.H., Kelly C.P., Ahuja V., Makharia G.K., 
   *Global Prevalence of Celiac Disease: Systematic Review and Meta-analysis*.
   Clin Gastroenterol Hepatol. 2018 Jun; 16(6):823-836. doi: 10.1016/j.cgh.2017.06.037.
2. Gigerenzer, G., *Calculated risks*, Simon and Schuster, 2003. 


