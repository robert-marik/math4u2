---
keywords:
- exponentials and logarithms
- logarithms
- logarithmic equation
- exponential equation
is_finished: true
---

# Sound

Sound is a mechanical wave that we perceive by hearing.
All people perceive the pitch and duration of a tone in approximately the same way, 
but the perception of loudness is very subjective. 
Loudness is determined by the amplitude of the oscillation in the medium 
through which the sound wave propagates. 
Since the amplitude of sound waves is not easily measured, 
the quantities of sound intensity $I$ and sound intensity level $L$
are used to compare loudness objectively.

*Sound intensity* expresses how much energy sound waves transfer to a unit area perpendicular to the direction of sound propagation per unit time.
A healthy ear can detect the smallest sound intensity $I_0=10^{-12}\,\text{W}/\text{m}^2$ at a frequency of $1000\,\text{Hz}$, which corresponds to the hearing threshold.
On the other hand, the sound intensity of $10\,\text{W}/\text{m}^2$ is loud enough to correspond to the pain threshold.
However, increasing the sound intensity $I$ ten times does not correspond to perceiving the sound ten times louder. 
Therefore, the sound intensity level $L$ is rather used to express sound loudness,
which uses a logarithmic scale in decibels (dB).

*Sound intensity level* $L$ in decibels is defined by the equation $$L=10\log{\frac{I}{I_0}},$$
where $I$ is the sound intensity at the given location 
and $I_0=10^{-12}\,\text{W}/\text{m}^2$, which corresponds to the hearing threshold.
The sound intensity level of $60\,\text{dB}$ corresponds to the loudness of a normal conversation, $90\,\text{dB}$ is the loudness of a lawnmower, and $110\,\text{dB}$ is the loudness of a discotheque.

There is a risk of hearing impairment for long-term listening 
(even though we are not in pain) of volumes higher than $85\,\text{dB}$.
From a volume higher than $100\,\text{dB}$, there is a risk of hearing damage within minutes.
 Let's explore the relation between sound intensity and sound intensity level, i.e., the loudness perceived by hearing.

>**Exercise 1.** The sound intensity is $1{,}27\cdot10^{-3}\,\text{W}/\text{m}^2$ 
>while listening to a speaker with a sound power of $20\,\text{W}$
>at a distance of $50\,\text{m}$ from it
>(assume uniform transmission of the sound wave into free half-space).
>How many decibels do we measure at this location?

\iffalse

*Solution.* We use the definition of sound intensity level $L=10\log{\frac{I}{I_0}},$ for calculation, where $I=1{,}27\cdot10^{-3}\,\text{W}/\text{m}^2$ is the sound intensity at the
given location and $I_0=10^{-12}\,\text{W}/\text{m}^2$.
$$L=10\log{\frac{I}{I_0}}=10\log{\left(\frac{1{,}27\cdot10^{-3}}{10^{-12}}\right)}=10\log{\left(1{,}27\cdot10^{9}\right)}=91\;\text{dB}\,.$$

The sound intensity level is $91$ dB at a distance $50$ m from the speaker, 
which corresponds to the noise level of a motorcycle or a lawnmower.

\fi

>**Exercise 2.** How will the sound intensity level change if there is
>twice the sound intensity at the location from the previous example, i.e., $2\cdot1{,}27\cdot10^{-3}\,\text{W}/\text{m}^2$ ?

\iffalse

*Solution.* We use the same formula as in the previous exercise:
$$L=10\log{\frac{I}{I_0}}=10\log{\left(\frac{2\cdot1{,}27\cdot10^{-3}}{10^{-12}}\right)}=10\log{\left(2{,}54\cdot10^{9}\right)}=94\;\text{dB}\,.$$
The calculation shows that twice the sound intensity does not correspond 
to twice the number of decibels. The sound intensity level will increase from
$91\,\text{dB}$ to $94\,\text{dB}\,$.

\fi

>**Exercise 3.** From the formula for the sound intensity level,
>find the value $\Delta L$, by which the sound intensity level $L$,
>changes if the sound intensity is doubled from $I$ to $2I$.

