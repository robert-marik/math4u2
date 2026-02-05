---
workflow: in progress
# workflow: translating
# workflow: finished
keywords:
- sequences and series
- geometric sequence
- financial literacy
is_finished: true
---

# Pyramid scheme
Imagine someone, on behalf of an investment company, offers you a quick way to grow your money. 
The only thing you need to do is to convince three of your friends to invest as well. 
However, your money won't actually be used to buy gold or stocks, it will be split between the people who joined the company before you. 
If you can convince three friends to join, you'll get a share of their money and also a portion from the other people they convince. 
This continues until the whole model collapses for lack of new investors and the company’s owner mysteriously flies off to the Bahamas. 
It has to be said that this sort of thing is not good for friendships.

You've just fallen victim to one of the most widespread fraudulent business models – *pyramid scheme*.

![Pyramid scheme](pyramida.png)

## Assignment 

The founder of the company (the first level of the pyramid) recruits three investors
(the second level of the pyramid) and collects a fixed entry fee of 20 000 CZK from each of them.
The task of each of the three investors is to bring in three new investors into the scheme
(the third level of the pyramid) and collect an entry fee of 20 000 CZK from each of them. 
The same process is repeated for the subsequent levels. For simplicity, we will assume that the recruitment
of new members always occurs only after the entire pyramid level is filled.  For example, recruiting new members
into the fourth level only begins after recruiting all nine investors to the third level.

The entry fee paid by new members is distributed among existing participants as follows: 
6 000 CZK will be given to person A, who brought in the new person, 
1 000 CZK will be given to person B, who brought in person A,  another
1 000 CZK will go to person C, who brought in person B, another
1 000 CZK will go to person D, who brought person C, and so on until the entry fee is divided. 
If the money is paid to the founder of the company, he gets the rest of the fee.

>**Exercise 1.** When will the newcomer get a refund for the joining fee?

\iffalse

*Solution.* A newcomer pays an entry fee of 20 000 CZK. In order to get the money back, they must recruit three new members, from whom they will receive a total of 18 000 CZK. Additionally, these recruited members must each bring in at least two more members, from whom the newcomer will receive the remaining 2 000 CZK.

\fi

>**Exercise 2.**
>When a certain level of the pyramid is reached, the founder of 
>the company does not receive money from the entry fees for the first time.
>
>1. Which level is it?
>2. After reaching this level, how many people are there in the entire pyramid? Compare this number to the number of people in your school or community.   
>3.  Determine the percentage of people who are in a loss after this
>    level is reached.

\iffalse

*Solutions of Exercise 2.*

*Solution of 2.1.*  If the founder of the company receives no money from the new member's entry fee for the first time, this means that there are 16 levels above that member (6 000  CZK goes to the person in the level above, $14\cdot 1\ 000$ CZK to the people in the 14 levels above, and the founder in the first level gets nothing). The new member is thus at level 17.

*Solution of 2.2.* The numbers of people in each level form a geometric sequence with the first term $a_1=1$ and the quotient $q=3$. 
The number of people in a pyramid of 17 levels is then the sum of the first 17 terms of this sequence. $$s_{n}=a_1\cdot\frac{q^n-1}{q-1},\qquad s_{17}=1\cdot\frac{3^{17}-1}{3-1}=64\ 570\ 081$$ 
We can see that the entire population of a larger country (roughly equivalent to the population of France) would have to be involved in the scheme.

*Solution of 2.3.* It follows from the solution of the first exercise that the lossy part of the pyramid consists of the last two levels. The number of people in loss is thus equal to the sum of the sixteenth term
and the seventeenth term of the geometric sequence: $a_{16}+a_{17}=3^{15}+3^{16}=57\ 395\ 628$. Now we can determine the percentage of people in the loss:
$$P=100\cdot\frac{57\ 395\ 628}{64\ 570\ 081}\,\%\doteq 88{,}89\ \%.$$

\fi

>**Exercise 3.**
>In real cases from the Czech Republic, the number of participants was in the order of units of thousands.
>Therefore, let's say that the number of participants in our
pyramid is between 2 000 and 8 000, after reaching a certain level.
>1. Which level is it?
>2.  Determine the percentage of people who are now at a loss.
>3.  Determine the total profit of the founder of the company.
>4.  Determine the total profit of the investor in the second level of the pyramid.
>5.  What percentage of all entry fees collected will be
>    paid to the people in the first three levels of the pyramid?

\iffalse

*Solutions of Exercise 3.*

