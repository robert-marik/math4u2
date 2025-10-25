---
# workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- sequences and series
- ratio
- geometric sequence
- arithmetic sequence
is_finished: true
---

# The Mathematics Hidden in a Sheet of Paper

## Paper Formats

The international standard for paper sizes is defined by ISO 216 and includes two main series. Series A includes formats A0 to A10, while series B includes formats B0 to B10. This standard is based on the original DIN 476 norm, which has been in use since 1922 in Germany. It was developed by the German mathematician and physicist Walter Porstmann.

The two series share two fundamental properties:

1. All formats are similar rectangles.

2. A smaller format is created from a larger one by halving it, i.e. dividing it into two mutually symmetric rectangles.[^1]

These properties are not arbitrary. They have both aesthetic value and practical applications. For example, each sheet of paper in the system can be produced from the largest sheet simply by cutting, without generating any waste.

Each series also has a specific additional property:

* In the A series, the area of ​​the largest paper A0 is $1\,\text{m}^2$.
* In the B series, the shorter side of the largest format B0 measures $1,\mathrm{m}$.

> **Exercise 1.** Determine the similarity ratio (reduction factor) between two consecutive
> paper formats, and also find the ratio of adjacent sides that each format must satisfy.

![Notation of side lengths for Exercise 1](math4you_00044.svg)

\iffalse

*Solution.* Let us first realize that we will be working with a rectangle (since halving a square never produces another square). The rectangle is divided along the axis of its longer side. If it were divided along the axis of the shorter side, the result would not be similar to the original rectangle – the longer side would remain unchanged while the shorter one would be halved.

Let $a$ be the longer side of the rectangle, $b$ the shorter side, and $k$ the reduction factor between two consecutive formats. We have $k\cdot a = b$ and $k\cdot b = \frac{a}{2}$. Substituting the first expression of $b$ into the second equation gives:
$$
\begin{align*}
k^2 \cdot a &= \frac{a}{2} \quad / :a \\
k^2 &= \frac{1}{2} \qquad \rightarrow \qquad k = \frac{1}{\sqrt{2}}=\frac{\sqrt{2}}{2}.
\end{align*}
$$
From the relation $k\cdot a = b$ it follows that the aspect ratio of the sides of the rectangle $a:b$ is the reciprocal of $k$, i.e. $\sqrt{2}$.

\fi

> **Exercise 2.** Calculate the dimensions of the largest A0 paper format, assuming that the lengths of its sides are integers in millimetres and its area is as close as possible to one square metre.

\iffalse

*Solution.* From the previous problem, we know that the dimensions of an A0 sheet are $b_0$ (shorter side) and
$b_0\cdot\sqrt{2}$ (longer side) where $b_0$ is the unknown length that needs to be calculated. We know that
$$
b_0\cdot b_0\cdot \sqrt{2} = 1000000\,\text{mm}^2,
$$
and therefore, solving for $b_0$ and after rounding to the nearest millimetre, we get the value $b_0\doteq 841\,\text{mm}$.
The length of the longer side is then $841\cdot \sqrt{2} \doteq 1189\,\text{mm}$.

\fi

> **Exercise 3.** In addition to the properties shared with series A, series B also has the property that the shorter side
>  of the largest format B0 measures exactly one metre. Show that if we assume that format A0 has an area of exactly
> one square metre, and we allow all formats to have non-integer dimensions, then for every non-negative integer $n$,
> the following holds:
> $$
> S(\mathrm{B}(n+1))=\sqrt{S(\mathrm{A}(n)) \cdot S(\mathrm{A}(n+1))},
> $$
> i.e. the area of ​​format $\mathrm{B}(n+1)$ is the geometric mean of the areas of formats $\mathrm{A}(n)$ and $\mathrm{A}(n+1)$.

\iffalse

*Solution.* Since the shorter side of format B0 measures $1,\mathrm{m}$, its longer side, according to the solution of Exercise 1 (which applies to format B as well, since the same geometric principles are used), must measure $\sqrt{2},\mathrm{m}$.
Therefore, the area of format B0 is $\sqrt{2}\,\text{m}^2$
and each subsequent sheet of the B(n) format has half the area of the previous one. Hence, 
$S\left( \mathrm{B}(n) \right) = \frac{\sqrt{2}}{2^n}\,\text{m}^2$ for each non-negative integer $n$.

Similarly, since $S(\mathrm{A}0)=1\,\mathrm{m}^2$
and every subsequent sheet of the format $\mathrm{A}(n)$ has half the area of the previous one,
it follows that $S\left( \mathrm{A}(n) \right) = \left( \frac{1}{2}\right)^n = \frac{1}{2^n}\,\text{m}^2$ for every $n$. Thus,
$$
\begin{align*}
\sqrt{S(\mathrm{A}(n)) \cdot S(\mathrm{A}(n+1))} &= \sqrt{\frac{1}{2^n} \cdot \frac{1}{2^{n+1}} }  
=\sqrt{\frac{1}{2^n} \cdot \frac{1}{2^n} \cdot \frac{1}{2} } \\
&= \frac{1}{2^n} \cdot \frac{\sqrt{2}}{2} = \frac{\sqrt{2}}{2^{n+1}} = S(\mathrm{B}(n+1)).
\end{align*}
$$

\fi

## Paper Folding

You may have once wondered how many times a sheet of A4 paper can be folded in half—and maybe you even tried it yourself. But what probably didn’t occur to you is that a mathematician can answer this question without ever folding the paper.

Let us consider the following simple model of paper folding.

![Paper folding model](math4you_00044_2.svg)

