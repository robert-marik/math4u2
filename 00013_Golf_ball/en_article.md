---
# workflow: in progress
workflow: translating
# workflow: finished
keywords:
- differential and integral calculus
- optimization
- quadratic equation
- derivative
is_finished: true
difficulty: 3
time: 30
---

# Golf Ball Hit

To describe the trajectory of a golf ball that has been hit, we need to recall a few facts about projectile motion. Projectile motion is the most general method of launching an object into motion in a uniform gravitational field. Assume that a point mass is launched at an angle in an environment without air resistance, with initial speed $v_0$. The corresponding initial velocity vector $\vec{v}_0$ makes an angle 
$\alpha \in \left(0,\frac{\pi}{2}\right)$ 
with the horizontal plane. In a Cartesian coordinate system, this vector is given by (see the figure):
$$\vec{v}_0=[v_0\cos\alpha,v_0\sin\alpha].$$

The motion of the object is affected by gravitational acceleration of magnitude $g$ acting vertically downward. In the horizontal direction, there is no component of gravitational acceleration, so the horizontal motion is uniform. In contrast, the vertical motion is influenced by gravity. Therefore, for the instantaneous velocity vector $\vec{v}=[v_x,v_y]$ at time $t \geq 0$, we have

$$
\begin{aligned}
        v_x=v_x(t) &= v_0 \cos\alpha,\\
        v_y=v_y(t) &= v_0 \sin\alpha-gt.
\end{aligned}
$$

For the coordinates $(x, y)$ of the point mass at time $t \geq 0$, we obtain

$$
\begin{aligned}
        x = x(t) &= v_0 t\cos\alpha,\\
        y = y(t) &= v_0 t\sin\alpha-\frac{1}{2}gt^2,
\end{aligned}\tag{1}
$$

because the instantaneous velocity at time $t$ is the derivative of the position at time $t$. Specifically, $v_x(t)=x'(t)$ and $v_y(t)=y'(t)$.

![Projectile motion](sikmy_vrh_upraveny.svg)

Now let us move on to the promised golf ball drive.

A golf player hits the ball with initial speed $v_0$ at an angle $\alpha \in \left(0,\frac{\pi}{2}\right)$. We assume that the ball is not affected by air resistance. Therefore, its motion satisfies the conditions of projectile motion without air resistance.

> **Task 1.** Prove that the trajectory of the golf ball is a part of a parabola.

\iffalse
*Solution.* To find the trajectory equation in the form $y=f(x)$, we need to convert the parametric representation (1) into a standard equation.

First, express $t$ from the first equation, i.e., $t=\frac{x}{v_0\cos\alpha}$, and substitute this into the second equation:

$$
 y = v_0\sin\alpha\, \frac{x}{v_0\cos\alpha} -\frac{1}{2}g\frac{x^2}{v_0^2\cos^2\alpha}= -\frac{g}{2v_0^2\cos^2\alpha}\cdot x^2+\frac{\sin\alpha}{\cos\alpha}\cdot x
$$

We see that the function $f$ describing the trajectory of the golf ball is a quadratic function

$$
 f(x)=Ax^2+Bx,
$$

where

$$
 A=-\frac{g}{2v_0^2\cos^2\alpha} \quad \text{and} \quad
 B=\frac{\sin\alpha}{\cos\alpha}.
$$

The graph of $f$ is a parabola. Therefore, the trajectory of the golf ball is a part of this parabola.
\fi

> **Task 2.** Compute the maximum height $y_{\text{max}}$ to be reached by the golf ball.

\iffalse
*Solution.* To compute the maximum height of the golf ball, we need to find the extreme value of the function $f$ describing the trajectory:

$$
 f(x) = -\frac{g}{2v_0^2\cos^2\alpha}\cdot x^2+\frac{\sin\alpha}{\cos\alpha}\cdot x
$$

Compute the derivative of $f$:

$$
f'(x) = -\frac{g}{2v_0^2\cos^2\alpha}\cdot2x+\frac{\sin\alpha}{\cos\alpha}
$$

To find the stationary point, set the derivative equal to zero:

$$
\frac{g}{v_0^2\cos^2\alpha}\cdot x=\frac{\sin\alpha}{\cos\alpha}.
$$