\iffalse

*Solution.* This is a generalization of the previous problem.$$\Delta L=10\log{\frac{2I}{I_0}}-10\log{\frac{I}{I_0}}=10\cdot\left(\log{\frac{2I}{I_0}}-\log{\frac{I}{I_0}}\right)=10\log\left(\frac{\frac{2I}{I_0}}{\frac{I}{I_0}}\right)=10\log2=3\;\text{dB}$$
When doubling the sound intensity, the sound intensity level increases by $3\,\text{dB}\,$.

This is a generalization of the previous problem.$$\Delta L=10\log{\frac{2I}{I_0}}-10\log{\frac{I}{I_0}}=10\cdot\left(\log{ \frac{2I}{I_0}}-\log{\frac{I}{I_0}}\right)=10\log\left(\frac{\frac{2I}{I_0}}{\frac{I} {I_0}}\right)=10\log2\doteq3\;\text{dB}$$
The sound intensity level increases by $3\,\text{dB}\,$ when the sound intensity doubles.

\fi

>**Exercise 4.** Sound intensity is inversely proportional
>to the square of the distance from the sound source.
>By how much does the sound intensity level change if the distance
>from the sound source is doubled? 

\iffalse

*Solution.* Since the sound intensity $I$ is inversely proportional to the square of 
the distance, we get $$I=\frac{k}{l^2},$$ where $l$ is the distance from 
the sound source. When the distance is doubled, the sound intensity will be
$$\tilde{I}=\frac{k}{(2l)^2}=\frac{1}{4}\cdot\frac{k}{l^2}=\frac{1}{4}I\,.$$
The sound intensity is reduced to $\frac{1}{4}$ of its original value.

$$\Delta L=10\log{\frac{\frac{1}{4}I}{I_0}}-10\log{\frac{I}{I_0}}=10\cdot\left(\log{\frac{\frac{1}{4}I}{I_0}}-\log{\frac{I}{I_0}}\right)=10\log\left(\frac{\frac{\frac{1}{4}I}{I_0}}{\frac{I}{I_0}}\right)=10\log\frac{1}{4}\doteq-6\;\text{dB}\,.$$
The sound intensity level is reduced by $6\,\text{dB}$ if 
we double our distance from the sound source. 

\fi

>**Exercise 5.** From the formula for the sound intensity level $L=10\log{\frac{I}{I_0}}$,
>express the sound intensity $I$.

\iffalse

*Solution.* First, we isolate the logarithmic function 
$\frac{L}{10}=\log{\frac{I}{I_0}}$ and then we use the
 inverse 
function of the logarithm, i.e., the exponential function:
$$10^{\frac{L}{10}}=\frac{I}{I_0}.$$
From here, we express the sound intensity
$$I=I_0 \cdot 10^{\frac{L}{10}}.$$

\fi

>**Exercise 6.** By how many times will the sound intensity increase
>if the sound intensity level increases by $20\,\text{dB}$?

\iffalse

*Solution.* The value of the sound intensity level changes from $L_1=L$ to $L_2=L+20\,\text{dB}$. We use formula $I=I_0 \cdot 10^{\frac{L}{10}}$ 
and express the quotient $\frac{I_2}{I_1}$:
$$\frac{I_2}{I_1}=\frac{I_0 \cdot 10^{\frac{L_2}{10}}}{I_0 \cdot 10^{\frac{L_1}{10}}}=\frac{10^{\frac{L+20}{10}}}{10^{\frac{L}{10}}}=10^{\frac{L+20}{10}-\frac{L}{10}}=10^2=100.$$

When the sound intensity level increases by $20\,\text{dB}$, the sound intensity increases a hundred times.

\fi

## Literature 
1. Kubera, Miroslav; Nečas, Tomáš; Beneš, Vojtěch. *Online učebnice fyziky pro gymnázia - Zvuk.* Available from <https://e-manuel.cz/kapitoly/mechanicke-vlneni/vyklad/zvuk/> [cit. 24.10.2023].

