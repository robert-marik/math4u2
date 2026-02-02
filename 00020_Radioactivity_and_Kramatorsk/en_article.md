---
keywords:
- exponentials and logarithms
- exponential function
- logarithmic function
- radioactivity
is_finished: true
# workflow: in progress
workflow: translating
# workflow: finished
difficulty: 2
time: 20
---

# The Deadly Flat in Kramatorsk

Apartment No. 85, Building 7, Kramatorsk (formerly USSR, today Ukraine), Mariyi Pryimachenko Street, was truly cursed and brought nothing but suffering to its residents. Between 1980 and 1989, two families lived there one after another and helplessly watched their children die of leukemia. In 1980, an eighteen-year-old daughter suddenly died; in 1982, her sixteen-year-old brother and their mother followed. None of this attracted the attention of the authorities, and the apartment was assigned to new tenants. Unfortunately, they were not lucky either, as their son soon died of leukemia as well.

![Building in Kramatorsk where the mysterious deaths occurred](house_no_7.jpg)

### The Accident at the Karansky Quarry

Only after another death, and thanks to the persistence of the new tenant, was the apartment inspected. Shocked inspectors discovered a strong source of radioactive radiation in the children’s room. A large section of the wall was cut out and examined. A careful investigation revealed a radioactive source embedded in the concrete panel—similar to those used in quarries.

Thanks to the labeling of radioactive sources, it was determined that the device had been lost in the late 1970s at the Karansky quarry. It was a small capsule containing the radioactive isotope cesium-137, emitting dangerous gamma radiation. The capsule was lost at the quarry and, by an unfortunate coincidence, ended up in the gravel used to manufacture the concrete panel just for this apartment.

In quarries, radioactive materials may be used, for example, to determine the density of rock or the fill level of opaque containers. Although the handling of such materials is subject to strict regulations, accidents can still happen.

#### For clarity, let us summarize what happened:  
- In the 1970s, a radioactive cesium-137 source was lost from industrial equipment at a quarry near Kramatorsk.
- Gravel and other material from the quarry were used to manufacture concrete panels for an apartment building.
- In one panel forming the wall of the children’s room in Apartment No. 85, a small radioactive source became permanently embedded in the concrete.
- A child’s bed was placed right next to this wall, where the children spent many hours (sleeping, playing, studying).
- Over the course of about one decade, several residents of the apartment (especially children) developed leukemia and died. Only then did people begin to consider the true cause of the mysterious deaths.
- Eventually, relatives and doctors called in experts, who measured extremely high radiation doses in the apartment and discovered the capsule containing a strong cesium-137 source directly inside the wall.

This story shows how powerful the effects of radioactive radiation on human health can be, how dangerous the “invisibility” of radiation is, and how important the safe handling of radioactive materials is.

### Radioactive Substances and Radioactive Radiation

A radioactive substance is a substance containing unstable atomic nuclei (radionuclides) that spontaneously decay and emit radiation.

We distinguish the following types of radiation:  

- Alpha radiation: a stream of heavy particles (helium nuclei); it has a short range and can be stopped by a thin layer of material (e.g., paper or human skin).
- Beta radiation: a stream of electrons or positrons; it has a longer range than alpha radiation but can still be relatively easily stopped by metal or a thicker layer of plastic.
-  Gamma radiation: highly penetrating electromagnetic radiation with high energy; shielding requires a thick layer of dense material (lead, concrete).

In our story, the main role is played by cesium-137, which emits gamma radiation. Gamma radiation can penetrate building structures as well as the human body and may damage cells and DNA.

### Radioactive Decay and Half-Life

Radioactivity (radioactive decay) is a spontaneous process in which unstable atomic nuclei transform into more stable nuclei while emitting radiation. For a large number of nuclei, this process follows a well-described law.

The number of undecayed nuclei satisfies the relation

$$
\tag{1}
N(t) = N_0 \mathrm{e}^{-\lambda t},
$$

where

