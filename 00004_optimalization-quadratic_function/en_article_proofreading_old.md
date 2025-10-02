---
title: Optimization - Quadratic functions
author: Math4U, Jakub Novák
---

# Optimization - Quadratic functions

## Assignment

The owner of a city taxi service is considering whether to buy more cars and how many to buy 
to maximize his earnings. He has 3 cars currently, each of which he 
earns an average of 60 000 CZK per month. However, according to years of experience in the industry 
he expects that with each car purchased, the average earnings of each car will decrease by 
5 000 CZK as there will be a partial spillover of customers into the new car. Must
also take into account that the cost of the driver and the car for one month is 40 000 CZK.

>**Exercise 1.** What is the monthly profit of a taxi owner now?

*Solution.* Each of the three cars earns the taxi owner a net profit (after deducting costs)
20 000 CZK, so the total current profit is 60 000 CZK.

>**Exercise 2.** Determine a function that expresses the profit of a taxi owner as a function of the number of 
cars. Which function is it and what does its graph look like?

*Solution.* Let $x$ denote the number of newly purchased cars and $y$ the profit of the owner in one night.
We know that the net profit of one car is 20 000 CZK, but we still have to subtract
the amount for the reduction in sales when $x$ cars are purchased. So in total, one car will bring 
a profit
$20\ 000-5\ 000x$ CZK to the owner. We obtain the total profit by multiplying this
expression by the new amount of the cars:

$$
y=(20\ 000-5\ 000x)(x+3)
$$

By multiplying and simplifying the right side, we can see that the function $$f\colon y= -5\ 000x^2 + 5\ 000x + 60\ 000$$ 
is quadratic. Its graph is a concave parabola because the coefficient of the quadratic term is negative.

>**Exercise 3.** Determine the owner's maximum possible profit. How much does this profit differ from 
the current profit? How many cars does the owner have to buy (or possibly sell)?

*Solution.*
Our task now is to determine the maximum of the function $f$. It is at the point that is

[It is located at the point whose x-coordinate is the arithmetic mean of the real roots of a quadratic polynomial]: # 

the arithmetic mean of the real roots of a quadratic polynomial (assuming
that they exist). We will determine these roots now:

$$
\begin{aligned}
-5\ 000x^2 + 5\ 000x + 60\ 000 &= 0 \\
x^2  - x - 12 &= 0\\
(x-4)(x+3)&=0
\end{aligned}
$$

The roots of the quadratic equation are $x_1=4$ and $x_2=-3$, therefore the maximum of the function $f$ is
at the point $$x_{max}=\frac{-3+4}{2}=\frac{1}{2}.$$ 

![Graph of function](04_graph_smaller.jpg)

However, this maximum i unreachable (it is not possible to 
buy half a car). The highest functional value that makes sense to consider is in
this case located at the nearest integer points, i.e. $x=0$ or $x=1$
(the value is same at both points, as follows from the symmetry of the parabola). However, this means
that it is not profitable for the owner to buy more cars because his current profit
is also maximal.