*Solution of 3.1.* The problem can be solved by gradual substituting natural numbers into the formula for the sum of the first
$n$ terms of the geometric sequence. However, we will present a solution using the exponential inequality.
It applies that $2\ 000 \leq s_n \leq  8\ 000$, therefore after substituting into the formula ($a_1=1$, $q=3$) 
we get: $$2\ 000  \leq  \dfrac{3^n-1}{2}  \leq  8\ 000$$ $$4\ 001  \leq   3^n  \leq   16\ 001$$ $$\log_3 4\ 001  \leq   n  \leq   \log_3 16\ 001.$$ Since $\log_3 4\ 001 \doteq 7{,}55$ and $\log_3 16\ 001 \doteq 8{,}81$,
the pyramid now has eight levels (by substituting in $s_8$ we can see that the number of people in the pyramid
is 3 280 now).

*Solution of 3.2.* Again, the losy parts of the pyramid are last two levels. Similar to solution 2.3, the number of people in the loss is equal to $a_7+a_8=3^6+3^7=2\ 916$. We determine the percentage share: $$P'=100\cdot\frac{2\ 916}{3\ 280}\,\%\doteq 88{,}90\,\%.$$
We can notice that the result is not very different from the result in 2.3, even though the 
numbers of people considered are different in orders of magnitude. 

*Solution of 3.3.* The founder of the company receives the entire input fee from each person in the second level
fee (20 000 CZK), from each person in the third level 14 000 CZK, from each person
in the fourth level 13 000 CZK, etc. Since the pyramid now has eight levels, the total profit $Z_1$ of the founder is 

$$Z_1=3\cdot 20\ 000 + 3^2\cdot 14\ 000 + 3^3\cdot 13\ 000 + \cdots + 3^7\cdot 9\ 000 = 31\ 155\ 000\,\text{CZK}.$$

*Solution of 3.4.* To clarify the situation of the investor on the second level, see the following figure.

![Illustration for the exercise 3.4](pyramida2.png)
 
The red-colored investor in the second level of the pyramid receives 6 000 CZK from each of the three blue-colored investors in the third level. These three investors then recruited other people into the scheme. The red investor collects 1 000 CZK from each green colored investor. Similarly, he collects 1 000 CZK from people recruited by green investors and all other people in "his" branch of the pyramid.
  
Let us now calculate the profit $Z_2$ of the red investor. The number of people from whom he receives 1 000 CZK is equal to the sum of $$3^2 + 3^3 + 3^4 + 3^5 + 3^6$$ (the whole pyramid should have eight levels). We must also not forget to subtract the entry fee. Thus $$Z_2=3\cdot 6\ 000 + (3^2+3^3 + 3^4 + 3^5 + 3^6 )\cdot 1\ 000 - 20\ 000 = 1\ 087\ 000\,\text{CZK}.$$ 

*Solution of 3.5.* From Exercise 3.1, we know that there are a total of 3 280 people in the pyramid, each except for the founder paid 20 000  CZK in entrance fees. The total amount of money collected is therefore 65 580 000 CZK. From parts 3.3 and 3.4 we know the profit of the founder and the investor in the second level, so we will also calculate the profit of the investor in the third level (similarly to part 3.4): $$Z_3=3\cdot 6\ 000 + (3^2+3^3 + 3^4 + 3^5 )\cdot 1\ 000 - 20\ 000 = 358\ 000\,\text{CZK}. $$ Now we can determine the share of funds paid out to people at the first three levels ($S$ is the total amount): $$P''=100\cdot\frac{Z_1 + 3\cdot Z_2 + 9\cdot Z_3}{S}=100\cdot\frac{37\ 638\ 000}{65\ 580\ 000}\doteq 57{,}39\,\%.$$ For a better understanding, it is important to realize that this share of the total "company income" is paid to only 13 people out of 3,280. Approximately $0{,}4\ \%$ of the people in the pyramid will thus receive more than half of the collected money. It is not surprising, therefore, that pyramid schemes are prohibited as a business model in a number of countries around the world (Unfortunately, the Czech Republic is not among them as of 2023.).

\fi

## Literature

* Yates K. *The Math of Life and Death: 7 Mathematical Principles That Shape Our Lives*. Scribner; Standard Edition (January 7, 2020). 

* Illinois Attorney General. *Pyramid schemes* [online]. Dostupné z
<https://ag.state.il.us/consumers/pyramid.html> [cit. 1.6.2023].
