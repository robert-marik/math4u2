---
keywords:
- optimalization
- quadratic equation
- derivation
is_finished: True
---

% Pozor, oprava provedena pouze v en_article

# The launch of the ball

## Oblique launch 

The oblique launch is the most general way of setting a object in a
homogeneous gravitational field into motion. Suppose that a body
(point mass) has been thrown obliquely in space without
resistance. The initial velocity is $\vec{v}_0$ and the angle between
and the vector $\vec{v}_0$ and horizontal direction is
$\alpha$. Introduce the Cartesian coordinate system with horizontal
$x$-axis and vertical $y$-axis as on the picture. The coordinates of
the initial velocity vector are

$$\vec{v}_0=(v_0\cos\alpha,v_0\sin\alpha).$$

The motion of the body is governed by an acceleration of gravity $g$
directed vertically downwards. The horizontal component of the
gravitational acceleration is zero. Therefore the motion in the
horizontal direction is unaffected by the gravitational field and the
horizontal component of the motion is a motion with constant
speed. The vertical component of the motion is affected by the
negative acceleration $-g$ and it is a movement with constant
acceleration and initial velocity $v_0t\sin\alpha$ (an uniformly
decelerated motion).

For the coordinates of the body we can use formulas for distance
of motion with constant speed and constant acceleration an get
$$
\begin{aligned}
        x(t) &= v_0 t\cos\alpha,\\
        y(t) &= v_0t\sin\alpha-\frac{1}{2}gt^2.
\end{aligned}\tag{1}
$$

![An oblique throw](math4you_00013.jpg)

## Motion of golf ball

A golfer hits the ball with an initial velocity $v_0$. The angle
between the initial velocity and the horizontal plane is
$\alpha$. Let's assume that drag forces are negligible. The motion of
the ball therefore satisfies the conditions for movement of an
obliquely thrown body in an environment without air resistance.

>**Exercise 1.**  Prove that the trajectory of a golf ball is a parabola.

*Solution.* To find the equation of the trajectory in the form
$y=f(x)$ it is necessary to eliminate the parameter $t$ from
the system (1).

We solve the first equation with respect to time
$t=\frac{x}{v_0\cos\alpha}$ 
and substitute into the second equation:
$$y(x) = v_0\sin\alpha\,\frac{x}{v_0\cos\alpha} -\frac{1}{2}g\frac{x^2}{v_0^2\cos^2\alpha}= -\frac{g}{2v_0^2\cos^2\alpha}\cdot x^2+\frac{\sin\alpha}{\cos\alpha}\cdot x\ .$$
From here we see that the $y$-coordinate of the trajectory is a
quadratic function of the $x$-coordinate and the trajectory of the
golf ball is a parabola.

>**Exercise 2.** Calculate the height of the throw, i.e. the maximal
>height $y_{max}$ that the launched ball reaches.

*Solution.* The height of the throw is the maximum of the function
from the previous exercise:
$$f\colon y = -\frac{g}{2v_0^2\cos^2\alpha}\cdot x^2+\frac{\sin\alpha}{\cos\alpha}\cdot x\ .$$

We calculate the derivative of the function $f$ as

$$
y'=-\frac{g}{2v_0^2\cos^2\alpha}\cdot2x+\frac{\sin\alpha}{\cos\alpha}.
$$

To find the stationary point, we set the derivative equal to zero and
obtain the equation
$$
\frac{g}{v_0^2\cos^2\alpha}\cdot x=\frac{\sin\alpha}{\cos\alpha}\ .
$$
The solution of this equation is
$$
x_{max}=\frac{v_0^2\sin\alpha\cos\alpha}{g}\ .
$$

Since the trajectory of motion is a quadratic function with vertex up,
the located stationary point must be a maximum. The $y$-coordiante of
the stationary point is the height of the throw.

The height of the throw is calculated by evaluating the function $f$
at the obtained coordinate $x_{max}$:
$$y_{max}=\frac{v_0^2\sin^2\alpha}{2g}\ .$$

> **Exercise 3.** Given constant initial velocity, find the angle
> $\alpha$ which guaranties maximal distance between the initial and
> the terminal point on the trajectory.

*Solution.* To find the maximum range angle we need to obtain the
terminal point $x_d$ of the trajectory as a function of the angle
$\alpha$ and find the maximum of the function $x_d(\alpha).$ Given
that $y=0$ when the ball hits a ground, we find zeros of the function
$$y(x) = -\frac{g}{2v_0^2\cos^2\alpha}\cdot x^2+\frac{\sin\alpha}{\cos\alpha}\cdot x.$$
From here we obtain:
$$0 = -\frac{g}{2v_0^2\cos^2\alpha}\cdot x^2+\frac{\sin\alpha}{\cos\alpha}\cdot x\ ,$$
$$0 = x\cdot\left(-\frac{g}{2v_0^2\cos^2\alpha}\cdot x+\frac{\sin\alpha}{\cos\alpha}\right)\ .$$
This factorized equation has two solutions. The first solution
$x=0$ corresponds to the place where the ball is launched and the
second solution $x_d$ to the place of impact
$$x_d(\alpha) = \frac{2v_0^2\sin\alpha\cos\alpha}{g}=\frac{v_0^2}{g}\sin2\alpha\ .$$ 
Now we need to find the maximum of the function $x_d(\alpha)$. It is
sufficient to find the stationary point, since it has been showed that
the trajectory is a parabola with vertex up. We calculate the
derivative of the function $x_d(\alpha)$ by $\alpha$

$$x_d'(\alpha)=\frac{v_0^2}{g}\cdot\cos2\alpha\cdot 2\ .$$ 

Letting the derivative equal to zero, we get 
$\cos2\alpha=0$, which is satisfied for $2\alpha=90^\circ$ (for the
ball to be launched, obviously
$\alpha\in\langle0^\circ,90^\circ\rangle$, so the solution is
unambiguous). Thus the stationary point is $\alpha=45^\circ$.

The maximum range in golf is achieved when hitting the ball at an
angle $\alpha=45^\circ$ and the ball lands at a distance of
$$x_d(45^\circ) =\frac{v_0^2}{g}\sin(2\cdot45^\circ)=\frac{v_0^2}{g}.$$

Note that it is possible to obtain the function $x_d(\alpha) =
\frac{v_0^2}{g}\sin2\alpha$ without calculus by using the symmetry of the
parabola. The vertex of the parabola is located in the
middle of the zeros. Therefore, for the $x$-coordinate
of the impact point can be evaluated as $x_d(\alpha) = 2\cdot x_{max}$.  This avoids
solving the quadratic equation obtained by substituting $y=0$ into the
function $y(x)$ and factorizing the right-hand side.

## Literature

1. Kubera, Miroslav; Nečas, Tomáš; Beneš, Vojtěch. *Online učebnice
   fyziky pro gymnázia - Vrhy* [online]. Available from
   <https://e-manuel.cz/kapitoly/pouziti-pohybovych-zakonu/vyklad/vrhy/>
   [cit. 27.9.2023].
2. Moc, Ondřej; Eisenmann, Petr. *Šikmý vrh z rozhledny*
   [online]. Available from
   <https://mfi.upol.cz/files/26/2602/mfi_2602_129_137.pdf>
   [cit. 27.9.2023]
