---
keywords:
- plane geometry
- chain fraction
- quadratic equation
is_finished: true
---

# The Golden Ratio and Continued Fractions

Let us have a line segment $AB$ and a point $C$ that lies on it. We say that point $C$ 
divides line segment $AB$ in the golden ratio, 
if the lengths of the segments satisfy equation $$\frac{|AB|}{|AC|}=\frac{|AC|}{|CB|}.$$ 
This ratio is often denoted by the Greek letter $\varphi$ 
and has a value of approximately $1{.}618$.

![A line segment divided in the ratio of the golden section](00027_1.jpg)

A nice example of the use of the golden ratio in everyday life is the credit card. 
It has the shape of a so-called golden rectangle, the sides of which satisfy the golden ratio. 
The golden rectangle is a popular shape because of its balanced appearance; 
it is neither too long nor too wide.

![Golden rectangle and golden spiral](00027_2.jpg)

The golden ratio is closely related to the Fibonacci sequence. 
The terms of the Fibonacci sequence are numbers 
$1$, $1$, $2$, $3$, $5$, $8$, $13$, $21$, $34$, $55$, ..., where each term 
is the sum of the two preceding ones. 
We also refer to the individual terms of this sequence as Fibonacci numbers. 
What is the connection between the Fibonacci sequence and the golden ratio? 
It holds that the limit of the ratio of two consecutive terms 
of this sequence equals the golden ratio $\varphi$.

If we construct squares whose side lengths correspond exactly to the Fibonacci numbers, 
it is possible to arrange them nicely next to each other 
in the shape of a golden rectangle as shown in the figure. 
We can then inscribe a quarter circle in each square and we get the so-called 
golden spiral. The golden spiral is a special case of the logarithmic spiral.

In nature, the golden ratio appears in the form of the Fibonacci sequence. 
We can find it in the arrangement of the leaves on the stems.
The leaves grow one above the other so that they do not shade each other, 
the transition from one leaf to the next has the character 
of a spiral growth around the stem. 
Similar arrangements are found in the scales of the pine cone, 
the seeds of the sunflower, or the the pineapple peel. 
The logarithmic spiral is also found in the mollusc shells or in the 
fiddlehead fern. Tornadoes, cyclones and galaxies also have this shape.

The golden ratio is widely used in art to achieve aesthetically impressive 
and harmonious compositions. Painters and photographers use this ratio 
to determine the placement of key elements in their works. 
Architects often integrate the golden ratio into building designs.

## Infinite Continued Fraction

An infinite continued fraction is an expression of the form
$$x = a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cfrac{1}{a_3 + \ddots}}},$$
where $a_0$ is an integer and the numbers $a_i$ are positive natural numbers for  $i\in\mathbb{N}$. A continued fraction can also be finite.

The golden ratio can be expressed by the continued fraction
$$\varphi = 1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \ddots}}}.$$

> **Exercise 1.**
> Calculate approximate values of the golden ratio using finite continued fractions
>
> 1. $$1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1}}}$$
> 2. $$1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1}}}}$$

*Solution.* 

1. $$1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1}}}= 1 + \cfrac{1}{1 + \cfrac{1}{2}}= 1 + \cfrac{1}{\frac{3}{2}}=\frac{5}{3}\doteq1{.}67$$
2. $$1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1}}}}=1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{2}}}=1 + \cfrac{1}{1 + \cfrac{1}{\frac{3}{2}}}=1 + \cfrac{1}{\frac{5}{3}}=\frac{8}{5}=1{.}6$$

> **Exercise 2.**
> Calculate the exact value of the golden ratio $\varphi$.

*Solution.* 
Let's assume that line segment $AB$ has length $1$. We divide this line segment 
by the point $C$ in the golden ratio. Then we have
$$\varphi=\frac{|AB|}{|AC|}=\frac{|AC|}{|CB|}.$$ Let's denote 
$x=|AC|$, i.e. $x$ is the length of the longer line segment of the line segment $AB$. 
Then $|BC|=1-x$ holds for the length of the line segment $BC$ 
and thus we obtain the equation
$$\frac{1}{x} = \frac{x}{1-x},\tag{1}$$
which is defined for $x\neq0 \text{ and } x\neq1$. 
However, we do not need to consider these extreme values, 
because they certainly do not correcpond to the golden ratio.
By manipulating (1), we obtain a quadratic equation
$$x^2 + x - 1 = 0,$$
whose roots are
$$x_{1,2} = \frac{-1 \pm \sqrt{5}}{2}.$$
In our case, $x$ is the length of the line segment; therefore, a negative value of $x$ is not valid. 
Thus, we have the only satisfying solution to equation (1)
$$x_1 = \frac{-1 + \sqrt{5}}{2}.$$
Now we can calculate the value of the golden section $\varphi$:
$$\varphi=\frac{|AB|}{|AC|}=\frac{1}{x} = \frac{1}{\frac{-1 + \sqrt{5}}{2}}=\frac{2}{\sqrt{5}-1}.$$
By rationalizing the denominator we then get
$$\varphi=\frac{\sqrt{5}+1}{2}\doteq1{.}618.$$

> **Exercise 3.**
> Solve an equation inspired by the golden ratio in a finite continued fraction
> $$ x = 1 + \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{x}}}. $$

*Solution.* 

Let's simplify the equation step by step.
$$
\begin{aligned}
x &= 1 + \cfrac{1}{1 + \cfrac{1}{\frac{x+1}{x}}}\qquad\text{for }x\neq0\\
x &= 1 + \cfrac{1}{1 + \cfrac{x}{x+1}}\qquad\text{for }x\neq-1\\
x &= 1 + \cfrac{1}{\frac{x+1+x}{x+1}}\\
x &= 1 + \frac{x+1}{2x+1}\\
x &= \frac{3x+2}{2x+1}\\
\end{aligned}
$$


Under the condition $x\neq -\frac12$ we obtain a quadratic equation
$$2x^2 - 2x - 2 = 0.$$
Its roots are
$$x_{1,2} = \frac{1 \pm \sqrt{5}}{2}.$$
Note that one of the solutions is again the golden ratio.

## Literature

* Wikipedia. *Golden ratio* [online]. Dostupné z https://en.wikipedia.org/wiki/Golden_ratio [cit. 10.\,11.\,2023].
* Wikipedia. *Řetězový zlomek* [online]. Dostupné z https://cs.wikipedia.org/wiki/Řetězový_zlomek [cit. 10.\,11.\,2023].

