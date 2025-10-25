---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- combinatoria, probabilidad y estadística
- estadística
- conocimientos financieros
is_finished: true
---




# Lectura de datos de un gráfico 

La Oficina Checa de Estadística (ČSÚ) se creó en 1969 y, como principal órgano del servicio estadístico 
estatal, se encarga de recopilar datos, procesarlos, elaborar y publicar información 
estadística sobre diversos aspectos del desarrollo de la República Checa y sus regiones. En la página web oficial 
del ČSÚ <https://www.czso.cz/> podemos encontrar de forma gratuita gráficos y tablas que resumen, 
por ejemplo, la evolución demográfica, las estadísticas electorales, la siniestralidad en el tráfico, la evolución de los precios de la vivienda y la evolución del desempleo. 
Analizaremos uno de los gráficos en las siguientes tareas.

![Sede del ČSÚ en Praga (año 2017)](03_graf_csu.jpg)


En la página web de la Oficina Checa de Estadística se puede encontrar un gráfico que muestra la evolución del salario medio bruto mensual, 
que podemos ver en la figura 2. En el eje horizontal se indican los trimestres de los años analizados, las columnas azules corresponden 
al salario bruto nominal medio de entonces y la curva roja muestra la evolución del salario nominal ajustado 
por efectos estacionales. Ambos se indican en el eje vertical izquierdo en coronas. 
La curva azul claro indica el crecimiento del salario nominal (se muestra en la escala vertical derecha en porcentaje) 
y la curva azul oscuro indica el crecimiento del salario real (también se muestra en la escala vertical derecha).

![Salario medio mensual y crecimiento salarial](03_graf_1.jpg)

**Glosario**

* Del *salario bruto* que el empleador paga al empleado se deducen las cantidades correspondientes al seguro médico
  y social y al impuesto sobre la renta. El empleado recibe entonces el *salario neto*, que es inferior en el importe de estos gastos.

* *El salario nominal* es el salario bruto mensual expresado en coronas. *El salario nominal ajustado por efectos estacionales*
  es el salario nominal que ha sido ajustado estadísticamente para eliminar el efecto de los cambios estacionales en el empleo y los salarios.

* El salario nominal es una cantidad concreta, mientras que el *salario real* expresa cuánto puede
  comprar el empleado con esa cantidad. Puede ocurrir que, aunque a los empleados se les aumente el salario nominal, como
  todos los comerciantes suben más los precios de sus productos y servicios (en otras palabras, hay una gran *inflación*), su salario real disminuye.

* *El ritmo de crecimiento* es la medida de la dinámica de la evolución salarial. El ritmo de crecimiento interanual indica cómo han aumentado los salarios (nominales y reales)
  durante el último año. Por ejemplo, si el ritmo de crecimiento interanual de los salarios es del 2 %, significa que los salarios han aumentado precisamente un 2 % durante el último año. 



>**Tarea 1.** Decide si cada afirmación se deduce o no del gráfico.
>
>1. Desde 2018, el salario nominal bruto medio no ha bajado de $30\,000\,\text{Kč}$.
>2. Si aumenta el salario nominal bruto medio, también aumenta el índice del salario nominal.
>3. El crecimiento de los salarios reales en 2020 fue el más bajo de los últimos cinco años.




*Solución.* 

1. La afirmación es cierta: todas las columnas azules de la tabla superan las $30\,000\,\text{Kč}$ desde 2018,
   como se puede ver en la figura 3.

![Salario medio mensual y crecimiento salarial](03_graf_graf_2.jpg)

2. La afirmación no es cierta: por ejemplo, al pasar del tercer al cuarto trimestre de 2021, se produjo
   un aumento del salario medio bruto nominal, pero una disminución del índice del salario nominal.

3. La afirmación no es cierta: los valores del crecimiento del salario real para 2022 y 2023 son más bajos.




>**Tarea 2.** Define los valores entre los que se mueven los valores de las magnitudes durante el período observado.



*Solución.* El salario nominal bruto medio durante el período analizado oscila entre $22\,000$ - $50\,000\,\text{Kč}$. 
El crecimiento del salario nominal se sitúa entre $0\,\%$ y $13\,\%$, mientras que los valores del crecimiento del salario real oscilan entre $-12\,\%$ y $10\,\%$.



> **Tarea 3** Intenta explicar las diferencias entre el crecimiento de los salarios nominales y reales aproximadamente desde
> el tercer trimestre de 2021. Por el contrario, ¿qué se puede decir de la situación entre 2015 y 2016, cuando
> ambos valores eran comparables?



*Solución.* En el gráfico podemos ver que, a partir del tercer trimestre de 2021, el índice de salarios reales cayó drásticamente, 
mientras que los otros dos indicadores no lo hicieron (el salario nominal bruto incluso creció ligeramente, como en períodos anteriores). 
Esto apunta a un posible culpable: la alta inflación. Podemos confirmar esta sospecha en la página web 
del ČSÚ <https://www.czso.cz/csu/czso/mira_inflace>, donde en 
las tablas que siguen la tasa de inflación se puede ver que el aumento comenzó precisamente en el tercer trimestre de 2021. 

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| - | -: | -: | -: | -: | -: | -: | -: | -: | -: | -: | -: | -: |
| **2020** | 2,9 | 3,0 | 3,1 | 3,1 | 3,1 | 3,1 | 3,2 | 3,2 | 3,3 | 3,3 | 3,2 | 3,2 |
| **2021** | 3,0 | 2,9 | 2,8 | 2,8 | 2,8 | 2,8 | 2,8 | 2,8 | 3,0 | 3,2 | 3,5 | 3,8 |
| **2022** | 4,0 | 5,2 | 6,1 | 7,0 | 8,1 | 9,4 | 10,6 | 11,7 | 12,7 | 13,5 | 14,4 | 15,1 |
| **2023** | 15,7 | 16,2 | 16,4 | 16,2 | 15,8 | 15,1 | 14,3 | 13,6 | 12,7 | 12,1 | 11,4 | 10,7 |
| **2024** | 9,4 | 8,2 | 7,1 | 6,3 | 5,6 | 4,9 | 4,4 | 3,9 | 3,5 | 3,1 | 2,7 | 2,4 |

Cabe esperar que, por el contrario, la tasa de inflación fuera baja en los años 2015 y 2016, lo que puede verificarse de nuevo en el mismo lugar que en el párrafo anterior.

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| -- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| **2015** | 0,3 | 0,3 | 0,3 | 0,4 | 0,4 | 0,5 | 0,5 | 0,4 | 0,4 | 0,4 | 0,3 | 0,3 |
| **2016** | 0,4 | 0,4 | 0,4 | 0,4 | 0,4 | 0,3 | 0,3 | 0,3 | 0,3 | 0,4 | 0,5 | 0,7 |
| **2017** | 0,8 | 1,0 | 1,2 | 1,3 | 1,5 | 1,7 | 1,8 | 2,0 | 2,2 | 2,3 | 2,4 | 2,5 |
| **2018** | 2,4 | 2,4 | 2,3 | 2,3 | 2,3 | 2,3 | 2,3 | 2,3 | 2,3 | 2,2 | 2,2 | 2,1 |




