---
keywords: function, rational fractional function, asymptote
is_finished: False
---

# Trophic Functions in Predator-Prey Models

Mathematical models play an important role in the study of nature.  These models not only make it possible to predict future developments, but they also serve several other important purposes.


The use of ecological models is sometimes referred to as a physical approach in ecology, as these models examine ecosystems in terms of population dynamics while employing mathematical methods originally developed for solving physical problems. The outputs of such models can provide the following types of insights:

* **Predictions** 
Working with mathematical models of ecosystems enables scientists to predict future developments. This may include the evolution of populations in a stable environment as well as evolution in environments with varying parameters.  Understanding the model will then reveal how the change in parameters
affects the ecosystem.

* **Understanding the principles** Mathematical models allow ecologists and
    scientists to examine the interactions between different components of ecosystems and
    to better understand the dynamics of these systems. Such models help to identify the key
    factors that influence the ecosystem structure and function.
* **Optimizsing decision making** Mathematical modelling of ecosystems
     can be used to optimize decision-making in areas such as
     biodiversity conservation, or forest and fisheries management. 
     It helps identify the effective strategies
     to achieve specific objectives.  
  One of the fundamental relationships in ecosystems is that between _predator and
 prey_. This relationship may be the only form of interaction in a given ecosystem or
may be complemented by other types of interactions. The importance of predator-prey models will be illustrated with the following historically significant examples.



## Lotka-Volterra Model


In 1926, one of the first predator–prey models was published by the Italian mathematician Vito Volterra. The motivation behind this model was the observation that, during fishing restrictions imposed in World War I, the percentage of predatory fish in the catch increased. 

The marine biologist Umberto D’Ancona noticed this phenomenon but was unable to explain it. He had actually expected the opposite: with fishing limited, he anticipated an increase in the proportion of smaller fish species that serve as food for predators. D’Ancona introduced this problem to his father-in-law, Volterra, who explained the observation using a simple predator–prey interaction model. 


The model consists of two equations. The first, describing the prey population, assumes that the population grows naturally but that this growth is slowed down by predation. An increase in predator numbers leads to slower growth of the prey population. If there are too many predators, the prey population may even decline and even die out. 
The second equation, describing the predator population, assumes that in the absence of prey, the predators would eventually die out. However, when prey is abundant, the predator population is more likely to increase.

 
In the system described above, cyclical population dynamics occur naturally. A sufficient prey population allows predators to thrive. As the predator population grows, it negatively affects the prey population, which then begins to decline. This leads to a food shortage for the predators, causing their numbers to drop as well. Over time, the predator population decreases to a level where the prey barely senses their presence. The prey population can then recover and grow toward its original size. The increase in prey population allows the predator population to grow again, closing the cycle.

These periodic changes in the sizes of both populations are reflected in historical records of snowshoe hare and lynx fur purchases in the Hudson Bay area.


Volterra’s model not only explains the origin of these cycles but also predicts that reducing the rate of hunting shifts the equilibrium point—around which both predator and prey populations oscillate—in favor of the predators rather than the prey. This phenomenon, observed by D’Ancona, is known as the _Volterra effect_.

The same model as Volterra's has been proposed in 1910 by the American mathematician
Alfred J. Lotka. For this reason, the model is known today as the Lotka-Volterra model.

![On the left, a typical pattern of predator and prey population sizes. A maximum in the prey population is followed by a maximum in the predator population, then a decline in both. On the right, the island fox, which has gone from being a top predator on its island to a prey endangered by extinction](1.jpg)

## Spruce Budworm Model


Similar periodic fluctuations to those described by the Lotka–Volterra model can also be observed in Canadian forests. Approximately every 30 to 40 years, a mass outbreak of the spruce budworm (_Choristoneura Fumiferana_) occurs. For most of the time, the population of this butterfly remains relatively small, but in certain years it increases by a factor of thousands. During such outbreaks, its caterpillars can kill up to 80% of trees in the forest, virtually destroying it. One of the most recent mass outbreaks began in 2006 in Quebec. By 2019, about 9.6 million hectares of forest had been affected[^1], which is more than the size of Hungary.

See [^1]: source at <https://www.nrcan.gc.ca>.

 
In 1978, scientists D. Ludwig, D. D. Jones, and C. S. Holling proposed a model that not only described the dynamics of the spruce budworm population but also helped clarify the underlying cause of these outbreaks: predation. Specifically, the consumption of budworm caterpillars by birds.

Birds naturally serve as a limiting factor on caterpillar numbers, but only up to a certain limit. As forests grow larger, they provide more food for the caterpillar population. The population then grows to such an extent that the birds reach their feeding limit and can no longer reduce the caterpillar population. At this stage, the role of birds as predators diminishes, and the caterpillar population can grow rapidly, eventually devastating the forest.