The solution is

$$
x_{0}=\frac{v_0^2\sin\alpha\cos\alpha}{g}.
$$

Since $f$ is a concave quadratic function, this stationary point $x_0$ is its (local and global) maximum.

The maximum height $y_{\text{max}}$ is obtained by substituting $x_0$ into $f$. After simplification, we get

$$
 y_{\text{max}}=f(x_{0})=\frac{v_0^2\sin^2\alpha}{2g}.
$$
\fi

> **Task 3.** Determine the angle $\alpha$ for which the ball reaches the maximum horizontal distance (for a given initial speed).

\iffalse
*Solution.* To compute the launch angle that maximizes the horizontal range, we first determine the $x$-coordinate $x_d$ of the landing point as a function of $\alpha$, e.i., we find the maximum of the function $x_d$. Since the ball hits the ground when its height is zero, we set

$$
 y = -\frac{g}{2v_0^2\cos^2\alpha}\cdot x^2+\frac{\sin\alpha}{\cos\alpha}\cdot x
$$

equal to $y=0$ and solve:

$$
\begin{aligned}
 0 &= -\frac{g}{2v_0^2\cos^2\alpha}\cdot x^2+\frac{\sin\alpha}{\cos\alpha}\cdot x \\[3mm]
 0 &= x\cdot\left(-\frac{g}{2v_0^2\cos^2\alpha}\cdot x+\frac{\sin\alpha}{\cos\alpha}\right)
\end{aligned}
$$

This factored equation has two solutions. The first, $x=0$, corresponds to the launch point, and the second, $x_d$, to the landing point. We can observe that

$$
x_d = x_d(\alpha) = \frac{2v_0^2\sin\alpha\cos\alpha}{g}=\frac{v_0^2}{g}\sin2\alpha.
$$

We now find the maximum of $x_d$. For $\alpha \in \left(0,\frac{\pi}{2}\right)$, the value $\sin 2\alpha$ is maximal when $\alpha=\frac{\pi}{4}$.

Thus, the maximum range is achieved when the ball is hit at angle $\alpha=\frac{\pi}{4}$, and the maximum distance is

$$
x_d \left(\frac{\pi}{4} \right) =\frac{v_0^2}{g}\sin\left(2\cdot \frac{\pi}{4} \right)=\frac{v_0^2}{g}.
$$

The function $x_d(\alpha) = \frac{v_0^2}{g}\sin2\alpha$ could also be found more easily by using symmetry of the parabola. The parabola vertex lies halfway along the ball trajectory; thus the landing point $x_d = 2 x_0$, where $x_0$ is the value computed in Task 2. This avoids solving the quadratic equation obtained by substituting $y=0$ into $y=f(x)$.
\fi

> **Additional questions to consider.** Think about how the situation changes if the golf ball is hit from an elevated point at height $h$ above the ground.
>
> 1) Is the trajectory still part of a parabola?  
> 2) What is the maximum height reached by the ball?  
> 3) How far will the ball travel?  
> 4) For a given initial speed, at what angle should the ball be hit to travel as far as possible?  

\iffalse
*Answer to Question 1.*  
For the coordinates $(x,\,y)$ of the ball at time $t \geq 0$, we have

$$
\begin{aligned}
       x &= v_0 t\cos\alpha,\\
       y &= h+v_0 t\sin\alpha-\frac{1}{2}gt^2.
\end{aligned}\tag{2}
$$

Similarly, as in Task 1, we obtain the trajectory as the graph of a function $f$:

$$
 y = h+v_0\sin\alpha\, \frac{x}{v_0\cos\alpha} -\frac{1}{2}g\frac{x^2}{v_0^2\cos^2\alpha},
$$

i.e.,

$$
 y = -\frac{g}{2v_0^2\cos^2\alpha}\cdot x^2+\frac{\sin\alpha}{\cos\alpha}\cdot x + h.
$$

This quadratic function differs from that in Task 1 only by the constant term, meaning their graphs are vertically shifted by $h$ in the direction of the $x$-axis.
*Answer to Question 2.*  
To find the maximum height of the hit golf ball, we obtain the same expression