* $N(t)$ denotes the amount of undecayed substance at time $t \geq 0$;
* $N_0$ is the initial amount of the substance, i.e., the amount at time $t = 0$;
* $\lambda$ is a constant characterizing the decay rate;
* $t$ is time.

The half-life of a radioactive substance (denoted by $T$) is the time required for the number of radioactive nuclei (and the intensity of the radiation) to decrease to one half of its original value. The half-life $T$ is closely related to the constant $\lambda$ in equation $(1)$.

For example, cesium-137 has a half-life of approximately 30 years. After 30 years, the amount of radioactive substance decreases to one half; after another 30 years (a total of 60 years), to one quarter; after 90 years, to one eighth, and so on.

### Radiation Intensity

Radiation intensity is a physical quantity that expresses the amount of radiation energy (or number of particles) passing through a unit area per unit time.

At a fixed distance from the source, the radiation intensity is directly proportional to the amount of undecayed material in the source. If we want to reduce the radiation intensity by a factor of $36$, we must reduce the number of nuclei by a factor of $36$.  

A point source emits energy uniformly in all directions. The farther we are from the source, the more the energy spreads over a larger surface area (a spherical surface). At a distance $r$ from the source, the surface area of the sphere is $4\pi r^2$. Thus, it is directly proportional to the square of the distance.

If the distance from the source increases, the radiation dose spreads over a larger area proportional to the square of the distance. Therefore, the radiation intensity decreases with the square of the distance. If the distance from the source increases $k$ times, the radiation intensity decreases $k^2$ times.

### Radiation Dose and Health Risk

Radiation dose expresses how much radiation energy is absorbed by a given amount of tissue. The commonly used units are the gray (Gy) and the sievert (Sv), the latter reflecting the biological effect on tissue. Long-term exposure to higher radiation doses increases the risk of tumors, leukemia, and other health problems.  

In Kramatorsk, the danger resulted from a combination of relatively short distance, constant presence in the room (many hours per day), and a long period of time (years).

We are now ready to solve the following tasks.

> **Task 1.** A radioactive source is embedded in the panel forming the wall of the children’s room—unfortunately right next to the bed of one of the children. Determine how the radiation intensity would change if the bed were moved from this wall to the opposite side of the room.  
> Assume that the original distance from the source to the bed was half a meter and that after moving the bed it would increase to three meters (i.e., six times farther).

\iffalse

*Solution.* From the previous section, we know that if the distance from the source increases $k$ times, the radiation intensity decreases $k^2$ times.  
If the distance increases $6$ times, the radiation intensity decreases $36$ times.

\fi

> **Problem 2.** The cesium-137 used as the radioactive source in the described incident has a half-life of 30 years. Determine how long it would take for the amount of undecayed cesium in the panel to decrease so that the radiation intensity at a distance of half a meter would be as low as the original intensity at a distance of $3$ meters (i.e., six times farther away).

\iffalse

*Solution.* From Problem 1, we know that increasing the distance $6$ times reduces the radiation intensity $36$ times. Since radiation intensity is directly proportional to the amount of undecayed material, we look for the time $t$ when the amount of radioactive material is $36$ times smaller.

We can use  equation $(1)$,

$$
N(t) = N_0 \mathrm{e}^{-\lambda t},
$$

and we seek $t$ such that $N(t) = \frac{1}{36}N_0$. By simple algebraic manipulation and then taking the natural logarithm of equation $(1)$, we obtain:

$$
\mathrm{e}^{-\lambda t} = \frac{N(t)}{N_0} 
$$

$$
-\lambda t  = \ln \frac{N(t)}{N_0}\tag{2}
$$

Since after thirty years the amount of radioactive substance decreases to one half (the half-life is 30 years), this means that  
$N(30)=\frac{1}{2}N_0$. Substituting $t=30$ into equation $(2)$, we obtain  

$$
-\lambda \cdot 30  = \ln \frac 12, 
$$

and therefore  

$$
\lambda = -\frac{1}{30} \ln \frac{1}{2} = \frac {\ln 2}{30}.
$$ 