Each time the paper is folded in half, part of it is used to create the fold. We can model the shape of the fold as a semicircle whose radius equals the thickness of the paper. We can also observe that paper stacks up with each fold: we start with a single layer, after the first fold we have two layers, after the second fold four layers, and so on. In the following problems, we will work with this model.

> **Exercise 4.** What would be the thickness of the stacked office paper after four,
> seven, ten, twenty-one, and forty-two folds?
> Assume that the thickness of the paper is $t_0=0{.}1\,\text{mm}$.

\iffalse

*Solution.* It is easy to see that after $k$ folds, there are $2^k$ layers of paper. The total thicknesses would therefore be:
$$
\begin{align*}
t_4=&t_0\cdot 2^4=1{.}6\,\text{mm}\\
t_7=&t_0\cdot 2^{7}=12{.}8\,\text{mm}\\
t_{10}=&t_0\cdot 2^{10}=102{.}4\,\text{mm}\\
t_{21}=&t_0\cdot 2^{21}\approx 209{.}7\,\text{m}\\
t_{42}=&t_0\cdot 2^{42}\approx 439\,804\,\text{km}
\end{align*}
$$

\fi

These results show that there must be some limit to how many times a sheet of paper can be folded. One way to understand this limit is by examining how much paper is actually consumed by the fold itself during each step.

> **Exercise 5.** How much paper is “lost” during folding?

\iffalse

*Solution.* Let us consider paper of thickness $t$. During the first fold, a semicircle with radius $t$ forms at the crease (see previous figure), so we need $\pi t$ of paper for the fold.
During the second fold, two semicircles are formed—one with radius $t$ and the other with radius $2t$, so we need $\pi t + 2\pi t$ of paper, and in total:
$$
\pi t+ (\pi t+2\pi t)\,.
$$
In the third fold, semicircles are formed with radii $t$, $2t$, $3t$ and $4t$. We therefore lose
$\pi t +2\pi t + 3\pi t + 4\pi t$ of paper.
The total loss will be:
$$
\pi t+ (\pi t+2\pi t) + (\pi t +2\pi t + 3\pi t + 4\pi t)
$$
Analogously, after $n$ folds we lose
$$
\pi t+ (\pi t+2\pi t) + \cdots + (\pi t +2\pi t + \cdots  + 2^{n-1}\pi t)
$$
of paper. Factoring out $\pi t$, we can notice that what remains inside the brackets is the sum of the first terms of arithmetic sequences:
$$
\pi t\left[1+(1+2)+(1+2+3+4)+\cdots+(1+2+\cdots+2^{n-1}) \right]\,.
$$
If we use the standard formula repeatedly for the sum of the first terms of an arithmetic sequence, we get:
$$
\frac{\pi t}{2}(1\cdot 2+2\cdot 3+4\cdot 5+\cdots+2^{n-1}\cdot(2^{n-1}+1))\,.
$$
The $k$-th term here can be written in general form as:
$$
2^{k-1}\cdot\left(2^{k-1}+1\right)=(2^2)^{k-1}+2^{k-1}.
$$
The expression for the total paper loss can thus be rewritten as:
$$
\frac{\pi t}{2}\left[\left((2^2)^0+(2^2)^1+\cdots+(2^2)^{n-1}\right)+\left(2^0+2^1+\cdots+2^{n-1}\right) \right]\,.
$$
We thus obtain the sum of the first terms of two geometric
sequences, so we can use the formula for their sum and get:
$$
\frac{\pi t}{2}\left( \frac{2^{2n}-1}{3} + 2^n-1 \right)\,.
$$
By factoring out $\frac{1}{3}$ from the brackets, we have:
$$
\frac{\pi t}{6}\left((2^n)^2+3\cdot 2^n-4\right)
$$
and by factoring the expression we get:
$$
\frac{\pi t}{6}(2^n+4)(2^n-1)\,.
$$
This final expression essentially gives an estimate of the minimum length of paper of thickness $t$ needed in order to be folded $n$ times.

\fi

> **Exercise 6.** How many times can a typical A4 office paper with a thickness of $0{.}1\text{mm}$ be folded?

\iffalse

*Solution.* Using the result of the previous exercise, we are looking for the greatest natural number $n$ such that the following inequality holds:
$$
\frac{\pi \cdot 0{.}1}{6}(2^n+4)(2^n-1)<297.
$$
Solving this inequality exactly would not be easy—but fortunately, it’s not necessary. We only need to try out a few suitable values of $n$:
$$
\begin{align*}
\frac{\pi \cdot 0{.}1}{6}(2^6+4)(2^6-1)\doteq224{.}31;\\
\frac{\pi \cdot 0{.}1}{6}(2^7+4)(2^7-1)\doteq 877{.}76.
\end{align*}
$$
According to this model, a sheet of this size can be folded at most six times.

\fi

As a curiosity, let us add that the first person to derive the equation from Exercise 5 was a high school student, Britney Gallivan from California. She is currently the Guinness World Record holder for the most times a piece of paper has been folded in half. She managed to fold paper twelve times.
However, she couldn’t use standard A4 paper to achieve this—she used toilet paper with a length of $1{.}219$ metres.
Moreover, she employed a different folding technique, alternating the folding directions.

## Literature

1. Niss, Mogens; Bluem Werner. *The Learning and Teaching of Mathematical Modelling*, Routledge 2020, 978-1-315-18931-4

2. *Most times to fold a piece of paper.* https://www.guinnessworldrecords.com/world-records/494571-most-times-to-fold-a-piece-of-paper

3. *Wikipedia. Paper size.*  https://en.wikipedia.org/wiki/Paper_size

[^1]: The side lengths of the formats that were created by halving are rounded down to whole millimeters. The most commonly used A4 format has dimensions $210 \times 297 \, \mathrm{mm}$.