$$
x_{0}=\frac{v_0^2\sin\alpha\cos\alpha}{g},
$$

as formerly derived in Task 2. (This is because the derivative of a constant function is the zero function — think about it.)

Substituting $x_0$ into $f$ gives

$$
 y_{\text{max}}=f(x_{0})=h+\frac{v_0^2\sin^2\alpha}{2g}.
$$

*Answer to Question 3.*  
Setting $y=0$ in

$$
 y = -\frac{g}{2v_0^2\cos^2\alpha}\cdot x^2+\frac{\sin\alpha}{\cos\alpha}\cdot x + h
$$

leads again to a quadratic equation:

$$
 -\frac{g}{2v_0^2\cos^2\alpha}\cdot x^2+\frac{\sin\alpha}{\cos\alpha}\cdot x + h = 0.
$$
This time, however, the equation is not in factored form, so we will solve it using the general formula for finding the roots of a quadratic equation. First, though, it will be useful to eliminate the fractions from the equation by multiplying by the expression $-2v_0^2\cos^2\alpha$. This gives us the quadratic equation
$$
 gx^2-2v_0^2\sin\alpha \cos\alpha \cdot x - 2hv_0^2 \cos^2\alpha = 0,
$$

which has two solutions:

$$
x_{1,2}=\frac{2v_0^2\sin\alpha \cos\alpha \pm \sqrt{4v_0^4\sin^2\alpha \cos^2\alpha+8ghv_0^2\cos^2\alpha}}{2g}.
$$

Simplifying we obtain 

$$
x_{1,2}=\frac{v_0\cos\alpha}{g} \cdot \left( v_0\sin\alpha \pm \sqrt{v_0^2\sin^2\alpha+2gh}\right).
$$

It is not difficult to realize that one of the roots (the one with the minus sign) is negative. Therefore, only one of the roots (the one with the plus sign) corresponds to our task. So the relevant range of the golf ball 

$$
x_d = \frac{v_0\cos\alpha}{g} \cdot \left( v_0\sin\alpha + \sqrt{v_0^2\sin^2\alpha+2gh}\right).
$$

Note that for $h=0$ we obtain

$$
x_d = \frac{v_0\cos\alpha}{g} \cdot \left( v_0\sin\alpha + \sqrt{v_0^2\sin^2\alpha}\right)=
\frac{v_0\cos\alpha}{g} \cdot 2v_0\sin\alpha=
\frac{v_0^2}{g} \sin 2\alpha,
$$

which matches the result from Task 3.

*Answer to Question 4.*  
Here the situation is more complicated. We would have to find the maximum of

$$
x_d(\alpha) = \frac{v_0\cos\alpha}{g} \cdot \left( v_0\sin\alpha + \sqrt{v_0^2\sin^2\alpha+2gh}\right),
$$

which is quite difficult. Skipping the derivation, we state only the result: the maximum occurs when the angle $\alpha$ satisfies

$$
\sin\alpha = \frac{v_0}{\sqrt{2v_0^2+2gh}}.
$$

Thus, we shall see that the optimal launch angle depends on the initial speed $v_0$ of the golf ball, the height $h$ of the goll ball launch point, and even also on gravitational acceleration $g$.

In the special case of $h=0$, the last expression becomes

$$
\sin\alpha = \frac{v_0}{\sqrt{2v_0^2}}=\frac{\sqrt{2}}{2},
$$

which corresponds to optimal angle $\alpha=\frac{\pi}{4}$, as previously found.
\fi

## References

1. Kubera, Miroslav; Nečas, Tomáš; Beneš, Vojtěch. *Online Physics Textbook for Grammar Schools – Projectile Motion* [online]. Available from: <https://e-manuel.cz/kapitoly/pouziti-pohybovych-zakonu/vyklad/vrhy/> [accessed 27.9.2023].
2. Moc, Ondřej; Eisenmann, Petr. *Projectile Motion from a Tower* [online]. Available from: <https://mfi.upol.cz/files/26/2602/mfi_2602_129_137.pdf> [accessed 27.9.2023]

## Links
* Projectile motion – https://cs.wikipedia.org/wiki/Vrh_%C5%A1ikm%C3%BD