Substituting the computed constant $\lambda$ back into $(2)$ gives  

$$
-\frac{\ln 2}{30} \cdot t  = \ln \frac{N(t)}{N_0}
$$

and consequently  

$$
t  = -30 \frac{\ln \frac{N(t)}{N_0}}{\ln 2}.
$$

We are looking for the time $t$ at which $N(t)$ (the amount of radioactive substance) is $36$ times smaller than at time $0$, that is,  $N(t)=\frac {1}{36}N_0$. For this time we obtain  

$$
t  = -30 \frac{\ln \frac{1}{36}}{\ln 2}=
30 \frac{\ln {36}}{\ln 2} \doteq 155 \; \text{years}.
$$

A reduction in radiation equivalent to moving the bed to the other side of the room would therefore occur after approximately 155 years.

\fi

> **Task 3.** Solve Problem 2 in general: for any radioactive substance with half-life $T$ and for a situation in which the distance from the source increases $k$ times.  
>
> More precisely: At time $t=0$, the bed is next to the wall. Determine how long ($t>0$) it would take for the amount of undecayed material in the panel to decrease so that the radiation intensity at the wall would equal the intensity at time $t=0$ at a distance $k$ times greater.

\iffalse

*Solution.*  
Proceeding in the same way as in Task 2, we obtain that for a radioactive substance with half-life $T$,

$$
\lambda = \frac{\ln 2}{T}. 
$$

Using the same steps again, we arrive at the relation

$$
t  = -T \frac{\ln \frac{N(t)}{N_0}}{\ln 2}. 
$$

Now, realize that if the distance from the source increases $k$ times, the radiation intensity becomes $k^2$ times smaller. Since the radiation intensity is directly proportional to the amount of undecayed material, we want to determine the time $t$ at which the amount of radioactive material is $k^2$ times smaller.

Thus, for the time $t$ satisfying $N(t)=\frac{1}{k^2}N_0$, we obtain

$$
t  = -T \frac{\ln \frac{1}{k^2}}{\ln 2}=
T \frac{\ln (k^2)}{\ln 2} = \frac{2\ \!T \ln k}{\ln 2}. 
$$

**Remark.**  
We can verify that substituting $T=30$ and $k=6$ into the last formula gives $t \doteq 155$ (the same result as in Problem 2).

\fi

In the following problem, we derive another formula describing radioactive decay. Its advantage is that the half-life of the radioactive substance appears explicitly in it. In many situations, it is also more convenient to use than formula $(1)$.

> **Problem 4.**  
> Show that relation $(1)$,  
> $N(t) = N_0 \mathrm{e}^{-\lambda t}$, can be written in the form  
>
> $$
> N(t) = N_0 \left( \frac{1}{2} \right)^{\!\small{\frac{t}{T}}},
> $$
>
> where $T$ is the half-life of the radioactive substance.

\iffalse
*Solution.*  
Substituting $t = T$ into relation $(1)$, we obtain (recall that $T$ is the half-life, that is, $N(T)=\frac{1}{2}N_0$):

$$
\begin{aligned}
 N(T) &= N_0 \mathrm{e}^{-\lambda T} \\
 \frac{1}{2}N_0 &= N_0 \left( \mathrm{e}^{-\lambda} \right)^T 
\end{aligned}
$$

After successive algebraic simplifications, we get:

$$
\begin{aligned}
 \frac{1}{2} &= \left( \mathrm{e}^{-\lambda} \right)^T  \\
 \mathrm{e}^{-\lambda} &= \left( \frac{1}{2} \right)^{\!\small{\frac{1}{T}}} 
\end{aligned}
$$

Substituting this last equality back into relation $(1)$, we obtain

$$
 N(t)=N_0 \mathrm{e}^{-\lambda t} 
 = N_0 \left( \mathrm{e}^{-\lambda} \right)^t 
 = N_0 \left[ \left(\frac{1}{2}\right)^{\!\small{\frac{1}{T}}} \right]^t 
 = N_0 \left( \frac{1}{2} \right)^{\!\small{\frac{t}{T}}}. 