In this case, predation is key to limiting the spruce budworm population. However, since birds have a much slower reproductive cycle than insects, their population can be considered constant. Through saturation, their ability to limit the budworm growth rate is thus restricted. Once the budworm population exceeds a certain threshold, this control mechanism fails, leading to uncontrollable overpopulation.

## Island Fox Model



The island fox (_Urocyon littoralis_) is a unique species, endemic only to the Channel Islands off the coast of California. It is about the size of a domestic cat and is unusually trusting due to the historical absence of natural predators. As a species, it is particularly sensitive and vulnerable due to low genetic variation and limited resistance to diseases introduced from the mainland. It is also one of the smallest canids, and unlike most others, it can climb trees.

As a result of human activity, the population of the island fox was near to extinction at the end of the millennium. On San Miguel Island, the population declined from
450 adults in 1994 to just 15 in 1999[^2]. A similar situation occurred also on the other islands, each of which is home to a distinct subspecies of the island fox.
 
The cause of the decline was a chain of events. In the 1940s, the production of the insecticide DDT led to the local extinction of the bald eagle (_Haliaeetus leucocephalus_), a fish-eating predator. On the island, it was eventually replaced by the golden eagle (_Aquila chrysaetos_), which prefers mammals as prey. This shift proved fatal for the island fox. Once the top predator on the islands, the fox suddenly became prey. By the turn of the millennium, it was on the verge of extinction.

Moreover, unlike in the Lotka–Volterra model, there was no hope of the foxes returning to their original numbers through oscillations, because the eagles also had alternative food sources, such as wild pigs and skunks.


[^2]: For source see <https://www.iucnredlist.org/species/22781/13985603>.


Fortunately, thanks to tremendous conservation efforts, the island fox was saved from extinction. Once the causes of the population decline were identified, it was possible to restore the population and create conditions for long-term stability. This involved the removal of feral pigs, the relocation of golden eagles to the mainland, the reintroduction of bald eagles, captive breeding of foxes, their reintroduction to the wild, and vaccination against diseases brought from the mainland.
All of this was achieved in record time—within a single decade. It became one of the most successful mammal rescue programs in history.

## Trophic Functions

An important component of predator-prey models, whether it be
any of the above examples, is the _trophic function_. This function
describes the effect of a single predator on a prey population. It is given by
the rate at which the growth of prey is slowed by a single predator. If $x$
is the size of the prey population and $y$ is the rate at which one predator
slows the growth of prey down (i.e., the amount of prey taken by a predator in
unit time), we can write this function mathematically in the form

$$
y=f(x).
$$ 

We'll try to find natural assumptions that
the trophic function must satisfy. Then we will try to find a suitable
analytical form.

> **Exercise 1.** Assumptions about the predator's effect on prey are reflected in
>    the properties that a trophic function must have. 
> 
> 1. A predator in an environment with a poor food supply also has a low
> catch. More prey means easier access to prey, and thus a higher
> catch.
> 2. Without food, a predator will not catch anything. If the prey population  is zero,
> the amount of prey a predator catches per unit time is also zero.
> 3. Predators consume food only until they are saturated. If food
> is abundant, predators will not catch more pray per unit time than 
> their saturation level.
> 
> Express these characteristics in terms that we use to describe
> properties of functions. Which propertyies of a functions correspondss to each of the points (characteristics) above?


\iffalse

_Solution._

1. The function $y=f(x)$ is increasing.

2. The function $y=f(x)$ goes through the origin, i.e., $f(0)=0$.

3. The function $y=f(x)$ is bounded above. Since the function is increasing and 
is bounded above, its graph has a horizontal asymptote at infinity.

\fi

## Holling's Type II Trophic Function

The trophic function indicates how much prey one predator kills 
per unit time for a given prey population size. It must therefore be defined on
a set of non-negative numbers and the function values will be non-negative (this follows 
from points 1 and 2 in Exercise 1). In the previous section it was shown that 
the trophic function has to pass through the origin
and grow to the horizontal asymptote (growth and boundedness from above). These
properties will not be satisfied if we look for a trophic function in the set of 
linear functions. So we try the simplest nonlinear function,
the inverse proportionality.

![On the left, two typical trophic functions, called Holling's functions. The growth rate of the function
of type II slows down. The type III function grows slowly at first, accelerates and then slows down again. On the right, the type II function as part of
transformed graph of inverse proportionality. (own figure)](2.svg)

> **Exercise 2.** Graph the function $y=\frac 1x$. On this function
> perform transformations that change the graph as described below.
>
> 1. Scale the graph $k$ times in the vertical direction. This does not change the monotonicity
> nor the position of the horizontal asymptote, but we can change the growth rate.
> 2. Flip the graph about the horizontal axis and translate $S$ units up. This produces a function
> which is positive and increasing for positive $x$ and the function grows to
> the asymptote $y=S$.
> 3. After the above transformations, the graph has a vertical asymptote at zero and
> one intersection with the x-axis to the right of the origin. Move the graph
> to the left so that the vertical asymptote is to the left of the y-axis and
> the intersection with the $x$-axis is shifted to the origin.

\iffalse

_Solution._ A function whose graph is obtained by rescaling the graph of the function
$y=\frac{1}{x}$ in the vertical direction by a factor of $k$ is 
$$
y=\frac{k}{x}.
$$
The flip about $x$-axis is achieved by multiplying the function by $-1$, and the upward shift is achieved by
by adding the value of $S$. These adjustments give the function $$y=S-\frac{k}{x}.$$ The shift
to the left by $b$ is achieved by substituting the expression $x+b$ for $x$. This gives us
the function $$y=S-\frac{k}{x+b}.$$ When converted to a common denominator,
the function takes the form 
$$
y=\frac{Sx+Sb}{x+b}-\frac{k}{x+b}=\frac{Sx + (Sb-k)}{x+b}.
$$ 
To ensure $f(0)=0$, the following condition must be satisfied.
$$
Sb-k=0
$$ 
This condition shows that the three constants are not independent
but are related by this equation.

\fi

*Note.* In the previous exercise, we derived an analytical form for
  one of the basic trophic functions. This is an increasing function that initially grows toward a horizontal asymptote, and the rate of growth
  gradually decreases. Such a function is called the Holling's type II
  function. It is common to write it in the form 
  $$
  f(x)=\frac {Sx}{x+b},\tag{1}
  $$
  where $S$ is the saturation level and $b$ is a constant. The role of the constant $b$ will be explained
  in the following exercise.

> **Exercise 3.** Show that for a population size equal to $b$, 
the value of the trophic function (1) is equal to half the 
saturation level.

\iffalse

_Solution._ By setting $x=b$ in (1), we get
$$
f(b)=\frac{Sb}{b+b}=\frac {Sb}{2b}=\frac {S}{2}.
$$ 
This proves the statement.

\fi     

The following exercise shows the reverse process, starting from a trophic function of the form
(1), we derive a form showing the successive transformations of the function $y=\frac 1x$.

> **Exercise 4.** Rewrite the equation of the function $$y=\frac {6x}{x+2}$$ into its basic form. Into such a form,  so that the successive transformations applied to the graph of the function $y=\frac 1x$ to obtain the given function can be easily read.

\iffalse

_Solution._ We can solve this problem by cleverly manipulating the fraction. In the numerator, we create a multiple
of the denominator, split this expression into two fractions, and cancel $(x+2)$ in the first one:

$$
\frac {6x}{x+2} = \frac {6(x+2)-12}{x+2}=\frac {6(x+2)}{x+2}-\frac {12}{x+2}=6-12\frac 1{x+2}
$$

This form of the equation of the given function shows that its graph is obtained by vertically stretching
the graph of the function $y=\frac 1x$ by a factor of $12$, flipping it about the
$x$-axis, shifting it $6$ units up, and $2$ units to the left.


The same result can also be obtained by polynomial long division of the numerator by the denominator.

\fi

> **Exercise 5.** Construct a trophic function given that the predator saturation is $6$, and that the consumption rate is half of the saturation for a prey population of $210$.
\iffalse

*Solution.*  From the note before Exercise 3 regarding the general form of a trophic function, we know that 
$$
y=\frac{Sx}{x+b},
$$
where $S$ is the predator saturation level. In this case,
$$
y=\frac{6x}{x+b}.
$$
We can determine the value of the parameter $b$ straight away using the result of Exercise 3, or compute it directly from the second condition in the problem. Since the consumption rate is half of the saturation for a prey population of $210$, we have:
$$
3=\frac{6\cdot 210}{210+b}.
$$
Solving this equation gives $b=210$. Therefore, the final form of the sought trophic function is
$$
y=\frac{6x}{x+210}.
$$

\fi

## References

### Literature

* Wikipedia, <https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations> March 3, 2024
* R Mařík, Dynamické modely populací (in Czech), <https://robert-marik.github.io/dmp/uvod.html>, March 3, 2024
* D. Ludwig, D.D. Jones, C.S. Holling: Qualitative analysis of insect outbreak systems: the spruce budworm and forest, Journal of Animal Ecology 47(1): 315–332, February 1978.

### Image Sources

* <https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations#/media/File:Lotka_Volterra_dynamics.svg>
* <https://www.npr.org/sections/thetwo-way/2016/08/11/489695842/once-nearly-extinct-california-island-foxes-no-longer-endangered> Kevork Djansezian/AP 