$$
 
\fi

**Remark.**  
From the relation $N(t)=N_0 \left( \frac{1}{2} \right)^{\!\small{\frac{t}{T}}}$, we can clearly see, for example, that if the half-life is $T=30 \;\text{years}$, then after $t=90 \; \text{years}$ one eighth of the original amount of the substance remains, since

$$
 N(t)=N_0\left( \frac{1}{2} \right)^{\!\small{\frac{t}{T}}}
 = N_0\left( \frac{1}{2} \right)^{\!\small{\frac{90}{30}}}
 = N_0\left( \frac{1}{2} \right)^{3}
 = \frac{1}{8}N_0.
$$


### Questions for Reflection (No Calculations Required)

* Why did the people in Kramatorsk take so long to realize that the problem was in the wall of the apartment rather than “just” coincidence or genetics?
* What role does the fact that radiation cannot be seen, felt, or heard play in this story?
* What would have happened if the same source had been located in a basement wall or a technical room that people visit only rarely?
* How would the risk change if adults, who spend less time in the room, had slept there instead of children?
* In your opinion, what responsibilities do companies and institutions working with radioactive sources have (labeling, records, inspections)?
* Can the use of radioactive substances be beneficial (e.g., in medicine, industry, energy production)?

### The Accident Was Not Unique  

A similar accident to the one at the Karansky quarry occurred at the beginning of 2023 in Australia, where a radioactive source was lost during transport over a distance of 1,400 kilometers. The search was truly like looking for a needle in a haystack, as the source was a tiny cylinder about 8 millimeters in size—roughly the size of a button battery. Fortunately, the Australian capsule was eventually found along the roadside on the transport route.

![Radioactive source lost in Australia in 2023 compared with a coin](australia-capsule-size2.png)

### References

* Wikipedia, [Kramatorsk radiological accident](https://en.wikipedia.org/wiki/Kramatorsk_radiological_accident),  
  September 28, 2023

* iRozhlas, [Radiation danger status. Australia searches for a lost piece of cesium-137, it could be anywhere](https://www.irozhlas.cz/zpravy-svet/australie-radiace-nebezpeci-varovani-radioaktivita-cesium-137-ozareni_2301311701_har>),  
  September 28, 2023

* CNN, [Missing radioactive capsule found on remote road in Australia](https://edition.cnn.com/2023/02/01/australia/australia-radioactive-capsule-found-intl-hnk/index.html), September 28, 2023

* IFL Science, [The Devastating Kramatorsk Radiological Accident Almost Killed An Entire Apartment Block](https://www.iflscience.com/the-devastating-kramatorsk-radiological-accident-almost-killed-an-entire-apartment-block-67384)

* Curious Archive, [Death in Apartment 85: The Kramatorsk Radiological Accident](https://www.curiousarchive.com/death-in-apartment-85-the-kramatorsk-radiological-accident/5)

* Amusing Planet, [The Building That Gave Its Residents Leukemia](https://www.amusingplanet.com/2023/11/the-building-that-gave-its-residents.html)

* Reddit, [In the 1970s, a capsule with radioactive Caesium-137 was lost in the sand quarry...](https://www.reddit.com/r/interestingasfuck/comments/zqrz3p/in_the_1970s_a_capsule_with_radioactive)

### Image Sources

* Wikimedia, [Artemka](https://commons.wikimedia.org/wiki/File:%D0%A3%D0%BB%D0%B8%D1%86%D0%B0_%D0%9C%D0%B0%D1%80%D0%B8%D0%B8_%D0%9F%D1%80%D0%B8%D0%B9%D0%BC%D0%B0%D1%87%D0%B5%D0%BD%D0%BA%D0%BE,_7.jpg), September 28, 2023

* CNN, [Missing radioactive capsule found on remote road in Australia](https://edition.cnn.com/2023/02/01/australia/australia-radioactive-capsule-found-intl-hnk/index.html), September 28, 2023
